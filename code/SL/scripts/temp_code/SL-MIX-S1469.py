from functools import reduce

# Deep space signal analysis protocol
received_frequencies = [243, 729, 2187, 81, 6561]
base_modulus = 1000

# Step 1: Apply modular exponentiation to normalize frequencies
normalized_freqs = [pow(freq, 3, base_modulus) for freq in received_frequencies]

# Step 2: Filter out signals below threshold using set operations
signal_threshold = 500
freq_set = set(normalized_freqs)
thresh_set = {x for x in range(0, signal_threshold)}
valid_signals = freq_set - thresh_set

# Step 3: Encode valid signals using a custom transformation
encoded_signals = {sig: (sig * 17 + 23) % base_modulus for sig in valid_signals}

# Step 4: Merge with baseline calibration data
baseline_calibration = {81: 400, 963: 550, 887: 620}
merged_data = encoded_signals | baseline_calibration

# Step 5: Calculate weighted average of merged signals
signal_weights = {k: k % 10 for k in merged_data.keys()}
total_weighted_sum = sum(merged_data[k] * signal_weights[k] for k in merged_data)
total_weights = sum(signal_weights.values())

# Final step: Decode signal strength
if total_weights != 0:
    decoded_signal_strength = (total_weighted_sum // total_weights) % 100
else:
    decoded_signal_strength = 0

print(f"Result: {decoded_signal_strength}")