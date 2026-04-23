import pandas as pd

def clean_data(input_file, output_file):

    df = pd.read_csv(input_file)

    print("Original Data:")
    print(df)

    df = df.drop_duplicates()

    df['Age'] = df['Age'].fillna(df['Age'].mean())

    df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

    df = df.dropna(subset=['Name'])

    df.to_csv(output_file, index=False)

    print("Cleaned data saved successfully!")

    return df   # ⭐ VERY IMPORTANT


# STEP 1: run cleaning ONCE
df = clean_data("data/raw_data.csv", "output/cleaned_data.csv")


# STEP 2: generate report from cleaned data
report = f"""
DATA CLEANING REPORT
----------------------
Total Rows: {len(df)}
Average Age: {df['Age'].mean():.2f}
Average Salary: {df['Salary'].mean():.2f}
Unique Departments: {df['Department'].nunique()}
"""

with open("output/report.txt", "w") as f:
    f.write(report)

print(report)