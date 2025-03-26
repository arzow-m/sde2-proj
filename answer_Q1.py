
import sys
import pandas as pd

def main(argv):
    print("Analyzing filtered job vacancy data...")

    if len(argv) != 2:
        print("Incorrect number of arguments", file=sys.stderr)
        sys.exit(1)

    input_wage_threshold = float(argv[1])  # User inputs wage threshold

    # Load pre-filtered job vacancy data
    try:
        df = pd.read_csv("q1_data.csv", encoding="utf-8-sig")
    except Exception as err:
        print(f"Unable to open file 'q1_data.csv': {err}", file=sys.stderr)
        sys.exit(1)

    if df.empty:
        print("No job vacancies found that match the criteria.")
        sys.exit(0)

    # Calculate the percentage of job vacancies above the wage threshold
    total_vacancies = len(df)
    high_wage_vacancies = len(df[df["VALUE"] > input_wage_threshold])

    if total_vacancies > 0:
        percentage = (high_wage_vacancies / total_vacancies) * 100
        print(f"Percentage of Software Engineer job vacancies requiring a Bachelor's degree and offering above ${input_wage_threshold}/hour: {percentage:.2f}%")
    else:
        print("No job vacancies found that match the criteria.")

if __name__ == "__main__":
    main(sys.argv)
