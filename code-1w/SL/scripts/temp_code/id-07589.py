from collections import defaultdict, Counter

# Simulated sensor data stream with noise and redundant readings
data_stream = [
    ('temp', 23.5), ('humidity', 45.0), ('temp', 24.1), ('pressure', 1013.25),
    ('humidity', 46.3), ('co2', 415), ('temp', 23.9), ('pressure', 1012.8),
    ('humidity', 47.1), ('temp', 24.0), ('co2', 417), ('humidity', 45.8)
]

# Irrelevant baseline constants for distraction
temp_baseline = 22.0
pressure_baseline = 1015.0
co2_baseline = 400

# Misleading intermediate aggregations (dead computations)
raw_sum = 0
for _, val in data_stream:
    raw_sum += val

# Distractor: unused transformation path
doubled_values = [v * 2 for k, v in data_stream if k == 'temp']
shifted_pressure = [v - pressure_baseline for k, v in data_stream if k == 'pressure']

# Relevant processing: extract only temperature and count occurrences
temps = [v for k, v in data_stream if k == 'temp']
humidity_vals = [v for k, v in data_stream if k == 'humidity']

# Compute mean temperature - relevant step
mean_temp = sum(temps) / len(temps)

# Anomaly detection based on deviation from mean (red herring computation)
anomalies = [t for t in temps if abs(t - mean_temp) > 0.4]

# Unused statistical distraction
variance = sum((t - mean_temp) ** 2 for t in temps) / len(temps)
std_dev = variance ** 0.5

# Simulated diagnostic flags with bit manipulation red herrings
flags = 0b101010
flags ^= 0b111100  # irrelevant toggle
flags |= 0b000001   # set debug bit (unused)

# Real logic begins: frequency analysis of sensor types
sensor_types = [k for k, _ in data_stream]
type_count = Counter(sensor_types)

# Only 'temp' and 'humidity' are active; others ignored
active_sensors = {k: v for k, v in type_count.items() if k in ['temp', 'humidity']}

# Weight assignment with conditional expression
weight_map = {s: 1.5 if s == 'temp' else 1.2 for s in active_sensors}

# Aggregate weighted score
weighted_scores = defaultdict(float)
for k, v in data_stream:
    if k in weight_map:
        weighted_scores[k] += v * weight_map[k]

aggregate_score = sum(weighted_scores.values())

# Decoy scoring using enumerate and zip (irrelevant)
indexed_temps = list(enumerate(temps))
indexed_humid = list(enumerate(humidity_vals))
zipped_pairs = list(zip(indexed_temps, indexed_humid))
avg_pair_ratio = sum((t[1] / h[1]) for (i, t), (j, h) in zipped_pairs) / len(zipped_pairs) if zipped_pairs else 0

# Correction factor based on anomaly presence (only depends on count)
anomaly_weight = len(anomalies) if len(anomalies) > 0 else 1

# Fake complexity: nested conditional expression with dummy branches
correction_factor = (
    2.5 if mean_temp > 25 else
    1.8 if mean_temp < 23 else
    2.1
)

# Key statement: final diagnostic computation
final_diagnostic = aggregate_score + correction_factor * anomaly_weight

# Output result
print(f"Result: {final_diagnostic}")