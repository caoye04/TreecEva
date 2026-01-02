import math

# Simulated sensor data processing for a distributed network node
def analyze_readings(raw_data):
    filtered = [x for x in raw_data if x > -50 and x < 50]
    baseline = sum(filtered) / len(filtered) if filtered else 0
    deviations = [(x - baseline) ** 2 for x in filtered]
    variance = sum(deviations) / len(deviations) if deviations else 0
    return math.sqrt(variance)

# Irrelevant helper: calculates geometric mean (not used in final path)
def geo_mean(data):
    if not data:
        return 0
    product = 1
    for x in data:
        product *= max(x, 1)
    return product ** (1 / len(data))

# Core transformation: frequency-based encoding
frequency_map = {
    'A': 2.5, 'B': 3.1, 'C': 1.8, 'D': 4.2
}

# Legacy system emulation (distractor)
legacy_weights = {k: v * 0.9 for k, v in frequency_map.items()}
legacy_weights['E'] = 5.0  # Unused extension

# Signal encoding with red herring operations
encoded_sequence = []
for char in "ABCDABCADC":
    code_point = ord(char) - ord('A') + 1
    signal = code_point * frequency_map.get(char, 0.5)
    encoded_sequence.append(round(signal, 2))

# Decoy function that looks important but isn't called
def decrypt_sequence(seq, key="default"):
    return [int(x - 1) for x in seq if x > 3]

# Secondary processing chain (some steps are irrelevant)
aggregated = 0
for i, val in enumerate(encoded_sequence):
    if i % 2 == 0:
        aggregated += val * 0.8
    else:
        aggregated += val * 1.2

# Another distractor: builds unused structure
snapshot_log = [
    {'step': i, 'value': encoded_sequence[i], 'flag': 'X' if i % 3 == 0 else 'Y'}
    for i in range(len(encoded_sequence))
]

# Conditional expression mix with lambda pre-processing
transform = lambda x: x if x < 6 else x * 0.75
processed_sequence = [transform(x) for x in encoded_sequence]

# Key computation buried among noise
threshold_mask = [1 if x > 3.0 else 0 for x in processed_sequence]
correlation_score = sum(
    processed_sequence[i] * threshold_mask[i]
    for i in range(len(processed_sequence))
)

# Real processing begins here — hidden in the middle
auxiliary_buffer = []
for val in processed_sequence:
    if val > 2.0:
        auxiliary_buffer.append(val * 1.5)
    elif val > 1.0:
        auxiliary_buffer.append(val * 0.5)
    else:
        auxiliary_buffer.append(val)

# Actual target logic
rolling_window = []
for i in range(2, len(auxiliary_buffer)):
    window_avg = (auxiliary_buffer[i-2] + auxiliary_buffer[i-1] + auxiliary_buffer[i]) / 3
    rolling_window.append(window_avg)

smoothed_signal = sum(rolling_window) / len(rolling_window) if rolling_window else 0

# Final transformation using misleadingly named intermediate
interference_factor = sum(threshold_mask) * 0.3
modulation_index = correlation_score / (1 + interference_factor)

# Critical statement: this is where the answer is determined
final_signal = round(smoothed_signal + modulation_index, 4)

# Output the result as required
print(f"Target result: {final_signal}")