from collections import defaultdict, Counter
import math

# Simulated sensor data from multiple environmental monitoring units
data_points = [
    (101.2, 'temp', 1), (98.6, 'temp', 2), (75.3, 'humid', 1), (80.1, 'humid', 2),
    (105.8, 'temp', 3), (70.0, 'humid', 3), (110.4, 'temp', 4), (60.2, 'humid', 4),
    (20.1, 'co2', 1), (45.6, 'co2', 2), (30.3, 'co2', 3), (50.8, 'co2', 4)
]

# Irrelevant mapping - distractor for categorical understanding
sensor_names = {'temp': 'TemperatureSensor', 'humid': 'HumidityProbe', 'co2': 'CarbonAnalyzer'}
sensor_status = {name: 'active' for name in sensor_names.values()}

# Distractor function - never called
def validate_calibration(data):
    return all(0 <= val <= 150 for val, _, _ in data)

# Misleading intermediate transformation
raw_aggregates = defaultdict(list)
for value, s_type, unit_id in data_points:
    raw_aggregates[s_type].append(value)

# Compute meaningless per-sensor averages (partial distractor)
average_readings = {k: sum(v)/len(v) for k, v in raw_aggregates.items()} # temp: ~98.875, humid: ~68.9, co2: ~36.7

# Real processing begins: isolate temperature and humidity only
filtered_data = [(v, u) for v, t, u in data_points if t in ['temp', 'humid']]

# Apply non-linear correction based on unit id (simulate calibration curve)
corrected_values = []
for value, unit_id in filtered_data:
    if unit_id == 1:
        corrected_values.append(value * 1.02)
    elif unit_id == 2:
        corrected_values.append(value * 0.98)
    elif unit_id == 3:
        corrected_values.append(value * 1.05)
    else:
        corrected_values.append(value * 0.95)

# Introduce tuple-based pairing with dummy placeholders
temp_hum_pairs = []
i = 0
while i < len(corrected_values) - 1:
    temp_hum_pairs.append((corrected_values[i], corrected_values[i+1]))  # (temp, humid)
    i += 2

# Transform pairs using complex formula: heat_index approximation
transformed_data = []
for t, h in temp_hum_pairs:
    hi = t + 0.5555 * (h - 58)  # Simplified approximation
    transformed_data.append(round(hi, 4))

# Dead code path - unused variant calculation
def calculate_wind_chill(temp, wind):
    return 35.74 + 0.6215*temp - 35.75*(wind**0.16) + 0.4275*temp*(wind**0.16)

# Threshold logic setup
thresholds = {
    'warning': 100.0,
    'critical': 105.0
}

# Auxiliary counter for event tracking (partially relevant)
event_counter = Counter()
for idx, reading in enumerate(transformed_data):
    if reading > thresholds['critical']:
        event_counter['critical'] += 1
    elif reading > thresholds['warning']:
        event_counter['warning'] += 1

# Decoy list comprehension - computes unused index shifts
index_shifts = [i * 2 + 1 for i in range(len(transformed_data)) if i % 2 == 0]

# Core diagnostic processor
weights = {0: 1.1, 1: 0.9, 2: 1.2, 3: 0.8}
weighted_sum = 0
for i, val in enumerate(transformed_data):
    weight = weights.get(i, 1.0)
    weighted_sum += val * weight

baseline = sum(transformed_data) / len(transformed_data)

# Secondary adjustment using zip and enumerate (required idiom)
adjustment_factors = [0.99, 1.01, 1.03, 0.97]
for i, (val, adj) in enumerate(zip(transformed_data, adjustment_factors)):
    transformed_data[i] = val * adj

adjusted_baseline = sum(transformed_data) / len(transformed_data)

# Final processing function
def process_metrics(metrics, limits):
    score = 0
    for m in metrics:
        if m > limits['critical']:
            score += 3
        elif m > limits['warning']:
            score += 1
    # Additional penalty based on deviation from adjusted baseline
    deviation = abs(metrics[0] - adjusted_baseline)
    penalty = int(deviation // 5)
    return score - penalty

# Execute critical statement
final_diagnostic = process_metrics(transformed_data, thresholds)

# Print result as required
print(f"Target result: {final_diagnostic}")