from itertools import combinations

# Simulate thermal regulation system diagnostics
temperature_readings = [23, 25, 27, 30, 33, 35]
base_threshold = 26
fluctuation_margin = 3
high_temp_events = 0
energy_buffer = 0
redundant_sum = 0

# Irrelevant statistical buffer calculations (distractor)
for temp in temperature_readings:
    if temp > base_threshold:
        high_temp_events += 1
    if temp < base_threshold:
        energy_buffer += base_threshold - temp

# Generate all 2-second fluctuation pairs (semi-relevant but not used directly)
potential_fluctuations = list(combinations(temperature_readings, 2))
valid_fluctuations = 0
for pair in potential_fluctuations:
    if abs(pair[0] - pair[1]) >= fluctuation_margin:
        valid_fluctuations += 1

# Secondary system health check with dead computation path (distractor)
system_health_flags = set()
for i, temp in enumerate(temperature_readings):
    if temp >= 30:
        system_health_flags.add(f"overheat_warning_{i}")
    elif temp <= 24:
        system_health_flags.add(f"low_temp_alert_{i}")

redundant_sum = sum(len(flag) for flag in system_health_flags)  # unused

# Core calculation chain
baseline_input = len(temperature_readings)
peak_load = high_temp_events * 17
auxiliary_offset = len(system_health_flags) or 1

# Efficiency degrades logarithmically with event frequency
if high_temp_events > 0:
    efficiency = int(100 / (1 + high_temp_events))
else:
    efficiency = 100

net_energy = baseline_input * peak_load // auxiliary_offset

# Key assignment point
thermal_capacity = net_energy // efficiency if efficiency else 0

Result: thermal_capacity