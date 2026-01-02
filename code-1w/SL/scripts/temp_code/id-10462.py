from collections import defaultdict
import math

def preprocess_entries(raw_entries):
    # Irrelevant transformation: counts lengths but not used in final logic
    length_count = defaultdict(int)
    for entry in raw_entries:
        length_count[len(entry)] += 1

    cleaned = []
    temp_buffer = []
    for item in raw_entries:
        stripped = item.strip().lower()
        if 'error' not in stripped and stripped != '':
            temp_buffer.append(stripped)
    
    # Real processing: split valid lines by comma and flatten
    for line in temp_buffer:
        parts = line.split(',')
        for part in parts:
            clean_part = part.strip()
            if clean_part.isnumeric():
                cleaned.append(int(clean_part))
    return cleaned

def analyze_distribution(values):
    stats = defaultdict(float)
    total = sum(values)
    count = len(values)
    stats['mean'] = total / count if count else 0
    
    # Distraction: variance calculated but not directly used
    variance = sum((x - stats['mean']) ** 2 for x in values) / count if count else 0
    stats['variance'] = variance
    
    # Semi-relevant: find outliers beyond 1.5 * IQR (simplified here)
    sorted_vals = sorted(values)
    q1 = sorted_vals[count // 4]
    q3 = sorted_vals[3 * count // 4]
    iqr = q3 - q1
    lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    
    filtered = [v for v in values if lower <= v <= upper]
    stats['filtered_count'] = len(filtered)
    
    # Dummy metric
    stats['peak_ratio'] = (max(filtered) / min(filtered)) if filtered else 0
    
    return stats, filtered

def calculate_final_score(data_chunk):
    interim_results = []
    scaling_factor = 1.75
    
    for val in data_chunk:
        # Complex transformation chain
        transformed = math.log(val + 1) * scaling_factor
        if transformed > 3.0:
            transformed -= 1.2
        elif transformed < 1.0:
            transformed += 0.8
        interim_results.append(round(transformed, 3))
    
    # Aggregation with distraction
    base_sum = sum(interim_results)
    penalty = len([r for r in interim_results if r > 4.0]) * 0.5
    bonus = len([r for r in interim_results if r < 2.0]) * 0.3
    
    # Final computation
    score = base_sum - penalty + bonus
    return int(round(score))

# Main execution
raw_input_data = [
    " 123, 456, error_code, 789 ",
    "",
    " 23, 45, 67, 89 ",
    "debug: off, 100, 200, 300 ",
    " 50, 50, 50, 9999 "  # 9999 will be filtered as outlier
]

# Step 1: Preprocess
processed_data = preprocess_entries(raw_input_data)

# Step 2: Analyze distribution (includes filtering)
distribution_metrics, refined_data = analyze_distribution(processed_data)

# Step 3: Calculate final score
final_score = calculate_final_score(refined_data)

# Output result
print(f"Result: {final_score}")