import pandas as pd
import os
import re

# Load CSV
df = pd.read_csv("data/python_code_first_10000.csv")

# Filter Accepted Samples
df = df[(df['Status_v0'] == 'Accepted') & (df['Status_v1'] == 'Accepted')]
df = df[df['improvement_frac'] > 0]  # Ensure improvement exists

# Define classification rules
def classify_code(code):
    if re.search(r'list\(|\.copy\(|deepcopy\(', code):
        return "ExtraUsageOfArrays"
    if re.search(r'for .* in range\(.*\):[^\n]*$', code) and 'break' not in code:
        return "LackingBreak"
    if re.search(r'for .* in range\(.*\):.*=.*\1', code):
        return "NotCaching"
    if re.search(r'for .* in range\(.*\):.*for .* in range\(.*\):', code):
        return "OverUseOfLoops"
    if re.search(r'int\(|float\(|str\(|list\(|tuple\(', code):
        return "UnnecessaryTypeConversion"
    return None

# Process and save 10 samples per class
samples_per_class = 10
selected_samples = {c: [] for c in ["ExtraUsageOfArrays", "LackingBreak", "NotCaching", "OverUseOfLoops", "UnnecessaryTypeConversion"]}

for _, row in df.iterrows():
    category = classify_code(row['code_v0'])
    if category and len(selected_samples[category]) < samples_per_class:
        function_name = f"smelly_function_{row['submission_id_v0']}"
        os.makedirs(f"dataset/{category}/{function_name}", exist_ok=True)
        
        with open(f"dataset/{category}/{function_name}/smelly_{function_name}.py", "w") as f:
            f.write(row['code_v0'])
        with open(f"dataset/{category}/{function_name}/refactored_{function_name}.py", "w") as f:
            f.write(row['code_v1'])
        
        selected_samples[category].append(function_name)
    
    if all(len(samples) >= samples_per_class for samples in selected_samples.values()):
        break

print("Gold samples extracted successfully!")