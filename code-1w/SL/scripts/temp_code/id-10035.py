import math

# Simulated sensor data from agricultural plots
temperature_readings = [23.4, 24.1, 22.9, 25.0, 23.8, 24.4, 26.1, 23.5, 22.7, 25.6]
humidity_readings = [61, 58, 64, 55, 62, 59, 57, 63, 60, 56]
soil_ph_levels = [6.2, 6.4, 6.1, 6.5, 6.3, 6.0, 6.6, 5.9, 6.7, 6.2]

# Irrelevant calibration constants for unused equipment
calibration_a = 0.87
reference_offset_z = 1.02
dummy_threshold = 42.0

# Misleading intermediate calculations (unused)
effective_wavelength = [round(math.sin(x / 10), 3) for x in range(10)]
attenuation_factor = sum([x * 0.01 for x in range(len(effective_wavelength))])

# Data alignment and filtering
aligned_indices = [i for i in range(min(len(temperature_readings), len(humidity_readings))) if temperature_readings[i] > 23.0]
filtered_temps = [temperature_readings[i] for i in aligned_indices]
filtered_humid = [humidity_readings[i] for i in aligned_indices]

# Distractor: unused transformation matrix
transform_matrix = [[i + j * 0.1 for j in range(3)] for i in range(3)]
matrix_trace = sum(transform_matrix[i][i] for i in range(3))

# Real processing begins: normalize relevant data
def normalize(data):
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

norm_temps = normalize(filtered_temps)
norm_humid = normalize(filtered_humid)

# Combine into composite score per plot
composite_scores = []
for i in range(len(norm_temps)):
    score = (norm_temps[i] * 0.6) + (norm_humid[i] * 0.4)
    composite_scores.append(round(score, 3))

# Slice only the top-performing 60% for yield modeling
sorted_scores = sorted(composite_scores, reverse=True)
top_performers = sorted_scores[:int(0.6 * len(sorted_scores))]

# Secondary filter based on soil pH (only indices 2, 4, 5, 7 were sampled)
valid_soil_indices = [2, 4, 5, 7]
mean_soil_ph = sum(soil_ph_levels[i] for i in valid_soil_indices) / len(valid_soil_indices)
ph_correction = abs(6.5 - mean_soil_ph) * 0.8

# Faux machine learning model (distraction)
predicted_yields = [score * (100 + ph_correction) + 5 for score in top_performers]
model_bias = sum(predicted_yields) / len(predicted_yields) - 50

# Actual yield calculation logic (obscured by distractions)
baseline_yield = 85.0
decline_rate = 0.05
adjusted_scores = [score * (1 - decline_rate) for score in top_performers]

# Final processing function
def calculate_optimal_yield(scores):
    if not scores:
        return 0.0
    raw_yield = baseline_yield * sum(scores) / len(scores)
    # Apply diminishing returns using logarithmic scaling
    scaling_factor = math.log(1 + len(scores))
    return round(raw_yield * scaling_factor, 3)

# Critical execution point
processed_data = adjusted_scores
final_yield = calculate_optimal_yield(processed_data)

# Output result as required
print(f"Result: {final_yield}")