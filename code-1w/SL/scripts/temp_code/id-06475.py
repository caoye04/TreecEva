from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    (100, 'sensor_A', 23.5), (101, 'sensor_B', 45.1), (102, 'sensor_A', 24.0),
    (103, 'sensor_C', 12.8), (104, 'sensor_B', 44.9), (105, 'sensor_A', 25.2),
    (106, 'sensor_D', 88.3), (107, 'sensor_C', 13.1), (108, 'sensor_A', 26.0)
]

# Irrelevant helper function (decoy)
def analyze_frequency(signal):
    return sum(math.sin(x * 0.1) for x in range(len(signal)))

# Unused transformation map (dead code path)
transformation_map = {
    'A': lambda x: x ** 2,
    'B': lambda x: x + 10,
    'C': lambda x: math.log(x + 1),
    'D': lambda x: abs(x - 50)
}

# Distractor: complex but unused data structure
class DataBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [0] * size
    
    def push(self, val):
        self.buffer.append(val)
        return self.buffer.pop(0)

buffer = DataBuffer(5)

# Sensor calibration offsets (some relevant, some misleading)
calibration = {
    'sensor_A': 0.95,
    'sensor_B': 1.02,
    'sensor_C': -0.15,
    'sensor_X': 5.0,  # irrelevant sensor
    'sensor_Y': -3.2  # irrelevant sensor
}

# Process raw telemetry into grouped readings
grouped_readings = defaultdict(list)
for timestamp, sensor_id, reading in telemetry_stream:
    if sensor_id in calibration:
        adjusted = reading * calibration[sensor_id]
        grouped_readings[sensor_id].append(adjusted)

# Distractor variables
aggregate_trace = []
total_segments = 0
redundant_sum = 0

for key, values in grouped_readings.items():
    aggregate_trace.extend(values)
    total_segments += len(values)
    redundant_sum += sum(v ** 0.5 for v in values if v > 20)

# Another red herring: frequency analysis on unrelated signal
signal_data = [x[2] for x in telemetry_stream]
frequency_metric = analyze_frequency(signal_data)

# Real computation begins: weight optimization based on variance
variance_map = {}
for sensor, readings in grouped_readings.items():
    mean_val = sum(readings) / len(readings)
    variance = sum((x - mean_val) ** 2 for x in readings) / len(readings)
    variance_map[sensor] = variance

# Optimization heuristic: inverse variance weighting
raw_weights = {s: 1 / (v + 0.1) for s, v in variance_map.items()}
total_weight = sum(raw_weights.values())
optimized_weights = {s: w / total_weight for s, w in raw_weights.items()}

# Performance log with enumerated events
performance_log = []
events = ['startup', 'calibration', 'sync', 'transfer', 'verify', 'report']
for idx, event in enumerate(events):
    char_count = sum(1 for c in event if c in 'aeiou')
    performance_log.append((idx, event, char_count * 10))

# Secondary distractor: set operations with no impact
unique_sensors = set(grouped_readings.keys())
expected_sensors = {'sensor_A', 'sensor_B', 'sensor_C', 'sensor_D'}
missing = expected_sensors - unique_sensors  # empty, but computed anyway

# Core processing function
def process_metrics(weights, log_entries):
    base_score = 0
    
    # Mix weights and log using zip and enumerate
    for i, (index, name, score) in enumerate(log_entries):
        if name == 'report':
            base_score += score * 2
        else:
            base_score += score
    
    # Apply weight adjustments from sensors
    adjustment = 0
    for (sensor, w), (i, _, _) in zip(weights.items(), enumerate(log_entries)):
        adjustment += w * (i + 1) * 0.5
    
    # Final non-linear transformation
    final = base_score * (1 + adjustment)
    
    # Distractor inside function
    temp_history = []
    for _, _, val in log_entries:
        temp_history.append(val ** 0.5 if val > 0 else 0)
    
    return int(final)

# Critical execution point
final_score = process_metrics(optimized_weights, performance_log)
print(f"Target result: {final_score}")