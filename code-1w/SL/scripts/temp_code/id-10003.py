import itertools

def analyze_pattern(sequence):
    count = 0
    trend = []
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend.append(1)
        elif sequence[i] < sequence[i-1]:
            trend.append(-1)
        else:
            trend.append(0)
    
    # Irrelevant computation (distractor)
    avg_fluctuation = sum(abs(a - b) for a, b in zip(trend, trend[1:])) / len(trend) if len(trend) > 1 else 0
    
    runs = 1
    for i in range(1, len(trend)):
        if trend[i] != trend[i-1]:
            runs += 1
    
    return runs

def filter_outliers(data, threshold=2):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    filtered = [x for x in data if abs(x - mean_val) <= threshold * std_dev]
    
    # Dead code path (misleading)
    if len(filtered) == 0:
        return [mean_val]
    
    return filtered

def transform_coordinates(coords_list):
    transformed = []
    for x, y in coords_list:
        radius = (x**2 + y**2) ** 0.5
        angle = (x + y) * 0.1
        transformed.append((radius, angle))
    
    # Unused but plausible computation
    total_energy = sum(r ** 2 for r, _ in transformed)
    
    return [t[0] for t in transformed]

def calculate_final_score(data_map):
    base = data_map['magnitude']
    weight = len(data_map['sequence'])
    
    # Real computation affecting result
    pattern_complexity = analyze_pattern(data_map['sequence'])
    adjusted_base = base * (1 + pattern_complexity / 10)
    
    # Distractor: unrelated string processing
    tag = data_map['tag']
    redundancy_factor = len(set(tag)) / len(tag) if tag else 1
    signal_quality = 0.8 + 0.2 * redundancy_factor
    
    # Actual contribution to answer
    final_score = adjusted_base * weight * signal_quality
    
    # Red herring variable
    normalized_entropy = sum((c / sum(data_map['sequence'])) ** 2 for c in data_map['sequence'] if c > 0)
    
    return int(final_score)

# Main execution
raw_sequence = [3, 5, 4, 7, 6, 9, 1]
data_stats = {
    'magnitude': 12,
    'sequence': raw_sequence,
    'tag': 'DYNFLOW'
}

# Preprocessing steps
filtered_seq = filter_outliers(raw_sequence)
processed_coords = [(i, val) for i, val in enumerate(filtered_seq)]
decay_profile = [x * 0.95**i for i, x in enumerate(raw_sequence)]  # unused

processed_data = data_stats.copy()
processed_data['sequence'] = filtered_seq

# Transform not used in final score but looks relevant
radial_values = transform_coordinates(processed_coords)

# Key statement
final_score = calculate_final_score(processed_data)
print(f"Target result: {final_score}")