from extractors.indeed import extractor_jobs as indeed_extractor
from extractors.weworkremotely import extractor_jobs as wwr_extractor

jobs = wwr_extractor("python")
print(jobs)
