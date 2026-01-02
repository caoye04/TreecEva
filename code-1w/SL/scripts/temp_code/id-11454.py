def analyze_signal(samples):
    filtered = [x for x in samples if x > 0.1]
    normalized = [x / max(filtered) for x in filtered]
    transformed = [round(x * 100) for x in normalized]
    return transformed


def compute_entropy(data):
    from math import log2
    freq_map = {}
    for val in data:
        freq_map[val] = freq_map.get(val, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq_map.values():
        prob = count / total
        entropy -= prob * log2(prob)
    return round(entropy, 3)


def generate_sequence(seed, length):
    seq = [seed]
    for _ in range(length - 1):
        next_val = (seq[-1] * 7 + 3) % 113
        seq.append(next_val)
    return seq

# Irrelevant helper (distractor)
def unused_checksum(arr):
    return sum(arr[i] * (i + 1) for i in range(len(arr))) % 1000

# Unused transformation (dead code path)
def obsolete_transform(x):
    return (x << 2) ^ 0xAFFE

# Core processing functions
def decode_payload(raw):
    shifted = [(x >> 1) & 0xFF for x in raw]
    adjusted = [x if x < 128 else 256 - x for x in shifted]
    return adjusted


def extract_features(signal):
    peaks = [i for i in range(1, len(signal)-1) if signal[i-1] < signal[i] > signal[i+1]]
    troughs = [i for i in range(1, len(signal)-1) if signal[i-1] > signal[i] < signal[i+1]]
    amplitude_mod = [signal[p] - signal[t] for p in peaks for t in troughs if t < p]
    if not amplitude_mod:
        return [0]
    return amplitude_mod[:5]


def aggregate_metrics(metrics_list):
    base_score = sum(metrics_list) * 0.73
    penalty = len([x for x in metrics_list if x < 5]) * 1.2
    bonus = 5.0 if len(metrics_list) > 3 else 0.0
    return int(base_score - penalty + bonus)

# Initialization sequence (mixed real and fake data)
signal_samples = [0.15, 0.4, 0.08, 0.62, 0.11, 0.89, 0.03, 0.54]
dummy_ids = generate_sequence(19, 15)  # Distractor data
raw_payload = [0xAB, 0xCD, 0xEF, 0x12, 0x34, 0x56, 0x78, 0x9A]

# Real processing chain
processed_signal = analyze_signal(signal_samples)
entropy_metric = compute_entropy(processed_signal)

# Decode and feature extraction
decoded = decode_payload(raw_payload)
features = extract_features(decoded)

# Build metric pipeline
intermediate_diagnostics = [sum(processed_signal[:3]), len(features), int(entropy_metric)]
feature_weights = [0.5, 0.3, 0.2]
weighted_diag = sum(intermediate_diagnostics[i] * feature_weights[i] for i in range(3))

# Simulated calibration (irrelevant)
calibration_offset = 0
for i in range(5):
    calibration_offset += (i * 17) % 9
    if calibration_offset > 20:
        break

# Final aggregation chain
processing_chain = [weighted_diag] + features + [len(dummy_ids) // 10]  # Inject distractor

# Key assignment point
temp_result = [x ** 2 for x in processing_chain if x > 0]
final_diagnostic = aggregate_metrics(processing_chain)

print(f"Result: {final_diagnostic}")