import math

# Simulated sensor data processing with embedded diagnostics
def process_sensor_stream(raw_readings, threshold=0.5):
    normalized = [x / 100.0 for x in raw_readings if x > 5]
    filtered = list(filter(lambda x: x < threshold, normalized))
    return [round(x * 1000) for x in filtered]

# Irrelevant helper: used nowhere but looks important
def encrypt_vector(data):
    return [d ^ 255 for d in data]

# Security sub-routine with red herring logic
def security_check(offset):
    mask = 0
    for i in range(8):
        mask |= (1 << i)
    temp_key = (offset * 31) & mask
    decoy_hash = sum([i * temp_key for i in range(5)])  # unused
    return temp_key - 22

# Data transformation with case conversion side-operation (distractor)
def transform_case_sensitive(data):
    result = []
    for item in data:
        text_repr = str(item)
        toggled = ''.join([c.lower() if c.isupper() else c.upper() for c in text_repr])
        if toggled.isdigit():
            result.append(int(toggled))
    return result or [113]

# Core metric aggregator (critical path)
def aggregate_metrics(data, base):
    shift = len(data) % 4
    adjusted = [(x >> shift) + base for x in data]
    checkpoint = sum(adjusted[:3])  # misleading focus point
    
    # Complex conditional that ultimately simplifies
    if len(data) > 4:
        factor = 2 if sum(data) % 2 == 0 else 1
        return int(math.sqrt(checkpoint ** 2) * factor)
    else:
        return checkpoint * 2

# Dead function: appears connected but unused
def validate_checksum(seq):
    return sum(seq) % 256 == 0

# Initialization sequence with decoy variables
raw_sensor_data = [73, 45, 67, 89, 23, 91, 15, 65]
scaling_factor = 1.7
baseline = 7
activation_code = [0xAA, 0xBB, 0xCC]

# Distractor computation chain
checksummed = [x ^ 0xFF for x in activation_code]
decoy_signal = sum(checksummed) / len(checksummed)

# Real processing begins here
processed = process_sensor_stream(raw_sensor_data, threshold=0.65)
transformed_data = transform_case_sensitive(processed)

# Unused alternate path
if len(transformed_data) > 10:
    transformed_data = [x * 2 for x in transformed_data]

offset = transformed_data[0] % 19

# Critical statement containing answer derivation
temp_diagnostic = aggregate_metrics(transformed_data, baseline)
final_diagnostic = aggregate_metrics(transformed_data, baseline) + security_check(offset)

print(f"Result: {final_diagnostic}")