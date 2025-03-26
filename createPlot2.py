'''
createPlot2.py

    Author(s): Arzow Maksum (1337424)

    Project: Software Design 2 Final Project: Question 2
    Date of last update: Mar 25, 2025

    Functional Summary:
    Reads data from a CSV file `plot2.csv` that contains job occupations and their corresponding average salaries.
    Processes the data to generate a bar chart visualizing the average full-time wage by occupation.
    The chart is displayed using Matplotlib, with the x-axis representing the job titles and the y-axis representing the average wage.
    Error checking ensures that all years in the data are consistent before generating the plot.

    Commandline arguments: 0
        No commandline arguments required.
'''

import matplotlib.pyplot as plt
import numpy as np
import csv
import sys

INPUT_DELIMITER = ","

try:
    csv_fh = open("plot2.csv", "r")

except Exception as err:
    print(f"Unable to open file 'plot2.csv': {err}", file=sys.stderr)
    sys.exit(1)

csvdata = csv.reader(csv_fh, delimiter= INPUT_DELIMITER)

jobs = []
salaries = []
years = []

for row in csvdata:
    year = row[0].strip()
    years.append(year)
    job = row[1].strip()

    first_title = job.split(',')[0]
    jobs.append(first_title)

    salary = row[2].strip()

    # convert salary to a float 
    try:
        salary = float(salary)
        salaries.append(salary)
    except ValueError:
        salaries.append(0) # error checking, appends 0$ salary if cannot convert to float

# error checking, ensures years are all the same
for i in range(len(years) - 1):
    if years[i] != years[i+1]:
        sys.stderr.write("Could not create graph. Conflicting years.")
        break
 
plt.bar(jobs, salaries, color='violet')
plt.title(f'Average full-time wage by occupation in {year}')
plt.xlabel('Occupation')
plt.ylabel('Average full-time wage (in CAD)')
plt.show()
