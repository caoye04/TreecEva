def analyze_metrics(data, threshold=5.0):
    above_threshold = [x for x in data if x > threshold]
    below_threshold = [x for x in data if x <= threshold]
    
    # Irrelevant transformation
    processed = list(map(lambda x: x ** 0.5 + 2, data))
    normalized = [round(p, 3) for p in processed]

    # Distractor: complex but unused structure
    stats_summary = {
        'count': len(data),
        'valid': len(above_threshold),
        'invalid': len(below_threshold),
        'ratio': len(above_threshold) / len(data) if data else 0
    }

    # Real computation path begins
    filtered = [x for x in data if x >= threshold]
    squared_filtered = [x ** 2 for x in filtered]
    return squared_filtered

# Simulate sensor readings
data_points = [3.4, 6.1, 7.8, 4.2, 9.0, 5.5, 2.1, 8.3]

# Unused helper — distractor
compute_deviation = lambda seq, base: sum((x - base) ** 2 for x in seq)

# Weight assignment with red herring
all_weights = [0.1, 0.25, 0.15, 0.2, 0.3]
dropped_weight = all_weights.pop()  # This modifies list but value not used directly

# Actual weights used
weights = [0.2, 0.3, 0.1, 0.4]

# Misleading intermediate calculation
baseline = sum(data_points) / len(data_points)
adjusted_values = [val - baseline + 1.5 for val in data_points]

# Key processing steps
results = analyze_metrics(data_points, threshold=5.0)

# Another distraction: zipping unrelated sequences
paired = list(zip(results[:3], adjusted_values[:3]))
transformed_pairs = [a * b for a, b in paired]

# Real aggregation logic
def compute_aggregate(values, w):
    if len(values) != len(w):
        min_len = min(len(values), len(w))
        values = values[:min_len]
        w = w[:min_len]
    
    total = 0.0
    for i in range(len(values)):
        total += values[i] * w[i]
    return int(total)  # Final answer is integer

# Secondary distraction: slicing and enumeration
enumerated_results = list(enumerate(results[::-1]))
reverse_scaled = [idx * val / 2 for idx, val in enumerated_results]

final_score = compute_aggregate(results, weights)

print(f"Target result: {final_score}")