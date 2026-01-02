import math

# Simulated sensor data and calibration parameters
data_stream = [127, 83, 255, 191, 64, 150, 200, 100, 75, 225]
calibration_key = 42
offset_table = {i: (i * 1.05) for i in range(10)}
noise_floor = 50
signal_ceiling = 200

# Irrelevant helper function (dead code path)
def analyze_spectrum(x):
    return sum([math.sin(val / 10) for val in x])

# Misleading intermediate processing
raw_energy = sum([x ** 2 for x in data_stream])
normalized_energy = raw_energy / len(data_stream)
effective_power = normalized_energy * 0.7  # Distractor computation

# Actual relevant logic begins here
bit_mask = 0xFF  # Used to simulate 8-bit truncation
clamped_data = [min(max(d, noise_floor), signal_ceiling) for d in data_stream]  # Apply bounds

# Bitwise manipulation for signal encoding (relevant)
encoded_signals = []
for val in clamped_data:
    shifted = (val << 1) & bit_mask  # Left shift and mask
    toggled = shifted ^ 0b10101010  # XOR with fixed pattern
    encoded_signals.append(toggled)

# Filtering based on parity and magnitude (relevant)
filtered_data = []
for e in encoded_signals:
    if e % 2 == 0 and e > 100:
        filtered_data.append(e)

# Red herring: unused statistical analysis
median_guess = sorted(clamped_data)[len(clamped_data)//2]
entropy_approx = -sum([math.log2(x/255) for x in clamped_data if x > 0])

# Threshold derived from bitwise properties of calibration key (relevant)
thresh_contributions = []
for i in range(8):
    if (calibration_key >> i) & 1:
        thresh_contributions.append(i * 10)
threshold = sum(thresh_contributions) + 5  # Final threshold value

# Real processing function
def process_signals(signals, limit):
    accumulator = 0
    for s in signals:
        if s > limit:
            # Integer division and modular arithmetic
            base = s // 10
            mod_adjust = (base % 7) * 2
            accumulator += base - mod_adjust
        else:
            accumulator += s % 10
    return accumulator + len(signals)

# Critical execution point
final_output = process_signals(filtered_data, threshold)

# Output result
print(f"Result: {final_output}")