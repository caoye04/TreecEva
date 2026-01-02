from collections import defaultdict, Counter

# Simulated sensor network diagnostic system
def collect_sensor_data():
    raw_readings = [
        (101, 23.4), (102, 24.1), (103, 25.6), (104, 22.9),
        (101, 23.5), (102, 24.0), (103, 26.1), (104, 23.0),
        (101, 23.3), (102, 24.2), (103, 25.8), (104, 23.1),
        (105, 19.8), (106, 20.1), (107, 18.9), (108, 195.7),
        (105, 19.9), (106, 20.0), (107, 19.0), (108, 196.2)
    ]
    return raw_readings

def filter_anomalies(readings):
    # Group by sensor ID
    grouped = defaultdict(list)
    for sid, val in readings:
        grouped[sid].append(val)
    
    # Compute median for each sensor (robust to outliers)
    medians = {}
    for sid, vals in grouped.items():
        sorted_vals = sorted(vals)
        n = len(sorted_vals)
        if n % 2 == 0:
            medians[sid] = (sorted_vals[n//2-1] + sorted_vals[n//2]) / 2
        else:
            medians[sid] = sorted_vals[n//2]
    
    # Identify sensors with potential hardware faults (high variance or extreme values)
    suspect_sensors = set()
    for sid, vals in grouped.items():
        if max(vals) > 100:  # Clear outlier like 195+ indicates fault
            suspect_sensors.add(sid)
        elif abs(sum(vals)/len(vals) - medians[sid]) > 0.5:
            suspect_sensors.add(sid)
    
    # Distractor: irrelevant statistical mode calculation
    all_values = [v for _, v in readings]
    value_counts = Counter(all_values)
    mode_value = value_counts.most_common(1)[0][0]  # Red herring
    mode_frequency = value_counts.most_common(1)[0][1]  # Unused
    
    # Filter out faulty sensors
    filtered = []
    for sid, val in readings:
        if sid not in suspect_sensors:
            filtered.append((sid, val))
    
    # Another distractor: unused transformation
    normalized = [round((v - 20) / 5, 2) for v in all_values if v < 100]  # Not used
    
    return filtered

def analyze_readings(valid_readings):
    # Re-group cleaned data
    temp_by_sensor = defaultdict(list)
    for sid, val in valid_readings:
        temp_by_sensor[sid].append(val)
    
    # Compute average temperature per working sensor
    avg_temps = []
    for sid in sorted(temp_by_sensor.keys()):
        avg = sum(temp_by_sensor[sid]) / len(temp_by_sensor[sid])
        avg_temps.append(avg)
    
    # System baseline and deviation tracking
    system_avg = sum(avg_temps) / len(avg_temps)
    deviations = [abs(t - system_avg) for t in avg_temps]
    
    # Distractor: complex but unused bit manipulation on sensor IDs
    sensor_ids = list(temp_by_sensor.keys())
    xor_fingerprint = 0
    for sid in sensor_ids:
        xor_fingerprint ^= (sid * 31)  # Hash-like pattern, unused
    shift_check = (xor_fingerprint >> 4) & 0xFF  # Dead code path
    
    # Real logic: count how many sensors are above threshold
    stable_count = sum(1 for t in avg_temps if 22.5 <= t <= 25.5)
    unstable_count = len(avg_temps) - stable_count
    
    # Diagnostic score based on stability ratio
    if unstable_count == 0:
        diagnostic_score = 100.0
    else:
        diagnostic_score = (stable_count / (stable_count + unstable_count)) * 100
    
    # Final weighted diagnostic incorporating deviation penalty
    total_deviation = sum(deviations)
    if total_deviation > 5.0:
        penalty = (total_deviation - 5.0) * 2
    else:
        penalty = 0
    
    final_diagnostic = diagnostic_score - penalty
    
    # Distractor: alternate formula never taken
    if len(avg_temps) > 10:
        alt_score = sum(avg_temps) * 1.5  # Unused path
    elif len(avg_temps) == 0:
        final_diagnostic = -1  # Edge case not triggered
    
    return final_diagnostic

# Irrelevant utility function (dead code)
def compress_data(data_list):
    compressed = []
    for i in range(0, len(data_list), 2):
        if i+1 < len(data_list):
            compressed.append((data_list[i] + data_list[i+1]) / 2)
    return compressed

# Unused constant definitions (distractors)
CALIBRATION_FACTOR = 0.987
THRESHOLD_WINDOW = (18.0, 30.0)
MAX_READINGS_PER_SENSOR = 100

# Main execution flow
sensor_data = collect_sensor_data()
filtered_readings = filter_anomalies(sensor_data)
final_diagnostic = analyze_readings(filtered_readings)
print(f"Result: {final_diagnostic}")