import itertools

def preprocess_readings(raw_readings):
    filtered = [x for x in raw_readings if x > 0]
    smoothed = []
    for i in range(len(filtered)):
        window = filtered[max(0, i-1):i+2]
        smoothed.append(sum(window) / len(window))
    return smoothed

def normalize_values(data):
    max_val = max(data)
    min_val = min(data)
    range_val = max_val - min_val
    normalized = [(x - min_val) / range_val for x in data]
    
    # Distractor: irrelevant transformation
    inverted = [1.0 - x for x in normalized]
    shuffled = list(itertools.islice(itertools.permutations(normalized[:3]), 0, 1))[0] if len(normalized) >= 3 else normalized
    
    return normalized

def calculate_entropy(arr):
    # This function is defined but not used
    from math import log
    total = sum(arr)
    if total == 0:
        return 0
    probabilities = [x / total for x in arr]
    entropy = -sum(p * log(p) for p in probabilities if p > 0)
    return entropy

def analyze_distribution(values):
    cumulative = 0
    for i, v in enumerate(values):
        if i % 2 == 0:
            cumulative += v * (i + 1)
        else:
            cumulative -= v
    
    # Secondary distractor computation
    pair_sums = [a + b for a, b in itertools.pairwise(values)]
    avg_pair = sum(pair_sums) / len(pair_sums) if pair_sums else 0
    
    # Final result based only on cumulative
    return int(cumulative * 100)

# Main execution
raw_sensor_data = [12, 15, 8, 23, 17, 19, 14, 20]

# Irrelevant preprocessing chain
processed_data = preprocess_readings(raw_sensor_data)
denoised_signal = [x * 0.9 for x in processed_data]  # Unused downstream

normalized_data = normalize_values(processed_data)

# Extraneous variable
aggregated_metric = sum([x**2 for x in normalized_data]) ** 0.5

# Key statement
equilibrium_score = analyze_distribution(normalized_data)

# Print final result
print(f"Result: {equilibrium_score}")