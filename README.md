# Software Design 2 Final Project - Job Vacancy Data Analysis

## Authors:
- Arzow Maksum
- Teigen Crook 
- Andrew McLean 
- Syed Raamis 

## Project Overview

This project focuses on analyzing job vacancy data, including various factors like occupation, hourly wages, geographic location, and job vacancy characteristics. The analysis consists of multiple steps, including filtering job vacancies, calculating annual salaries, and generating visualizations based on the data. The data processing includes filtering for specific occupations, calculating average yearly salaries based on hourly wages, and providing visual insights into job vacancies using pie and bar charts. 

## Data Files

- **`14100328.csv`**: The raw job vacancy data used in the analysis.
- **`q2_data.csv`**: The filtered data containing job vacancies, occupations, years, and hourly wages used by `answerQ2.py`.
- **`plot1.csv`**: The CSV file containing data for `createPlot1.py` to generate pie charts based on job vacancy wage thresholds.
- **`plot2.csv`**: The output of the average salary calculation (from `answerQ2.py`) to be used in data visualization.
- **`plot3.csv`**: Contains data used for `createPlot3.py` to generate bar charts on the top 5 job vacancies.

## Requirements

To run the scripts in this project, you'll need the following Python libraries:

- `pandas` (for data manipulation)
- `matplotlib` (for plotting graphs)
- `csv` (for reading and writing CSV files)
