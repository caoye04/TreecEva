import itertools

def analyze_readings(readings):
    # Irrelevant transformation: case conversion on numeric mimic
    str_values = [str(int(x)) for x in readings]
    upper_vals = [v.upper() for v in str_values]  # Distractor: looks important
    normalized = [x / max(readings) for x in readings if x > 0]
    return sum(normalized) / len(normalized)


def detect_anomalies(seq, limit):
    anomalies = []
    for i, val in enumerate(seq):
        if val < 0:
            anomalies.append(i)
        if i > limit * 2:  # Dead code path due to limit relation
            break
    return anomalies[:limit]

# Decoy function – never called but looks critical
def compute_score(elements, weights):
    total = 0
    for e, w in zip(elements, weights):
        total += e * w ** 2
    return total / len(weights)

# Misleading data structure with irrelevant entries
system_logs = {
    'errors': [0, 1, 0, 1, 2],
    'timestamp': '2023-08-17',
    'version': 'v2.4.1',
    'debug_mode': True,
    'cache_hits': 421
}

# Real data used in computation
health_data = {
    'sensor_A': [120, 135, 140, 128, 139],
    'sensor_B': [88,  92,  85,  90,  87],
    'sensor_C': [62,  60,  63,  65,  61],
    'baseline': 1.0
}

thresholds = {
    'high': 130,
    'low':  90,
    'critical': 50
}

# Complex nested logic with distractors
flag_map = {'A': True, 'B': False, 'C': True}

intermediate_scores = {}
for key, readings in health_data.items():
    if key == 'baseline':
        continue
    
    # Bitwise decoy
    sensor_id = sum([ord(c) for c in key[-1]]) ^ 256
    
    # Multiple comparisons and logical operations
    above_high = sum(1 for v in readings if v > thresholds['high'])
    below_low = sum(1 for v in readings if v < thresholds['low'])
    valid_range = sum(1 for v in readings if thresholds['low'] <= v <= thresholds['high'])
    
    # Logical short-circuit red herring
    if flag_map.get(key[-1], False) and above_high > 0:
        adjustment = 1.1
    else:
        adjustment = 0.95  # Always taken due to flag_map
    
    # Real calculation path
    avg = sum(readings) / len(readings)
    
    # Irrelevant itertools usage as distraction
    rolling_pairs = list(itertools.pairwise(readings))
    volatility = sum(abs(a - b) for a, b in rolling_pairs)  # Not actually used later
    
    score = avg * adjustment
    intermediate_scores[key] = score

# Dictionary manipulation with cross-references
aggregated = 0
for k, v in intermediate_scores.items():
    if 'A' in k:
        aggregated += v * 1.05
    elif 'B' in k:
        aggregated += v * 0.98
    else:
        aggregated += v

# Unused but plausible dead path
if system_logs['debug_mode']:
    temp_result = [x * 0.5 for x in system_logs['errors'] if x > 1]

# Key statement
final_diagnostic = int(aggregated - 100)  # Final deterministic answer

print(f"Result: {final_diagnostic}")