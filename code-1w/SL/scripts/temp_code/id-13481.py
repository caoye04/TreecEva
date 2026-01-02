import itertools

# Simulated sensor array data from a drone flight
sensor_readings = [104, 92, 115, 88, 97, 109, 96, 111]

def analyze_stability(data):
    # Irrelevant transformation: frequency domain mockup
    freq_components = [abs((d - 100) ** 2) for d in data]  # distractor
    moving_avg = [sum(data[i:i+3]) // 3 for i in range(len(data)-2)]
    variance_proxy = sum((x - sum(data)/len(data))**2 for x in data) / len(data)
    return variance_proxy < 64  # threshold check (not used directly)

# Redundant function that computes unused health metric
def compute_health_index(values):
    if len(values) == 0:
        return 0
    base = sum(v ** 0.5 for v in values if v > 0) / len(values)
    adjustment = 1 + (len([v for v in values if v > 100]) / len(values))
    return round(base * adjustment, 2)

# Core evaluation logic (obscured by noise)
def evaluate_performance(metrics, weights):
    weighted_sum = 0
    for i in range(len(metrics)):
        if i % 2 == 0:
            weighted_sum += metrics[i] * weights[i] * 0.9  # even indices discounted
        else:
            weighted_sum += metrics[i] * weights[i] * 1.1  # odd indices amplified
    
    # Distractor: unused combinatorial analysis
    combinations = list(itertools.combinations(weights, 3))
    avg_combo = sum(sum(c) for c in combinations) / len(combinations) if combinations else 0
    
    # Real computation continues
    penalty = 0
    for val in metrics:
        if val > 100:
            penalty += (val - 100) * 0.5
    
    result = weighted_sum - penalty
    return int(result)

# Irrelevant preprocessing: slicing and filtering noise
deviations = [abs(x - 100) for x in sensor_readings]
high_dev = deviations[2:6]  # slice not used later
inverted_seq = sensor_readings[::-1]
paired_diffs = [inverted_seq[i] - inverted_seq[i+1] for i in range(len(inverted_seq)-1)]

# Key data structures
metrics = [
    sensor_readings[0],           # launch stability
    deviations[1],                # early deviation
    compute_health_index([92,88]), # fake health index (distractor call)
    105,                          # mid-flight target
    deviations[4],                # post-turn error
    98                            # landing precision
]

weights = [0.8, 1.2, 0.5, 1.0, 0.9, 1.1]

# Unused recursive helper (dead path)
def recursive_dampen(val, depth=0):
    if depth >= 3 or val <= 50:
        return val
    return recursive_dampen(val * 0.7, depth + 1)

# Unused set operations (distractor)
unique_readings = set(sensor_readings)
expected_range = set(range(85, 120))
overlap_count = len(unique_readings & expected_range)  # computed but unused

# Main logic obscured in middle of noise
temp_adjusted = [x * 1.05 for x in metrics if x > 90]
buffer_slice = temp_adjusted[1:4]

final_score = evaluate_performance(metrics, weights)

# More distractions
summary_stats = {
    'max': max(sensor_readings),
    'min': min(sensor_readings),
    'range': max(sensor_readings) - min(sensor_readings)
}

# Final output
print(f"Result: {final_score}")