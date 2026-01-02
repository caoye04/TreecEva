def analyze_component(x, threshold=5):
    return x > threshold

# Simulated sensor readings from a distributed system
temperature_readings = [23, 19, 25, 30, 18]
humidity_readings = [45, 60, 53, 70, 40]
pressure_readings = [1013, 1008, 1015, 1020, 1005]

# Misleading aggregation (not used in final result)
avg_temp = sum(temperature_readings) / len(temperature_readings)
temp_flags = [analyze_component(t, 20) for t in temperature_readings]

# Real processing begins here
sensor_z_scores = []
for i in range(len(temperature_readings)):
    z = (temperature_readings[i] - 20) * 2 + (humidity_readings[i] // 10)
    sensor_z_scores.append(z)

# Auxiliary dictionary for state tracking (some entries are distractions)
sensor_state = {
    'active': True,
    'calibration_offset': 0.5,
    'last_updated': '2023-11-05',
    'z_scores': sensor_z_scores
}

# Conditional logic with red herring branches
if sensor_state['active']:
    adjusted_scores = [score + 1 for score in sensor_z_scores if score % 2 == 0]
else:
    adjusted_scores = [score - 1 for score in sensor_z_scores]

# Dead code path (never executed due to constant condition)
DEBUG_MODE = False
if DEBUG_MODE:
    print('Debug: Processing raw data')
    for idx, val in enumerate(adjusted_scores):
        adjusted_scores[idx] = val * 2

# Core calculation using lambda and dictionary operation
baseline = list(map(lambda x: x * 0.8, adjusted_scores))
offset_map = {i: baseline[i] + 3 for i in range(len(baseline))}

# Final performance model with modular arithmetic and filtering
benchmark_data = []
for i in range(len(offset_map)):
    value = offset_map[i]
    if i % 2 == 0:
        benchmark_data.append((value * 1.1) % 17)
    else:
        benchmark_data.append((value * 0.9) % 13)

# Secondary irrelevant computation (distractor)
total_pressure = sum(pressure_readings)
pressure_avg_deviation = total_pressure / len(pressure_readings) - 1010

# Main function that computes the final answer
def calculate_performance(data):
    raw_total = sum(data)
    penalty = len([x for x in data if x < 5]) * 1.5
    bonus = len([x for x in data if x > 10]) * 0.7
    return int(raw_total - penalty + bonus)

final_score = calculate_performance(benchmark_data)
print(f"Target result: {final_score}")