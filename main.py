from extractors.indeed import indeed_extractor
from extractors.wanted import wanted_extractor

keyword = input("what do you want to search for?")

indeed_jobs = indeed_extractor(keyword)
wanted_jobs = wanted_extractor(keyword)
jobs = indeed_jobs + wanted_jobs

file = open(f"{keyword}.csv", "w")
for job in jobs:
    file.write(f"{job['position']}, {job['company']}, {job['location']}\n")
file.close()
