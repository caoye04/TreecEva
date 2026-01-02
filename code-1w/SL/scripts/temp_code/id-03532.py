import math

# Simulated sensor readings with noise and calibration data
data_stream = [18, -5, 22, 47, 33, 12, 99, 4, 29, 38, 41, 67, 73, 2, 14, 88, 91]
calibration_offset = 3
noise_floor = [1, -2, 0, 3, -1, 2, 0, -3, 1, 2]

# Irrelevant transformation: frequency domain mockup (dead path)
freq_weights = [math.sin(x * 0.1) for x in range(10)]
weighted_magnitude = sum(abs(w * 1.5) for w in freq_weights)

# Primary processing pipeline
raw_signals = [x + calibration_offset for x in data_stream]  # Apply offset
even_filtered = [x for x in raw_signals if x % 2 == 0]  # Keep even values

# Misleading intermediate: peak detection (unused)
peaks = []
for i in range(1, len(even_filtered)-1):
    if even_filtered[i] > even_filtered[i-1] and even_filtered[i] > even_filtered[i+1]:
        peaks.append(even_filtered[i])

# Slice operation: focus on stable segment (middle 10 elements of original stream)
stable_window = data_stream[4:14]
adjusted_window = [x + calibration_offset for x in stable_window]

# Set operations to remove duplicates and apply exclusion zone
exclusion_set = {20, 21, 22, 23, 24}
valid_candidates = {x for x in adjusted_window if x not in exclusion_set}

# Further filter: only values above median threshold
sorted_candidates = sorted(valid_candidates)
median_val = sorted_candidates[len(sorted_candidates)//2]
high_confidence_set = {x for x in valid_candidates if x > median_val}

# Decoy statistic: mean deviation (not used in final result)
mean_val = sum(high_confidence_set) / len(high_confidence_set)
mean_deviation = sum(abs(x - mean_val) for x in high_confidence_set)

# Final filtering based on bit properties: numbers with odd number of set bits
bit_condition_met = []
for x in high_confidence_set:
    if bin(x).count('1') % 2 == 1:  # Has odd number of 1s in binary
        bit_condition_met.append(x)

# Sort and take top 5 to simulate confidence ranking
bit_condition_met.sort(reverse=True)
ranked_results = bit_condition_met[:5]

# Key computation: sum of filtered data after all conditions
filtered_data = [x for x in ranked_results if x < 80]  # Final size cap
filtered_sum = sum(filtered_data)

# Output result
print(f"Result: {filtered_sum}")