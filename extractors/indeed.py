from selenium import webdriver
from bs4 import BeautifulSoup


def job_searching(results: list, jobs: list) -> list:
    for job in jobs:
        title = job.find("h2", class_="jobTitle")
        if title:
            title = title.find("span")
            company = job.find("span", class_="companyName")
            location = job.find("div", class_="companyLocation")
            job_data = {
                'company': company.text.replace(",", " "),
                'location': location.text.replace(",", " "),
                'position': title.text.replace(",", " ")
            }
            results.append(job_data)
    return results


def indeed_extractor(keyword):
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
