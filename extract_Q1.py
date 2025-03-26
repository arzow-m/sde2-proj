
import sys
import pandas as pd

def main():
    print("Extracting relevant data...")

    # Load stats CSV file into a pandas dataframe
    try:
        df = pd.read_csv("14100328.csv", encoding="utf-8-sig")
    except Exception as err:
        print(f"Unable to open file '14100328.csv': {err}", file=sys.stderr)
        sys.exit(1)

    print("CSV loaded successfully!")

    # Normalize occupation titles (removing extra numbers and trimming any extra spaces)
    df["National Occupational Classification"] = df["National Occupational Classification"].str.strip().str[:-7]

    # Ensure "VALUE" column is treated as numeric, coercing errors to NaN
    df["VALUE"] = pd.to_numeric(df["VALUE"], errors="coerce")

    # Filter data for Software Engineers with Bachelor's degree as job vacancy characteristic
    filtered_df = df[
        (df["National Occupational Classification"] == "Software engineers and designers") &
        (df["Job vacancy characteristics"] == "Bachelor's degree") &
        (df["Statistics"] == "Average offered hourly wage") &
        (df["VALUE"].notna())  # Ensure VALUE is not empty
    ]

    # Keep relevant columns
    filtered_df = filtered_df[["National Occupational Classification", "Job vacancy characteristics", "Statistics", "VALUE"]]

    if filtered_df.empty:
        print("No relevant data found.")
    else:
        filtered_df.to_csv("q1_data.csv", index=False, encoding="utf-8-sig")
        print("Filtered data saved successfully to 'q1_data.csv'.")

if __name__ == "__main__":
    main()
