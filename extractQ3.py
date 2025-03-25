'''
extractQ3.py

    Author(s): Teigen Crook (1331121), Arzow Maksum (1337424), Andrew McLean (1328723), Syed Raamis (1334868)

    Project: Team Project
    Date of last update: March 19, 2025

    Functional Summary:
    Takes in data file containing information about job vacancies for computing professionals by province. Prints out the rows relevent to location, occupation, and job vacancy characteristics.

    Commandline arguments: 4
        argv[1] = name of the input file
        argv[2] = geographic location
        argv[3] = year
        argv[4] = occupation
'''

import csv
import sys

INPUT_DELIMITER = ","

if len(sys.argv) < 4:
    print("incorrect number of command line arguments")
    sys.exit(1)


datafile = sys.argv[1]
location_name = sys.argv[2]
given_year = sys.argv[3]
given_occupation = sys.argv[4]

csv_fh = open(datafile, "r")
csvdata = csv.reader(csv_fh,delimiter=INPUT_DELIMITER)

for row in csvdata:
    header = row
    break

print(f'{header[0]},"{header[1]}","{header[3]}","{header[5]}","{header[12]}"')

for row in csvdata:
    ref_date = row[0].strip("")
    geo = row[1].strip("")
    occupation = row[3].strip("")
    stats = row[5].strip("")
    value = row[12].strip("")

    year = ref_date.split("-")[0]
    occupation_name = occupation.split("[")[0].strip()

    if geo.lower() == location_name.lower() and occupation_name.lower() == given_occupation.lower() and year == given_year and stats == "Job vacancies":
        
        if row[12] != "" and row[12] != "0":
            print(f'"{year}","{row[1]}","{occupation_name}","{row[5]}","{row[12]}"')

csv_fh.close()