from itertools import combinations

# Simulate sensor data segmentation and anomaly detection
raw_readings = [12.4, 15.1, 9.8, 18.3, 14.0, 7.2, 21.5, 13.7]
segment_size = 3
thresholds = {'low': 10.0, 'high': 20.0}

# Irrelevant preprocessing: shuffle order (not actually used)
temp_sorted = sorted(raw_readings, reverse=True)
offset_correction = sum(r ** 0.5 for r in raw_readings if r > 15) / len(raw_readings)

def chunk_data(data, size):
    """Split data into overlapping segments."""
    return [data[i:i+size] for i in range(len(data) - size + 1)]

segments = chunk_data(raw_readings, segment_size)

# Misleading auxiliary calculation: pairwise differences (unused later)
pairwise_diffs = [abs(a - b) for a, b in combinations(raw_readings[:4], 2)]
max_pair_diff = max(pairwise_diffs) if pairwise_diffs else 0.0

# State tracker for valid windows
validity_flags = []
penalty_counter = 0

for seg in segments:
    below_low = len([x for x in seg if x < thresholds['low']])
    above_high = len([x for x in seg if x > thresholds['high']])
    in_range = len([x for x in seg if thresholds['low'] <= x <= thresholds['high']])
    
    # Heuristic: segment valid if majority within normal range
    is_valid = in_range >= 2
    validity_flags.append(is_valid)
    
    # Red herring: count penalties even though not used in final score
    if below_low > 1 or above_high > 0:
        penalty_counter += 1

# Compute cumulative quality index (distractor)
cumulative_index = sum(1 for f in validity_flags if f) * 0.75

# Core logic: weight each segment by stability metric
stability_scores = []
for seg in segments:
    mean_val = sum(seg) / len(seg)
    variance = sum((x - mean_val) ** 2 for x in seg) / len(seg)
    stability = 1 / (1 + variance)  # higher stability = lower variance
    stability_scores.append(stability)

# Final computation path
aggregate_stability = sum(s for s, v in zip(stability_scores, validity_flags) if v)
base_score = aggregate_stability * 100
adjustment = len(segments) - len(validity_flags)  # always zero, but adds confusion

# Key assignment
final_score = int(base_score + adjustment)

# Print result as required
print(f"Result: {final_score}")