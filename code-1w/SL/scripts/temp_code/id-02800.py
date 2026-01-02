import math

# Simulated sensor data processing pipeline with red herrings
def generate_noise(length):
    return [math.sin(i * 0.5) + 0.5 for i in range(length)]

# Irrelevant transformation - distractor
def transform_coordinates(x, y):
    rad = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    return rad * math.cos(2*theta), rad * math.sin(2*theta)

# Unused recursive function - dead code path
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Real signal filter but with misleading name and extra logic
def extract_relevant_features(raw_data):
    temp_result = []
    accumulation = 0
    for val in raw_data:
        if abs(val) > 0.3:  # actual filtering condition
            accumulation += val * 1.7
    # Decoy assignment - looks important but unused
    scaling_factor = accumulation / (len(raw_data) + 1e-8)
    return accumulation  # Only this matters

# Bit manipulation decoy - looks like critical crypto but unused
def scramble_bits(value):
    value = (value << 3) & 0xFF
    value ^= 0b10101010
    value = (value >> 2) | (value << 6)
    return value & 0xFF

# Dictionary-based state tracker with irrelevant entries
def build_diagnostics(signal_peak, noise_floor, sample_count):
    return {
        'status': 'nominal',
        'peak_voltage': signal_peak,
        'baseline_drift': noise_floor * 0.07,
        'checksum': (sample_count * 3) % 256,
        'timestamp_ms': 1567890,
        'version': '2.1.0',
        'aux_data': {'mode': 'calibration', 'gain': 1.2}
    }

# Real processing chain
raw_sensor_stream = [0.1, -0.4, 0.8, -0.2, 0.6, 0.9, -0.7, 0.3]
noise_component = generate_noise(len(raw_sensor_stream))

# Mix real and fake data
combined_buffer = []
for i in range(len(raw_sensor_stream)):
    combined_buffer.append(raw_sensor_stream[i] + noise_component[i] * 0.1)

# Apply real filter disguised among irrelevant operations
magnitude_snapshot = max([abs(x) for x in raw_sensor_stream])
size_hint = len(raw_sensor_stream)
diag_metadata = build_diagnostics(magnitude_snapshot, 0.15, size_hint)

# Critical filtering step - key to answer
filtered_data = []
threshold_adjustment = 0.25
for val in combined_buffer:
    if abs(val) > 0.25 + threshold_adjustment:  # effective threshold = 0.5
        filtered_data.append(val * 2.0)

# Another decoy dictionary operation
data_headers = {
    'format': 'binary16',
    'endianness': 'little',
    'compression': None,
    'payload_size': len(filtered_data)
}

data_headers['checksum'] = sum(filtered_data) * 100  # looks important but unused

# Core computation masked by context
feature_score = extract_relevant_features(filtered_data)

# Final transformation with red herring
if len(filtered_data) > 3:
    feature_score -= 1.4
else:
    feature_score += 2.1

# Actual final output calculation
final_output = int(abs(feature_score) + 0.5)  # round to nearest integer

# Misleading post-processing block (never reached due to logic)
counterfactual_path = False
if counterfactual_path and diag_metadata['status'] == 'fault':
    alternate_acc = 0
    for v in raw_sensor_stream:
        alternate_acc += int(scramble_bits(int(abs(v) * 100)))
    final_output = alternate_acc // 3

print(f"Result: {final_output}")