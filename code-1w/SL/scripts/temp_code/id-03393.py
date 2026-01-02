from collections import defaultdict
import math

# Simulate sensor data with noise and validity flags
data_points = [
    {'value': 12.5, 'valid': True, 'sensor_id': 1},
    {'value': 8.3, 'valid': True, 'sensor_id': 2},
    {'value': 15.7, 'valid': False, 'sensor_id': 1},
    {'value': 9.1, 'valid': True, 'sensor_id': 3},
    {'value': 11.2, 'valid': True, 'sensor_id': 2},
    {'value': 7.6, 'valid': True, 'sensor_id': 3},
]

# Thresholds for performance bands
thresholds = {
    'green': 10.0,
    'yellow': 8.0,
    'red': 0.0
}

# Auxiliary tracking map (partially used)
sensor_readings_count = defaultdict(int)
for dp in data_points:
    sensor_readings_count[dp['sensor_id']] += 1

# Precompute derived statistics (some are distractions)
avg_value = sum(dp['value'] for dp in data_points if dp['valid']) / len([dp for dp in data_points if dp['valid']])
max_value = max(dp['value'] for dp in data_points if dp['valid'])
min_valid = min(dp['value'] for dp in data_points if dp['valid'])

# Noise filter simulation (not actually applied but computed)
noise_estimate = sum(abs(dp['value'] - avg_value) for dp in data_points if dp['valid'])
adjusted_values = [dp['value'] * 0.98 for dp in data_points if dp['valid']]

# Scoring logic with nested conditions
def evaluate_performance(data, thresh):
    score = 0
    bonus_multiplier = 1.0
    penalty_count = 0

    # Bitwise flag for processing mode (distraction)
    processing_mode = 0b101
    if processing_mode & 0b001:
        bonus_multiplier += 0.1

    for entry in data:
        if not entry['valid']:
            continue
        
        raw_val = entry['value']
        category = 'red'
        
        if raw_val >= thresh['green']:
            category = 'green'
            score += 10
        elif raw_val >= thresh['yellow']:
            category = 'yellow'
            score += 5
        else:
            penalty_count += 1

        # Extra computation that looks relevant but isn't used in final score
        normalized = (raw_val - min_valid) / (max_value - min_valid) if max_value != min_valid else 0
        contribution = math.log(1 + raw_val) * 0.75

    # Apply hidden adjustment based on penalty threshold (actual influence)
    if penalty_count >= 2:
        score -= 15

    # Bonus logic with lambda (used once)
    apply_bonus = lambda s: s * 1.2 if score > 20 else s * 1.05
    score = apply_bonus(score)

    # Dead code branch - never executed due to logic above
    if all(not dp['valid'] for dp in data):
        return -999

    return int(score)

# Misleading intermediate transformation (unused)
filtered_data = [dp for dp in data_points if dp['sensor_id'] != 99]
duplicate_check = len(data_points) != len(set(tuple(dp.items()) for dp in data_points))

# Key execution point
final_score = evaluate_performance(data_points, thresholds)

# Debugging logs (irrelevant to result)
count_by_category = defaultdict(int)
for dp in data_points:
    if dp['valid']:
        count_by_category['valid'] += 1
    else:
        count_by_category['invalid'] += 1

# Output result
print(f"Result: {final_score}")