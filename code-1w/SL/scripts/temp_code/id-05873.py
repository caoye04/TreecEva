import itertools

# Sensor data processing simulation with noise filtering and diagnostic computation

def collect_sensor_data():
    raw_readings = [1.2, 3.7, 2.5, 8.1, 4.3, 6.9, 5.0, 7.2, 3.0, 9.5, 2.1, 6.3]
    timestamps = list(range(1000, 1000 + len(raw_readings)))
    labeled_readings = {f't{t}': v for t, v in zip(timestamps, raw_readings)}
    return labeled_readings

# Irrelevant helper - looks useful but unused in final path
def smooth_signal(data):
    smoothed = []
    for i in range(len(data)):
        window = data[max(0, i-1):min(i+2, len(data))]
        smoothed.append(sum(window) / len(window))
    return smoothed

# Decoy function: appears related but never called
def compute_entropy(arr):
    from math import log
    total = sum(arr)
    probs = [v/total for v in arr if v > 0]
    return -sum(p * log(p) for p in probs)

# Real processing chain
noise_floor = 2.3
saturation_threshold = 8.0
normal_range = (3.0, 7.0)

sensor_map = collect_sensor_data()
values_only = list(sensor_map.values())

# Distractor: complex slicing with no impact
trimmed_slice = values_only[1::2][::-1][:5]
offset_correction = sum(trimmed_slice[:3]) / 3 if len(trimmed_slice) >= 3 else 0

# Actual filtering logic
valid_readings = []
for val in values_only:
    if val < saturation_threshold and val > noise_floor:
        valid_readings.append(val)

# Red herring: bitwise operation on float (never executed due to type check)
def apply_mask(x):
    if isinstance(x, int):
        return x ^ 0xFF
    return x

# Another distraction: unused list comprehension with itertools
extended_pairs = [pair for pair in itertools.combinations(values_only, 2) if abs(pair[0] - pair[1]) > 1.5]
count_high_variance_pairs = len(extended_pairs)

# Core logic disguised among distractions
def classify_risk(value):
    if value < normal_range[0]:
        return 'LOW'
    elif value > normal_range[1]:
        return 'HIGH'
    else:
        return 'NORMAL'

risk_levels = [classify_risk(v) for v in valid_readings]

# Accumulation with early termination condition
risk_score = 0
for level in risk_levels:
    if level == 'HIGH':
        risk_score += 3
    elif level == 'LOW':
        risk_score += 1
    else:
        risk_score += 0
    if risk_score >= 10:  # early cap that doesn't trigger
        break

# Critical transformation chain
adjusted_readings = [v * 0.85 for v in valid_readings if v > 2.5]  # further filter and scale

def analyze_trend(data):
    if len(data) < 3:
        return 0
    # Use slicing to get trend direction
    start_avg = sum(data[:2]) / 2
    end_avg = sum(data[-2:]) / 2
    return round(end_avg - start_avg, 4)

trend_index = analyze_trend(adjusted_readings)

# Filtered data used in final step
filtered_data = [round(x, 3) for x in adjusted_readings if normal_range[0] <= x <= normal_range[1]]

# Secondary decoy: complex dictionary manipulation not used
summary_stats = {
    'count': len(valid_readings),
    'peak': max(valid_readings),
    'stable_ratio': len([v for v in valid_readings if classify_risk(v) == 'NORMAL']) / len(valid_readings),
    'flagged': any(v > 7.0 for v in valid_readings)
}

# Final processing function
previous_baseline = [6.1, 5.8, 6.0, 5.9]

# This function actually computes the answer
def process_readings(readings):
    if not readings:
        return -1
    
    # Summation with conditional scaling
    base_sum = sum(readings)
    
    # Bitwise influence (using length as int)
    n = len(readings)
    modifier = n ^ 5 if n < 10 else n & 7  # XOR-based modifier
    
    # Use of itertools in meaningful way
    pairs = list(itertools.combinations(readings, 2))
    if pairs:
        avg_product = sum(a * b for a, b in pairs) / len(pairs)
        return round(base_sum + avg_product / (modifier + 1), 4)
    else:
        return round(base_sum / (modifier + 1), 4)

# Execution point of interest
final_diagnostic = process_readings(filtered_data)

# Print required output
print(f"Target result: {final_diagnostic}")