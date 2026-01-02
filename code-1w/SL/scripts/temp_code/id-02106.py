import math

# Simulated sensor network diagnostic system
def analyze_pattern(sequence):
    if len(sequence) < 3:
        return False
    trend = all(sequence[i] <= sequence[i+1] for i in range(len(sequence)-1))
    oscillation = sum(1 for i in range(1, len(sequence)-1) if sequence[i-1] < sequence[i] > sequence[i+1])
    return trend or oscillation > 2

# Irrelevant helper - distractor
def calculate_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    return -sum((count/total) * math.log2(count/total) for count in counts.values())

# Dead code path - never called
def legacy_compatibility_mode(config):
    mode_flag = config.get('legacy', False)
    if mode_flag:
        for i in range(len(config['buffer'])):
            config['buffer'][i] ^= 0xFF
    return config

# Decoy function that looks important but isn't used in main flow
def compute_signal_strength(signal, noise_floor=0.05):
    magnitude = sum(x**2 for x in signal)**0.5
    interference = noise_floor * len(signal)
    return magnitude / (interference + 1e-8)

# Core processing with multiple concepts

# Bit manipulation lookup table (partial use)
binary_weights = {i: (1 << i) for i in range(8)}

# Unused transformation map
transform_map = {
    'A': lambda x: x * 1.05,
    'B': lambda x: x * 0.98,
    'C': lambda x: x + math.sin(x)
}

# Conditional expression heavy logic

thresholds = {
    'temp': [70, 100],
    'pressure': [30, 60],
    'vibration': [5, 15],
    'humidity': [20, 80]
}

sensor_data = [
    {'sensor': 'T1', 'type': 'temp', 'reading': 95, 'timestamp': 1680000000},
    {'sensor': 'P2', 'type': 'pressure', 'reading': 45, 'timestamp': 1680000001},
    {'sensor': 'V3', 'type': 'vibration', 'reading': 12, 'timestamp': 1680000002},
    {'sensor': 'H1', 'type': 'humidity', 'reading': 65, 'timestamp': 1680000003},
    {'sensor': 'T2', 'type': 'temp', 'reading': 102, 'timestamp': 1680000004},
    {'sensor': 'P1', 'type': 'pressure', 'reading': 65, 'timestamp': 1680000005},
    {'sensor': 'V2', 'type': 'vibration', 'reading': 3, 'timestamp': 1680000006}
]

# Distractor variables
baseline_correction = sum(binary_weights[i] for i in range(4))  # unused in logic
redundant_checksum = 0
for item in sensor_data:
    redundant_checksum ^= hash(str(item['reading'])) & 0xFFFF

# Real logic buried among distractions
def validate_range(value, bounds):
    low, high = bounds
    return low <= value <= high

# Complex nested processing
status_codes = []
for entry in sensor_data:
    reading = entry['reading']
    s_type = entry['type']
    limits = thresholds.get(s_type, [0, 100])
    
    # Conditional expression with side effect lookalike (no side effects)
    code = 1 if validate_range(reading, limits) else -1
    status_codes.append(code)

# Extract readings by type - relevant
readings_by_type = {}
for entry in sensor_data:
    t = entry['type']
    if t not in readings_by_type:
        readings_by_type[t] = []
    readings_by_type[t].append(entry['reading'])

# Set operations on keys - relevant
expected_types = {'temp', 'pressure', 'vibration', 'humidity'}
active_types = set(readings_by_type.keys())
missing_types = expected_types - active_types

# Diagnostic accumulator
system_health = 0

# Process each type with pattern analysis
for s_type, readings in readings_by_type.items():
    in_bounds = sum(1 for r in readings if validate_range(r, thresholds[s_type]))
    anomaly_score = len(readings) - in_bounds
    
    # Only temp and pressure contribute to final diagnostic
    if s_type in ['temp', 'pressure']:
        trend_stable = analyze_pattern(readings)
        weight = 10 if trend_stable else 25
        system_health += anomaly_score * weight

# Dummy aggregation - irrelevant
aggregate_metrics = {
    'count': len(sensor_data),
    'anomalies': sum(1 for c in status_codes if c == -1),
    'completeness': len(active_types) / len(expected_types),
    'entropy_proxy': calculate_entropy(status_codes) if status_codes else 0
}

# Key computation buried in abstraction
auxiliary_factor = len(missing_types) + 1
primary_contributions = []

for record in sensor_data:
    val = record['reading']
    t = record['type']
    # Only high temp readings above threshold have secondary effect
    if t == 'temp' and val > thresholds['temp'][1]:
        # Each excessive temp reading adds modular contribution
        primary_contributions.append(val % 17)

# Final processing with conditional expression
base_diagnostic = system_health + (sum(primary_contributions) if primary_contributions else 0)
adjustment = 0

# Nested conditionals with red herring branches
if len(primary_contributions) > 1:
    if aggregate_metrics['completeness'] >= 0.75:
        adjustment = -5
    else:
        adjustment = 10  # dead branch due to completeness = 1.0
elif baseline_correction > 100:  # false
    adjustment = 20
else:
    adjustment = 2  # never reached due to primary_contributions having length 2

# Final answer calculation
final_diagnostic = base_diagnostic + adjustment

# Print result as required
print(f"Result: {final_diagnostic}")