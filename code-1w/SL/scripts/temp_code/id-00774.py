import itertools

# Simulated sensor data from a distributed environmental monitoring system
temperature_readings = [23.5, 24.1, 22.8, 25.0, 19.3, 24.7, 23.9, 26.2, 21.4, 25.8]
humidity_readings = [45, 47, 50, 43, 60, 46, 48, 42, 55, 44]
pressure_readings = [1013, 1015, 1012, 1016, 1018, 1014, 1011, 1017, 1019, 1010]

# Irrelevant transformation: circular shift (distraction)
def shift_list(lst, n):
    return lst[n:] + lst[:n]

circular_shifted = shift_list(temperature_readings, 3)  # unused later

# Misleading statistical decoy: computes but does not use extreme values
max_temp = max(temperature_readings)
min_humidity = min(humidity_readings)
avg_pressure = sum(pressure_readings) / len(pressure_readings)

# Data pairing with zip (required feature)
sensor_data = list(zip(temperature_readings, humidity_readings))

diagnostic_flags = []
outlier_threshold = 25.5
outlier_count = 0
running_sum = 0

# Primary processing loop with enumerate (required feature)
for i, (temp, hum) in enumerate(sensor_data):
    if temp > outlier_threshold:
        outlier_count += 1
        running_sum += temp * 2
    elif hum > 55:
        # High humidity branch – red herring, not part of final calculation
        adjusted_value = (temp + 273.15) * (hum / 100)  # Kelvin conversion distraction
        diagnostic_flags.append(adjusted_value)
    else:
        running_sum += temp + (hum * 0.1)

# Decoy function using itertools – never called
def generate_combinations(data):
    return list(itertools.combinations(data, 2))

# Unused dictionary transformation – distractor
diagnostic_map = {f'sensor_{i}': val for i, val in enumerate(pressure_readings)}
filtered_diagnostics = {k: v for k, v in diagnostic_map.items() if v > 1014}

# Another irrelevant computation: set operations with no impact
temp_set = set(temperature_readings)
pressure_set = set(pressure_readings)
common_values = temp_set & pressure_set  # Always empty, just noise

# Linear search for specific condition (relevant only if found)
flagged_index = -1
for idx in range(len(temperature_readings)):
    if temperature_readings[idx] == 19.3 and humidity_readings[idx] == 60:
        flagged_index = idx

# Core logic hidden among distractions
baseline_offset = 100
aggregate_score = running_sum + baseline_offset

# Key statement embedded in non-trivial context
final_diagnostic = aggregate_score // outlier_count

# Dead code path: conditional that will never trigger (misdirection)
if len(diagnostic_flags) > 100:
    final_diagnostic *= 2

# Output required result
print(f"Result: {final_diagnostic}")