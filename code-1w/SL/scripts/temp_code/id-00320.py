from itertools import cycle

# Simulate sensor readings with noise and valid data segments
def generate_sensor_data():
    base_signal = [12, 15, 14, 18, 22, 25, 24, 20, 17, 16]
    noise = [0, 3, -2, 1, 0, -1, 2, 0, -3, 1]
    return [base_signal[i] + noise[i] for i in range(10)]

data_stream = generate_sensor_data()

# Irrelevant helper: computes moving average but never used
def moving_average(lst, window=3):
    return [sum(lst[i:i+window]) / window for i in range(len(lst) - window + 1)]

# Track state with multiple redundant variables
critical_threshold = 21
trigger_points = []
accumulated_bias = 0.0
reading_count = len(data_stream)
valid_segments = 0

# Misleading flag system based on unrelated condition
system_flags = []
for val in data_stream:
    if val > 20:
        system_flags.append('HIGH')
    elif val < 15:
        system_flags.append('LOW')
    else:
        system_flags.append('NORMAL')

# Dead code path: processes negative values that don't exist
degraded_readings = []
for val in data_stream:
    if val < 0:  # Impossible condition
        degraded_readings.append(abs(val))

# Actual logic begins here: detect rising edge patterns
edge_transitions = 0
for i in range(1, len(data_stream)):
    if data_stream[i-1] < 18 and data_stream[i] >= 18:
        edge_transitions += 1

# Use of tuple unpacking and conditional expression
status_code, mode_flag = (99, 'ACTIVE') if edge_transitions >= 2 else (0, 'STANDBY')
activation_state = 1 if mode_flag == 'ACTIVE' else 0

# Bitwise tracking of detection events (only some bits are meaningful)
detection_signature = 0
for i, val in enumerate(data_stream):
    if val > critical_threshold:
        detection_signature |= (1 << (i % 8))

# Compute checksum of data (irrelevant to final result)
data_checksum = sum(d ^ 7 for d in data_stream) % 100

# Real computation chain starts here
baseline_reference = sum(data_stream[:5]) / 5
recent_reference = sum(data_stream[5:]) / 5
improvement_rate = recent_reference - baseline_reference

# Apply conditional scaling based on transition count
scaling_factor = 1.5 if edge_transitions > 1 else 0.8
adjusted_improvement = improvement_rate * scaling_factor

# Introduce distractor list comprehension with side-effect-free computation
distractor_series = [x * 2 + 1 for x in range(7) if x % 3 != 0]
side_metric = sum(distractor_series) // 3  # Unused later

# Core decision logic using logical operations and iteration
growth_pattern_detected = (improvement_rate > 0) and (edge_transitions >= 2)
strong_signal_burst = any(val > 23 for val in data_stream)

# Final performance evaluation with nested conditionals and arithmetic
final_score = 0
if growth_pattern_detected:
    final_score += 45
    if strong_signal_burst:
        final_score += 30
    else:
        final_score += 10
    
    # Additional boost based on signature bit count (only lower 4 bits matter)
    active_bits = bin(detection_signature & 0xF).count('1')
    final_score += active_bits * 7
else:
    final_score += 20

# Override prevention check (redundant due to logic flow)
if status_code == 99 and activation_state == 1:
    final_score = max(final_score, 50)

# Spurious mutation that doesn't affect outcome
temp_score = final_score
final_score += (data_checksum % 2)  # Adds at most 1, but masked by prior logic
final_score = temp_score  # Undo change — red herring!

# Print result as required
print(f"Result: {final_score}")