import math

def analyze_sensor(value, threshold, mode):
    if mode == 'A':
        return int(value > threshold)
    elif mode == 'B':
        return int(abs(value - threshold) < 0.1)
    else:
        return 0

def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        p = v / total
        if p > 0:
            entropy -= p * math.log(p)
    return round(entropy, 6)

def shift_sequence(seq, n):
    # Irrelevant helper function (dead code path)
    return seq[-n:] + seq[:-n]

def validate_checksum(data):
    # Unused validation logic (distractor)
    checksum = 0
    for d in data:
        checksum = (checksum + d) % 257
    return checksum == 131

def filter_outliers(stream, factor=1.5):
    # Computes but ultimately unused result
    median_val = sorted(stream)[len(stream)//2]
    mad = sorted([abs(x - median_val) for x in stream])[len(stream)//2]
    threshold = factor * mad
    return [x for x in stream if abs(x - median_val) <= threshold]

def aggregate_diagnostics(diagnostics, thresholds):
    base_score = 0
    for i, (d, t) in enumerate(zip(diagnostics, thresholds)):
        if i % 2 == 0:
            base_score += d * (t % 7)
        else:
            base_score -= (d + 1) // (t % 3 + 1)
    
    adjustment = 0
    temp_series = [diagnostics[i] * thresholds[i] for i in range(len(diagnostics)) if thresholds[i] > 0]
    if len(temp_series) >= 3:
        trend = temp_series[-1] - temp_series[0]
        if trend > 5:
            adjustment = 8
        elif trend < -5:
            adjustment = -8
        else:
            adjustment = int(compute_entropy(temp_series))
    
    # Key red herring: complex-looking but irrelevant bit manipulation
    decoy_state = 0
    for val in diagnostics:
        decoy_state ^= (val * 17) % 19
        decoy_state = (decoy_state << 1) | (decoy_state >> 7)
    decoy_state &= 0xFF
    
    # Another distraction: string-based encoding that doesn't affect output
    encoded = ''.join([chr(97 + (d % 26)) for d in diagnostics[:4]])
    modifier = sum([ord(c) - 96 for c in encoded]) if 'm' in encoded else 0
    
    final_score = base_score + adjustment  # Actual determinant of answer
    
    # Conditional expression used per language-specific requirement
    final_diagnostic = final_score if final_score >= 0 else -final_score
    
    return final_diagnostic

# Simulated sensor readings and configurations
sensor_readings = [102, 104, 97, 110, 108]
target_thresholds = [95, 100, 90, 115, 105]
modes = ['A', 'B', 'A', 'A', 'B']

# Generate diagnostic flags
raw_diagnostics = [
    analyze_sensor(sensor_readings[i], target_thresholds[i], modes[i]) 
    for i in range(len(sensor_readings))
]

# Unused outlier filtering (distractor path)
filtered_diagnostics = filter_outliers([d * 10 for d in raw_diagnostics] + [255, -12])

# Entropy computed but not directly used in final decision
auxiliary_entropy = compute_entropy(raw_diagnostics + [1, 1])

# Critical computation occurs here
final_diagnostic = aggregate_diagnostics(raw_diagnostics, target_thresholds)

print(f"Result: {final_diagnostic}")