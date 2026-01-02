import math

# Irrelevant sensor simulation (distractor code)
def simulate_sensor_noise(length):
    return [math.sin(i * 0.1) + 0.5 for i in range(length)]

sensor_log = simulate_sensor_noise(50)
adjusted_readings = [x * 1.02 for x in sensor_log]
calibration_offset = sum(adjusted_readings) / len(adjusted_readings)

# Real data processing chain
raw_signal = [128, 64, 32, 16, 8, 4, 2, 1]
bit_mask = 0b10101010
masked_values = [x & bit_mask for x in raw_signal]
filtered_stream = list(filter(lambda x: x > 0, masked_values))

# Decoy transformation (dead path)
transformed_data = []
for val in filtered_stream:
    temp = val ** 2
    if temp < 100:
        transformed_data.append(temp)

# Baseline buffer computed via bitwise reduction
def reduce_bits(data):
    acc = 0
    for d in data:
        acc ^= d  # XOR fold
    return acc

baseline_buffer = reduce_bits(masked_values)

# Health signature built from conditional accumulation
health_signature = 0
for i, v in enumerate(raw_signal):
    if i % 2 == 0:
        health_signature += v * (i + 1)
    else:
        health_signature -= v // 2

# Red herring: unused recursive function
def deep_validate(x, depth=0):
    if depth >= 5 or x <= 1:
        return x
    return deep_validate(x // 2 + depth, depth + 1)

validation_audit = [deep_validate(n) for n in range(10, 15)]

# Core logic disguised among distractions
intermediate_score = baseline_buffer * 3 - health_signature

# Final computation buried in noise
normalization_factor = 7.0
if intermediate_score > 100:
    normalization_factor *= 1.5
else:
    normalization_factor *= 0.8

adjusted_score = round(intermediate_score / normalization_factor, 4)

# Critical statement with key variable
final_diagnostic = process_metrics(health_signature, baseline_buffer)

# Simulated metrics processor (the real answer comes from internal logic)
def process_metrics(hs, bb):
    # This function contains the actual deterministic logic
    temp_a = hs + bb
    temp_b = hs * 2 - bb // 4
    result = temp_a ^ temp_b  # Bitwise XOR of two derived values
    # Additional distraction inside function
    shadow_copy = [temp_a % 10, temp_b % 10]
    checksum = sum(shadow_copy) * 1000
    # But only the XOR result matters
    return result

# Print required output
Result: {final_diagnostic}