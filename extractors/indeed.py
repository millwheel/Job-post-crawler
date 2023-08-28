from selenium import webdriver
from bs4 import BeautifulSoup

base_url = "https://kr.indeed.com/jobs?q="
browser = webdriver.Chrome()
browser.get(f"{base_url}python")
soup = BeautifulSoup(browser.page_source, "html.parser")


def job_searching(results: list, jobs: list) -> list:
    for job in jobs:
        title = job.find("h2", class_="jobTitle")
        if title:
            title_name = title.find("span")
            company_name = job.find("span", class_="companyName")
            company_location = job.find("div", class_="companyLocation")
            job_data = {
                'company': company_name.string,
                'region': company_location.string,
                'position': title_name.string
            }
            results.append(job_data)
    return results


def extractor_jobs(keyword):
    results = []
    base_url = "https://kr.indeed.com/jobs?q="
    browser = webdriver.Chrome()
    browser.get(f"{base_url}{keyword}")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    jobs = soup.find_all("li", class_="css-5lfssm")
    results = job_searching(results, jobs)
    next_page = soup.find("a", attrs={'data-testid': 'pagination-page-next'})
    while next_page:
        next_url = next_page['href']
        browser.get(f"https://kr.indeed.com{next_url}")
        soup = BeautifulSoup(browser.page_source, "html.parser")
        jobs = soup.find_all("li", class_="css-5lfssm")
        results = job_searching(results, jobs)
        next_page = soup.find("a", attrs={'data-testid': 'pagination-page-next'})
    return results

