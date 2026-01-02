import math

# Simulated sensor data processing for environmental monitoring system
def analyze_readings(readings):
    filtered = [x for x in readings if 10 <= x <= 100]
    smoothed = []
    for i in range(len(filtered)):
        window = filtered[max(0, i-2):min(i+3, len(filtered))]
        smoothed.append(sum(window) / len(window))
    return smoothed

# Irrelevant helper: computes statistical dispersion (not used in final result)
def calculate_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

# Core transformation pipeline
def transform_sequence(seq, key_factor):
    processed = []
    temp_buffer = []
    for val in seq:
        if val % 2 == 0:
            temp_buffer.append(val * key_factor)
        else:
            temp_buffer.append(int(math.sqrt(val)) * 3)
    processed.extend(temp_buffer[::-1])  # Reverse and extend
    
    # Dead code path - never executed due to prior logic
    if len(processed) > 1000:
        fallback = [x >> 2 for x in processed]
        return fallback[::3]
    
    return processed[:50]  # Truncate to first 50 elements

# Secondary metric calculator (distractor)
def compute_robustness_index(values):
    if not values:
        return 0
    sorted_vals = sorted(values)
    q1 = sorted_vals[len(sorted_vals)//4]
    q3 = sorted_vals[3*len(sorted_vals)//4]
    iqr = q3 - q1
    return round(iqr * 1.5, 3)

# Main evaluation logic with multiple concepts
metric_data = [64, 81, 36, 49, 25, 16, 9, 4, 1, 100]
base_threshold = 5
aux_cache = []

for i, val in enumerate(metric_data):
    if i % 3 == 0:
        aux_cache.append(val + 2)
    elif i % 3 == 1:
        aux_cache.append(val - 1)
    else:
        aux_cache.append(val * 2)

# Unused intermediate structure (red herring)
aggregated_stats = {
    'sum': sum(aux_cache),
    'max': max(aux_cache),
    'min': min(aux_cache),
    'range': max(aux_cache) - min(aux_cache)
}

# Key transformation using list comprehension and slicing
def evaluate_performance(data, threshold):
    # Step 1: Transform based on threshold
    adjusted = [x - threshold for x in data]
    
    # Step 2: Apply non-linear scaling
    scaled = [int(math.log(x + 1, 2)) if x > 0 else 0 for x in adjusted]
    
    # Step 3: Accumulate with offset
    cumulative = []
    acc = 0
    for v in scaled:
        acc += v
        cumulative.append(acc)
    
    # Step 4: Extract pattern using slicing
    pattern = cumulative[1::2]  # Every second element starting from index 1
    
    # Step 5: Final reduction
    total_impact = sum(pattern)
    
    # Step 6: Apply bonus logic (only if conditions met)
    bonus = 0
    if len(pattern) >= 4 and pattern[0] < pattern[-1]:
        bonus = 10
    
    # Step 7: Combine results
    raw_score = total_impact + bonus
    
    # Step 8: Normalize through bit manipulation (obscure but valid)
    normalized = (raw_score << 1) ^ 7  # Shift and XOR
    
    # Final computation
    final_normalized = normalized + (len(data) // 2)
    return final_normalized

# Execution point of interest
final_score = evaluate_performance(metric_data, base_threshold)

# Print result as required
print(f"Result: {final_score}")