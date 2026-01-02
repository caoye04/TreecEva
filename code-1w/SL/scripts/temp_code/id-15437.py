def analyze_temperatures(temp_readings):
    adjusted = []
    outlier_count = 0
    base_reference = sum(temp_readings) / len(temp_readings)
    
    for i, temp in enumerate(temp_readings):
        deviation = abs(temp - base_reference)
        if deviation > 15:
            outlier_count += 1
            continue
        adjusted.append(temp * 0.9 + base_reference * 0.1)
    
    if outlier_count > 2:
        adjustment_factor = 0.95
    else:
        adjustment_factor = 1.05

    # Irrelevant string processing (distractor)
    status_messages = ['Normal', 'Elevated', 'Critical']
    log_entries = []
    for idx, val in enumerate(adjusted):
        if val < 0:
            log_entries.append(f"{val:.1f}°C: {status_messages[0]}")
        elif val < 20:
            log_entries.append(f"{val:.1f}°C: {status_messages[1]}")
        else:
            log_entries.append(f"{val:.1f}°C: {status_messages[2]}")
    
    # Unused helper computation (distractor)
    cumulative_xor = 0
    for val in temp_readings:
        cumulative_xor ^= int(val) % 256
    
    return adjusted, adjustment_factor


def calculate_stability_index(data):
    if len(data) == 0:
        return 0
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    return (1 / (1 + variance)) * 100


def calculate_final_score(data_list):
    raw_sum = sum(data_list)
    count_above_mean = 0
    mean_val = sum(data_list) / len(data_list)
    for val in data_list:
        if val > mean_val:
            count_above_mean += 1
    
    # Bitwise manipulation as secondary feature (semi-relevant)
    magic_seed = len(data_list) ^ 255
    perturbation = (magic_seed & 170) >> 4  # Use only some bits
    
    # Final score influenced by multiple factors
    stability = calculate_stability_index(data_list)
    base_score = raw_sum + stability
    final_score = base_score * (1 + (perturbation * 0.01))
    
    # Dead code path (distractor)
    if False:
        backup_calc = [x for x in data_list if x % 2 == 0]
        final_score -= sum(backup_calc)

    return int(final_score)

# Main execution
sensor_inputs = [23.5, 19.1, 27.3, -5.2, 41.8, 22.0, 18.9, 20.1, 25.5, 24.3]
processed_data, scale_factor = analyze_temperatures(sensor_inputs)

for i, val in enumerate(processed_data):
    processed_data[i] = val * scale_factor

final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")