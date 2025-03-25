'''
createPlot3.py

    Author(s): Teigen Crook (1331121), Arzow Maksum (1337424), Andrew McLean (1328723), Syed Raamis (1334868)

    Project: Team Project
    Date of last update: March 20, 2025

    Functional Summary:
        takes in a csv file and outputs a bar graph that displays the 5 jobs for a specific occupation and in a given prvince with the greatest amount of vacancies.
'''

import matplotlib.pyplot as plt
import numpy as np
import csv

INPUT_DELIMITER = ","

csv_fh = open("plot3.csv","r")
csv_plot_file = csv.reader(csv_fh,delimiter=INPUT_DELIMITER)

vacancies = []
jobs = []
for row in csv_plot_file:
    header = row
    break

for row in csv_plot_file:
    year = row[0].strip()
    job = row[1].strip()
    job_vacancies = row[2].strip()

    jobs.append(job)

    try:
        job_vacancies = int(job_vacancies)
        vacancies.append(job_vacancies)
    except ValueError:
        vacancies.append(0)

for i in range (5):
    jobs[i] = jobs[i] + (' ' * i)

print(jobs)

plt.bar(jobs,vacancies, color='green')
plt.title(f'most in demand jobs for {job} in {year}')
plt.xlabel(f'jobs for {job}')
plt.ylabel(f'number of vacancies')
plt.show()