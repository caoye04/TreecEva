from itertools import combinations
from functools import reduce

# Simulate sensor data with noise and valid readings
def preprocess_sensor_data(raw):
    filtered = [x for x in raw if x > 0]
    normalized = [round(x / sum(filtered), 4) for x in filtered]
    return normalized

# Misleading helper: computes pairwise products but not used in final result
def compute_pairwise_products(lst):
    return [a * b for a, b in combinations(lst, 2)]

# Core scoring logic
def calculate_element_score(val, weight):
    return val ** 2 * weight if val > 0.1 else val * weight * 0.5

def calculate_final_score(data, weights):
    # Irrelevant intermediate: tracking indices (not used)
    index_log = []
    temp_results = []
    
    for i, (d, w) in enumerate(zip(data, weights)):
        index_log.append(i)  # Distractor: logged but unused
        if d < 0.05:
            continue  # Skip noisy low readings
        score = calculate_element_score(d, w)
        temp_results.append(score)
    
    # Real computation
    total_score = reduce(lambda acc, x: acc + x, temp_results, 0.0)
    
    # Dead code path: never executed due to data constraints
    if len(temp_results) > 100:
        backup = sum(compute_pairwise_products(temp_results))
        total_score = max(total_score, backup)
    
    return round(total_score, 4)

# Main execution
raw_sensor_readings = [0.12, 0.0, 0.33, 0.01, 0.51, 0.04, 0.67, 0.22, 0.11, 0.0]
distortion_factor = 1.07  # Unused parameter (red herring)
scaling_matrix = [[1, 2], [3, 4]]  # Irrelevant data structure

processed_data = preprocess_sensor_data(raw_sensor_readings)
weights = [1, 2, 1, 3, 2, 1, 4]  # Weight vector aligned to first 7 valid elements

# Extend weights to match data length with filler zeros (only first 7 used)
weights = weights + [0] * (len(processed_data) - len(weights)) if len(processed_data) > len(weights) else weights

# Key statement
total_score = calculate_final_score(processed_data, weights)

print(f"Result: {total_score}")