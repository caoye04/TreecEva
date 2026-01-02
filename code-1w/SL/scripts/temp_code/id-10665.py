def collect_sensor_data():
    readings = [127, 255, 193, 84, 205]
    processed = []
    offset_correction = 3
    for val in readings:
        corrected = (val + offset_correction) % 256
        if corrected > 100:
            processed.append(corrected * 0.9)
        else:
            processed.append(corrected * 1.1)
    return set(processed)


def calculate_efficiency(logs):
    base_efficiency = 0.78
    adjustment_factor = 0.03
    boost_count = 0
    for entry in logs:
        if entry > 150:
            boost_count += 1
    if boost_count >= 3:
        base_efficiency += adjustment_factor * 2
    elif boost_count == 2:
        base_efficiency += adjustment_factor
    temp_debug = base_efficiency * 100  # irrelevant tracking
    return base_efficiency


def filter_anomalies(raw_set):
    anomalies = {x for x in raw_set if x < 90 or x > 220}
    clean_set = raw_set - anomalies
    score_weights = [0.1, 0.2, 0.3]  # unused distraction
    return sorted(clean_set)


def harvest_results(data_list, rates):
    total = 0
    multiplier = rates
    for i, item in enumerate(data_list):
        if i % 2 == 0:
            total += item * multiplier
        else:
            total += item * (multiplier * 0.5)
    bonus_check = total > 300  # red herring
    if bonus_check:
        total *= 1.05  # not actually triggered
    return int(total)

# Main execution flow
sensor_logs = [110, 200, 180, 95, 210]
sensor_data = collect_sensor_data()
efficiency = calculate_efficiency(sensor_logs)
cleaned_data = filter_anomalies(sensor_data)
final_yield = harvest_results(cleaned_data, efficiency)
print(f"Result: {final_yield}")