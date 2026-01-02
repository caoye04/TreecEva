import math

# Simulated sensor readings from environmental monitoring stations
temperature_readings = [23.4, 25.1, 22.8, 26.5, 24.3, 27.0, 23.9, 25.6]
humidity_readings = [56, 61, 58, 63, 55, 60, 57, 62]
co2_levels = [410, 425, 405, 430, 415, 420, 408, 435]

# Irrelevant transformation: normalize humidity to arbitrary scale (distractor)
normalized_humidity = [round((h - 50) / 10, 2) for h in humidity_readings]

# Misleading statistical summary (dead path)
mean_temp = sum(temperature_readings) / len(temperature_readings)
adjusted_temps = [t - mean_temp + 25 for t in temperature_readings]
variance = sum((t - mean_temp) ** 2 for t in temperature_readings) / len(temperature_readings)

# Bitmask simulation for faulty sensors (XOR-based error detection - partially relevant)
fault_mask = 0b10101010
sensor_status_bits = 0b11110000
error_flags = fault_mask ^ sensor_status_bits  # XOR to detect inconsistencies

# Filter high-risk CO2 levels (above 420 ppm)
elevated_co2_indices = {i for i, co2 in enumerate(co2_levels) if co2 > 420}

# Compute temperature volatility using rolling differences (distraction)
volatility = []
for i in range(1, len(temperature_readings)):
    change = abs(temperature_readings[i] - temperature_readings[i-1])
    volatility.append(round(change, 2))

# Identify stable temperature zones (within ±1.0°C of moving average)
stable_zones = set()
moving_avg_window = []
for i, temp in enumerate(temperature_readings):
    moving_avg_window.append(temp)
    if len(moving_avg_window) > 3:
        moving_avg_window.pop(0)
    if len(moving_avg_window) == 3:
        window_avg = sum(moving_avg_window) / 3
        if abs(temp - window_avg) <= 1.0:
            stable_zones.add(i)

# Humidity correlation filter: find indices where humidity > 60 and rising
high_humidity_rising = set()
for i in range(1, len(humidity_readings)):
    if humidity_readings[i] > 60 and humidity_readings[i] > humidity_readings[i-1]:
        high_humidity_rising.add(i)

# Core logic: find optimal monitoring set using set intersection
valid_candidates = set(range(len(temperature_readings)))

# Apply filters: exclude elevated CO2, include stable zones, and match humidity trends
candidate_set = valid_candidates - elevated_co2_indices
candidate_set = candidate_set & stable_zones
candidate_set = candidate_set & high_humidity_rising

# Decoy calculation: entropy of CO2 distribution (unused)
co2_probs = [co2 / sum(co2_levels) for co2 in co2_levels]
entropy = -sum(p * math.log(p) for p in co2_probs if p > 0)

# Secondary decoy: simulate pressure drift (irrelevant)
base_pressure = 1013.25
pressure_drift = [base_pressure * (1 + 0.001 * i) for i in range(len(temperature_readings))]

def calculate_shadow_index(readings):
    # Unused recursive function (red herring)
    if len(readings) <= 1:
        return 0
    mid = len(readings) // 2
    return readings[mid] + calculate_shadow_index(readings[:mid])

# Determine optimal sensor subset based on consensus across metrics
optimal_set = set()
for idx in candidate_set:
    # Additional constraint: must have moderate temperature (23-25.5°C)
    if 23 <= temperature_readings[idx] <= 25.5:
        # And not flagged in error bitmask (bit check)
        if not (error_flags & (1 << idx)):
            optimal_set.add(idx)

# Key execution point
filtration_score = len(optimal_set)

# Final output
print(f"Result: {filtration_score}")