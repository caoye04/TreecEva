from itertools import combinations
from collections import defaultdict

# Simulate sensor data with noise and redundancy
def generate_sensor_readings():
    base_values = [2.5, 3.0, 4.5, 5.0, 6.5]
    readings = []
    for val in base_values:
        readings.extend([val] * 3)
    return readings

# Noise injection (irrelevant to final result)
def add_noise(data, factor=0.1):
    import random
    random.seed(42)
    return [x + random.uniform(-factor, factor) for x in data]

# Filtering outliers (semi-relevant but bypassed in logic path)
def filter_outliers(data, threshold=1.0):
    mean = sum(data) / len(data)
    return [x for x in data if abs(x - mean) < threshold]

# Core processing function
def process_sensor_data(raw):
    # Unnecessary transformation chain
    scaled = [x * 2 for x in raw]
    shifted = [x - 1 for x in scaled]
    normalized = [x / 2 for x in shifted]  # This just recovers original values
    
    # Distractor: complex set operations with unused result
    unique_vals = set(normalized)
    pairwise_sums = {a + b for a, b in combinations(unique_vals, 2)}
    large_sums = {s for s in pairwise_sums if s > 8.0}  # Unused
    
    # Actual relevant aggregation
    count_dict = defaultdict(int)
    for val in normalized:
        count_dict[val] += 1
    
    # Weighting mechanism
    weights = {v: 1 + (0.1 * c) for v, c in count_dict.items()}
    weighted_sum = sum(v * weights[v] for v in count_dict)
    
    # Red herring normalization
    temp_factor = len(pairwise_sums) if pairwise_sums else 1  # Used nowhere
    debug_log = f'Processed {len(count_dict)} unique values'  # Dead code
    
    return list(count_dict.keys()), weighted_sum

# Final scoring logic
def calculate_final_score(data_tuple):
    values, base_score = data_tuple
    
    # Irrelevant combinatorial check
    if len(values) >= 3:
        triplets = list(combinations(values, 3))
        valid_triplets = [t for t in triplets if sum(t) > 10]
        adjustment = len(valid_triplets) * 0.5
    else:
        adjustment = 0
    
    # Dummy dictionary operation
    score_map = {i: base_score / (i + 1) for i in range(3)}
    fallback = score_map.get(9, 0)  # Irrelevant lookup
    
    # Key calculation
    multiplier = 2 if any(v > 5 for v in values) else 1
    final_score = (base_score + adjustment) * multiplier
    
    # Extra distraction
    metadata_summary = {
        'version': '2.1',
        'calibrated': True,
        'checksum': hash(str(values)) % 1000
    }
    
    return final_score

# Execution flow
raw_sensor_data = generate_sensor_readings()
noisy_data = add_noise(raw_sensor_data)  # Not actually used
clean_data = filter_outliers(noisy_data)  # Not used either
primary_data = generate_sensor_readings()  # Original clean source
processed_data = process_sensor_data(primary_data)
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")