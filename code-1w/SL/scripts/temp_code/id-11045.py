from collections import defaultdict, Counter
import math

# Simulated sensor data with noise and redundant entries
data_log = [
    {'sensor': 'temp', 'value': 23.5, 'status': 'ok'},
    {'sensor': 'pressure', 'value': 1013, 'status': 'ok'},
    {'sensor': 'temp', 'value': 24.1, 'status': 'ok'},
    {'sensor': 'humidity', 'value': 45, 'status': 'warning'},
    {'sensor': 'temp', 'value': -999, 'status': 'error'},  # Invalid reading
    {'sensor': 'pressure', 'value': 1015, 'status': 'ok'},
    {'sensor': 'humidity', 'value': 47, 'status': 'ok'},
    {'sensor': 'temp', 'value': 23.9, 'status': 'ok'},
]

# Weight configuration for scoring (meaningful only for specific sensors)
weights = {'temp': 0.4, 'pressure': 0.35, 'humidity': 0.25}

# Irrelevant statistical counters (distractors)
reading_counter = Counter(entry['sensor'] for entry in data_log)
duplicate_count = sum(1 for count in reading_counter.values() if count > 1)

# Data structure for intermediate processing (some fields unused)
sensor_aggregates = defaultdict(lambda: {'sum': 0, 'count': 0, 'max': float('-inf'), 'invalid': 0})
processed_values = []
flagged_readings = []

# Misleading normalization factor (not actually used in final score)
normalization_factor = max(weight for weight in weights.values()) if weights else 1

# Primary aggregation loop with red herrings and dead logic branches
for entry in data_log:
    sensor = entry['sensor']
    value = entry['value']
    status = entry['status']

    # Filter out invalid readings
    if value == -999 or status == 'error':
        sensor_aggregates[sensor]['invalid'] += 1
        continue

    # Update aggregates only for valid data
    sensor_aggregates[sensor]['sum'] += value
    sensor_aggregates[sensor]['count'] += 1
    if value > sensor_aggregates[sensor]['max']:
        sensor_aggregates[sensor]['max'] = value

    processed_values.append(value)

    # Dead logic branch: status 'warning' is never acted upon beyond logging
    if status == 'warning':
        flagged_readings.append(entry)  # Unused later
        temp_offset = 0.5  # Distractor variable

# Spurious transformation (no impact on result)
sorted_sensors = sorted(sensor_aggregates.keys())
avg_temp_spurious = sensor_aggregates['temp']['sum'] / sensor_aggregates['temp']['count'] if sensor_aggregates['temp']['count'] else 0

# Decoy function that is defined but not used in critical path
def analyze_trend(values):
    if len(values) < 2:
        return 0
    return sum(values[i+1] - values[i] for i in range(len(values)-1))

# Another decoy: computes variance but unused
variance_proxy = 0
if processed_values:
    mean_val = sum(processed_values) / len(processed_values)
    variance_proxy = sum((x - mean_val) ** 2 for x in processed_values) / len(processed_values)

# Core calculation hidden among distractions
def calculate_stability_index(count, invalid):
    if count == 0:
        return 0.0
    return (count - invalid) / (count + invalid)  # Higher = more stable

def calculate_final_score(log, weight_map):
    stability_scores = {}
    avg_values = {}

    # Extract averages and stability from aggregates
    for sensor_name, agg in sensor_aggregates.items():
        count = agg['count']
        invalid = agg['invalid']
        total = count + invalid
        if total > 0:
            stability_scores[sensor_name] = calculate_stability_index(count, invalid)
            avg_values[sensor_name] = agg['sum'] / count if count > 0 else 0

    # Only temperature, pressure, humidity contribute to final score
    weighted_sum = 0.0
    for sensor in ['temp', 'pressure', 'humidity']:
        if sensor in weight_map:
            avg_val = avg_values.get(sensor, 0)
            stability = stability_scores.get(sensor, 0)
            contribution = avg_val * stability * weight_map[sensor]
            weighted_sum += contribution

    # Final transformation: scale by number of valid sensor types
    active_sensors = len([s for s in ['temp', 'pressure', 'humidity'] if s in avg_values])
    scaling_factor = 1 + 0.1 * active_sensors  # Minor boost for more sensors

    final = weighted_sum * scaling_factor

    # Red herring: this block looks important but doesn't affect anything
    diagnostic_code = 0
    if final > 50:
        diagnostic_code = 1
    elif final > 30:
        diagnostic_code = 2
    else:
        diagnostic_code = 3  # Triggered here, but unused

    return final

# Execute main computation
temp_correction_matrix = [[1.01, -0.01], [0.02, 0.99]]  # Unused matrix

final_score = calculate_final_score(data_log, weights)

# Output result as required
print(f"Result: {final_score}")