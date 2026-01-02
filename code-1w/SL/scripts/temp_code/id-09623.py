def normalize_values(raw_inputs):
    min_val = min(raw_inputs)
    max_val = max(raw_inputs)
    return [(x - min_val) / (max_val - min_val) if max_val != min_val else 0 for x in raw_inputs]

def calculate_entropy(data):
    from math import log2
    frequency = {}
    for item in data:
        frequency[item] = frequency.get(item, 0) + 1
    total = len(data)
    entropy = 0
    for count in frequency.values():
        prob = count / total
        if prob > 0:
            entropy -= prob * log2(prob)
    return entropy

# Simulated sensor readings and metrics
temperature_readings = [23.4, 25.1, 24.8, 26.0, 22.7, 25.3, 24.9, 25.1, 24.2, 23.9]
humidity_readings = [45, 47, 50, 52, 48, 55, 53, 49, 46, 51]
pressure_readings = [1013, 1015, 1012, 1016, 1014, 1011, 1013, 1017, 1015, 1010]

# Normalize all sensor streams
norm_temp = normalize_values(temperature_readings)
norm_humidity = normalize_values(humidity_readings)
norm_pressure = normalize_values(pressure_readings)

# Compute derived features (some are distractions)
drift_temp = sum(norm_temp[i] - norm_temp[i-1] for i in range(1, len(norm_temp)))
redundancy_check = calculate_entropy([round(x, 1) for x in norm_temp])

# Assemble multi-dimensional normalized data
normalized_data = list(zip(norm_temp, norm_humidity, norm_pressure))

# Define metric weights (key part of logic)
metric_weights = [0.6, 0.3, 0.1]  # Temperature prioritized

# Auxiliary function to simulate system health scoring
def apply_weighted_sum(weights, data_matrix):
    totals = []
    for row in data_matrix:
        weighted_sum = sum(w * x for w, x in zip(weights, row))
        totals.append(weighted_sum)
    return totals

# Evaluate overall performance using weighted aggregation
def evaluate_performance(weights, dataset):
    scores = apply_weighted_sum(weights, dataset)
    base_score = sum(scores) / len(scores)
    
    # Distraction: adjust based on stability (not actually used in final answer)
    temp_stability = 1 - abs(drift_temp) / 10
    penalty_factor = 0.95 if temp_stability < 0.9 else 1.0
    
    # Final score before unused adjustments
    final_raw = base_score * 100
    
    # Additional unused transformations (dead code paths)
    if final_raw > 75:
        adjusted = final_raw * 0.9 + 10
    elif final_raw < 60:
        adjusted = final_raw * 1.1
    else:
        adjusted = final_raw
    
    # Irrelevant bitwise obfuscation (distraction only)
    magic_offset = (len(norm_pressure) ^ 5) & 3
    cryptic_flag = (0x1A << 2) | 0x0F
    
    return final_raw  # Only final_raw matters

# Key execution point
final_score = evaluate_performance(metric_weights, normalized_data)
print(f"Result: {final_score}")