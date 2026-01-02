def analyze_temperatures(temp_readings):
    avg_temp = sum(temp_readings) / len(temp_readings)
    above_avg_count = 0
    temp_anomalies = []
    for i, t in enumerate(temp_readings):
        if t > avg_temp:
            above_avg_count += 1
            temp_anomalies.append((i, t - avg_temp))
    return avg_temp, above_avg_count, temp_anomalies


def transform_coordinates(coords_list):
    transformed = []
    offset_x, offset_y = 10, -5
    scaling_factor = 1.5
    for x, y in coords_list:
        new_x = (x + offset_x) * scaling_factor
        new_y = (y + offset_y) * scaling_factor
        transformed.append((new_x, new_y))
    return transformed


def calculate_final_score(data_points):
    base_values = [d['value'] for d in data_points]
    weights = [d['weight'] for d in data_points]
    weighted_sum = sum([v * w for v, w in zip(base_values, weights)])
    total_weight = sum(weights)
    
    # Irrelevant transformation (distractor)
    dummy_coords = [(1, 2), (3, 4), (5, 6)]
    transformed_dummy = transform_coordinates(dummy_coords)
    
    adjustment_factor = 0.9
    if total_weight > 10:
        adjustment_factor = 1.1
    
    preliminary_score = weighted_sum / total_weight if total_weight != 0 else 0
    
    # Secondary adjustment based on count (semi-relevant)
    count_bonus = len(data_points) * 0.05
    adjusted_score = preliminary_score * adjustment_factor + count_bonus
    
    # Additional noise variables
    outlier_flags = [abs(d['value']) > 50 for d in data_points]
    flagged_count = sum(outlier_flags)
    
    # Final irrelevant string processing (distractor)
    status_labels = ['valid', 'invalid', 'pending']
    labeled_data = list(zip(data_points, status_labels * (len(data_points)//3 + 1)))
    label_summary = ''.join([lbl for _, lbl in labeled_data[:len(data_points)]])
    
    final_score = int(round(adjusted_score * 10)) / 10.0  # Rounded to one decimal
    return final_score

# Main execution
raw_temps = [23, 18, 35, 27, 21, 40, 31]
avg_t, count_high, anomalies = analyze_temperatures(raw_temps)

# Prepare mixed data structure
coordinates = [(2, 3), (4, 1), (6, 5)]
transformed_coords = transform_coordinates(coordinates)

processed_data = [
    {'value': avg_t, 'weight': 0.3},
    {'value': count_high * 2.5, 'weight': 0.4},
    {'value': len(anomalies) * 10, 'weight': 0.3}
]

# Introduce dead code path (distractor)
if False:
    backup_weights = [0.2, 0.5, 0.3]
    processed_data = [{'value': v['value'], 'weight': w} for v, w in zip(processed_data, backup_weights)]

final_score = calculate_final_score(processed_data)
print(f"Target result: {final_score}")