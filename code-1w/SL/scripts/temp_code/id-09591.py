def analyze_temperatures(temp_list):
    avg_temp = sum(temp_list) / len(temp_list)
    above_avg_count = 0
    temp_anomalies = []
    for i, t in enumerate(temp_list):
        if t > avg_temp:
            above_avg_count += 1
            temp_anomalies.append((i, t - avg_temp))
    return avg_temp, above_avg_count, temp_anomalies


def transform_coordinates(coord_pairs):
    transformed = []
    magnitude_sum = 0.0
    for x, y in coord_pairs:
        mag = (x**2 + y**2) ** 0.5
        magnitude_sum += mag
        transformed.append((mag, x + y))
    normalized = [(m/magnitude_sum, s) for m, s in transformed]
    return normalized


def calculate_final_score(data_map):
    base_score = 0
    bonus = 0
    penalty = 0
    
    # Extract temperature insights
    temps = data_map['temperatures']
    coord_pairs = data_map['coordinates']
    
    _, count_above, anomalies = analyze_temperatures(temps)
    base_score += count_above * 10
    
    # Process coordinates
    norm_coords = transform_coordinates(coord_pairs)
    for magnitude, _ in norm_coords:
        if magnitude > 0.5:
            bonus += 5
    
    # Simulate sensor reliability adjustments (distractor logic)
    sensor_flags = [True, False, True, True]
    reliability_mask = [not flag for flag in sensor_flags]  # Unused
    debug_checksum = 0
    for i, flag in enumerate(sensor_flags):
        debug_checksum ^= (i + 1) * int(flag)
    
    # Destructuring with enumerate and zip (required features)
    indices = list(range(len(temps)))
    temp_with_index = list(zip(indices, temps))
    cumulative_shift = 0
    for idx, (i, temp) in enumerate(temp_with_index):
        if idx % 2 == 0:
            cumulative_shift += temp % 7
    
    # Final scoring logic
    final_multiplier = 1.5 if len(anomalies) > 2 else 1.0
    final_score = (base_score + bonus - penalty) * final_multiplier
    
    # Irrelevant state tracking (distractor)
    history_log = []
    for step in range(3):
        history_log.append(f'Step {step}: Active')
    
    return int(final_score)

# Main execution
raw_temps = [23, 18, 31, 27, 29, 16]
data_inputs = {
    'temperatures': raw_temps,
    'coordinates': [(3, 4), (1, 1), (5, 12), (0, 2)]
}

processed_data = data_inputs
final_score = calculate_final_score(processed_data)
print(f'Result: {final_score}')