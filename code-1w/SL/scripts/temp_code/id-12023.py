def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if x > -50 and x < 50]
    normalized = [round(x / max(filtered), 3) for x in filtered]
    return normalized

raw_sensor_data = [-120, -45, 33, 78, 12, -67, 0, 44, 23, -10, 88, 55, -30]
offset_correction = sum([i * 2 for i in range(len(raw_sensor_data)) if i % 3 == 0])
baseline_shift = 0.0

# Irrelevant transformation chain (distractor)
shadow_buffer = [x * 1.5 for x in raw_sensor_data]
decoy_spectrum = []
for i, val in enumerate(shadow_buffer):
    if i % 2 == 0:
        decoy_spectrum.append(val ** 0.5)
    else:
        decoy_spectrum.append(val // 10)

processed_signal = preprocess_signal(raw_sensor_data)
spectral_weights = [abs(x) ** 1.2 for x in processed_signal]

# Simulate redundant data alignment
index_map = dict(enumerate([i for i in range(len(spectral_weights)) if spectral_weights[i] > 0.5]))
reindexed_data = [spectral_weights[i] * 1.1 for i in index_map.values() if i % 2 == 0]

# Core logic disguised among distractions
transient_mask = [1 if x > 0.3 else 0 for x in reindexed_data]
aggregation_key = sum(transient_mask) * 1.5

# Decoy function that's never called (dead code path)
def encrypt_sequence(seq):
    return [sum(seq[:i]) % 100 for i in range(1, len(seq)+1)]

# Another red herring: unused complex calculation
phantom_entropy = 0.0
for i in range(len(decoy_spectrum)):
    if i in [1, 3, 5]:
        phantom_entropy += decoy_spectrum[i] * 0.1

# Real work begins: transformation using slicing and zip
sliced_window = spectral_weights[1:-1]
shifted_slice = spectral_weights[0:-2]
paired_deltas = [a - b for a, b in zip(sliced_window, shifted_slice)]

transformed_data = []
for i, delta in enumerate(paired_deltas):
    if i % 2 == 0:
        transformed_data.append(abs(delta) * 2.5)
    else:
        transformed_data.append(abs(delta) / 1.5)

def generate_control_flags(length):
    flags = []
    for i in range(length):
        if i == 0:
            flags.append(3)
        elif i % 5 == 0:
            flags.append(15)
        else:
            flags.append(i % 7)
    return flags

def analyze_pattern(signal, mask):
    accumulator = 0.0
    # Use enumerate to track position and apply conditional amplification
    for idx, (val, flag) in enumerate(zip(signal, mask)):
        if idx % 3 == 0:
            accumulator += val * flag * 0.1
        elif val > 1.0:
            accumulator -= val * 0.05
        else:
            accumulator += flag * 0.02
    # Nested correction based on bit manipulation of control flow
    temp_adjust = 0
    for j in range(1, 5):
        temp_adjust |= (mask[0] >> j)
    accumulator += temp_adjust * 0.01
    return round(accumulator, 6)

control_sequence = generate_control_flags(len(transformed_data))

# Unused but plausible-looking diagnostic
auxiliary_check = sum([x for x, y in zip(transformed_data, control_sequence) if y > 5])

final_diagnostic = analyze_pattern(transformed_data, control_sequence)
print(f"Result: {final_diagnostic}")