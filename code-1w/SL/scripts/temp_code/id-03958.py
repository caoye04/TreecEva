from collections import defaultdict, Counter
import math

# Simulated sensor data ingestion (real and dummy)
sensor_readings = [14, 18, 22, 25, 19, 24, 30, 33, 28, 37, 40, 36, 45, 50, 48]

def preprocess(data):
    # Real preprocessing step: smooth with moving average
    smoothed = []
    for i in range(2, len(data)):
        smoothed.append(sum(data[i-2:i+1]) // 3)
    return smoothed

def evaluate_stability(metric):
    # Distractor function – looks important but unused
    if metric < 10:
        return 'LOW'
    elif metric < 25:
        return 'MEDIUM'
    else:
        return 'HIGH'

def compute_entropy(values):
    # Another distractor: computes entropy but not used in final path
    counts = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def generate_fallback_thresholds(data):
    # Dead code path – never called
    fallback_map = defaultdict(int)
    for val in data:
        fallback_map[val] = val * 0.75 + 10
    return fallback_map

# Irrelevant transformation chain
raw_stats = {
    'peak': max(sensor_readings),
    'trough': min(sensor_readings),
    'mean': sum(sensor_readings) // len(sensor_readings),
    'range': max(sensor_readings) - min(sensor_readings)
}

# Red herring variables
baseline_offset = 7
adjustment_factor = 1.35
interim_result = (raw_stats['mean'] * baseline_offset) % 41

# Real data flow begins here
filtered_data = [x for x in sensor_readings if x > raw_stats['mean']]
shifted_data = [x - 15 for x in filtered_data]  # Normalize around base

# Apply non-linear transformation (relevant)
transformed_data = []
for val in shifted_data:
    if val == 0:
        transformed_data.append(1)
    else:
        transformed_data.append(int(math.log(val) ** 2 + 1))

# Build threshold map (critical component)
threshold_map = defaultdict(float)
categories = ['A', 'B', 'C', 'D']
for idx, cat in enumerate(categories):
    threshold_map[cat] = math.sin(idx * math.pi / 2) * 10

# Unused diagnostic branch (misleading)
temporary_diagnostics = {}
for k in threshold_map:
    temp_score = abs(threshold_map[k]) * 0.5
nonsensical_flag = temp_score > 3.0  # Dead computation

# Core analysis function (nested logic)
def analyze_pattern(seq, thresholds):
    accumulator = defaultdict(int)
    for i, value in enumerate(seq):
        # Complex conditional with multiple concepts
        if i % 2 == 0:
            accumulator['even_index'] += value * 3
        else:
            accumulator['odd_index'] += int(value * 0.5)

        # Additional branching logic
        if value > 5:
            accumulator['high_count'] += 1
            accumulator['magnitude_sum'] += value
        elif value > 2:
            accumulator['mid_count'] += 1
        else:
            accumulator['low_impact'] += 1

    # Composite calculation
    score_component_1 = accumulator['even_index'] + accumulator['magnitude_sum']
    score_component_2 = accumulator['high_count'] * 12
    
    # Final computation path
    result = score_component_1 - score_component_2 + accumulator['odd_index']
    
    # Introduce irrelevant secondary processing
    shadow_copy = dict(accumulator)
    for k in shadow_copy:
        shadow_copy[k] = shadow_copy[k] * 0.1  # Never used

    return result

# Trigger the key statement
final_diagnostic = analyze_pattern(transformed_data, threshold_map)

# Output the target result
print(f"Target result: {final_diagnostic}")