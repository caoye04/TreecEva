from collections import defaultdict, Counter

# Simulated sensor data from agricultural plots
temperature_readings = [23.4, 24.1, 22.7, 25.3, 23.9, 24.4, 23.0, 22.1]
humidity_readings = [61, 65, 63, 59, 67, 62, 60, 64]
light_exposure = [8.2, 8.5, 8.0, 8.7, 8.3, 8.6, 8.1, 8.4]  # hours per day

# Irrelevant calibration offset (red herring)
calibration_factor = 1.02
offset_matrix = [[i * j for j in range(3)] for i in range(3)]

# Distractor: unused function simulating soil pH adjustment
def adjust_ph_level(soil_samples, agent_concentration):
    return [max(0.0, min(14.0, ph + agent_concentration)) for ph in soil_samples]

# Misleading intermediate transformation
transformed_light = list(map(lambda x: round(x ** 0.5 * 10), light_exposure))

# Sensor fusion with weighting (relevant part embedded)
def normalize_sensor(seq, min_val, max_val):
    return [(x - min_val) / (max_val - min_val) for x in seq]

temp_norm = normalize_sensor(temperature_readings, 20.0, 30.0)
humid_norm = normalize_sensor(humidity_readings, 40.0, 80.0)
light_norm = normalize_sensor(light_exposure, 6.0, 12.0)

# Combine normalized inputs using zip and enumerate (key python idiom)
sensor_fused = []
for idx, (t, h, l) in enumerate(zip(temp_norm, humid_norm, light_norm)):
    weight = 0.4 if idx % 2 == 0 else 0.6
    fused = t * 0.4 + h * 0.3 + l * 0.3
    sensor_fused.append(round(fused * weight, 3))

# Dead code path: simulation of wind impact (never used)
def compute_wind_effect(wind_speeds, direction_angles):
    import math
    return [w * math.cos(math.radians(a)) for w, a in zip(wind_speeds, direction_angles)]

wind_bearing = [120, 135, 110, 150, 130, 145, 125, 140]
apparent_wind_impact = compute_wind_effect([4.2, 5.1, 3.8, 6.0, 4.5, 5.3, 4.0, 5.8], wind_bearing)

# Construct plot-level data structure
plot_ids = ['P01', 'P02', 'P03', 'P04', 'P05', 'P06', 'P07', 'P08']
aggregated_data = defaultdict(dict)
for i, pid in enumerate(plot_ids):
    aggregated_data[pid]['fused_index'] = sensor_fused[i]
    aggregated_data[pid]['base_yield_potential'] = int((sensor_fused[i] + 0.1) * 1500)
    aggregated_data[pid]['maintenance_flag'] = (i % 3 == 0)

# Decoy statistics using Counter (distractor)
maintenance_counts = Counter(aggregated_data[pid]['maintenance_flag'] for pid in plot_ids)

# Threshold logic with conditional expressions and bitwise masking
baseline_threshold = 0.65
adjustment_flags = [1 if t > 0.6 else 0 for t in temp_norm]
humidity_flags = [1 if h > 0.7 else 0 for h in humid_norm]

# Bitwise combination of environmental conditions (mixed relevance)
combined_flags = [a ^ b | (i & 1) for i, (a, b) in enumerate(zip(adjustment_flags, humidity_flags))]

threshold_map = {}
for idx, pid in enumerate(plot_ids):
    base_thresh = baseline_threshold
    if combined_flags[idx]:
        base_thresh += 0.05
    if idx in [2, 5]:
        base_thresh -= 0.03
    threshold_map[pid] = round(base_thresh, 3)

# Unused debug trace (irrelevant)
critical_plots = [pid for pid, t in threshold_map.items() if t < 0.62]

# Core calculation function with nested logic
def calculate_stable_yield(data_dict, thresholds):
    cumulative_yield = 0
    yield_corrections = []
    
    for pid, values in data_dict.items():
        index = values['fused_index']
        potential = values['base_yield_potential']
        required = thresholds[pid]
        
        # Multi-step eligibility check with short-circuit logic
        if index >= required and not values.get('maintenance_flag', False):
            adjusted = potential * (index / required)
            if adjusted > 1200:
                adjusted = 1200 + (adjusted - 1200) * 0.5  # saturation curve
            yield_corrections.append(adjusted * 0.95)
        elif values.get('maintenance_flag'):
            # Recovery path: uses lambda in unexpected way
            recovery_fn = lambda x: x * 0.7 if x < 1000 else x * 0.6
            yield_corrections.append(recovery_fn(potential))
        else:
            yield_corrections.append(potential * 0.3)
    
    # Final aggregation with outlier suppression
    sorted_yields = sorted(yield_corrections)
    trim_count = len(sorted_yields) // 4
    trimmed = sorted_yields[trim_count:-trim_count] if trim_count > 0 else sorted_yields
    
    # Apply weighted average using enumerate
    total_weighted = 0.0
    total_weight = 0.0
    for i, val in enumerate(trimmed):
        weight = 1.0 + (i * 0.1)  # increasing weight for higher yields
        total_weighted += val * weight
        total_weight += weight
    
    final = total_weighted / total_weight if total_weight > 0 else 0
    return round(final, 4)

# Execution point of interest
final_yield = calculate_stable_yield(aggregated_data, threshold_map)

# Output result as required
print(f"Target result: {final_yield}")