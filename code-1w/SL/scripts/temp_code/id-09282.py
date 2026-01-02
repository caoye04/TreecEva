def filter_anomalies(data, limit):
    """Remove values exceeding threshold limit."""
    anomalies_detected = 0
    filtered = []
    temp_sum = 0.0
    for val in data:
        if abs(val) > limit:
            anomalies_detected += 1
        else:
            filtered.append(val)
            temp_sum += val
    debug_mean = temp_sum / len(filtered) if filtered else 0
    return filtered


def process_readings(valid_data, base):
    """Apply calibration and compute deviation score."""
    calibrated = [x * 0.98 + 1.5 for x in valid_data]
    deviation_total = 0
    normalized_str = ''
    for val in calibrated:
        deviation_total += abs(val - base)
    
    # Irrelevant string processing (distractor)
    status = 'CALIBRATED'
    status_lower = status.lower()
    char_count = len(status_lower)
    vowel_count = sum(1 for c in status_lower if c in 'aeiou')
    normalized_str += status_lower.replace('a', 'X').swapcase()

    # More distraction: unused statistical computation
    squared_deviations = [abs(x - base)**2 for x in calibrated]
    variance_proxy = sum(squared_deviations) / len(squared_deviations) if squared_deviations else 0

    result = int(deviation_total * 100) % 97
    return result

# Main execution
sensor_data = [3.2, -1.4, 5.6, 1000, -2.3, 4.1, -5.5, 0.8, 1000, 6.7]
threshold = 10
baseline = 2.0

# Extraneous variable assignments (distractors)
duplicate_data = sensor_data.copy()
temp_log = []
data_size = len(duplicate_data)
sorted_copy = sorted([abs(x) for x in sensor_data])
median_approx = sorted_copy[len(sorted_copy)//2]

interim_list = [x for x in sensor_data if x != 1000]
sum_interim = sum(interim_list)

final_diagnostic = process_readings(filter_anomalies(sensor_data, threshold), baseline)
print(f"Result: {final_diagnostic}")