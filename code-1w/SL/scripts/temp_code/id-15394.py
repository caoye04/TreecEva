from collections import defaultdict, Counter

# Simulate sensor data with timestamps and readings
def generate_sensor_data():
    raw_data = [
        (1001, 'temp', 23.5), (1002, 'pressure', 101.3), (1003, 'temp', 24.1),
        (1004, 'humidity', 45), (1005, 'temp', 22.8), (1006, 'pressure', 100.7),
        (1007, 'temp', 25.3), (1008, 'humidity', 50), (1009, 'temp', 23.9)
    ]
    return raw_data

def analyze_trends(values):
    # Irrelevant helper function – not used in final logic
    if len(values) < 3:
        return 0
    trend = sum(1 for i in range(1, len(values)) if values[i] > values[i-1])
    return trend * 0.5

def filter_critical_entries(data_list, min_val, max_val):
    # Filters entries by numeric threshold – partially relevant
    filtered = []
    temp_count = 0
    for entry in data_list:
        timestamp, sensor_type, value = entry
        if sensor_type == 'temp' and min_val <= value <= max_val:
            filtered.append((timestamp, value))
            temp_count += 1
    # Dead code: temp_count is never used beyond this
    temp_count_snapshot = temp_count  # Distractor variable
    return filtered

def compute_baseline(readings, weight=0.1):
    # Computes a moving average baseline – misleading computation
    avg = sum(readings) / len(readings)
    adjusted = avg * (1 + weight) if avg < 24 else avg * (1 - weight)
    return round(adjusted, 2)

def evaluate_performance(log, thresh):
    # Core logic begins here
    temperature_readings = []
    pressure_readings = []  
    humidity_readings = []

    # Parse and separate sensor types
    for item in log:
        ts, s_type, val = item
        if s_type == 'temp':
            temperature_readings.append(val)
        elif s_type == 'pressure':
            pressure_readings.append(val)
        elif s_type == 'humidity':
            humidity_readings.append(val)

    # Compute summary stats – only mean_temp matters
    mean_temp = sum(temperature_readings) / len(temperature_readings)
    mean_pressure = sum(pressure_readings) / len(pressure_readings)  # Unused
    mean_humidity = sum(humidity_readings) / len(humidity_readings)  # Unused

    # Flag anomalies using threshold
    anomalies = [t for t in temperature_readings if abs(t - mean_temp) > thresh]
    anomaly_count = len(anomalies)

    # Use Counter to count frequency (overkill but adds complexity)
    temp_counter = Counter(temperature_readings)
    mode_temp = temp_counter.most_common(1)[0][1]  # Frequency of most common

    # State tracker for irrelevant condition chain
    state_flags = defaultdict(bool)
    state_flags['initial'] = True
    state_flags['calibrated'] = (mean_pressure > 100)
    state_flags['stable_humidity'] = (abs(mean_humidity - 47.5) < 5)

    # Decision matrix with red herring conditions
    base_score = 100
    if mean_temp > 23.5:
        base_score += 10
    if anomaly_count == 0:
        base_score += 15
    else:
        base_score -= 5 * anomaly_count

    # Irrelevant bonus logic based on distractor flags
    if state_flags['calibrated'] and state_flags['stable_humidity']:
        base_score += 2  # Looks important but doesn't always trigger

    # Final adjustment using mode frequency (distractor)
    distraction_bonus = mode_temp * 0.5
    final_score = int(base_score - distraction_bonus)  # Only this is printed

    return final_score

# Main execution
if __name__ == "__main__":
    data_log = generate_sensor_data()
    threshold = 1.0
    
    # Extraneous pre-processing step
    cleaned_data = filter_critical_entries(data_log, 20, 30)
    extracted_temps = [val for _, val in cleaned_data]
    baseline = compute_baseline(extracted_temps)
    
    # Key statement
    final_score = evaluate_performance(data_log, threshold)
    print(f"Target result: {final_score}")