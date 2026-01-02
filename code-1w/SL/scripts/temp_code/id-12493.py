from collections import defaultdict
import math

def preprocess_records(raw_entries):
    # Irrelevant transformation: counts per category (not used in final score)
    category_count = defaultdict(int)
    for entry in raw_entries:
        category_count[entry['category']] += 1

    # Relevant processing: extract and normalize values
    values = [e['value'] for e in raw_entries if e['active']]
    normalized = [v / max(values) * 100 for v in values]  # Scale to 0-100

    stats = {}
    stats['mean'] = sum(normalized) / len(normalized)
    stats['spread'] = max(normalized) - min(normalized)
    
    # Dead code path: never accessed later
    if len(normalized) > 100:
        outlier_count = len([v for v in normalized if v > 95])
        stats['outlier_ratio'] = outlier_count / len(normalized)
    else:
        stats['placeholder'] = -1  # Unused field

    return normalized, stats

def calculate_final_score(data_list):
    # Additional distraction: unused helper function
    def smooth_noise(signal):
        return [signal[i] + 0.1 * math.sin(i) for i in range(len(signal))]

    base = sum(data_list)
    penalty = 0
    threshold = 75

    # Logical chain with multiple steps
    above_threshold = [x for x in data_list if x > threshold]
    if len(above_threshold) >= 3:
        bonus_factor = 1.2
        adjustment = len(above_threshold) * 0.5
    else:
        bonus_factor = 1.0
        adjustment = -2.0

    # Compute cluster density (only matters if dense clusters exist)
    sorted_vals = sorted(data_list)
    gaps = [sorted_vals[i+1] - sorted_vals[i] for i in range(len(sorted_vals)-1)]
    dense_regions = sum(1 for g in gaps if g < 5)

    if dense_regions > 4:
        penalty -= 3  # Reduce penalty for high density
    else:
        penalty += 1

    # Final computation
    raw_score = base * bonus_factor + adjustment + penalty
    return int(round(raw_score))

# Main execution
raw_data = [
    {'value': 45, 'category': 'A', 'active': True},
    {'value': 67, 'category': 'B', 'active': True},
    {'value': 89, 'category': 'A', 'active': True},
    {'value': 92, 'category': 'C', 'active': True},
    {'value': 78, 'category': 'B', 'active': True},
    {'value': 94, 'category': 'A', 'active': True},
    {'value': 33, 'category': 'D', 'active': False},  # Inactive, filtered out
    {'value': 88, 'category': 'B', 'active': True},
    {'value': 76, 'category': 'A', 'active': True},
    {'value': 91, 'category': 'C', 'active': True}
]

processed_data, summary_stats = preprocess_records(raw_data)
intermediate_result = [math.sqrt(x) for x in processed_data if x > 50]  # Distractor calculation

final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")