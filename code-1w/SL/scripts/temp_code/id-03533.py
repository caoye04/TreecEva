import math

# Simulated bio-signal processing system (irrelevant to final result)
def analyze_waveform(signal):
    if len(signal) == 0:
        return 0
    norm = sum([x ** 2 for x in signal]) / len(signal)
    return math.sqrt(norm)

# Unused diagnostic function (dead code path)
def legacy_diagnosis(data):
    cumulative = 0
    for i in range(len(data)):
        cumulative += data[i] * (i + 1)
    return cumulative % 17

# Distractor: complex transformation with no impact
transform_matrix = [[1, -1, 0], [0, 1, -1], [1, 0, -1]]
rotated_data = [sum(transform_matrix[i][j] * (j + 1) for j in range(3)) for i in range(3)]

# Irrelevant signal synthesis
synthetic_wave = []
for t in range(10):
    synthetic_wave.append(int(5 * math.sin(t * 0.5) + 7))

# Real computation begins here — key data structures
health_signature = [84, 92, 77, 63, 88, 95, 72]

# Misleading normalization (not used in final logic)
normalized_sig = [x / max(health_signature) for x in health_signature]
scaled_product = 1
for val in normalized_sig:
    scaled_product *= (val + 0.1)

# Threshold map uses conditional expressions and bit manipulation
base_threshold = 80
adjustment_flag = (len(health_signature) > 5) << 1 | (sum(health_signature) // 100 & 1)

# Conditional expression chain (python idiom)
threshold_factor = 1.1 if adjustment_flag & 1 else 0.9
threshold_factor *= 0.95 if adjustment_flag >> 1 else 1.05

# Build threshold_map with dummy entries (only one matters)
threshold_map = {}
for i in range(10):
    threshold_map[f'node_{i}'] = base_threshold * (0.8 + (i % 3) * 0.1)

# Critical override — only this matters
threshold_map['primary'] = base_threshold * threshold_factor

# Auxiliary checksum (red herring)
checksum = 0
for k, v in threshold_map.items():
    checksum ^= int(v)

# Core logic: count how many exceed adjusted primary threshold
def process_metrics(metrics, limits):
    primary_limit = limits['primary']
    above_count = 0
    below_penalty = 0
    
    for metric in metrics:
        # Conditional expression inside loop
        delta = metric - primary_limit
        contribution = delta if delta > 0 else (-0.5 * abs(delta))
        above_count += 1 if metric >= primary_limit else 0
        below_penalty += 1 if metric < primary_limit * 0.85 else 0
    
    # Composite score with weighted components
    stability_index = len(metrics) - below_penalty
    raw_score = above_count * 10 + stability_index * 5
    
    # Final adjustment using bitwise logic (key step)
    flag_mask = (above_count & 7) ^ (stability_index & 7)
    if flag_mask > 4:
        raw_score += 8
    else:
        raw_score -= 3
    
    # One more conditional expression twist
    final_adjust = raw_score * 1.1 if above_count >= 4 else raw_score * 0.9
    
    # This is the actual answer variable
    return int(final_adjust)

# Execution point of interest
final_diagnostic = process_metrics(health_signature, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")