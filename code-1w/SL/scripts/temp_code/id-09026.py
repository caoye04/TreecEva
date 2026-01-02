def analyze_component(values, threshold=0.5):
    above_threshold = [v for v in values if v > threshold]
    normalized = [round(v / sum(above_threshold), 4) for v in above_threshold]
    return normalized if normalized else [0.0]


def calculate_entropy(data):
    import math
    entropy = 0.0
    for x in data:
        if x > 0:
            entropy -= x * math.log2(x)
    return round(entropy, 4)

# Simulated sensor benchmark readings
timestamps = [1001, 1002, 1003, 1004, 1005]
sensor_a = [0.65, 0.42, 0.73, 0.81, 0.54]
sensor_b = [0.39, 0.68, 0.77, 0.51, 0.85]
sensor_c = [0.58, 0.63, 0.49, 0.72, 0.60]

# Irrelevant preprocessing (distractor)
delay_offsets = [t - 1000 for t in timestamps]
scaling_factor = sum(delay_offsets) / len(delay_offsets)

# Core data aggregation
sensor_data = list(zip(sensor_a, sensor_b, sensor_c))
processed_chunks = {}

for i, (a, b, c) in enumerate(sensor_data):
    chunk_id = f"block_{i}"
    raw_row = [a, b, c]
    filtered_row = [val for val in raw_row if val >= 0.5]  # Only values >= 0.5 matter
    
    # Distractor: unused transformation
    inverted = [round(1 - v, 3) for v in raw_row]
    
    if len(filtered_row) >= 2:
        avg_filtered = sum(filtered_row) / len(filtered_row)
    else:
        avg_filtered = 0.5  # default fallback
    
    processed_chunks[chunk_id] = {
        'raw': raw_row,
        'filtered_avg': avg_filtered,
        'count_valid': len(filtered_row)
    }

# Weight configuration (some are misleading)
weights = {
    'base': 0.4,
    'stability': 0.3,
    'redundancy': 0.2,  # not actually used
    'coverage': 0.1
}

# Misleading auxiliary computation (dead path)
total_inverted_impact = 0.0
for block in processed_chunks.values():
    if 'inverted' in block:  # never true
        total_inverted_impact += sum(block['inverted'])

benchmark_data = []
for idx, (block_id, data) in enumerate(processed_chunks.items()):
    score = data['filtered_avg'] * weights['base']
    
    # Additional logic using enumerate meaningfully
    if idx % 2 == 0 and data['count_valid'] > 2:
        score += weights['stability'] * 0.5
    
    coverage_bonus = weights['coverage'] * (data['count_valid'] / 3)
    score += coverage_bonus
    
    benchmark_data.append(score)

# Final performance calculation
def calculate_performance(metrics, config):
    base_weight = config['base']
    adjusted = [m * 1.1 if m > 0.5 else m * 0.9 for m in metrics]
    
    # Use of enumerate and zip in final processing
    indexed = list(enumerate(adjusted))
    pairs = list(zip([x[1] for x in indexed[::2]], [x[1] for x in indexed[1::2]]))
    
    pair_contributions = []
    for a, b in pairs:
        pair_contributions.append((a + b) / 2)
    
    composite = sum(adjusted) + sum(pair_contributions)*0.1
    
    # Dummy entropy use (not affecting final result)
    _ = calculate_entropy(analyze_component(sensor_a))
    
    return int(round(composite * 100))

final_score = calculate_performance(benchmark_data, weights)
print(f"Target result: {final_score}")