import itertools

def analyze_sensor_readings(readings):
    # Irrelevant preprocessing: normalize readings (not used in final path)
    normalized = [r / max(readings) for r in readings]
    smoothed = [sum(readings[i:i+3]) / 3 for i in range(len(readings)-2)]
    
    # Distractor: frequency analysis using itertools (dead end)
    freq_count = {k: len(list(g)) for k, g in itertools.groupby(sorted(readings))}
    entropy_proxy = sum([f * f for f in freq_count.values()])  # Misleading metric

    # Real logic: count anomalies above threshold 75
    anomalies = [r for r in readings if r > 75]
    return len(anomalies)

def compute_stability_index(logs):
    # Dead code path: calculates volatility but never used
    diffs = [abs(logs[i] - logs[i-1]) for i in range(1, len(logs))]
    volatility = sum(diffs) / len(diffs) if diffs else 0
    
    # Another red herring: pattern detection with zip
    pairs = list(zip(logs, logs[1:]))
    trend_changes = sum(1 for a, b in pairs if (a > 80) != (b > 80))
    
    # Actual relevant part: number of stable periods (<= 10 consecutive values below 60)
    stable_period_count = 0
    current_stable = 0
    for val in logs:
        if val < 60:
            current_stable += 1
            if current_stable == 10:
                stable_period_count += 1
                current_stable = 0
        else:
            current_stable = 0
    return stable_period_count

def validate_calibration(sequence):
    # Unrelated calibration check (decoy function)
    expected_checksum = sum(sequence) % 100
    measured_power = sum(s ** 0.5 for s in sequence if s % 2 == 0)
    return expected_checksum < 50

def aggregate_metrics(data, limits):
    # Core logic hidden among distractions
    
    # Irrelevant transformation
    filtered_data = {k: [v for v in vals if v > limits[k]] for k, vals in data.items()}
    total_exceedances = sum(len(exceeds) for exceeds in filtered_data.values())
    
    # Misleading aggregation: harmonic mean of thresholds (unused)
    active_sensors = [k for k, v in data.items() if len(v) > 5]
    harmonic_limit = len(active_sensors) / sum(1/limits[k] for k in active_sensors) if active_sensors else 0
    
    # Critical real computation chain
    sensor_scores = []
    for sensor, readings in data.items():
        # Step 1: anomaly count from analyze_sensor_readings
        anomaly_count = analyze_sensor_readings(readings)
        
        # Step 2: stability from compute_stability_index
        stability_score = compute_stability_index(readings)
        
        # Step 3: weighted combination
        score = anomaly_count * 3 - stability_score * 2
        sensor_scores.append(score)
    
    # Step 4: sum all sensor scores
    total_score = sum(sensor_scores)
    
    # Step 5: apply decoy calibration check (does not affect result)
    _ = validate_calibration([int(x) for x in data['turbine_1']])
    
    # Step 6: final adjustment based on threshold cross-count
    adjustment_factor = 0
    for readings in data.values():
        adjustment_factor += sum(1 for r in readings if r > 90)
    
    # Final result
    final_diagnostic = total_score + adjustment_factor * 5
    return final_diagnostic

# Main execution
if __name__ == '__main__':
    # Simulated industrial turbine sensor data
    turbine_data = {
        'turbine_1': [65, 70, 80, 95, 96, 45, 50, 55, 60, 65, 70, 85, 90, 92],
        'turbine_2': [50, 55, 60, 65, 70, 75, 80, 82, 83, 84, 85, 98, 99, 100],
        'turbine_3': [40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 91, 93, 94],
        'turbine_4': [55, 58, 59, 61, 62, 63, 64, 59, 58, 57, 56, 55, 97, 98]
    }
    
    # Threshold configuration (used selectively)
    thresholds = {
        'turbine_1': 75,
        'turbine_2': 70,
        'turbine_3': 80,
        'turbine_4': 60
    }
    
    # Dead variable assignments (distractors)
    system_status = 'nominal'
    last_maintenance = '2023-10-05'
    uptime_hours = 8760
    maintenance_factor = 0.98
    
    # Key execution point
    final_diagnostic = aggregate_metrics(turbine_data, thresholds)
    
    # Output result
    print(f"Result: {final_diagnostic}")