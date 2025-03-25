'''
extractQ1.py

    Author(s): Teigen Crook (1331121), Arzow Maksum (1337424), Andrew McLean (1328723), Syed Raamis (1334868)

    Project: Milestone 3 Question 1
    Date of last update: Mar 12, 2025

    Functional Summary:
    Takes in a data file containing information about software job vacancies, education requirements, and hourly wages.
    Filters the data to include only software engineering roles in Canada that require a Bachelor's degree
    and pay above a user-defined hourly wage. Calculates the percentage of such vacancies relative to the total
    number of software engineering vacancies.

    Commandline arguments: 2
        argv[1] = the relevant data file
        argv[2] = minimum hourly wage (user-defined)
'''

import csv
import sys

INPUT_DELIMITER = ","

if len(sys.argv) < 3:
    print("Usage: python extractQ1.py <input_file> <min_hourly_wage>")
    sys.exit(1)


datafile = sys.argv[1]  
min_hourly_wage = float(sys.argv[2])


csv_fh = open(datafile, "r")
csvdata = csv.reader(csv_fh, delimiter=INPUT_DELIMITER)


header = next(csvdata)
print(f"{header[0]},{header[1]},{header[2]},{header[3]},{header[4]}")


total_vacancies = 0
meeting_criteria = 0


for row in csvdata:

    quarter = row[0].strip()
    job_vacancies_overall = int(row[1].strip())
    job_vacancies_bachelors = int(row[2].strip())
    avg_wage_overall = float(row[3].strip())
    avg_wage_bachelors = float(row[4].strip())

    
    total_vacancies += job_vacancies_bachelors

  
    if avg_wage_bachelors >= min_hourly_wage:
        meeting_criteria += job_vacancies_bachelors
        print(f"{quarter},{job_vacancies_bachelors},{avg_wage_bachelors}")


csv_fh.close()


if total_vacancies > 0:
    percentage = (meeting_criteria / total_vacancies) * 100
    print(f"\nPercentage of software engineering vacancies requiring a Bachelor's degree and paying above ${min_hourly_wage}/hour: {percentage:.2f}%")
else:
    print("No software engineering vacancies found in the dataset.")
