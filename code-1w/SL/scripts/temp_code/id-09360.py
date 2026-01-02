import itertools

# Simulated sensor data processing with embedded logic chain
def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if abs(x) > 0.1]
    normalized = [round(x / max(filtered), 4) for x in filtered]
    return normalized

# Irrelevant transformation - distractor
def smooth_data(signal):
    if len(signal) < 3:
        return signal
    smoothed = [signal[0]]
    for i in range(1, len(signal) - 1):
        smoothed.append((signal[i-1] + signal[i] + signal[i+1]) / 3)
    smoothed.append(signal[-1])
    return smoothed

# Bit manipulation for checksum - partially relevant
def compute_checksum(seq):
    chk = 0
    for val in seq:
        int_val = int(abs(val * 1000))
        chk ^= int_val  # XOR into checksum
    return chk & 0xFFFF

# Core pattern analysis - critical function
def extract_features(data):
    diffs = [abs(data[i+1] - data[i]) for i in range(len(data)-1)]
    avg_change = sum(diffs) / len(diffs)
    peak_count = sum(1 for i in range(1, len(data)-1) if data[i] > data[i-1] and data[i] > data[i+1])
    return avg_change, peak_count

# Data transformation pipeline
base_sequence = [128, 64, 32, 16, 8, 4, 2, 1]
decoy_signal = [0.15, -0.25, 0.35, -0.12, 0.18]

# Real processing path
scaled_vals = [x * 3.14159 for x in base_sequence]
transformed_data = preprocess_signal(scaled_vals)

# Generate control sequence using itertools - required feature
key_sequence = []
for x in itertools.accumulate([1, -1, 1, -1, 1], lambda a, b: a + b):
    key_sequence.append(x * 50)

# Dead code path - red herring
if len(decoy_signal) > 10:
    processed_decoy = smooth_data(decoy_signal)
    decoy_checksum = compute_checksum(processed_decoy)
else:
    temp_buffer = [x * 100 for x in decoy_signal if x > 0]
    buffer_sum = sum(temp_buffer)
    # Unused variable - distraction
    final_output_tag = f"TAG-{buffer_sum:.0f}"

# Secondary irrelevant computation
shadow_checksum = 0
for i, val in enumerate(transformed_data):
    shadow_checksum += int(val * (i + 1))
    shadow_checksum %= 99991

# Actual analysis logic
features = extract_features(transformed_data)
signal_strength = sum(transformed_data) * features[0]

# Misleading intermediate diagnostic
preliminary_diag = (signal_strength * 1000) ^ compute_checksum(key_sequence)

# Final determination - answer depends on this
final_diagnostic = 0
for i in range(len(transformed_data)):
    if i % 2 == 0:
        final_diagnostic += int(transformed_data[i] * 100) & key_sequence[i % len(key_sequence)]
    else:
        final_diagnostic -= int(transformed_data[i] * 100) | (i * 7)

# Critical output
print(f"Result: {final_diagnostic}")