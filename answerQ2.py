'''
answerQ2.py

    Project: Software Design 2 Final Project: Question 2
    Date of last update: Mar 25, 2025

    Functional Summary:
    Reads a CSV file containing job vacancy data, including occupation, full-time status, and hourly wage.
    Processes the data to calculate the average yearly salary for a user-defined occupation for a user-defined year.
    Writes the calculated average salary into a new CSV file `plot2.csv` for later use in data visualization.
    The annual salary is calculated based on an 8-hour workday, 5-day workweek, and 4 weeks per month.

    Commandline arguments: 0
        No commandline arguments required.
'''

import csv
import sys

INPUT_DELIMITER = ","

try:
    csv_fh = open("q2_data.csv", "r")
except Exception as err:
    print(f"Unable to open file 'q2_data.csv': {err}", file=sys.stderr)
    sys.exit(1)
    
csvdata = csv.reader(csv_fh, delimiter= INPUT_DELIMITER)

for row in csvdata:
    header = row
    break # extract header 

# create empty list to store results 
results = []

for row in csvdata:
    year = row[0]
    occupation = row[2]
    full_time = row[3]
    hourly_wage = row[5]

    # attempting to cast hourly_wage to a float 
    try:
        hourly_wage = float(hourly_wage)

    except IOError as err:
        print(f"Could not convert hourly wage into a float: {err}", file = sys.stderr)
        sys.exit(1)

    # create a list with all above into, append into result array
    results.append([year, occupation, full_time, hourly_wage])

# calculate total salaries in csv file 
total_salaries = 0
count = 0

for result in results:
    # calculate annual salary based on hourly wage 
    salary = ((((result[3] * 8) * 5) * 4) * 12)
    total_salaries += salary
    count += 1

average_salary = total_salaries / count

# attempting to cast average_salary to an int  
try:
    average_salary = int(average_salary)

except IOError as err:
    print(f"Could not convert total salary into a float: {err}", file = sys.stderr)
    sys.exit(1)

# open the csv file where the plotting material will be stored
try: 
    q2_data_fh = open("plot2.csv", "a", encoding = "utf-8-sig")

except IOError as err:
    print("Unable to open file '{}': ".format("plot2.csv", err), file = sys.stderr)
    sys.exit(1)

# set up the csv writer
csv_writer = csv.writer(q2_data_fh)

valid_row = [result[0], occupation, average_salary]
csv_writer.writerow(valid_row)

print(f"The average yearly salary for {occupation} in 2015 is {average_salary}$")
