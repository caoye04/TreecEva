from collections import defaultdict, Counter

# Sensor data simulation with noise filtering
temperature_readings = [22, 23, 21, 24, 19, 25, 22, 20, 23, 24]
humidity_readings = [45, 47, 46, 50, 44, 52, 48, 43, 49, 51]
pressure_readings = [1013, 1015, 1012, 1016, 1010, 1017, 1014, 1009, 1015, 1013]

total_samples = len(temperature_readings)
sample_weights = [1.0 if i % 2 == 0 else 0.9 for i in range(total_samples)]

# Irrelevant transformation: pressure z-scores (not used later)
mean_pressure = sum(pressure_readings) / total_samples
std_pressure = (sum((p - mean_pressure) ** 2 for p in pressure_readings) / total_samples) ** 0.5
z_scores = [(p - mean_pressure) / std_pressure for p in pressure_readings]

# Data alignment using zip and enumerate
data_stream = list(enumerate(zip(temperature_readings, humidity_readings)))

# Track valid readings per category using defaultdict
validity_map = defaultdict(int)
efficiency_accumulator = 0.0

for idx, (temp, hum) in data_stream:
    # Intermediate logic with conditional expressions
    temp_category = 'optimal' if 21 <= temp <= 24 else 'suboptimal'
    hum_category = 'optimal' if 45 <= hum <= 50 else 'suboptimal'
    
    # Update validity map (only some categories contribute)
    if temp_category == 'optimal' and hum_category == 'optimal':
        validity_map['stable'] += 1
        efficiency_accumulator += temp * sample_weights[idx]
    elif temp_category == 'suboptimal':
        validity_map['unstable'] += 1
        efficiency_accumulator -= 1.5

# Secondary counter for humidity patterns
humidity_counter = Counter(hum // 5 * 5 for hum in humidity_readings)  # Bucket by 5
mode_bucket = humidity_counter.most_common(1)[0][0]

# Case conversion distraction (unused)
distraction_label = "TEMP_STABLE".lower().replace('_', '-')

# Efficiency baseline calculation
raw_efficiency = efficiency_accumulator / total_samples

# Correction logic based on mode bucket
if mode_bucket >= 45:
    correction_offset = 1.1
else:
    correction_offset = 0.95

# Temperature factor derived from frequency of optimal temps
optimal_temp_count = sum(1 for t in temperature_readings if 21 <= t <= 24)
temperature_factor = optimal_temp_count / total_samples

# Final adjustment step — critical execution point
efficiency_score = raw_efficiency * 10
final_adjustment = temperature_factor * correction_offset
efficiency_score += final_adjustment * 5

Result: efficiency_score