from collections import defaultdict
import itertools

# Simulate sensor data aggregation and weighted scoring with noise filtering
def collect_sensor_data():
    raw_data = [45, 32, 78, 33, 45, 88, 32, 12, 45, 78, 91, 12]
    frequency = defaultdict(int)
    for val in raw_data:
        frequency[val] += 1

    # Filter out rare readings (appearing only once)
    filtered = [val for val in raw_data if frequency[val] > 1]
    return list(set(filtered))  # Remove duplicates while preserving intent

# Misleading auxiliary function that computes unused metric
def compute_variance(values):
    mean = sum(values) / len(values)
    squared_diffs = [(v - mean) ** 2 for v in values]
    var = sum(squared_diffs) / len(squared_diffs)
    return var  # Computed but not used

# Auxiliary distraction: generate all pairs (not ultimately relevant)
def generate_combinations(vals):
    pairs = list(itertools.combinations(vals, 2))
    count_large_sums = sum(1 for a, b in pairs if a + b > 100)
    return count_large_sums  # Used to create distraction

# Core logic: calculate score using weights on cleaned data
def calculate_final_score(data, weights):
    sorted_data = sorted(data)
    weighted_sum = 0
    normalization_factor = sum(weights)
    
    # Apply weights in reverse order to largest values
    for i, val in enumerate(sorted_data):
        weighted_sum += val * weights[-(i % len(weights)) - 1]
    
    adjusted_score = weighted_sum / normalization_factor
    
    # Extra computation that looks important but doesn't affect result
    outlier_count = sum(1 for x in data if x < 20)
    temp_adjustment = outlier_count * 0.5
    
    # Final adjustment based on data stability (dummy condition)
    if len(data) % 2 == 0:
        adjusted_score += 1.0  # Minor deterministic bump
    
    return int(adjusted_score)  # Ensure integer result

# Main execution flow
data = collect_sensor_data()
weights = [0.1, 0.3, 0.4, 0.2]

# Distraction block: unused computations to increase cognitive load
variance = compute_variance(data)
data_pairs_count = generate_combinations(data)
shadow_copy = data.copy()
shadow_copy.append(999)  # Dead-end mutation

# Key statement
final_score = calculate_final_score(data, weights)

# Additional red herring: string processing unrelated to final score
log_tag = "SENSOR_LOG_"
segments = log_tag.split("_")
joined = "-".join([s for s in segments if s]) + f"_{len(data)}"

print(f"Result: {final_score}")