from selenium import webdriver
from bs4 import BeautifulSoup


def extractor_jobs(keyword):
    base_url = "https://kr.indeed.com/jobs?q="
    browser = webdriver.Chrome()
    browser.get(f"{base_url}{keyword}")
    results = []
    soup = BeautifulSoup(browser.page_source, "html.parser")
    jobs = soup.find_all("li", class_="css-5lfssm")
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
