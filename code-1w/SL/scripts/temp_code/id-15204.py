def analyze_fragment(data, offset):
    return sum(data[i] * (i + 1) for i in range(len(data)) if i % 2 == offset)

resource_map = {
    'nodes': [3, 1, 4, 1, 5, 9, 2],
    'weights': [0.5, 1.5, 2.0, 0.8, 1.2],
    'flags': [True, False, True, True, False]
}

# Irrelevant preprocessing step (distractor)
baseline_shift = sum(resource_map['nodes'][::2]) - len(resource_map['weights'])

# Misleading intermediate calculation
aggregate_score = 0
for idx, w in enumerate(resource_map['weights']):
    aggregate_score += w * resource_map['nodes'][idx % len(resource_map['nodes'])]

# Conditional expression with slicing (required feature)
adjusted_nodes = resource_map['nodes'][1:-1] if len(resource_map['nodes']) > 4 else resource_map['nodes']

threshold = 7.5
utilization_log = []

for i in range(len(adjusted_nodes)):
    # Simulate load sampling
    sample = adjusted_nodes[i] * (1.1 if i % 2 == 0 else 0.9)
    
    # Dead code branch (distractor)
    if sample < 0:
        utilization_log.append(0)
    elif sample > threshold:
        utilization_log.append(threshold * 0.6)
    else:
        utilization_log.append(sample * 0.7)

# Another irrelevant helper function (distractor)
def calculate_entropy(vector):
    total = sum(vector)
    if total == 0:
        return 0.0
    return -sum((x / total) * ((x / total) ** 0.5) for x in vector if x > 0)

entropy_value = calculate_entropy(resource_map['nodes'])

# Core logic: evaluating system capacity using multiple concepts
rolling_sum = 0
peak_load = 0
for val in utilization_log:
    rolling_sum += val
    if rolling_sum > peak_load:
        peak_load = rolling_sum
    if rolling_sum > threshold * 0.8:
        rolling_sum = 0  # Reset on overload

# Final evaluation using dictionary and conditional logic
def evaluate_system_load(res_map, thresh):
    base = sum(res_map['nodes'])
    modifier = len(res_map['weights']) if base > 15 else len(res_map['weights']) * 0.5
    
    # Use of dictionary operation and conditional expression
    extra_buffer = res_map.get('extra', [0])[0] if 'extra' in res_map else 0
    
    intermediate = analyze_fragment(res_map['nodes'], 1)
    return int((base * modifier + intermediate) // (thresh / 2.5) + extra_buffer)

# Key assignment statement
final_capacity = evaluate_system_load(resource_map, threshold)

print(f"Result: {final_capacity}")