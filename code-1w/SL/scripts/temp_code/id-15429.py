def analyze_sensor_data(raw_readings):
    filtered = [x for x in raw_readings if x > 0]
    base_average = sum(filtered) / len(filtered) if filtered else 0
    adjusted_values = [x * 1.05 for x in filtered]
    return sum(adjusted_values) / len(adjusted_values) if adjusted_values else 0


def calculate_backflow(flow_sequence, pressure):
    backflow_total = 0
    for i in range(len(flow_sequence)):
        if i % 3 == 0 and flow_sequence[i] < pressure:
            backflow_total += pressure - flow_sequence[i]
    return backflow_total


def optimize_pressure(current_flow, threshold):
    if current_flow < threshold:
        return current_flow * 1.75
    else:
        return current_flow * 0.9

# Sensor inputs and system parameters
readings = [120, -5, 130, 0, 110, 125, -30, 115]
base_pressure = 118
emergency_cap = 200
hysteresis_window = [105, 125]

# Initial data processing
baseline = analyze_sensor_data(readings)

# Simulate flow dynamics
flow_pattern = [int(baseline * (1 + i * 0.05)) for i in range(5)]
temp_offset = sum([x for x in flow_pattern if x > base_pressure])

# Calculate stabilization metrics
instability_score = abs(baseline - base_pressure)
stabilized_flow = baseline - (instability_score * 0.2)

# Misleading diagnostic block (distractor - does not affect final result)
diagnostic_log = []
for reading in readings:
    status = "OK" if reading > 100 else "LOW"
    diagnostic_log.append(f"Sensor: {status}")

# Secondary irrelevant computation chain
buffer_capacity = 500
utilization_ratio = buffer_capacity * 0.78 / (len(readings) or 1)
threshold = hysteresis_window[1] - 8

# Key computational step
final_adjustment = optimize_pressure(stabilized_flow, threshold)

# Final assignment (target variable)
optimized_flow_rate = int(final_adjustment + 0.5)  # Round to nearest integer

# Additional red herring logic
if optimized_flow_rate > emergency_cap:
    optimized_flow_rate = emergency_cap * 0.8

# Output target result
print(f"Result: {optimized_flow_rate}")