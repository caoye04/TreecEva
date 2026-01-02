from collections import defaultdict

# Simulate sensor readings over time with noise and redundancy
time_series_data = [102, 98, 100, 105, 97, 103, 101, 99, 104, 96]

# Irrelevant auxiliary calculation (distractor)
baseline_average = sum(time_series_data) / len(time_series_data)
scaled_readings = [x * 1.02 for x in time_series_data if x > 97]

# Track frequency of adjusted values
freq_map = defaultdict(int)
for val in time_series_data:
    adjusted = val - 95
    freq_map[adjusted] += 1

# Misleading trend analysis (dead computation path)
trend_changes = 0
for i in range(1, len(time_series_data)):
    if (time_series_data[i] - time_series_data[i-1]) > 0:
        trend_changes += 1

# Core logic: detect anomalies using threshold and count parity
anomalies = []
for reading in time_series_data:
    if abs(reading - baseline_average) > 3:
        anomalies.append(reading)

# Compute diagnostic metrics
parity_flag = len(anomalies) % 2
aggregate_score = sum(anomalies) * parity_flag

# Secondary adjustment based on bit manipulation pattern
effective_mask = 0
for i, v in enumerate(anomalies):
    effective_mask ^= (v & 0xF)  # XOR lower nibble across anomalies
correction_factor = effective_mask * (1 if len(anomalies) > 2 else 0)

# Final system diagnostic (key statement)
final_diagnostic = aggregate_score + correction_factor

print(f"Result: {final_diagnostic}")