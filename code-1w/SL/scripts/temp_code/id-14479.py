import math

# Simulated sensor fusion and diagnostic system for environmental monitoring

def collect_sensor_data():
    # Real data collection (simplified)
    return {
        'temperature': [23.5, 24.1, 22.9, 25.3, 26.0],
        'humidity': [45, 47, 50, 44, 46],
        'pressure': [1013, 1015, 1012, 1010, 1008]
    }

def generate_calibration_matrix():
    # Generate a realistic 3x3 calibration matrix
    base = [[1.02, 0.01, -0.03],
            [0.02, 1.01, 0.005],
            [-0.01, 0.003, 1.00]]
    noise = [[0.001 * (i + j) for j in range(3)] for i in range(3)]
    return [[base[i][j] + noise[i][j] for j in range(3)] for i in range(3)]

def validate_data_integrity(data):
    # Check if all sensor lists have same length
    lengths = [len(v) for v in data.values()]
    return len(set(lengths)) == 1

def compute_rolling_average(values, window=3):
    if len(values) < window:
        return [sum(values)/len(values)]
    avgs = []
    for i in range(len(values) - window + 1):
        avgs.append(sum(values[i:i+window]) / window)
    return avgs

def detect_anomalies(readings):
    # Simple anomaly detection based on deviation from median
    sorted_vals = sorted(readings)
    median = sorted_vals[len(sorted_vals)//2]
    threshold = 1.5 * (max(readings) - min(readings))
    anomalies = [x for x in readings if abs(x - median) > threshold]
    return len(anomalies)

def apply_calibration(raw_values, factor):
    # Apply scalar calibration
    return [v * factor for v in raw_values]

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def matrix_multiply(A, B):
    # Multiply two matrices
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

def extract_diagnostic_features(data):
    # Extract statistical features for diagnostics
    features = {}
    for sensor, readings in data.items():
        features[f'{sensor}_mean'] = sum(readings) / len(readings)
        variance = sum((x - features[f'{sensor}_mean'])**2 for x in readings) / len(readings)
        features[f'{sensor}_std'] = math.sqrt(variance)
        features[f'{sensor}_trend'] = readings[-1] - readings[0]
    return features

def calculate_entropy(values):
    # Calculate entropy of distribution
    total = sum(values)
    probs = [v/total for v in values]
    return -sum(p * math.log(p) for p in probs if p > 0)

def fuse_sensors(data_dict):
    # Fuses sensor data into composite index
    temp_weighted = sum(data_dict['temperature']) * 0.4
    humid_weighted = sum(data_dict['humidity']) * 0.3
    press_weighted = sum(data_dict['pressure']) * 0.001 * 0.3
    return (temp_weighted + humid_weighted + press_weighted) / len(next(iter(data_dict.values())))

def analyze_correlations(data):
    # Dummy correlation analysis
    temp = data['temperature']
    humid = data['humidity']
    n = len(temp)
    mean_temp = sum(temp)/n
    mean_humid = sum(humid)/n
    cov = sum((temp[i]-mean_temp)*(humid[i]-mean_humid) for i in range(n))
    var_temp = sum((t-mean_temp)**2 for t in temp)
    var_humid = sum((h-mean_humid)**2 for h in humid)
    if var_temp == 0 or var_humid == 0:
        return 0
    return cov / (math.sqrt(var_temp) * math.sqrt(var_humid))

def derive_health_index(metrics):
    # Compute system health index from various metrics
    base = 100
    for key, val in metrics.items():
        if 'std' in key:
            base -= abs(val) * 2
        if 'trend' in key:
            base -= abs(val) * 0.5
    return max(0, min(100, base))

def filter_outliers(data, threshold=2):
    # Remove outliers more than threshold standard deviations away
    filtered = {}
    for sensor, readings in data.items():
        mean = sum(readings) / len(readings)
        std = math.sqrt(sum((x - mean)**2 for x in readings) / len(readings))
        filtered[sensor] = [x for x in readings if abs(x - mean) <= threshold * std]
    return filtered

def compute_fourier_component(signal, freq=1):
    # Simplified Fourier-like component extraction
    n = len(signal)
    real = sum(signal[i] * math.cos(2 * math.pi * freq * i / n) for i in range(n))
    imag = sum(signal[i] * math.sin(2 * math.pi * freq * i / n) for i in range(n))
    return math.sqrt(real**2 + imag**2)

def evaluate_stability_index(ts_data):
    # Evaluate time series stability
    if len(ts_data) < 2:
        return 0
    diffs = [abs(ts_data[i+1] - ts_data[i]) for i in range(len(ts_data)-1)]
    return 1 / (1 + sum(diffs)/len(diffs))

def process_readings(sensor_data, calibration_matrix):
    # Core processing function with multiple stages
    
    # Step 1: Validate input
    if not validate_data_integrity(sensor_data):
        return -1
    
    # Step 2: Preprocess - filter outliers
    clean_data = filter_outliers(sensor_data)
    
    # Step 3: Extract features
    features = extract_diagnostic_features(clean_data)
    
    # Step 4: Calibrate temperature using matrix (only first 3 elements matter)
    temp_array = [[clean_data['temperature'][0]], 
                  [clean_data['temperature'][1]], 
                  [clean_data['temperature'][2]]]
    calibrated_temp_col = matrix_multiply(calibration_matrix, temp_array)
    calibrated_temp = [row[0] for row in calibrated_temp_col]
    
    # Step 5: Apply additional scalar calibration to humidity
    calibrated_humidity = apply_calibration(clean_data['humidity'], 1.015)
    
    # Step 6: Compute derived metrics (many are distractions)
    rolling_temp = compute_rolling_average(calibrated_temp)
    temp_anomalies = detect_anomalies(calibrated_temp)
    humid_entropy = calculate_entropy(calibrated_humidity)
    pressure_stability = evaluate_stability_index(clean_data['pressure'])
    
    # Step 7: Correlation analysis (distraction)
    correlation_score = analyze_correlations(clean_data)
    
    # Step 8: Fourier analysis on pressure (red herring)
    pressure_fourier = compute_fourier_component(clean_data['pressure'])
    
    # Step 9: Fuse sensors into composite reading (partially relevant)
    fused_value = fuse_sensors(clean_data)
    
    # Step 10: Derive health index from features (this updates features dict)
    health_index = derive_health_index(features)
    
    # Step 11: Create diagnostic set with irrelevant tags
    diagnostic_tags = {"stable", "calibrated", "validated", "anomaly_free"}
    if temp_anomalies > 0:
        diagnostic_tags.add("temp_warning")
    
    # Step 12: Final computation path - this is the actual answer path
    # The real answer comes from: 
    #   (mean of calibrated first 3 temps) + (health_index / 10) + (stability contribution)
    base_temp_mean = sum(calibrated_temp[:3]) / 3
    stability_contribution = 0.5 * pressure_stability
    final_diagnostic = base_temp_mean + (health_index / 10) + stability_contribution
    
    # Irrelevant dictionary operations below
    report_summary = {
        'diagnostics': diagnostic_tags,
        'metrics': features,
        'fused': fused_value,
        'entropy': humid_entropy,
        'fourier_peak': pressure_fourier,
        'correlation': correlation_score
    }
    
    # More distraction: update dict with unused data
    report_summary.update({'version': '2.1', 'calibration_applied': True})
    report_summary['timestamp'] = 1234567890
    
    # Only this line matters for the answer
    return final_diagnostic

# Main execution
sensor_data = collect_sensor_data()
calibration_matrix = generate_calibration_matrix()
final_diagnostic = process_readings(sensor_data, calibration_matrix)
print(f"Result: {final_diagnostic}")