'''
extractQ3.py

    Project: Team Project
    Date of last update: March 19, 2025

    Functional Summary:
        takes the pre-processed csv file and stores the job vacancy values in an array. It then sorts the array (ascending order) and then stores the top five greatest vacancies in another csv file.
'''

import csv
import sys

INPUT_DELIMITER = ","

if len(sys.argv) < 1:
    print("incorrect number of command line arguments")
    sys.exit(1)

csv_fh = open("Q3Processed.csv", "r",)
csvfile = csv.reader(csv_fh,delimiter=INPUT_DELIMITER)

for row in csvfile:
    header = row
    break

list_of_vacancies = []
top_five_vacancies = []

for row in csvfile:

    
    year = row[0].strip("")
    geo = row[1].strip("")
    occupation = row[2].strip("")
    vacancies = row[4].strip("")
    
    list_of_vacancies.append(int(vacancies))

sorted_list = sorted(list_of_vacancies)

#print("Sorted list:", sorted_list)

top_five_vacancies.append(sorted_list.pop())

while len(top_five_vacancies) < 5:
    
    temp = sorted_list.pop()

    if temp != top_five_vacancies[-1]:
        top_five_vacancies.append(temp)

print("Year,Occupation,Vacancies")

for i in range (5):
    print(f"{year},{occupation},{top_five_vacancies[i]}")

csv_fh.close()
