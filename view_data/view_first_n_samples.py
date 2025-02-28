import pandas as pd

# Define file paths
input_csv = "data/python_code_sample.csv"  # The large CSV file
# output_csv = "data/python_code_last_1000.csv"  # Output file with last 1000 rows
N = 10000
output_csv = f"data/python_code_first_{N}.csv"  # Output file with last 1000 rows

# # Read only the required last 1000 rows
# df = pd.read_csv(input_csv)

# Read CSV and select only relevant columns
df = pd.read_csv(input_csv)

# Extract first 1000 rows and save to a new CSV file
# df.tail(1000).to_csv(output_csv, index=False)
df.head(N).to_csv(output_csv, index=False)

# print(f"Saved the last 1000 rows to {output_csv}")
print(f"Saved the last {N} rows to {output_csv}")


import pandas as pd

# Define file paths and parameters
input_csv = "data/python_code_sample.csv"
N = 1000  # Number of top rows to keep
output_csv = f"data/python_code_top_{N}_improvement.csv"  # New output filename

# Read CSV
df = pd.read_csv(input_csv)

# 1. Filter rows with improvement_frac >= 10
filtered_df = df[df['improvement_frac'] >= 10]

# 2. Sort by improvement_frac descending and take top N rows
sorted_df = filtered_df.sort_values(by='improvement_frac', ascending=False)
top_df = sorted_df.head(N)

# Save to new CSV
top_df.to_csv(output_csv, index=False)

print(f"Saved top {len(top_df)} rows with ≥10% improvement to {output_csv}")
print(f"Minimum improvement in saved data: {top_df['improvement_frac'].min()}%")
print(f"Maximum improvement in saved data: {top_df['improvement_frac'].max()}%")
