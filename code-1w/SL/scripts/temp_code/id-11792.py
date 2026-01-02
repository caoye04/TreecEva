def analyze_pattern(sequence):
    frequency = {}
    for item in sequence:
        frequency[item] = frequency.get(item, 0) + 1
    return frequency

# Simulate sensor data bursts
data_stream = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

distraction_counter = 0
for i in range(len(data_stream)):
    if data_stream[i] % 2 == 0:
        distraction_counter += (i * 2) // 3  # Irrelevant accumulation

# Analyze occurrence pattern
occurrence_map = analyze_pattern(data_stream)

# Compute burst intensity (actual relevant logic)
burst_intensity = {}
for key, count in occurrence_map.items():
    burst_intensity[key] = count ** 2

# Filter strong signals
effective_signals = {k: v for k, v in burst_intensity.items() if v >= 9}

# Prepare summary
summary_stats = {
    'total_unique': len(occurrence_map),
    'max_frequency': max(occurrence_map.values()),
    'signal_power': sum(effective_signals.values())
}

# Define decay factors (distractor structure)
decay_factors = {x: 0.95 ** x for x in range(1, 6)}
temp_correction = 0
for val in decay_factors.values():
    temp_correction += val * 0.1  # Unused correction term

# Build data summary using dictionary and lambda
data_summary = {
    'items': list(effective_signals.keys()),
    'weights': list(effective_signals.values()),
    'scale_factor': (lambda x: x * 1.5)(summary_stats['signal_power'])
}

# Penalty map based on rare patterns (set operation)
all_keys = set(occurrence_map.keys())
frequent_keys = set(effective_signals.keys())
rare_keys = all_keys - frequent_keys  # Set difference - unused but plausible

penalty_map = {key: 2 for key in rare_keys}
penalty_map['default'] = 1  # Default penalty

# Dead code branch - simulates error handling
if len(rare_keys) > 10:
    for k in penalty_map:
        penalty_map[k] *= 0.5  # Never executed

# Core scoring function
def calculate_final_score(summary, penalties):
    base = summary['scale_factor']
    adjustment = len(summary['items']) * 3
    
    # Use of lambda in reduction
    reducer = lambda a, b: a + b
    weight_sum = reducer(0, summary['weights'])
    
    penalty_value = penalties.get('default', 0)
    
    # Introduce irrelevant local calculation
    shadow_score = 0
    for w in summary['weights']:
        shadow_score += w * 0.01  # Minor distraction
    
    return int(base + adjustment - penalty_value)

# Final computation
final_score = calculate_final_score(data_summary, penalty_map)
print(f"Target result: {final_score}")