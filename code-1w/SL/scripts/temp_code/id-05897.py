import itertools

# Simulated sensor data with noise and redundant readings
data_stream = [18, 22, 14, 30, 26, 28, 10, 34, 12, 24, 20, 16, 32, 8, 36]
noise_floor = 9
amplification_factor = 2
offset_correction = -4

# Irrelevant transformation: frequency simulation (dead code path)
frequencies = [x * 0.5 for x in data_stream if x > 20]
modulated_signal = [f * 1.2 for f in frequencies]

# Distractor: secondary processing chain with no impact
temp_buffers = []
for i, val in enumerate(data_stream):
    if i % 3 == 0:
        temp_buffers.append(val + 5)
processed_buffer = [b ** 0.5 for b in temp_buffers if b > 20]

# Core logic begins: extract and correct raw values
corrected_values = []
for val in data_stream:
    corrected = (val * amplification_factor) + offset_correction
    corrected_values.append(corrected)

# Misleading filter: appears important but unused later
crude_filter = [v for v in corrected_values if v >= 25]

# Real processing: identify peaks using rolling comparison
peaks = []
for i in range(1, len(corrected_values) - 1):
    if corrected_values[i] > corrected_values[i - 1] and corrected_values[i] > corrected_values[i + 1]:
        peaks.append(corrected_values[i])

# Decoy function: never called
def analyze_peaks(peaks_list):
    return sorted([p * 0.1 for p in peaks_list], reverse=True)

# Use of enumerate and zip: align indices with transformed peak data
indexed_peaks = list(enumerate(peaks))
shifted_peaks = [p - 10 for p in peaks]
paired_data = list(zip(indexed_peaks, shifted_peaks))

# Extract meaningful subset based on index parity and value threshold
selected_pairs = [item for item in paired_data if item[0][0] % 2 == 1 and item[1] > 20]

# Final filtering: extract original peak values from selected pairs
extracted_originals = [item[0][1] for item in selected_pairs]

# Secondary distraction: combinatorial generation with no use
cartesian_mix = list(itertools.product(extracted_originals[:2], [2, 3]))
expanded_set = [a * b for a, b in cartesian_mix if a > b]

# Actual target computation path
baseline_reference = 42
filtered_data = [x for x in extracted_originals if x < baseline_reference]
filtered_sum = sum(filtered_data)

# Red herring: floating point accumulation with rounding (unused)
approximate_total = round(sum([x * 1.05 for x in filtered_data]), 4)
error_margin = abs(approximate_total - filtered_sum)

# Output the required result
print(f"Result: {filtered_sum}")