import math

# Sensor simulation data (irrelevant initialization)
sensor_baselines = {c: (10 + i) ** 1.5 for i, c in enumerate('ABCDE')}
noise_profile = [math.sin(x / 3) for x in range(10)]

def generate_synthetic(n):
    return [(i * 1.7) % 5 + noise_profile[i % len(noise_profile)] for i in range(n)]

# Irrelevant helper function (dead code path)
def legacy_calibrate(x):
    return x * 0.98 + 0.13

# Core processing pipeline
raw_readings = [4.2, 8.1, 3.3, 9.7, 6.5, 2.8, 7.4, 5.0]

# Distractor transformation (not used in final result)
temp_normalized = [max(0, x - 2.0) for x in raw_readings if x > 3.0]

# Real preprocessing with slicing and filtering
trimmed = raw_readings[1:-1]  # Remove first and last
filtered = [x for x in trimmed if x > 4.0]
squared_devs = [(x - 6.0) ** 2 for x in filtered]

# Threshold system with misleading structure
config_flags = {'adaptive': False, 'strict_mode': True, 'legacy': False}
threshold_map = {
    'low': sum([1 for x in raw_readings if x < 4.0]),
    'high': sum([1 for x in raw_readings if x > 8.0]),
    'critical': len(raw_readings) // 2
}

# Decoy aggregation (unused)
summary_stats = {
    'range': max(raw_readings) - min(raw_readings),
    'median_guess': sorted(raw_readings)[len(raw_readings)//2],
    'entropy': 0.0  # Placeholder, not computed
}

# Actual data processing chain
processed_data = []
for val in filtered:
    shifted = val - 1.5
    if shifted > 5.0:
        processed_data.append(shifted ** 0.5)
    else:
        processed_data.append(shifted / 2.0)

# Red herring: complex but unused calculation
def compute_entropy(data):
    total = sum(data)
    return -sum((x/total) * math.log(x/total) for x in data if x > 0)

unused_entropy = compute_entropy([1, 2, 3])  # Dead computation

# Critical analysis function with nested logic
def analyze_readings(data, thresholds):
    if not data:
        return -1
    
    # Nested conditional red herrings
    adjustment = 0
    if thresholds['low'] > 2:
        adjustment += 5
    elif thresholds['high'] == 1:
        adjustment -= 2
    else:
        adjustment = 3
    
    base_score = sum(data) * 10
    
    # Real logic buried in distractions
    if config_flags['strict_mode'] and thresholds['critical'] >= 3:
        base_score = base_score * 0.8  # Apply penalty
    
    # Final computation using list slicing and set operations
    unique_caps = list(set([int(x) for x in data]))
    capped_sum = sum(unique_caps[:3])  # Only first three unique values
    
    # Interference: multiple competing formulas
    candidate_1 = base_score + adjustment
    candidate_2 = capped_sum * 12
    fallback = math.ceil(max(data) * 3)
    
    # The real answer derivation
    if len(data) >= 3 and max(data) > 2.5:
        result = candidate_2  # This is actually selected
    elif base_score > 50:
        result = candidate_1
    else:
        result = fallback
    
    return result

# Trigger point: critical function call
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Output the target result
print(f"Target result: {final_diagnostic}")