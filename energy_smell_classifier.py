import os
import pandas as pd
import ast
import shutil
import argparse 
import autopep8
from pathlib import Path


def clean_code(code):
    """Format Python code using autopep8"""
    try:
        return autopep8.fix_code(code, options={'aggressive': 1})
    except Exception as e:
        print(f"Formatting error: {str(e)}")
        return code  # Fallback to original code


# Create mapping between smell types and explanations
SMELL_EXPLANATIONS = {
    "NotCaching": "Avoided redundant computations through caching",
    "OverUseOfLoops": "Optimized loop usage for better performance",
    "ExtraUsageOfArrays": "Replaced array with more efficient data structure",
    "UnnecessaryTypeConversion": "Removed unnecessary type conversions",
    "LackingBreak": "Added early loop termination with break",
    "Unknown": "Unclassified energy optimization"
}

def analyze_code_pair(code_v0, code_v1):
    """Rule-based classifier using code patterns and metrics"""
    # Basic metrics
    metrics = {
        'loops_removed': code_v0.count('for ') - code_v1.count('for '),
        'breaks_added': code_v1.count('break') - code_v0.count('break'),
        'cache_keywords': any(kw in code_v1 for kw in ['cache', 'memo']),
        'type_conversions': code_v0.count('int(') - code_v1.count('int(')
    }
    
    return metrics

def classify_row(row):
    """Classify energy smell type based on metrics and code patterns"""
    code_v0 = row['code_v0']
    code_v1 = row['code_v1']
    
    # Get code metrics
    metrics = analyze_code_pair(code_v0, code_v1)
    
    # Classification rules (ordered by priority)
    if (row['memory_v1'] < row['memory_v0']) and metrics['cache_keywords']:
        return "NotCaching"
        
    if (row['code_v1_loc'] < row['code_v0_loc']) and metrics['loops_removed'] > 0:
        return "OverUseOfLoops"
        
    if ('.append(' in code_v0) and ('.append(' not in code_v1):
        return "ExtraUsageOfArrays"
        
    if metrics['type_conversions'] > 0 and row['cpu_time_v1'] < row['cpu_time_v0']:
        return "UnnecessaryTypeConversion"
        
    if metrics['breaks_added'] > 0 and row['cpu_time_v1'] < row['cpu_time_v0']:
        return "LackingBreak"
        
    return "Unknown"

def process_chunk(chunk, output_dir="EnergySmells"):
    """Process a chunk of 50 rows"""
    # Filter accepted samples
    chunk = chunk[(chunk['status_v0'] == 'Accepted') & 
                (chunk['status_v1'] == 'Accepted')]
    
    for _, row in chunk.iterrows():
        try:
            # Classify energy smell
            smell_type = classify_row(row)
            explanation = SMELL_EXPLANATIONS.get(smell_type, "Unclassified optimization")
            
            # Create directory structure
            smell_dir = Path(output_dir) / smell_type.replace(' ', '_')
            smell_dir.mkdir(parents=True, exist_ok=True)
            
            # Generate filenames
            base_name = f"sample_{row['submission_id_v0']}"
            sanitized_explanation = explanation.replace(' ', '_').replace('(', '').replace(')', '')
            
            # Write files
            with open(smell_dir / f"{base_name}_{sanitized_explanation}.py", 'w') as f:
                f.write(clean_code(row['code_v0']))
                
            with open(smell_dir / f"{base_name}_refactored_{sanitized_explanation}.py", 'w') as f:
                f.write(clean_code(row['code_v1']))
                
        except Exception as e:
            print(f"Error processing row {row.name}: {str(e)}")


def main(input_csv, chunk_size=200):  # ← Modified chunk size
    """Process CSV in chunks of 'chunk_size' rows"""
    if Path("EnergySmells").exists():
        shutil.rmtree("EnergySmells")

    total_processed = 0    
    for chunk in pd.read_csv(input_csv, chunksize=chunk_size):
        process_chunk(chunk)
        total_processed += len(chunk)
        print(f"Processed {total_processed} rows...")
        
    print(f"Processed {Path(input_csv).name} with chunk size {chunk_size}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_csv", help="Path to input CSV")
    parser.add_argument("--chunk_size", type=int, default=200, 
                      help="Rows per chunk (default: 200)")
    args = parser.parse_args()
    
    main(args.input_csv, args.chunk_size)
