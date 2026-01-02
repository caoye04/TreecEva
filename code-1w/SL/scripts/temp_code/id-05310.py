import itertools

# Simulated sensor data with noise and redundant readings
data_stream = [18, 22, 19, 25, 24, 23, 17, 21, 20, 26]
noise_filter = [1, -1, 0, 1, -1]

# Step 1: Apply noise correction (only some values are relevant)
corrected_readings = []
for i in range(len(data_stream)):
    adjusted = data_stream[i] + noise_filter[i % len(noise_filter)]
    corrected_readings.append(adjusted)

# Irrelevant transformation: frequency simulation (dead-end computation)
frequency_map = {}
for val in corrected_readings:
    freq_key = val % 7
    frequency_map[freq_key] = frequency_map.get(freq_key, 0) + 1

# Step 2: Extract peaks using sliding window (relevant processing)
peaks = []
window_size = 3
for i in range(1, len(corrected_readings) - 1):
    if corrected_readings[i-1] < corrected_readings[i] > corrected_readings[i+1]:
        peaks.append(corrected_readings[i])

# Distractor: secondary peak analysis (not used later)
secondary_peaks = [p for p in peaks if p % 2 == 0]
peak_gaps = [peaks[i+1] - peaks[i] for i in range(len(peaks)-1)] if len(peaks) > 1 else [0]

# Step 3: Group consecutive values using itertools (relevant)
consecutive_groups = []
sorted_peaks = sorted(peaks)
for k, g in itertools.groupby(enumerate(sorted_peaks), lambda ix: ix[0] - ix[1]):
    group = list(map(lambda x: x[1], g))
    if len(group) >= 2:
        consecutive_groups.append(group)

# Step 4: Compute stability metric (semi-relevant, distracts from core)
stability_score = 0
if consecutive_groups:
    longest_group = max(consecutive_groups, key=len)
    stability_score = sum(longest_group) / len(longest_group)
else:
    stability_score = min(peaks) if peaks else 20

# Step 5: Normalize peaks to baseline (relevant)
baseline = sum(corrected_readings[:5]) / 5
normalized_peaks = [round(p / baseline, 3) for p in peaks]

# Step 6: Calculate weighted contribution (core logic)
weights = [0.5 ** i for i in range(len(normalized_peaks))]
weighted_sum = sum(norm * weight for norm, weight in zip(normalized_peaks, weights))

# Step 7: Final scoring with threshold filtering
def calculate_final_score(data):
    filtered = [x for x in data if x > 1.05]  # only significant deviations
    if not filtered:
        return int(stability_score)
    return int(sum(filtered) * 100)

processed_data = normalized_peaks
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")