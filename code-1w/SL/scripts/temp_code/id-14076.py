from collections import defaultdict, Counter
from itertools import zip_longest

# Simulated sensor data aggregation (real-world context: environmental monitoring)
sensor_readings = [
    {'temp': 23.5, 'humidity': 65, 'co2': 410, 'sensor_id': 'S1', 'status': 'active'},
    {'temp': 25.1, 'humidity': 60, 'co2': 425, 'sensor_id': 'S2', 'status': 'active'},
    {'temp': 22.8, 'humidity': 68, 'co2': 395, 'sensor_id': 'S3', 'status': 'active'},
    {'temp': 24.3, 'humidity': 63, 'co2': 418, 'sensor_id': 'S4', 'status': 'inactive'},
]

# Irrelevant auxiliary data — distractor
legacy_mappings = {
    'L1': {'x': 10, 'y': 20},
    'L2': {'x': 15, 'y': 25},
    'L3': {'x': 30, 'y': 40}
}

# Dead function — misleading but unused
def legacy_transform(data):
    return [d['x'] * 2 + d['y'] for d in data.values()]

# Real processing pipeline starts here
status_filter = lambda s: s['status'] == 'active'
active_sensors = list(filter(status_filter, sensor_readings))

# Extract and scale CO2 levels — relevant
co2_levels = [reading['co2'] for reading in active_sensors]
scaled_co2 = [round(c * 1.02) for c in co2_levels]  # calibration factor

# Bit manipulation for checksum simulation — actual use in logic
checksum = 0
for val in co2_levels:
    checksum ^= int(val)
    checksum = (checksum << 1) & 0xFFFF

# Create shifted baselines — partially relevant
baseline_shift = sum(co2_levels) // len(co2_levels)
adjusted_readings = [{
    'temp': r['temp'],
    'humidity': r['humidity'],
    'co2': r['co2'] - baseline_shift + 100  # normalize around 100
} for r in active_sensors]

# Data transformation with zip_longest — real use
transposed = list(zip_longest(
    [a['temp'] for a in adjusted_readings],
    [a['humidity'] for a in adjusted_readings],
    [a['co2'] for a in adjusted_readings],
    fillvalue=0
))

# Apply nonlinear transformation using lambda
transform_fn = lambda x: (x ** 2) / (x + 10) if x > 0 else 0
transformed_data = [
    tuple(transform_fn(val) for val in row)
    for row in transposed
]

# Decoy statistical summary — irrelevant
summary_stats = defaultdict(float)
for reading in sensor_readings:
    for k, v in reading.items():
        if isinstance(v, (int, float)):
            summary_stats[k] += v

# Unused counter — red herring
count_by_status = Counter(r['status'] for r in sensor_readings)

# Configuration with decoy keys
config = {
    'calibration_factor': 1.02,
    'threshold': 400,
    'mode': 'strict',
    'debug_trace': True,
    'version': '2.1',
    'use_legacy': False
}

# Core metric processor — only this matters
def process_metrics(data, cfg):
    total_score = 0.0
    for row in data:
        filtered = [v for v in row if v > cfg['threshold'] * 0.1]
        if len(filtered) >= 2:
            product = 1
            for v in filtered:
                product *= v
            total_score += product % 100
        else:
            total_score += sum(filtered)
    
    # Final adjustment based on checksum (used earlier)
    global checksum
    adjustment = (checksum % 50) / 10.0
    return round(total_score + adjustment, 6)

# Key execution point
final_diagnostic = process_metrics(transformed_data, config)

# Print result as required
print(f"Target result: {final_diagnostic}")