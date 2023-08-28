from extractors.indeed import extractor_jobs as indeed_extractor
from extractors.weworkremotely import extractor_jobs as wwr_extractor

keyword = input("what do you want to search for?")

wwr = wwr_extractor(keyword)
indeed = indeed_extractor(keyword)
jobs = wwr + indeed

print(jobs)

file = open(f"{keyword}.csv", "w")
for job in jobs:
    file.write(f"{job['position']}, {job['company']}, {job['region']}\n")
file.close()
