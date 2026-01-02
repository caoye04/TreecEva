from collections import defaultdict

# Simulate sensor data with timestamps and readings
data = [
    (1, 'temp', 23.5), (2, 'pressure', 1013.2), (3, 'temp', 24.1),
    (4, 'humidity', 45), (5, 'temp', 22.8), (6, 'pressure', 1012.7),
    (7, 'humidity', 47), (8, 'temp', 25.3), (9, 'pressure', 1014.1)
]

# Misleading aggregation - not used in final result
dummy_agg = defaultdict(list)
for timestamp, sensor_type, reading in data:
    dummy_agg[sensor_type].append(reading)

# Secondary processing: extract temperature readings above threshold
high_temp_readings = [r for t, s, r in data if s == 'temp' and r > 24.0]

# Irrelevant transformation chain
adjusted_values = [round(x * 1.015, 2) for x in high_temp_readings]  # minor adjustment
intermediate_sum = sum(adjusted_values)  # dead-end computation

# Core logic: count valid temp-pressure cycles
valid_cycles = 0
last_pressure = None
for _, sensor_type, reading in data:
    if sensor_type == 'pressure':
        last_pressure = reading
    elif sensor_type == 'temp' and last_pressure is not None:
        if reading > 23.0 and (last_pressure > 1013.0):
            valid_cycles += 1

# Conditional scoring based on cycle count and humidity presence
cycle_bonus = valid_cycles * 10 if valid_cycles >= 2 else 0

# Distractor: complex unused formula involving humidity
humidity_vals = [r for _, s, r in data if s == 'humidity']
humidity_index = sum(h * 0.7 for h in humidity_vals) / len(humidity_vals) if humidity_vals else 0

# Final score calculation depends only on valid_cycles and a fixed offset
def calculate_final_score(raw_data):
    base_score = 50
    # Recompute valid_cycles locally (redundant but consistent)
    local_cycles = 0
    pressure_snapshot = None
    for ts, st, rd in raw_data:
        if st == 'pressure':
            pressure_snapshot = rd
        elif st == 'temp' and pressure_snapshot:
            if rd > 23.0 and pressure_snapshot > 1013.0:
                local_cycles += 1
    cycle_points = local_cycles * 15
    return base_score + cycle_points

final_score = calculate_final_score(data)
print(f"Target result: {final_score}")