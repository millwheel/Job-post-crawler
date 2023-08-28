from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def wanted_extractor(keyword):
    base_url = "https://www.wanted.co.kr/search?query="
    extend = "&tab=position"
    browser = webdriver.Chrome()
    browser.get(f"{base_url}{keyword}{extend}")
    body = browser.find_element(By.CSS_SELECTOR, "body")
    for _ in range(10):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    jobs = soup.find_all("div", class_="JobCard_container__FqChn")
    results = []
    for job in jobs:
        title = job.find("strong", class_="JobCard_title__ddkwM")
        company = job.find("span", class_="JobCard_companyName__vZMqJ")
        location = job.find("span", class_="JobCard_location__2EOr5")
        job_data = {
            'company': company.string.replace(",", " "),
            'location': location.string.replace(",", " "),
            'position': title.string.replace(",", " ")
        }
        results.append(job_data)
    return results
