import itertools

def preprocess_readings(raw_data):
    # Normalize sensor data by removing negative values and capping at 100
    cleaned = [max(0, min(x, 100)) for x in raw_data]
    smoothed = [sum(cleaned[i:i+3]) / 3 for i in range(len(cleaned) - 2)]
    return [round(x, 1) for x in smoothed]

# Simulate environmental sensor inputs (mock data)
sensor_inputs = [105, -20, 45, 67, 90, 120, 33, 88, 75, 60]
filtered_data = preprocess_readings(sensor_inputs)

# Auxiliary calculation: peak-to-peak variation (not directly used later)
pk_to_pk = max(filtered_data) - min(filtered_data)
compression_factor = len(sensor_inputs) / len(filtered_data)  # Red herring metric

# Define energy states using tuple unpacking and transformations
base_levels = [x * 1.1 for x in filtered_data]
adjusted_levels = [x * 0.95 + 2 for x in base_levels]
energy_states = list(zip(base_levels, adjusted_levels))

# Threshold logic with distractor comparisons
threshold = 50.0
high_activity_count = sum(1 for x in adjusted_levels if x > threshold)
low_activity_count = sum(1 for x in adjusted_levels if x < threshold * 0.6)

# Dummy string processing to add cognitive load
status_labels = ['HIGH' if x > threshold else 'LOW' for x in adjusted_levels]
label_concat = ''.join(status_labels)
distinct_patterns = set(itertools.permutations(['HIGH', 'LOW'], 2))  # Unused set operation

# Core analysis function with nested logic
def analyze_stability(states, limit):
    scores = []
    for base, adj in states:
        deviation = abs(adj - base)
        if base < limit:
            impact = deviation * 0.8
        else:
            if adj > base:
                impact = deviation * 1.2
            else:
                impact = deviation * 0.9
        normalized_impact = round(impact, 2)
        scores.append(normalized_impact)
    
    # Aggregate score using complex reduction
    total_drift = sum(scores)
    stability_penalty = len([s for s in scores if s > 5.0]) * 1.5
    final_score = total_drift - stability_penalty
    
    # Introduce irrelevant control flow
    if total_drift > 100:
        adjustment = 10
    else:
        adjustment = 0  # Dead code path (never subtracted)
    
    return int(round(final_score))

# Execute main computation
equilibrium_score = analyze_stability(energy_states, threshold)

# Print result as required
print(f"Result: {equilibrium_score}")