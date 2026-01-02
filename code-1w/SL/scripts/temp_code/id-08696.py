def analyze_pattern(sequence):
    counts = {}
    for item in sequence:
        counts[item] = counts.get(item, 0) + 1
    return counts

# Simulate sensor data drift (irrelevant computation)
drift_compensation = sum([i * 0.01 for i in range(100)])

# Real data: character frequency analysis from encoded signals
raw_signal = 'abccbaadefggfed'
frequency_map = analyze_pattern(raw_signal)

# Extract unique characters and sort by occurrence
top_chars = sorted(frequency_map.keys(), key=lambda x: (-frequency_map[x], x))

# Threshold derivation using set operations
expected_chars = set('abcdefg')
observed_chars = set(frequency_map.keys())
missing_detection = expected_chars - observed_chars
spurious_detection = observed_chars - expected_chars

# Auxiliary calculation: position tracking (distractor)
position_index = {char: idx for idx, char in enumerate(top_chars)}

# Weight assignment based on frequency rank (relevant)
weights = {char: 5 - min(i, 4) for i, char in enumerate(top_chars)}

# Signal quality score with red herring accumulation
total_energy = 0
adjusted_weights = []
for c in raw_signal:
    total_energy += ord(c) % 7
    if c in weights and len(adjusted_weights) < 10:
        adjusted_weights.append(weights[c] * 0.95)

# Normalize weights (semi-relevant)
normalized_weights = [w / max(adjusted_weights) if adjusted_weights else 1 for w in adjusted_weights]

# Thresholds for scoring bands (critical setup)
thresh_a = len(observed_chars) >= 6
tthresh_b = len(missing_detection) == 0
temporal_ratio = len(raw_signal) / (len(expected_chars) + 1)

thresholds = {
    'strict': thresh_a and tthresh_b,
    'dynamic': temporal_ratio > 1.2,
    'legacy_mode': False
}

# Main dataset: multiple measurements
data = [
    {'val': 23, 'flag': True, 'type': 'A'},
    {'val': 15, 'flag': False, 'type': 'B'},
    {'val': 41, 'flag': True, 'type': 'A'}
]

# Secondary processing with list comprehension and zip (mixed relevance)
enhanced_data = [
    {**item, 'adj_val': item['val'] * (1.1 if item['flag'] else 1.0)}
    for item in data
]
summary_pairs = list(zip([d['val'] for d in data], [d['adj_val'] for d in enhanced_data]))

# Accumulation with distractors
dummy_accum = 0
for a, b in summary_pairs:
    dummy_accum += a ^ int(b)  # Bitwise distraction

correction_factor = sum(normalized_weights[:len(data)]) if normalized_weights else 1.0

# Core logic: conditional scoring
def calculate_final_score(entries, config):
    base = 0
    bonus = 0
    for entry in entries:
        base += entry['adj_val']
        if config['strict'] and entry['type'] == 'A':
            bonus += 5
    if config['dynamic']:
        bonus += int(len(entries) * 1.5)
    
    # Final adjustment using tuple unpacking
    scaling_tuple = (1.05, 0.95, 1.0)
    multiplier, _, _ = scaling_tuple  # Unpacking with ignored values
    return int((base + bonus) * multiplier)

# Execute main computation
final_score = calculate_final_score(enhanced_data, thresholds)

print(f"Result: {final_score}")