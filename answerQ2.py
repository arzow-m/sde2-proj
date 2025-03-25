import csv
import sys

INPUT_DELIMITER = ","

csv_fh = open("q2_data.csv", "r")
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