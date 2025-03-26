'''
createPlot1.py

    Author(s): Teigen Crook (1331121), Andrew McLean (1328723)
    Project: Team Project
    Date of last update: March 26, 2025

    Functional Summary:
        Takes in a CSV file containing the percentage and outputs a circle/pie chart that displays 
        the percentage of Canadian software vacancies that require both a bachelor's degree AND make above
        a user-defined hourly wage.
'''

import matplotlib.pyplot as plt
import csv

INPUT_DELIMITER = ","

# Open and read the CSV file containing the percentage data
csv_fh = open("plot1.csv", "r")
csv_plot_file = csv.reader(csv_fh, delimiter=INPUT_DELIMITER)

# Read the header (first row) of the CSV
header = next(csv_plot_file)

# Extract the percentage value from the CSV (assuming percentage is in the third column)
percentage = 0
for row in csv_plot_file:
    percentage = float(row[2].strip())  # Assuming percentage is in the third column of the file

# Calculate the remaining percentage (100 - percentage)
remaining_percentage = 100 - percentage

# Create labels for the pie chart
labels = [f"Above Wage Threshold: {percentage:.2f}%", f"Below Wage Threshold: {remaining_percentage:.2f}%"]

# Data for the pie chart
sizes = [percentage, remaining_percentage]

# Set up colors for the pie chart
colors = ['#66b3ff', '#ff6666']

# Create the pie chart
plt.figure(figsize=(6, 6))  # Set the figure size to make the chart circular
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, wedgeprops={'edgecolor': 'black'})

# Title the pie chart
plt.title("Percentage of Job Vacancies Requiring a Bachelor's Degree and Above the Wage Threshold")

# Show the pie chart
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
plt.show()
