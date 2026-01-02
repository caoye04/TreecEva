from collections import defaultdict, Counter
import math

# Simulated sensor data processing pipeline for environmental monitoring
raw_readings = [104, 95, 110, 90, 120, 85, 115, 100]
threshold = 100
temp_offsets = [3, -2, 5, -4, 6, -1, 2, 0]

# Irrelevant auxiliary data (distractor)
legacy_codes = {'A': 65, 'B': 66, 'Z': 90}
lookup_matrix = [[i * j for j in range(5)] for i in range(5)]

# Preprocessing with red herring transformations
adjusted_readings = []
for i, val in enumerate(raw_readings):
    adjusted = val + temp_offsets[i]
    if adjusted > threshold + 5:
        adjusted -= 10  # arbitrary correction
    adjusted_readings.append(adjusted)

# Dead code path - never executed due to logic (distractor)
if len(adjusted_readings) < 5:
    for i in range(len(adjusted_readings)):
        adjusted_readings[i] = int(math.sqrt(adjusted_readings[i]))

# Bit manipulation decoy (unrelated to final result)
bit_flags = 0b10101010
inverted_flags = bit_flags ^ 0b11111111
shifted_flags = inverted_flags >> 2

# Statistical summary with distraction via multiple structures
reading_stats = defaultdict(int)
for r in adjusted_readings:
    if r >= threshold:
        reading_stats['high'] += 1
    else:
        reading_stats['low'] += 1

freq_counter = Counter(adjusted_readings)
duplicate_count = sum(1 for v in freq_counter.values() if v > 1)

# Simulated time-series segments (unused, distractor)
segments = []
current_seg = []
for x in adjusted_readings:
    current_seg.append(x)
    if len(current_seg) == 4:
        segments.append(current_seg)
        current_seg = []

# Complex conditional scoring with actual logic buried in noise
penalty_rate = 0.85
bonus_multiplier = 1.2
base_score = 500

# Misleading intermediate calculation (not used in final path)
mock_score = base_score
for k in range(reading_stats['low']):
    mock_score -= int(penalty_rate * 15)

# Core evaluation logic hidden among distractions
def apply_correction(data_list):
    corrected = 0
    for d in data_list:
        if d > threshold:
            corrected += (d - threshold) * 2
        elif d < threshold:
            corrected -= (threshold - d) // 2
    return corrected

# Another decoy function that looks important but isn't called
def legacy_calibrate(x):
    return (x * 17) % 101

# Actual relevant metric computation
effective_deviation = apply_correction(adjusted_readings)

# High-level aggregation with plausible but unused alternatives
candidate_bases = [base_score + effective_deviation]
if duplicate_count > 1:
    candidate_bases.append(base_score + effective_deviation - 20)

primary_base = max(candidate_bases)

# Distractor: fake normalization chain
normalized_metrics = []
for val in adjusted_readings:
    norm = val / 100.0
    if norm > 1.0:
        norm = 1.0 + math.log10(norm)
    normalized_metrics.append(round(norm, 3))

# Unused logical branch with complex conditions (red herring)
if reading_stats['high'] >= 5 and any(x % 7 == 0 for x in adjusted_readings):
    primary_base *= bonus_multiplier

# Main data structure for evaluation
metric_data = {
    'deviation': effective_deviation,
    'base': primary_base,
    'size': len(adjusted_readings),
    'anomalies': reading_stats['low']
}

baseline = {
    'tolerance': 15,
    'weight_a': 0.6,
    'weight_b': 0.4
}

# Final computation buried after distractions
def evaluate_performance(metrics, config):
    raw_dev = metrics['deviation']
    base_val = metrics['base']
    n_anomalies = metrics['anomalies']
    
    # Real formula mixed with irrelevant weight discussion in comments
    # Weight A applies to stability, B to performance headroom
    score = base_val
    if raw_dev > 0:
        score += raw_dev * config['weight_a']
    else:
        score += raw_dev * config['weight_b']  # penalty applied differently
    
    # Final adjustment based on anomaly count
    if n_anomalies == 0:
        score *= 1.1
    elif n_anomalies <= 2:
        score *= 1.05
    else:
        score *= (1.0 - n_anomalies * 0.02)
        
    return int(score)

# Execution point of interest
final_score = evaluate_performance(metric_data, baseline)

# Print result as required
print(f"Target result: {final_score}")