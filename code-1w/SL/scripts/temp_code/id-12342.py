import itertools

# Simulated sensor data processing system for environmental monitoring
sensor_ids = ['S1', 'S2', 'S3', 'S4']
data_points = [127, 255, 83, 191]
noise_floor = 64
calibration_factor = 0.87

# Irrelevant symbolic constants (distractors)
MAX_BUFFER_SIZE = 1024
PACKET_OVERHEAD = 12
RETRY_LIMIT = 3
TIMEOUT_DELAY = 0.5

# Simulated raw signal input with noise injection
raw_signals = [dp ^ noise_floor for dp in data_points]
filtered_signals = [int(fs * calibration_factor) for fs in raw_signals]

# Advanced feature extraction using bit manipulation and arithmetic
feature_vector = []
for fs in filtered_signals:
    high_bits = (fs >> 5) & 0x7
    low_bits = fs & 0x1F
    combined_feature = (high_bits ^ low_bits) + (fs % 11)
    feature_vector.append(combined_feature)

# Dead code path: unused transformation chain (red herring)
def legacy_transform(x):
    return (x << 2) | (x >> 1)

legacy_results = [legacy_transform(fv) for fv in feature_vector]  # Unused

# Control flow with conditional masking (partially relevant)
mask_threshold = 20
masked_features = [
    fv if fv > mask_threshold else (fv | 0x10) 
    for fv in feature_vector
]

# Decoy statistical computation (misleading intermediate result)
mean_masked = sum(masked_features) / len(masked_features)
variance_proxy = sum((x - mean_masked) ** 2 for x in masked_features) / len(masked_features)

# Real logic begins: pattern detection using itertools
consecutive_pairs = list(itertools.pairwise(masked_features))
pattern_matches = []
for a, b in consecutive_pairs:
    if (a & 0x1) and (b % 3 == 0) and (abs(a - b) > 5):
        pattern_matches.append(a + b)

# Secondary filtering based on logical conditions
trigger_conditions = [
    (pm >> 3) & 1 for pm in pattern_matches
]
activation_count = sum(trigger_conditions)

# Simulated metric generation with redundant operations
metric_data = []
base_multiplier = 2.5
for i, pm in enumerate(pattern_matches):
    # Complex but partially irrelevant transformation
    scaled = pm * base_multiplier
    adjusted = scaled - (i * 0.7)
    normalized = max(adjusted, 10.0)
    metric_data.append(normalized)

# Spurious function call with no side effects (distractor)
def calculate_checksum(data):
    return sum(data) % 256

checksum = calculate_checksum(raw_signals)  # No impact on final result

# Unused recursive function (dead code - red herring)
def recursive_doubler(n, depth=0):
    if depth >= 3:
        return n
    return recursive_doubler(n * 2, depth + 1)

# Base threshold derived from feature statistics (relevant)
base_threshold = sum(feature_vector) // len(feature_vector)

# Main evaluation logic with short-circuiting and logical complexity
def evaluate_performance(metrics, threshold):
    if not metrics or threshold < 5:
        return -1
    
    aggregate = 0.0
    weight_sequence = [1.1, 0.9, 1.2, 0.8]  # Cycling weights
    
    for i, m in enumerate(metrics):
        weight = weight_sequence[i % len(weight_sequence)]
        contribution = m * weight
        
        # Logical gate with short-circuit behavior
        if contribution > threshold * 1.5 and (int(contribution) & 7) != 5:
            aggregate += contribution
        elif i % 2 == 0:
            aggregate += contribution * 0.5
        else:
            continue
    
    # Final adjustment using bitwise and arithmetic mix
    int_part = int(aggregate)
    frac_part = aggregate - int_part
    final = (int_part ^ 0xFF) + frac_part  # Bit flip on lower byte
    
    # One last correction: undo excess bitflip if over threshold
    if (int_part ^ 0xFF) > threshold * 2:
        final = int_part + frac_part  # Revert bit manipulation
    
    return final

# Critical execution point
final_score = evaluate_performance(metric_data, base_threshold)

# Output the target result
print(f"Target result: {final_score}")