import math

# Simulated sensor readings with noise and calibration data
temperature_readings = [23.5, 19.0, 25.3, 18.7, 30.2, 27.8, 24.1, 20.5, 31.0, 26.4]
humidity_readings = [45, 48, 53, 50, 37, 41, 46, 52, 39, 44]
pressure_readings = [1013, 1015, 1012, 1018, 1009, 1014, 1016, 1011, 1020, 1008]

# Calibration offset (irrelevant to final computation)
calibration_matrix = [[0.1, -0.2], [0.3, 0.15], [-0.1, 0.05]]
adjusted_temp = [t + sum(calibration_matrix[i % 3]) for i, t in enumerate(temperature_readings)]

# Noise filter threshold (distractor)
noise_floor = 18.5
spike_threshold = 30.0

# Derived metrics (some irrelevant)
avg_temp = sum(temperature_readings) / len(temperature_readings)
temp_variance = sum((t - avg_temp) ** 2 for t in temperature_readings) / len(temperature_readings)
humidity_ratio = [h / 100 for h in humidity_readings]

def apply_offset(data, factor):
    # Unused function - red herring
    return [x * factor + 2 for x in data]

def compute_dew_point(temp, humidity):
    # Complex but unused calculation - dead path
    a, b = 17.27, 237.7
    alpha = ((a * temp) / (b + temp)) + math.log(humidity / 100)
    return (b * alpha) / (a - alpha)

dew_points = [compute_dew_point(t, h) for t, h in zip(temperature_readings, humidity_readings)]

# Data windowing (slicing operation - relevant)
recent_temps = temperature_readings[-7:]

# Outlier detection and filtering logic
extreme_indices = []
for i, t in enumerate(recent_temps):
    if t < noise_floor or t > spike_threshold:
        extreme_indices.append(i)

# Masked filtering with list comprehension and slicing
masked_temps = [
    recent_temps[i] for i in range(len(recent_temps))
    if i not in extreme_indices
]

# Secondary filter based on pressure correlation (partially misleading)
valid_pressures = [p for p in pressure_readings if 1010 <= p <= 1017]
pressure_influence = sum(valid_pressures) / len(valid_pressures) if valid_pressures else 1013

# Control flow with nested conditionals (3 levels deep)
final_candidates = []
for temp in masked_temps:
    if temp >= avg_temp:
        adjusted = temp * (pressure_influence / 1013)
        if 20 <= adjusted <= 28:
            category = 'optimal'
            if math.sin(math.pi * adjusted / 30) > 0.5:
                category = 'enhanced'
            final_candidates.append((adjusted, category))

# Extract values and filter by category
refined_values = [val for val, cat in final_candidates if cat == 'enhanced']

# Key assignment point
filtered_data = [round(x, 1) for x in refined_values]

# Dead code path - never executed
if len(refined_values) > 10:
    filtered_data.append(999.9)

# Critical statement
filtered_sum = sum(filtered_data)

# Irrelevant transformation chain
decoys = [filtered_sum + i for i in range(3)]
decoys = [d * 0.9 for d in decoys]

# Output result
print(f"Result: {filtered_sum}")