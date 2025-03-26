'''
extractQ2.py

    Author(s): Arzow Maksum (1337424)

    Project: Software Design 2 Final Project: Question 2
    Date of last update: Mar 25, 2025

    Functional Summary:
    Takes in a data file containing information about job vacancies, including job titles and hourly wages.
    Filters the data to include only full-time, software-related roles for a user-defined occupation and year.
    Outputs the filtered data into a new CSV file, containing the occupation, year, month, and wage data, for further analysis.

    Commandline arguments: 2
        argv[1] = the relevant occupation (e.g., "Architects")
        argv[2] = the year for the data filter (e.g., "2023")
'''

import sys
import pandas as pd

def exclude_column(column):
    # exclude column 15 from being read
    return column != 15

def main(argv):
    print("Script started")

    if len(argv) != 3:
        print("Incorrect number of arguments", file=sys.stderr)
        sys.exit(1)

    input_occupation = argv[1]
    input_year = argv[2]

    # load stats csv file into a pandas dataframe, skip col 15 due to "mixed types error"
    try:
        df = pd.read_csv("14100328.csv", encoding="utf-8-sig", usecols=exclude_column)

    except Exception as err:
        print(f"Unable to open file '14100328.csv': {err}", file=sys.stderr)
        sys.exit(1)

    print("CSV loaded successfully!")

    # get the year and month from 'REF_DATE'
    # .str[:4] is a vectorized string operation that allows you to do string manipulation
    # only slice does not require method name 
    # i.e. for upper() it would be .str.upper()
    df["National Occupational Classification"]= df["National Occupational Classification"].str[0:-7] # this ensures user does not need to input nums after occupation
    df["Year"] = df["REF_DATE"].str[0:4]
    df["Month"] = df["REF_DATE"].str[5:7]

    # filter data based on the occupation and year (full-time hours is assumed with the question)
    filtered_df = df[
        (df["National Occupational Classification"] == input_occupation) &
        (df["Year"] == input_year) &
        (df["Job vacancy characteristics"] == "Full-time") &
        (df["Statistics"] == "Average offered hourly wage") &
        (df["VALUE"].notna())  # ensure VALUE is not empty
    ]

    # filter the df to only keep relevant columns
    filtered_df = filtered_df[["Year", "Month", "National Occupational Classification", "Job vacancy characteristics", "Statistics", "VALUE"]]

    if filtered_df.empty:
        print("No data found for the given filters.")
    else:
        # save filtered data to a new csv file
        # does not include the index column to the new file 
        filtered_df.to_csv("q2_data.csv", index=False, encoding="utf-8-sig")
        print("Filtered data saved successfully to 'q2_data.csv'.")

# call main 
main(sys.argv)
