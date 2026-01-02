def analyze_pattern(sequence):
    counts = {}
    for item in sequence:
        counts[item] = counts.get(item, 0) + 1
    return counts

sequence_data = ['A', 'B', 'C', 'A', 'B', 'A']

# Irrelevant transformation - distractor
transformed = [ord(c) - ord('A') + 1 for c in sequence_data]
duplicate_check = [x for x in transformed if transformed.count(x) > 1]
unique_filtered = list(set(duplicate_check))

stats = analyze_pattern(sequence_data)

# Semi-relevant preprocessing
frequencies = list(stats.values())
mean_freq = sum(frequencies) / len(frequencies)
adjusted = [f - mean_freq for f in frequencies]

# Mock normalization (not used in final result)
normalized = [round((x - min(adjusted)) / (max(adjusted) - min(adjusted)) * 100, 2) for x in adjusted if max(adjusted) != min(adjusted)]

config = {
    'thresholds': {'A': 2.5, 'B': 1.8, 'C': 1.0},
    'weights': {'A': 3, 'B': 2, 'C': 1},
    'penalty_factor': 0.9,
    'bonus_enabled': True
}

metadata_log = "Processing run: metrics_v2"
log_parts = metadata_log.split(': ')
version_tag = log_parts[1] if len(log_parts) > 1 else "unknown"

# Unused diagnostic computation - red herring
diagnostic_sum = sum([len(key) * val for key, val in stats.items()])

snapshot = config['thresholds'].copy()
snapshot['D'] = 0.5  # Extraneous addition

# Key function with mixed logic
def process_metrics(freq_dict, limits):
    base = 0
    penalty = 0
    for key, count in freq_dict.items():
        threshold = limits[key]
        if count > threshold:
            base += count * 10
        else:
            base += count * 5
        # Conditional bonus not triggered due to logic
        if key == 'C' and count >= threshold:
            base += 20
    temp_result = base * 0.95
    # Simulate adjustment based on unused weight
    weight_sum = sum(config['weights'].values())  # Computed but not fully used
    if weight_sum > 5 and config['bonus_enabled']:
        temp_result += 10
    return int(temp_result)

# Critical execution point
final_score = process_metrics(stats, config['thresholds'])

print(f"Result: {final_score}")