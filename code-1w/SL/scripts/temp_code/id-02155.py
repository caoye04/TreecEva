import itertools

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 26.0, 23.7]
humidity_readings = [45, 47, 50, 44, 46, 52, 43, 48]
pressure_readings = [1013, 1012, 1015, 1010, 1014, 1009, 1016, 1011]

# Irrelevant transformation - red herring (bit manipulation on pressure)
decoys = [(p << 2) ^ 0xA for p in pressure_readings]
mask_sequence = [decoy & 0xFF for decoy in decoys]

# Misleading aggregation path (unused)
avg_decoy_value = sum(mask_sequence) / len(mask_sequence)
threshold_filter = [d for d in mask_sequence if d > avg_decoy_value]

# Real signal processing begins here
filtered_temps = [t for t in temperature_readings if 23.0 <= t <= 25.0]
scaled_humidity = [(h - 40) * 0.5 for h in humidity_readings if h > 40]  # Only above baseline

# Cross-correlation using itertools (real computation)
paired_metrics = list(itertools.product(filtered_temps[:4], scaled_humidity[:4]))
correlation_sum = sum(abs(t * h - 100) for t, h in paired_metrics)

# Distractor: unused recursive function
def calculate_entropy(data, depth=0):
    if depth >= 3 or len(data) == 0:
        return 0.0
    mid = len(data) // 2
    return data[0] * 0.1 + calculate_entropy(data[1:], depth + 1)

entropy_estimate = calculate_entropy(pressure_readings)  # Dead end

# Signal conditioning with tuple unpacking and conditional branching
processed_signals = []
for i, temp in enumerate(filtered_temps):
    if i % 2 == 0:
        offset = humidity_readings[i] // 10
        processed_signals.append((temp + offset, f'T{i}'))
    else:
        # Simulate correction
        corrected = round(temp * 0.98, 2)
        processed_signals.append((corrected, f'C{i}'))

# Another distractor: character counting in labels (misleading)
label_chars = ''.join(label for _, label in processed_signals)
char_frequency = {c: label_chars.count(c) for c in set(label_chars)}
total_chars = sum(char_frequency.values())  # Looks important but isn't used

# Core diagnostic logic
abnormal_threshold = 25.5
high_temp_count = sum(1 for val, _ in processed_signals if val > abnormal_threshold)
base_score = len(processed_signals) * 10 + int(correlation_sum % 7)

# Final analysis function
def analyze_readings(signals):
    if not signals:
        return -1
    
    # Unpacking with destructuring
    values, tags = zip(*signals)
    
    # Decoy calculation inside function
    tag_analysis = sum(len(t) for t in tags) * 0.1
    
    # Real scoring logic
    mean_val = sum(values) / len(values)
    tag_correction = 5 if any('C' in t for t in tags) else 0
    stability_bonus = 10 if all(v < 26.0 for v in values) else -5
    
    # Final formula
    score = mean_val * 10 + tag_correction + stability_bonus - high_temp_count * 3
    return int(score)

# Execution point of interest
final_diagnostic = analyze_readings(processed_signals)
print(f"Target result: {final_diagnostic}")