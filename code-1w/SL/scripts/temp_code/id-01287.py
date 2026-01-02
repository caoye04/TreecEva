from itertools import groupby

# Simulated sensor data stream with noise
data_stream = [104, 98, 101, 103, 97, 110, 109, 108, 102, 100, 99, 105, 107, 106, 96]

# Noise filter threshold and baseline calibration
threshold = 102
baseline_offset = 2
noise_floor = 95

# Step 1: Filter out noise below floor (irrelevant to final logic but part of preprocessing)
cleaned_data = [x for x in data_stream if x > noise_floor]

# Step 2: Apply baseline correction (distraction - not used later)
corrected_data = [x - baseline_offset for x in cleaned_data]

# Step 3: Identify segments above threshold using groupby (core logic start)
above_threshold = [x > threshold for x in cleaned_data]
segment_groups = [(k, len(list(g))) for k, g in groupby(above_threshold)]

# Step 4: Extract lengths of 'True' segments where values exceed threshold
distress_segments = [length for is_above, length in segment_groups if is_above]

# Step 5: Compute resilience metric (semi-relevant transformation)
resilience_metric = sum([seg ** 0.5 for seg in distress_segments])

# Step 6: Count total fluctuations (distraction - computed but unused)
fluctuation_pairs = [(cleaned_data[i], cleaned_data[i+1]) for i in range(len(cleaned_data)-1)]
transition_count = sum(1 for a, b in fluctuation_pairs if (a > threshold) != (b > threshold))

# Step 7: Prepare processed data using lambda-based transformation
rolling_window = lambda seq, size: [seq[i:i+size] for i in range(0, len(seq), size)]
chunks = rolling_window(cleaned_data, 3)
processed_data = [sum(chunk) / len(chunk) for chunk in chunks if len(chunk) == 3]

# Step 8: Calculate efficiency score based on stabilized averages
def calculate_efficiency(means):
    valid_stable = [m for m in means if abs(m - threshold) <= 5]
    stability_bonus = len(valid_stable) * 0.5
    return int(sum(valid_stable) / len(valid_stable) + stability_bonus)

# Key assignment
efficiency_score = calculate_efficiency(processed_data)

print(f"Result: {efficiency_score}")