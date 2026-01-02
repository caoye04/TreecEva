from collections import defaultdict, Counter

# Sensor data from thermal array (simulated)
temperature_readings = [23.5, 24.1, 24.1, 25.3, 26.0, 25.3, 24.1, 23.5, 27.2, 26.0]

timestamp_map = {i: ts for i, ts in enumerate(['08:00', '08:15', '08:30', '08:45', '09:00', '09:15', '09:30', '09:45', '10:00', '10:15'])}

# Misleading preprocessing: frequency analysis of temperatures (not directly used later)
temp_frequencies = Counter(temperature_readings)
duplicate_count = sum(count - 1 for count in temp_frequencies.values() if count > 1)

# System configuration parameters (some are red herrings)
config_flags = {"calibration_mode": False, "debug_output": True, "legacy_protocol": False}
base_voltage = 12.4
current_draw = 3.8
power_consumption = base_voltage * current_draw  # Irrelevant to final result

# Real computation begins
stable_temps = [t for t in temperature_readings if 24.0 <= t <= 26.5]
avg_stable_temp = sum(stable_temps) / len(stable_temps) if stable_temps else 0

# Efficiency model based on variation
temp_variance = sum((t - avg_stable_temp) ** 2 for t in stable_temps) / len(stable_temps)
efficiency_factor = max(0.5, 1.0 - (temp_variance / 10.0))  # Stabilized efficiency

# Base capacity derived from sensor count and initial state
sensor_coverage = defaultdict(int)
for i, temp in enumerate(temperature_readings):
    sensor_coverage[i // 2] += temp

active_zones = len([v for v in sensor_coverage.values() if v > 45.0])
base_capacity = active_zones * 1000.0

# Key assignment with distractor context
thermal_capacity = base_capacity * efficiency_factor

# Additional irrelevant logging
device_logs = []
for idx, (temp, time) in enumerate(zip(temperature_readings, timestamp_map.values())):
    status = "HIGH" if temp > 25.0 else "NORMAL"
    device_logs.append(f"[{time}] Sensor{idx}: {temp}°C ({status})")

# Output target result
print(f"Result: {thermal_capacity}")