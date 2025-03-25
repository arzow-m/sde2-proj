import matplotlib.pyplot as plt
import numpy as np
import csv

INPUT_DELIMITER = ","

csv_fh = open("plot2.csv", "r")
csvdata = csv.reader(csv_fh, delimiter= INPUT_DELIMITER)

jobs = []
salaries = []

for row in csvdata:
    year = row[0].strip()
    job = row[1].strip()

    first_title = job.split(',')[0]
    jobs.append(first_title)

    salary = row[2].strip()
    # convert salary to a float 
    try:
        salary = float(salary)
        salaries.append(salary)
    except ValueError:
        salaries.append(0)
 
plt.bar(jobs, salaries, color='violet')
plt.title(f'Average full-time wage by occupation in {year}')
plt.xlabel('Occupation')
plt.ylabel('Average full-time wage (in CAD)')
plt.show()