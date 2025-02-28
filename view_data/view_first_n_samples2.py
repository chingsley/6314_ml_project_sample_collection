import pandas as pd

# Define file paths and parameters
input_csv = "data/python_code_sample.csv"
N = 10000  # Number of top rows to keep
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
