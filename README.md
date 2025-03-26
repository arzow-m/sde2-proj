# Software Design 2 Final Project - Job Vacancy Data Analysis

## Authors:
- Arzow Maksum
- Teigen Crook 
- Andrew McLean 
- Syed Raamis 

## Project Overview

This project focuses on analyzing job vacancy data, including various factors like occupation, hourly wages, geographic location, and job vacancy characteristics. The analysis consists of multiple steps, including filtering job vacancies, calculating annual salaries, and generating visualizations based on the data. The data processing includes filtering for specific occupations, calculating average yearly salaries based on hourly wages, and providing visual insights into job vacancies using pie and bar charts. 

## File Breakdown

### 1. **`extractQ2.py`**
   - **Description**: This script filters job vacancy data based on the user's input for occupation and year. It then exports the filtered data into a CSV file that contains relevant information such as occupation, year, month, and hourly wages.
   - **Command-line Arguments**:
     - `argv[1]`: Occupation (e.g., "Architects")
     - `argv[2]`: Year (e.g., "2023")
   - **Usage**:
     ```bash
     python extractQ2.py "Architects" "2023"
     ```

### 2. **`answerQ2.py`**
   - **Description**: This script processes the filtered job vacancy data (output from `extractQ2.py`), calculates the average yearly salary for the specified occupation, and writes the results to `plot2.csv` for further use.
   - **Command-line Arguments**: None
   - **Usage**:
     ```bash
     python answerQ2.py
     ```

### 3. **`createPlot1.py`**
   - **Description**: This script generates a pie chart showing the percentage of Canadian job vacancies that require both a bachelor's degree and offer an hourly wage above a user-defined threshold.
   - **Command-line Arguments**: None
   - **Usage**: This script is automatically invoked by `answerQ2.py`.
   - **Features**: The pie chart is displayed showing the percentage of job vacancies above and below the defined wage threshold.

### 4. **`createPlot3.py`**
   - **Description**: This script takes job vacancy data for a specific occupation and geographic location, sorts the job vacancies, and outputs the top 5 occupations with the greatest number of vacancies in a bar chart.
   - **Command-line Arguments**: None
   - **Usage**:
     ```bash
     python createPlot3.py
     ```

### 5. **`extractQ3.py`**
   - **Description**: This script filters job vacancy data based on geographic location, year, and occupation, and then prints the relevant rows for further processing. This data is used for analyzing the most in-demand jobs in specific locations.
   - **Command-line Arguments**:
     - `argv[1]`: Geographic location
     - `argv[2]`: Year
     - `argv[3]`: Occupation
   - **Usage**:
     ```bash
     python extractQ3.py "Ontario" "2023" "Software Engineer"
     ```

### 6. **`extractQ3Processed.py`**
   - **Description**: This script processes the pre-filtered CSV data and sorts the job vacancies, saving the top 5 occupations with the most job vacancies for each occupation.
   - **Command-line Arguments**: None
   - **Usage**:
     ```bash
     python extractQ3Processed.py
     ```

## Data Files

- **`14100328.csv`**: The raw job vacancy data used in the analysis.
- **`q2_data.csv`**: The filtered data containing job vacancies, occupations, years, and hourly wages used by `answerQ2.py`.
- **`plot1.csv`**: The CSV file containing data for `createPlot1.py` to generate pie charts based on job vacancy wage thresholds.
- **`plot2.csv`**: The output of the average salary calculation (from `answerQ2.py`) to be used in data visualization.
- **`plot3.csv`**: Contains data used for `createPlot3.py` to generate bar charts on the top 5 job vacancies.

## How to Use

1. **Preprocessing Job Vacancies**:
   - Run `extractQ2.py` to filter job vacancies by occupation and year.
     Example:
     ```bash
     python extractQ2.py "Software Engineers" "2023"
     ```

2. **Calculate Average Yearly Salary**:
   - After filtering the data, use `answerQ2.py` to calculate the average yearly salary based on hourly wages.
     Example:
     ```bash
     python answerQ2.py
     ```

3. **Generate Pie Chart (Plot1)**:
   - You can define a wage threshold and generate a pie chart showing the percentage of job vacancies that meet the wage condition using `createPlot1.py`. This will be invoked automatically after running `answerQ2.py`.
     Example:
     ```bash
     python createPlot1.py
     ```

4. **Top 5 Vacancies for Specific Occupation**:
   - If you want to analyze the top 5 job vacancies for a specific occupation and province, run `extractQ3.py` followed by `extractQ3Processed.py` to generate the data and sort the vacancies.
     Example:
     ```bash
     python extractQ3.py "Ontario" "2023" "Software Engineer"
     python extractQ3Processed.py
     ```

5. **Generate Bar Chart (Plot3)**:
   - Use `createPlot3.py` to generate a bar chart for the top 5 most in-demand jobs for a given occupation in a specific region.
     Example:
     ```bash
     python createPlot3.py
     ```

## Requirements

To run the scripts in this project, you'll need the following Python libraries:

- `pandas` (for data manipulation)
- `matplotlib` (for plotting graphs)
- `csv` (for reading and writing CSV files)

## Conclusion

This project provides an end-to-end analysis of job vacancies in Canada, with various filtering and processing steps, as well as visualizations that display insights into job trends. The results are stored in CSV files, and the final analysis can be visualized using pie and bar charts.
