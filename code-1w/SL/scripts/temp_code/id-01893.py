from collections import defaultdict, Counter

# Simulated sensor network data with metadata
def collect_sensor_data():
    raw_readings = [
        (101, 23.5, 'temp'), (102, 45.0, 'pressure'), (103, 23.5, 'temp'),
        (104, 67.2, 'humidity'), (105, 45.0, 'pressure'), (106, 29.8, 'temp'),
        (107, 67.2, 'humidity'), (108, 33.1, 'temp'), (109, 45.0, 'pressure')
    ]
    return raw_readings

def validate_calibration(signal_log):
    # Irrelevant validation for calibration drift (dead path)
    timestamps = [i * 10 + 3 for i in range(len(signal_log))]
    offsets = [abs(t % 7 - 3.5) for t in timestamps]
    adjusted = [signal_log[i][1] + offsets[i] for i in range(len(signal_log))]
    return all(x < 100 for x in adjusted)

def filter_anomalies(data_seq, mode='strict'):
    # Extract only temperature readings
    temp_only = [entry for entry in data_seq if entry[2] == 'temp']
    values = [x[1] for x in temp_only]
    mean_val = sum(values) / len(values)
    
    # Compute rolling deviation (distractor)
    deviances = [abs(v - mean_val) for v in values]
    avg_dev = sum(deviances) / len(deviances)
    
    # Threshold filtering (actual relevant logic)
    filtered = [entry for entry in temp_only if abs(entry[1] - mean_val) <= 2 * avg_dev]
    return filtered

def build_threshold_map(records):
    # Builds a dummy map with irrelevant complexity
    count_map = Counter([r[2] for r in records])
    base_thresholds = {'temp': 25.0, 'pressure': 40.0, 'humidity': 60.0}
    
    # Complex transformation that doesn't affect final result
    adjustment_factor = sum(count_map.values()) / (max(count_map.values()) + 1)
    enhanced = defaultdict(float)
    for k, v in base_thresholds.items():
        enhanced[k] = v * adjustment_factor
        if k == 'temp':
            enhanced[k] += 5.0  # Over-adjustment corrected later
    
    # Final correction
    enhanced['temp'] = 27.0  # Hardcoded override - key simplification
    return enhanced

def analyze_variance(dataset):
    # Dead-end statistical analysis
    temps = [x[1] for x in dataset if x[2] == 'temp']
    n = len(temps)
    mu = sum(temps) / n
    squared_diffs = [(x - mu)**2 for x in temps]
    variance = sum(squared_diffs) / (n - 1) if n > 1 else 0
    pseudo_z_scores = [(x - mu) / (variance**0.5 + 1e-8) for x in temps]
    outlier_flags = [abs(z) > 2 for z in pseudo_z_scores]
    return sum(outlier_flags)  # Unused result

def process_readings(entries, limits):
    # Core processing logic
    readings = [e[1] for e in entries]
    category_breakdown = defaultdict(int)
    for e in entries:
        category_breakdown[e[2]] += 1
    
    # Red herring: unused frequency map
    freq_report = {k: v / len(entries) for k, v in category_breakdown.items()}
    
    # Actual logic: count how many exceed temp threshold
    temp_threshold = limits['temp']
    high_temp_count = sum(1 for r in readings if r > temp_threshold)
    
    # Secondary logic: average of those below threshold
    valid_readings = [r for r in readings if r <= temp_threshold]
    safe_average = sum(valid_readings) / len(valid_readings) if valid_readings else 0
    
    # Final diagnostic score: combination metric
    diagnostic_score = (high_temp_count * 1000) + round(safe_average * 100)
    return int(diagnostic_score)

# Main execution flow
if __name__ == '__main__':
    # Step 1: Collect raw data
    sensor_data = collect_sensor_data()
    
    # Step 2: Validate calibration (result not used)
    is_valid = validate_calibration(sensor_data)
    
    # Step 3: Filter anomalies to get clean temperature data
    filtered_data = filter_anomalies(sensor_data, mode='strict')
    
    # Step 4: Build threshold configuration (appears complex)
    threshold_map = build_threshold_map(sensor_data)
    
    # Step 5: Perform irrelevant variance analysis
    anomaly_count = analyze_variance(sensor_data)
    
    # Step 6: Process filtered data with thresholds
    final_diagnostic = process_readings(filtered_data, threshold_map)
    
    # Output result
    print(f"Result: {final_diagnostic}")