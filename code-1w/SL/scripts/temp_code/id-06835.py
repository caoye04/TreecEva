import math

# Simulated sensor array data from environmental monitoring system
def get_sensor_readings():
    return [23.4, 19.5, 20.1, 25.3, 18.7, 22.0, 20.3, 19.8, 21.5, 24.0]

# Outlier detection (distractor: not actually used in final computation)
def remove_outliers(data, threshold=2.0):
    mean = sum(data) / len(data)
    std = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
    return [x for x in data if abs(x - mean) <= threshold * std]

# Irrelevant transformation function (dead code path)
def smooth_data(data, window=3):
    smoothed = []
    for i in range(len(data)):
        start = max(0, i - window // 2)
        end = min(len(data), i + window // 2 + 1)
        smoothed.append(sum(data[start:end]) / (end - start))
    return smoothed

# Unused signal processing (decoy function)
def fourier_approximate(data, harmonics=2):
    n = len(data)
    result = [0] * n
    for k in range(harmonics):
        real = sum(data[i] * math.cos(2 * math.pi * k * i / n) for i in range(n))
        imag = sum(data[i] * math.sin(2 * math.pi * k * i / n) for i in range(n))
        for i in range(n):
            result[i] += real * math.cos(2 * math.pi * k * i / n)
            result[i] -= imag * math.sin(2 * math.pi * k * i / n)
    return result

# Core evaluation logic
weights = (0.4, 0.3, 0.2, 0.1)

# Sensor metrics: temperature stability, fluctuation count, average, and peak deviation
def extract_metrics(readings):
    avg_temp = sum(readings) / len(readings)
    temp_changes = [abs(readings[i] - readings[i-1]) for i in range(1, len(readings))]
    fluctuations = sum(1 for delta in temp_changes if delta > 1.0)
    stability_score = sum(1 for delta in temp_changes if delta < 0.5)
    peak_deviation = max(abs(temp - avg_temp) for temp in readings)
    
    # Return tuple of key metrics
    return (stability_score, fluctuations, avg_temp, peak_deviation)

# Complex weighting system with misleading branches
def apply_weighting(metrics, weights):
    m1, m2, m3, m4 = metrics
    w1, w2, w3, w4 = weights
    
    # Distractor: complex normalization that isn't used
    normalized_m1 = (m1 - 5) / 5 if m1 > 5 else 0
    adjusted_m3 = m3 if m3 > 20 else m3 * 1.1
    
    # Real calculation hidden among alternatives
    candidate_a = m1 * w1 + (10 - m2) * w2 + (m3 - 18) * w3 + (4 - m4) * w4
    candidate_b = m1 * 0.5 + m4 * 0.5  # Irrelevant alternative
    candidate_c = sum(metrics[:3]) * 0.333  # Red herring
    
    # Actual selection logic
    if m3 >= 20 and m4 <= 3.5:
        selected = candidate_a
    elif m3 < 20:
        selected = candidate_b
    else:
        selected = candidate_c
        
    return selected

# Secondary adjustment with slicing distraction
def adjust_for_trend(readings, base_score):
    recent = readings[-4:]  # Last 4 readings
    older = readings[:4]   # First 4 readings
    recent_avg = sum(recent) / len(recent)
    older_avg = sum(older) / len(older)
    trend = recent_avg - older_avg
    
    # Slicing-based pattern analysis (partially relevant)
    increasing_pairs = sum(1 for i in range(len(recent)-1) if recent[i] < recent[i+1])
    decreasing_pairs = sum(1 for i in range(len(recent)-1) if recent[i] > recent[i+1])
    
    # Only trend matters in adjustment
    return base_score + (trend * 2) - abs(increasing_pairs - decreasing_pairs)

# Main evaluation pipeline
def evaluate_performance(metrics, weights):
    # Step 1: Apply primary weighting
    raw_score = apply_weighting(metrics, weights)
    
    # Step 2: Get original readings again (simulating state access)
    all_readings = get_sensor_readings()
    
    # Step 3: Adjust for recent trend
    adjusted_score = adjust_for_trend(all_readings, raw_score)
    
    # Step 4: Apply arbitrary calibration constant (hidden in comment)
    # Calibration factor: 1.05 derived from historical data
    calibrated = adjusted_score * 1.05
    
    # Step 5: Round to nearest integer (final step)
    return round(calibrated)

# Execution flow
if __name__ == "__main__":
    # Initialize system
    sensor_data = get_sensor_readings()
    
    # Process data through main pipeline (distraction: multiple processing functions exist)
    processed_data = remove_outliers(sensor_data)  # Result not used further
    filtered_data = smooth_data(sensor_data)       # Dead code assignment
    freq_domain = fourier_approximate(sensor_data) # Completely irrelevant
    
    # Extract meaningful metrics
    metrics = extract_metrics(sensor_data)
    
    # Evaluate performance - KEY STATEMENT
    final_score = evaluate_performance(metrics, weights)
    
    # Output result
    print(f"Result: {final_score}")