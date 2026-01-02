import itertools

# Simulated sensor data processing pipeline with diagnostic analysis
raw_readings = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
offset_correction = 2
filtered_readings = [x + offset_correction for x in raw_readings if x > 2]

# Irrelevant transformation: frequency sweep emulation (dead path)
frequency_sweep = [i * 0.1 for i in range(10)]
amplitude_modulation = [f ** 2 for f in frequency_sweep]
modulated_signal = sum(amplitude_modulation)  # Unused variable

# Core data transformation
rolling_window = []
for i in range(len(filtered_readings) - 2):
    window_avg = sum(filtered_readings[i:i+3]) / 3
    rolling_window.append(round(window_avg))

# Decoy statistical analysis (not used in final result)
mean_value = sum(rolling_window) / len(rolling_window)
variance_proxy = sum((x - mean_value) ** 2 for x in rolling_window)
entropy_estimate = len(rolling_window) > 5  # Misleading boolean flag

# Bit manipulation layer for error detection (partially relevant)
def compute_checksum(seq):
    checksum = 0
    for val in seq:
        checksum ^= val  # XOR-based accumulation
        checksum = (checksum << 1) & 0xFF | (checksum >> 7)  # Rotate left
    return checksum & 0xFF

# Secondary transformation chain
shifted_data = [x << 1 for x in rolling_window]  # Left shift by 1
inverted_mask = [~x & 0xF for x in shifted_data][:4]  # Truncated irrelevant result

# Use itertools to generate combinations (distractor with partial relevance)
all_pairs = list(itertools.combinations(rolling_window, 2))
pair_summaries = [sum(pair) for pair in all_pairs]
dominant_pair_count = len([s for s in pair_summaries if s > 10])  # Used later as weight

# Real processing begins: pattern transformation
transformation_key = compute_checksum(rolling_window[:4])
transformed_data = [(x ^ transformation_key) % 10 for x in rolling_window]

# Recursive pattern analyzer (only some branches contribute)
def analyze_pattern(seq):
    if len(seq) <= 1:
        return seq[0] if seq else 777  # Base case (777 is red herring)
    if sum(seq) < 20:
        return seq[0] * 2
    # Main logic branch
    reduced = [seq[i] + seq[i+1] for i in range(0, len(seq)-1, 2)]
    if len(reduced) == 1:
        return reduced[0] * 3
    return analyze_pattern(reduced)  # Recursive call

# Dead recursive function (never called)
def debug_trace_path(data, level=0):
    if level > 3:
        return 999
    return debug_trace_path(data[1:], level + 1)

# Key execution point
final_diagnostic = analyze_pattern(transformed_data)

# Output requirement
print(f"Result: {final_diagnostic}")