import itertools

# Sensor simulation data (irrelevant in part)
sensor_offsets = [0.1, -0.3, 0.4, 0.05]
base_calibration = {f'sensor_{i}': (i % 3) - 1 for i in range(5)}

# Irrelevant preprocessing chain
def adjust_signal(x, factor=1.0):
    return x * factor + 0.01

def deprecated_filter(seq):
    return [x for x in seq if x > 0.5]  # Unused function

data_stream = [18, 23, 15, 40, 8, 33, 27, 12]
offset_index = sum([i for i, x in enumerate(data_stream) if x > 20]) % 4

# Real processing begins here
processed_data = []
for i, val in enumerate(data_stream):
    temp = val
    if i % 2 == 0:
        temp = temp // 2
    if temp < 20 and i < len(data_stream) - 1:
        temp += data_stream[i + 1] % 4
    processed_data.append(temp)

# Threshold system with red herring entries
threshold_map = {}
for k, v in base_calibration.items():
    key_num = int(k.split('_')[1])
    if key_num % 2 == 0:
        threshold_map[k] = 18 + v * 3
    else:
        threshold_map[k] = 12 + abs(v)

# Decoy aggregation (never used)
rolling_stats = list(itertools.accumulate([x % 7 for x in data_stream], lambda a, b: a + b * 0.9))
summary_moments = {"skew": 0.8, "kurt": 3.1, "dummy": rolling_stats[-1]}

# Core logic hidden among distractions
def evaluate_stability(x):
    if x < 10:
        return 2
    elif x < 25:
        return 1
    else:
        return 0

def count_transitions(seq):
    changes = 0
    for i in range(1, len(seq)):
        if seq[i] != seq[i-1]:
            changes += 1
    return changes

def analyze_readings(data, thresholds):
    # Extract relevant thresholds (only sensor_0 to sensor_3 matter)
    relevant_thresholds = [thresholds[f'sensor_{i}'] for i in range(4)]
    
    # Map data points to categories based on threshold crossings
    category_map = []
    for i, reading in enumerate(data):
        cross_count = 0
        for t in relevant_thresholds:
            if reading > t:
                cross_count += 1
        category_map.append(evaluate_stability(cross_count))
    
    # Accumulate diagnostic score
    score = 0
    for val in category_map:
        score += val * 3
    
    # Apply transition penalty only if more than 3 transitions
    transitions = count_transitions(category_map)
    if transitions > 3:
        score -= 2
    
    # Final adjustment using first reading and offset (distractor partially used)
    adjustment = int(sensor_offsets[offset_index] * 10)  # maps to -3, from offset_index
    score += adjustment
    
    return score

# Unused recursive function (red herring)
def forecast_next(val_list, depth=3):
    if depth == 0 or len(val_list) == 0:
        return 0
    avg = sum(val_list) / len(val_list)
    return avg + forecast_next([x - avg for x in val_list[::2]], depth - 1)

# Critical execution point
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Output the result
print(f"Result: {final_diagnostic}")