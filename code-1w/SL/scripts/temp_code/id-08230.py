import itertools

# Simulated sensor data from multiple sources
temperature_readings = [23.5, 24.1, 22.9, 25.0, 23.8]
humidity_readings = [45, 47, 50, 44, 46]
pressure_readings = [1013, 1012, 1015, 1011, 1014]

# Irrelevant backup data (distractor)
backup_temperatures = [26.0, 25.8, 26.1]  
backup_notes = ['stable', 'minor fluctuation', 'check calibration']

# System thresholds (some are decoys)
CRITICAL_TEMP = 30.0
WARNING_HUMIDITY = 75
PRESSURE_TOLERANCE = 5
UNUSED_THRESHOLD = 999  # Dead constant

# Historical baseline for comparison (partially relevant)
historical_avg_temp = 24.0
historical_avg_humidity = 48

# Data validation function (looks important but unused)
def validate_sensor_input(data, min_val, max_val):
    return all(min_val <= x <= max_val for x in data)

# Auxiliary transformation (used only once, subtle relevance)
def normalize(data):
    mean_val = sum(data) / len(data)
    return [round(x - mean_val, 2) for x in data]

# Complex metric generator with red herrings
def generate_metrics(temp, humidity, pressure):
    # Normalize inputs
    norm_temp = normalize(temp)
    norm_humidity = normalize(humidity)
    norm_pressure = normalize(pressure)
    
    # Compute various indices (many irrelevant)
    volatility_index = sum(abs(t) for t in norm_temp) / len(norm_temp)
    correlation_hint = sum(norm_temp[i] * norm_humidity[i] for i in range(len(norm_temp)))
    pressure_stability = sum(1 for p in norm_pressure if abs(p) < 0.5)
    
    # Fake composite metrics (distractors)
    phantom_metric_1 = volatility_index * correlation_hint
    phantom_metric_2 = pressure_stability ** 2
    temp_humidity_ratio = (sum(temp) / len(temp)) / (sum(humidity) / len(humidity))
    
    # Real feature: detect anomalous readings
    anomalies = 0
    for t, h, p in zip(temp, humidity, pressure):
        if t > CRITICAL_TEMP or h > WARNING_HUMIDITY:
            anomalies += 1
    
    # Real metric used later
    adjusted_volatility = round(volatility_index * 100) if anomalies == 0 else 0
    
    # Return includes many decoys
    return {
        'volatility': adjusted_volatility,
        'phantom_a': phantom_metric_1,
        'phantom_b': phantom_metric_2,
        'baseline_drift': abs(sum(norm_temp)),
        'anomaly_count': anomalies
    }

# Unused alternative evaluation (dead path)
def legacy_evaluation(data):
    return sum(x**2 for x in data) / len(data)

# Main processing begins here
metric_set = generate_metrics(temperature_readings, humidity_readings, pressure_readings)

# Simulated benchmark dataset (only specific part matters)
benchmark_data = {
    'ref_temp': historical_avg_temp,
    'ref_humid': historical_avg_humidity,
    'tolerance': PRESSURE_TOLERANCE,
    'weights': {'vol': 0.6, 'drift': 0.3, 'bonus': 0.1},
    'penalty_factor': 5
}

# Large block of set operations and combinations (some relevant, some not)
sensor_ids = {'S1', 'S2', 'S3', 'S4', 'S5'}
external_ids = {'X1', 'S2', 'X3', 'S4'}
overlapping_sensors = sensor_ids & external_ids  # {'S2', 'S4'}
unique_local = sensor_ids - external_ids          # {'S1', 'S3'}

# Generate Cartesian product of normalized readings (mostly irrelevant)
norm_t = normalize(temperature_readings)
norm_h = normalize(humidity_readings)
reading_pairs = list(itertools.product(norm_t[:3], norm_h[:3]))  # Partial use
pair_summation = sum(a * b for a, b in reading_pairs)  # Distractor

# Critical function with mixed logic
def evaluate_performance(metrics, config):
    base_score = metrics['volatility']
    drift_penalty = 0
    
    # Conditional bonus/penalty logic
    if metrics['anomaly_count'] == 0:
        drift_comp = metrics['baseline_drift']
        if drift_comp < 1.0:
            drift_penalty = -5  # Small penalty
        elif drift_comp > 2.0:
            drift_penalty = -15
        else:
            drift_penalty = -10
        
        # Bonus path (never reached due to condition above)
        high_pressure_bonus = 0  # Dead variable
        if metrics['phantom_b'] > 100:
            high_pressure_bonus = 20
    
    # Weighted calculation (only base_score and drift_penalty matter)
    w = config['weights']
    final = base_score + drift_penalty
    
    # Decoy arithmetic with unreachable branches
    extra_boost = 0
    for i in range(3):
        if i == 5:  # Impossible condition
            extra_boost += 10
    
    # Final adjustment
    penalty = config['penalty_factor'] * metrics['anomaly_count']
    final -= penalty
    
    # This looks like an important transformation but isn't
    fake_normalization = final / (1 + abs(pair_summation)) if pair_summation != 0 else final
    
    return int(final)  # Only this matters

# Execute main evaluation
final_score = evaluate_performance(metric_set, benchmark_data)

# Print result as required
print(f"Target result: {final_score}")