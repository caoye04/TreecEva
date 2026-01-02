import itertools

def preprocess_signals(raw_samples, noise_floor):
    cleaned = []
    peak_magnitude = 0
    total_energy = 0
    
    for sample in raw_samples:
        if abs(sample) < noise_floor:
            adjusted = 0
        else:
            adjusted = sample - noise_floor if sample > 0 else sample + noise_floor
        
        cleaned.append(adjusted)
        total_energy += adjusted ** 2
        
        if abs(adjusted) > peak_magnitude:
            peak_magnitude = abs(adjusted)
    
    normalization_factor = 1 / peak_magnitude if peak_magnitude > 0 else 1
    normalized = [c * normalization_factor for c in cleaned]
    
    return normalized, total_energy


def detect_anomalies(data_stream, sensitivity):
    anomaly_count = 0
    moving_avg = 0
    avg_window = []
    false_alarm_risk = 0.0
    
    for val in data_stream:
        avg_window.append(val)
        if len(avg_window) > 5:
            avg_window.pop(0)
        
        moving_avg = sum(avg_window) / len(avg_window)
        deviation = abs(val - moving_avg)
        
        if deviation > sensitivity:
            anomaly_count += 1
            
            # Simulate risk adjustment (not used in final result)
            if deviation > 2 * sensitivity:
                false_alarm_risk += 0.05
            
    # Dummy post-processing to add interference
    final_adjustment = 0
    for i in range(anomaly_count):
        final_adjustment ^= (i + 1)  # Bitwise distraction
    
    return anomaly_count * 10 + 7


def analyze_sensor_array():
    # Simulated raw sensor readings
    sensor_readings = [0.1, -0.3, 0.8, 1.4, -2.1, 3.0, 0.5, -1.2, 2.5, 2.6, 2.7, -0.9, 1.0]
    
    # Irrelevant baseline metrics
    baseline_stats = {
        'mean_offset': 0.05,
        'calibration_cycle': 3,
        'drift_compensation': True
    }
    
    # Noise parameters
    ambient_noise = 0.5
    detection_threshold = 0.4
    
    # Preprocess signal
    processed_signal, energy_metric = preprocess_signals(sensor_readings, ambient_noise)
    
    # Apply filtering based on dynamic criteria
    filtered_data = []
    cumulative_shift = 0
    
    for x in processed_signal:
        if x != 0:
            cumulative_shift += x * 0.1
            filtered_data.append(x + cumulative_shift)
        else:
            filtered_data.append(0)
    
    # Introduce red herring computation
    entropy_proxy = 0
    for combo in itertools.combinations([abs(x) for x in filtered_data if x != 0], min(3, len([x for x in filtered_data if x != 0]))):
        product = 1
        for c in combo:
            product *= max(c, 0.1)
        entropy_proxy += product
    
    # Key statement
    filtration_score = detect_anomalies(filtered_data, detection_threshold)
    
    # Additional irrelevant state tracking
    performance_log = []
    for step in range(3):
        performance_log.append({"step": step, "status": "complete"})
    
    print(f"Result: {filtration_score}")
    
    return filtration_score

result = analyze_sensor_array()