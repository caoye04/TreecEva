import itertools

# System calibration parameters for thermal regulation
base_temperature = 298.15
pressure_coefficient = 1.023
humidity_factor = 0.87

# Initialize sensor array readings (simulated)
sensor_readings = [23.5, 24.1, 22.9, 25.0, 23.8]

calibration_offset = sum(sensor_readings) / len(sensor_readings) - base_temperature

# Redundant environmental compensation (not used in final calculation)
compensation_matrix = []
for i, reading in enumerate(sensor_readings):
    compensated = reading * pressure_coefficient * (1 + i * 0.01)
    compensation_matrix.append(compensated)

# Historical average comparison (distractor computation)
historical_min = min(sensor_readings)
historical_max = max(sensor_readings)
historical_avg = (historical_min + historical_max) / 2
avg_deviation = abs(historical_avg - (sum(sensor_readings) / len(sensor_readings)))

# Core system constants
reference_voltage = 5.0
resistance_factor = 0.91
base_capacity = int(sum(sensor_readings))  # Derived from raw sensor data

# Efficiency calculation with conditional modifiers
efficiency_logs = []
temperature_stable = True
for temp in sensor_readings:
    if abs(temp - base_temperature) > 50:
        temperature_stable = False
    status = 'STABLE' if temperature_stable else 'FLUCTUATING'
    efficiency_logs.append(status)

# Determine efficiency factor based on stability and resistance
efficiency_factor = resistance_factor
if 'FLUCTUATING' not in efficiency_logs:
    efficiency_factor *= 1.15
else:
    efficiency_factor *= 0.95

# Additional distractor: simulate redundant state tracking using itertools
event_counter = 0
for _ in itertools.cycle([1]):
    event_counter += 1
    if event_counter == 3:
        break

# Critical assignment point
thermal_capacity = base_capacity * efficiency_factor

# Final output
print(f"Result: {thermal_capacity}")