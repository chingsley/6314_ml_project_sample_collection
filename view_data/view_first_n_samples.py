import pandas as pd

# Define file paths
input_csv = "data/python_code_sample.csv"  # The large CSV file
# output_csv = "data/python_code_last_1000.csv"  # Output file with last 1000 rows
N = 10000
output_csv = f"data/python_code_first_{N}.csv"  # Output file with last 1000 rows

# # Read only the required last 1000 rows
# df = pd.read_csv(input_csv)

# Read CSV and select only relevant columns
df = pd.read_csv(input_csv, usecols=["problem_id", "code_v0", "code_v1"])

# Extract last 1000 rows and save to a new CSV file
# df.tail(1000).to_csv(output_csv, index=False)
df.head(N).to_csv(output_csv, index=False)

# print(f"Saved the last 1000 rows to {output_csv}")
print(f"Saved the last {N} rows to {output_csv}")
