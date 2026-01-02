def transform_value(x):
    if x < 0:
        return x ** 2 + 3
    elif x == 0:
        return 7
    else:
        return x * 2 - 1

# Sensor simulation (irrelevant but plausible)
sensor_offsets = {'A1': 0.5, 'B2': -1.2, 'C3': 0.0, 'D4': 2.1}
decoys = [transform_value(i - 5) for i in range(10)]

# Real data pipeline starts
raw_readings = [3, -2, 0, 7, 4, -1, 6]
processed_data = []
for val in raw_readings:
    temp = val ** 2
    temp = temp - val
    temp = abs(temp - 4)
    processed_data.append(transform_value(temp))

# Irrelevant frequency map (distraction)
frequency_map = {}
for item in processed_data:
    freq = processed_data.count(item)
    frequency_map[item] = freq

# Threshold logic with red herring branches
def evaluate_stability(x):
    if x > 20:
        return 'OVERHEAT'
    elif 10 <= x <= 20:
        return 'STABLE'
    else:
        return 'CAUTION'  # This path is unused but looks important

# Another decoy function
def calculate_resilience_score(data):
    base = sum(d % 5 for d in data if d > 5)
    penalty = len([d for d in data if d < 3])
    return base * 2 - penalty  # Computation never used

# Core logic buried in noise
def filter_anomalies(seq, limit):
    result = []
    for i, v in enumerate(seq):
        if i == 0:
            continue  # Skip first
        if abs(v - seq[i-1]) > limit:
            result.append(v)
    return result if result else [limit * 2]

# Misleading normalization block (dead code)
normalized = []
scaling_factor = 1.7
for x in processed_data:
    norm = (x - min(processed_data)) / (max(processed_data) - min(processed_data) + 1e-8)
    normalized.append(round(norm * scaling_factor, 3))

# Critical dictionary structure (relevant)
threshold_map = {
    'low': 5,
    'mid': 12,
    'high': 18
}

# Unused diagnostic matrix (distractor)
diagnostic_matrix = [
    [transform_value(i+j) for j in range(5)] 
    for i in range(4)
]

# Real analysis function
def analyze_readings(data, thresholds):
    count_high = 0
    cumulative = 0
    for reading in data:
        if reading > thresholds['mid']:
            count_high += 1
            cumulative += reading
        elif reading > thresholds['low']:
            cumulative += reading // 2
    # Final computation buried in logic
    if count_high > 3:
        final_score = cumulative * 2
    else:
        final_score = cumulative + 100
    return final_score

# Dead recursive branch (looks important but unused)
def recursive_check(n):
    if n <= 1:
        return 1
    return n + recursive_check(n-2)

# Unused string-based analysis (red herring)
data_tag = "".join(str(int(r % 7)) for r in processed_data)
checksum = sum(ord(c) for c in data_tag) % 50

# Actual execution path
filtered_data = filter_anomalies(processed_data, threshold_map['low'])
final_diagnostic = analyze_readings(processed_data, threshold_map)
print(f"Result: {final_diagnostic}")