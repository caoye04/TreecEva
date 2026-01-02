from itertools import combinations

# System parameters for signal processing simulation
target_samples = 8
signal_threshold = 15
peak_span = 6
dummy_offset = 2.5  # Irrelevant constant for minor distraction

# Generate sample data representing sensor readings
sensor_readings = [n * n for n in range(1, target_samples + 1)]

# Filter sequences above threshold (simulated anomaly detection)
valid_sequences = []
for seq in combinations(sensor_readings, 3):
    if sum(seq) > signal_threshold:
        valid_sequences.append(seq)

# Critical computation: count how many valid sequences have range exactly equal to peak_span
peak_combinations = sum(1 for combo in valid_sequences if max(combo) - min(combo) == peak_span)

# Output result as required
print(f"Result: {peak_combinations}")