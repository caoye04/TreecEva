import itertools

# Simulate multi-sensor diagnostic system with noise filtering and health scoring
def analyze_sensor_stream(raw_readings, threshold=75):
    filtered_data = []
    noise_counter = 0
    spike_buffer = []

    for reading in raw_readings:
        if reading < 0:
            noise_counter += 1
            continue
        if reading > 100:
            spike_buffer.append(reading)
            continue
        filtered_data.append(reading)

    # Irrelevant statistics (distractor)
    avg_spike = sum(spike_buffer) / len(spike_buffer) if spike_buffer else 0
    noise_ratio = noise_counter / len(raw_readings) if raw_readings else 0

    # Core logic: compute health score from valid readings
    base_score = sum(filtered_data)
    penalty = 0
    for i in range(1, len(filtered_data)):
        if filtered_data[i] < filtered_data[i-1]:
            penalty += 1

    health_score = base_score - penalty * 2

    # Dead code path - never executed under current conditions
    if False:
        health_score = max(health_score, 50)

    return health_score

# System configuration
sensor_inputs = [88, 92, -5, 76, 81, 95, 102, 67, 73, -3, 88, 79, 110, 65]
system_mode = 'diagnostic'
system_offset = 17  # Calibration offset for hardware drift

# Generate auxiliary test patterns (distractor using itertools)
repeated_cycle = list(itertools.repeat(sensor_inputs[0:3], 2))
flattened_cycle = [item for sublist in repeated_cycle for item in sublist]
extended_diagnostics = [x * 1.05 for x in flattened_cycle if x > 70]

# Secondary analysis on extended data (irrelevant to final result)
smoothed_values = []
for val in extended_diagnostics:
    if val > 80:
        smoothed_values.append(val * 0.95)
    else:
        smoothed_values.append(val * 1.02)

average_smoothed = sum(smoothed_values) / len(smoothed_values) if smoothed_values else 0
device_stability_index = average_smoothed / 100

# Primary diagnostic analysis (core relevant computation)
aggregate_health_score = analyze_sensor_stream(sensor_inputs)

# Final calibration step — this is where the answer is determined
temp_debug_flag = False
if temp_debug_flag:
    final_diagnostic = 0
else:
    final_diagnostic = aggregate_health_score + system_offset

print(f"Result: {final_diagnostic}")