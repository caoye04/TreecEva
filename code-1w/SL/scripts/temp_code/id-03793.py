def analyze_pattern(sequence, threshold=5):
    count = 0
    temp_buffer = []
    for i, val in enumerate(sequence):
        if val > threshold:
            count += 1
            temp_buffer.append(i)
    return count, temp_buffer

# Simulate sensor readings over time
data_stream = [3, 7, 2, 8, 6, 1, 9, 4, 5]

# Extract indices where readings exceed normal levels
anomaly_count, anomaly_indices = analyze_pattern(data_stream)

# Misleading computation: unrelated to final result
dummy_weights = [x * 0.1 for x in range(len(data_stream))]
total_weighted = sum(dummy_weights)

# Transform indices into positional parity markers
parity_map = list(map(lambda idx: idx % 2, anomaly_indices))

# Count how many anomalies occurred at even timestamps
even_anomalies = sum(1 for p in parity_map if p == 0)

# Simulate data packet structure
packets = [(i, val) for i, val in enumerate(data_stream) if val > 4]
packet_sum = sum(val for _, val in packets)  # Distractor

# Correlate multiple metrics
stats_summary = {
    'high_readings': anomaly_count,
    'even_peak_count': even_anomalies,
    'peak_positions': anomaly_indices
}

# Secondary analysis: gap analysis between anomalies
gaps = [anomaly_indices[i+1] - anomaly_indices[i] for i in range(len(anomaly_indices)-1)]
mean_gap = sum(gaps) / len(gaps) if gaps else 0

# Irrelevant smoothing operation (dead-end computation)
smoothed = [g * 0.9 for g in gaps]
avg_smoothed = sum(smoothed) / len(smoothed) if smoothed else 0

# Core logic disguised among distractors
def calculate_baseline(peaks):
    base = 0
    for i, p in enumerate(peaks):
        if i % 2 == 0:
            base += p * 2
        else:
            base -= p
    return base

baseline_value = calculate_baseline(anomaly_indices)

# Integrate with parity data using zip
combined_effects = 0
for idx, par in zip(anomaly_indices, parity_map):
    combined_effects += idx + par

# Final performance metric calculation
interim_metric = stats_summary['high_readings'] * stats_summary['even_peak_count']

# Key statement
final_score = baseline_value + interim_metric

print(f"Result: {final_score}")