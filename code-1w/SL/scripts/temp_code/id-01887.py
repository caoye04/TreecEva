import math

# Simulated sensor data processing with diagnostic evaluation
def process_sensor_readings(raw_data, threshold=0.75):
    normalized = [x / max(raw_data) for x in raw_data]
    filtered = [x for x in normalized if x > threshold]
    return filtered if filtered else [threshold]

# Irrelevant helper: computes statistical dispersion (not used in final path)
def compute_dispersion(seq):
    mean_val = sum(seq) / len(seq)
    variance = sum((x - mean_val) ** 2 for x in seq) / len(seq)
    return math.sqrt(variance)

# Signal encoding using bit manipulation and slicing
def encode_signal(segment):
    shifted = [(x * 100) % 256 for x in segment]
    bitwise_transform = [int(x) ^ 42 | 15 for x in shifted]  # XOR and OR mix
    packed = int(sum(bitwise_transform[i] << (i * 8) for i in range(min(4, len(bitwise_transform)))) )
    return packed

# Decoy function: looks important but unused
def analyze_pattern(seq):
    if len(seq) < 3:
        return False
    trend = all(seq[i] <= seq[i+1] for i in range(len(seq)-1))
    return trend

# Weight adjustment based on conditional logic and slicing
weights = [0.1, 0.2, 0.35, 0.15, 0.08, 0.12]
baseline = [1.0, 0.8, 0.6, 0.4, 0.2]

# Dead code path: never invoked
obsolete_modes = ['legacy', 'debug', 'safe']
mode_thresholds = {m: 0.5 + i*0.1 for i, m in enumerate(obsolete_modes)}

def deprecated_calibration(mode):
    return mode_thresholds.get(mode, 0.5)

# Main data pipeline
raw_segments = [
    [120, 150, 175, 200],
    [90, 110, 105, 130],
    [210, 190, 225, 240],
    [85, 95, 100, 115]
]

# Process each segment with threshold filtering
processed_segments = []
for seg in raw_segments:
    processed = process_sensor_readings(seg, threshold=0.8)
    processed_segments.append(processed)

# Encode segments into integers using bit operations
encoded_segments = []
for p_seg in processed_segments:
    # Use only first 3 elements if available (slicing)
    trimmed = p_seg[:3]
    # Pad with 0.8 if length < 3
    while len(trimmed) < 3:
        trimmed.append(0.8)
    encoded = encode_signal(trimmed)
    encoded_segments.append(encoded)

# Distractor variables - look relevant but unused
redundant_checksum = sum(encoded_segments) % 1000
temporal_weights = [w ** 2 for w in weights[:4]]

# Conditional weight adjustment (only some weights are actually used)
adjusted_weights = [
    w * (1.1 if i % 2 == 0 else 0.9) for i, w in enumerate(weights)
][:4]

# Actual aggregation uses only first 4 encoded values and adjusted weights
# Summation with modular arithmetic and conditional scaling
weighted_sum = 0
for i in range(4):
    contribution = encoded_segments[i] * adjusted_weights[i]
    if contribution > 10000:
        contribution = contribution % 97  # Modular reduction
    weighted_sum += int(contribution)

# Final diagnostic computed from aggregated metric
final_diagnostic = weighted_sum // 4

# Misleading comment: do not trust intermediate checksums
# Note: final_diagnostic depends only on first 4 segments and weight logic

Result: "Target result: " + str(final_diagnostic)