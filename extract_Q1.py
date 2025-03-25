'''
extractQ1.py

    Author(s): Teigen Crook (1331121), Arzow Maksum (1337424), Andrew McLean (1328723), Syed Raamis (1334868)

    Project: final project Q1
    Date of last update: Mar 25, 2025

    Functional Summary:
    Takes in data file containing information about hourly wages for professionals in a diverse amount of industries. 
    Redirects the rows relevant to location, occupation, hourly wages, and full-time hours. 

    Commandline arguments: 2
        argv[1] = name of the input file
        argv[2] = geographic location
        argv[3] = occupation input by the user 
'''

import csv
import sys

INPUT_DELIMITER = ","

if len(sys.argv) < 3:
    print("incorrect number of command line arguments")
    sys.exit(1)


datafile = sys.argv[1]
location_name = sys.argv[2]
user_occupation = sys.argv[3]

csv_fh = open(datafile, "r")
csvdata = csv.reader(csv_fh,delimiter=INPUT_DELIMITER)

for row in csvdata:
    header = row
    break

print(f"{header[0]},{header[1]},{header[3]},{header[4]},{header[12]}")

for row in csvdata:
    ref_date = row[0].strip("")
    geo = row[1].strip("")
    dguid = row[2].strip("")
    occupation = row[3].strip("")
    full_or_part_time = row[4].strip("")
    stats = row[5].strip("")
    uom = row[6].strip("")
    uom_id = row[7].strip("")
    scalar_factor = row[8].strip("")
    scalar_id = row[9].strip("")
    vector = row[10].strip("")
    coord = row[11].strip("")
    hourly_wage = row[12].strip("")
    status = row[13].strip("")
    symbol = row[14].strip("")
    terminated = row[15].strip("") # this is always empty 
    decimals = row[16].strip("")

    if geo.lower() == location_name.lower() and occupation.lower() == user_occupation.lower() and full_or_part_time == "Full-time":
        
        if row[12] != "" and float(row[12]) < 150.0:
            print(f"{row[0]},{row[1]},{row[3]},{row[4]},{row[12]}")

        # else: 
        #    print(f"{row[0]},{row[1]},{row[3]},{row[4]},{row[12]}")

csv_fh.close()
