def analyze_conditions(data_points):
    cumulative_index = 0
    temp_offsets = [d[0] * 0.5 + d[1] for d in data_points]
    adjustment_factor = 0
    
    # Misleading intermediate computation (not used later)
    fake_aggregate = sum([abs(t - 25) for t in temp_offsets if t > 10])
    
    for i, val in enumerate(temp_offsets):
        if i % 2 == 0:
            adjustment_factor += val * 0.1
        else:
            adjustment_factor -= val * 0.05
    
    return adjustment_factor


def calculate_adjustment(temps, humids):
    base_value = 0
    decay_rate = 0.9
    history_log = []  # Unused tracking variable (distractor)
    
    # Real computation begins
    temp_sum = sum(temps)
    humid_values = list(humids.values())
    avg_humidity = sum(humid_values) / len(humid_values)
    
    for idx, (t, h) in enumerate(zip(temps, humid_values)):
        weighted_contribution = (t * 1.2) - (h * 0.8)
        if weighted_contribution > 0:
            base_value += weighted_contribution * (decay_rate ** idx)
    
    # Distractor block: irrelevant transformation
    outlier_check = [t for t in temps if t < 0]
    correction_offset = len(outlier_check) * 100  # Never applied
    
    # Another misleading calculation
    phantom_score = 0
    for h in humids:
        phantom_score += len(h) * humids[h]
    
    return int(base_value)

# Main execution context
sensor_ids = ['s1', 's2', 's3']
temperature_readings = [23.5, 26.0, 24.8]
humidity_map = {k: v * 1.5 for k, v in zip(sensor_ids, [45, 50, 47])}

# Secondary distractor variables
normalization_constant = 1.0 / (sum(temperature_readings) / len(temperature_readings))
scaled_data = [(t * normalization_constant, h) for t, h in zip(temperature_readings, humidity_map.values())]

intermediate_diagnostic = analyze_conditions(scaled_data)

# Key statement
final_score = calculate_adjustment(temperature_readings, humidity_map)

print(f"Result: {final_score}")