import math

def preprocess_records(raw_entries):
    # Irrelevant transformation (not used in final path)
    temp_scale = [x * 1.5 for x in raw_entries if x > 10]
    filtered = [x for x in raw_entries if x % 2 == 1]  # Keep only odd values
    shifted = [x + 5 for x in filtered][:len(filtered)//2]  # Partial shift (distractor)
    return filtered  # Only filtered matters


def validate_entry(value):
    return 0 <= value <= 100


def calculate_ranking(data_slice):
    # Misleading normalization
    normalized = [round(x / max(data_slice), 2) for x in data_slice]
    weights = [1.1 if i % 2 == 0 else 0.9 for i in range(len(normalized))]
    weighted_vals = [n * w for n, w in zip(normalized, weights)]
    
    # Core logic: median of top half after sorting
    sorted_vals = sorted(weighted_vals, reverse=True)
    midpoint = len(sorted_vals) // 2
    top_half_avg = sum(sorted_vals[:midpoint]) / midpoint if midpoint > 0 else 0
    
    # Secondary distraction: entropy calculation (unused)
    entropy = 0
    for p in normalized:
        if p > 0:
            entropy -= p * math.log(p)
    
    # Actual answer contributor
    adjustment = 0.75 if len(data_slice) > 4 else 1.0
    score = int(top_half_avg * 100 * adjustment)
    return score

# Main execution flow
raw_input_data = [12, 45, 23, 67, 34, 89, 13, 27]
disregarded_threshold = 30

# Unused filtering branch (dead path)
if any(x < disregarded_threshold for x in raw_input_data):
    alternate_route = [x**2 for x in raw_input_data if x < disregarded_threshold]

processed_data = preprocess_records(raw_input_data)

# Critical computation point
final_score = calculate_ranking(processed_data)

# Output result
print(f"Result: {final_score}")