from collections import defaultdict, Counter
import math

# Simulated sensor array with redundant and auxiliary data
sensor_ids = ['S1', 'S2', 'S3', 'S4', 'S5']
auxiliary_tags = ['A7', 'B9', 'C3', 'D2', 'E8']

# Real measurement data (relevant)
sensor_data = [144, 256, 169, 121, 196]  # perfect squares for root extraction

def analyze_pattern(sequence):
    # Irrelevant pattern analysis (distractor)
    freq = Counter(sequence)
    return max(freq.values()) - min(freq.values())

def validate_consistency(log_entries):
    # Dead code path — never used in execution (red herring)
    if len(log_entries) < 3:
        return False
    trend = all(log_entries[i] <= log_entries[i+1] for i in range(len(log_entries)-1))
    return trend

def accumulate_diagnostics(values, mode='safe'):
    # Unused accumulation function (decoy)
    total = 0
    for v in values:
        if mode == 'aggressive':
            total += int(math.sqrt(v)) * 2
        else:
            total += int(math.sqrt(v))
    return total

def apply_mask(data, mask_level=3):
    # Bit manipulation distraction: applies XOR shift mask (not used in final result)
    masked = []
    for d in data:
        masked.append(d ^ (mask_level << 2))  # irrelevant transformation
    return masked

def compute_entropy(values):
    # Scientific-sounding but irrelevant computation (misleading intermediate)
    norm = sum(values)
    probs = [v / norm for v in values]
    entropy = -sum(p * math.log2(p) for p in probs if p > 0)
    return round(entropy, 4)

def extract_signatures(tags, base_offset=10):
    # Unused tagging logic (distractor)
    sig_map = {}
    for i, tag in enumerate(tags):
        sig_map[tag] = (i + base_offset) ** 2 % 7
    return sig_map

def process_readings(readings, factor):
    # Core relevant logic hidden among distractions
    adjusted = [x // factor for x in readings]  # integer division
    
    # Conditional expression based on threshold
    refined = [val if val > 30 else val * 2 for val in adjusted]
    
    # Key transformation: take square roots (since inputs are perfect squares)
    roots = [int(math.sqrt(x)) for x in refined]
    
    # Use of enumerate and zip to align with dummy identifiers (partially relevant)
    indexed_roots = {i: root for i, root in enumerate(roots)}
    paired = list(zip(sensor_ids, roots))
    
    # Actual computation for final result
    temp_sum = sum(roots)
    correction = len(paired) * 2
    diagnostic_score = temp_sum - correction
    
    # Secondary adjustment using set operations (minimal but valid use)
    unique_roots = set(roots)
    if len(unique_roots) > 3:
        diagnostic_score += 5
    
    return diagnostic_score

# Calibration parameter (relevant)
calibration_factor = 4

# Auxiliary metadata (irrelevant)
metadata_log = defaultdict(str)
for sid in sensor_ids:
    metadata_log[sid] = 'UNCALIBRATED'

# Decoy data structure
aux_data = {
    'checksums': [apply_mask(sensor_data)[0] for _ in range(3)],
    'pattern_delta': analyze_pattern(sensor_data),
    'entropy': compute_entropy(sensor_data)
}

# Critical execution point
final_diagnostic = process_readings(sensor_data, calibration_factor)

# Print required output
print(f"Result: {final_diagnostic}")