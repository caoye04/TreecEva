import math

# Simulated sensor array data (temperature in Celsius)
sensor_readings = [23.5, 19.0, 25.3, -1.2, 30.8, 18.7, 27.4, 22.0, 20.1, 35.6, 15.3]

timestamps = ['t01', 't02', 't03', 't04', 't05', 't06', 't07', 't08', 't09', 't10', 't11']
location_tags = ['A1', 'B2', 'C3', 'D4', 'E5', 'F6', 'G7', 'H8', 'I9', 'J10', 'K11']

# Irrelevant transformation: reverse timestamps for no reason
timestamps_reversed = timestamps[::-1]

# Decoy function: appears useful but unused
def analyze_trend(data):
    return sum(1 for i in range(1, len(data)) if data[i] > data[i-1])

# Another decoy: complex string-based checksum (never called)
compute_checksum = lambda tags: ''.join([tag[-1] for tag in tags if tag.startswith('A') or len(tag) == 2])

# Distractor: unrelated statistical calculation
central_value = sensor_readings[len(sensor_readings)//2]
variance_proxy = sum((x - sum(sensor_readings)/len(sensor_readings))**2 for x in sensor_readings) / len(sensor_readings)

# Filter logic: only temperatures above freezing and below critical threshold
filtered_data = [temp for temp in sensor_readings if 0 < temp < 35]

# Red herring: create a parallel list that does nothing
flagged_status = ['alert' if t > 30 else 'normal' for t in sensor_readings]

# Bit manipulation decoy: convert float to int bits (unused)
to_bit_pattern = lambda x: bin(int(x))[2:] if x > 0 else bin(int(x) & 0b11111111)[-8:]
bit_mapped = [to_bit_pattern(int(t)) for t in sensor_readings]

# Core logic disguised among noise
base_threshold = 22.5
dynamic_factor = len([x for x in filtered_data if x > base_threshold]) / len(filtered_data)

# Threshold function using lambda with closure-like behavior
threshold_func = lambda x: x > (base_threshold * (1 + 0.1 * dynamic_factor))

# Real processing function buried in middle of distractions
def process_readings(data, func):
    high_readings = []
    cumulative_weight = 0.0
    for val in data:
        # Weighted progression based on exponential proximity
        if val > 0:
            weight = math.exp(val / 10)
            cumulative_weight += weight
        if func(val):
            high_readings.append(val)
    # Final diagnostic is the rounded difference
    diagnostic_score = len(high_readings) * 100 - int(cumulative_weight)
    return diagnostic_score

# Dead code path: never executed but looks important
def legacy_diagnostic(seq):
    total = 0
    for i, v in enumerate(seq):
        total += v * (i % 3 + 1)
    return total >> 2

# Critical execution point
final_diagnostic = process_readings(filtered_data, threshold_func)

# Output result as required
print(f"Result: {final_diagnostic}")