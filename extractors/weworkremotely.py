from requests import get
from bs4 import BeautifulSoup


def wwr_extractor(keyword):
    base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
    response = get(f"{base_url}{keyword}")
    if response.status_code != 200:
        print("Can't request website")
    else:
        results = []
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all("section", class_="jobs")
        for job_section in jobs:
            job_posts = job_section.find_all('li', class_="feature")
            for post in job_posts:
                anchors = post.find_all('a')
                anchor = anchors[1]
                company, kind, location = anchor.find_all('span', class_="company")
                title = anchor.find('span', class_="title")
                job_data = {
                    'company': company.string.replace(",", " "),
                    'location': location.string.replace(",", " "),
                    'position': title.string.replace(",", " ")
                }
                results.append(job_data)
        return results
