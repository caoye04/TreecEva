from collections import defaultdict
import math

# Simulate sensor data processing with performance evaluation

def collect_sensor_data():
    # Real data collection (simplified)
    return [78, 85, 92, 64, 71]

def apply_calibration(data):
    # Apply arbitrary calibration curve
    calibrated = []
    for x in data:
        if x < 70:
            calibrated.append(x * 1.1)
        elif x > 90:
            calibrated.append(x * 0.95)
        else:
            calibrated.append(x)
    return calibrated

def analyze_outliers(data):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    outliers = [x for x in data if abs(x - mean_val) > 1.5 * std_dev]
    return outliers  # Unused downstream

def compute_rolling_average(data, window=3):
    rolling = []
    for i in range(len(data) - window + 1):
        rolling.append(sum(data[i:i+window]) / window)
    return rolling  # Used only for distraction

def generate_diagnostic_report(data):
    report = defaultdict(lambda: 'N/A')
    report['count'] = len(data)
    report['max'] = max(data)
    report['min'] = min(data)
    report['range'] = report['max'] - report['min']
    report['median'] = sorted(data)[len(data)//2]
    # Irrelevant transformations
    temp_hist = {i: sum(1 for x in data if i*10 <= x < (i+1)*10) for i in range(10)}
    normalized = [round((x - min(data)) / (max(data) - min(data)) * 100) for x in data]
    adjusted_scores = [x + 5 for x in normalized if x < 50]  # Dead code path
    return report

def filter_critical_readings(data, threshold=75):
    critical = [x for x in data if x < threshold]
    return [c * 1.2 for c in critical]  # Not used

def calculate_efficiency_factor(n):
    # Unrelated recursive function (red herring)
    if n <= 1:
        return 1
    return n * 0.9 + calculate_efficiency_factor(n - 1) * 0.1

def transform_metrics(metrics):
    transformed = {}
    for k, v in metrics.items():
        if 'score' in k:
            transformed[k] = round(v * 1.05, 2)
        elif 'count' in k:
            transformed[k] = int(v * 0.9)
        else:
            transformed[k] = v
    # Add derived metrics
    if 'accuracy_score' in transformed:
        transformed['precision_boost'] = transformed['accuracy_score'] * 0.1
    return transformed

def evaluate_performance(metrics, weights):
    base = 0
    weight_sum = 0
    for key in weights:
        if key in metrics:
            base += metrics[key] * weights[key]
            weight_sum += weights[key]
    if weight_sum == 0:
        return 0
    raw_score = base / weight_sum
    # Apply non-linear adjustment
    adjusted = math.log(raw_score + 1) * 10
    final = round(adjusted, 2)
    return final

def main():
    # Step 1: Collect raw sensor data
    raw_data = collect_sensor_data()
    
    # Step 2: Calibrate sensor readings
    calibrated_data = apply_calibration(raw_data)
    
    # Step 3: Analyze outliers (result not used)
    outliers = analyze_outliers(calibrated_data)
    
    # Step 4: Compute rolling average (distraction)
    rolling_avg = compute_rolling_average(calibrated_data)
    
    # Step 5: Generate full diagnostic report (contains distractors)
    report = generate_diagnostic_report(calibrated_data)
    
    # Step 6: Filter critical readings (dead end)
    critical_readings = filter_critical_readings(calibrated_data)
    
    # Step 7: Calculate unrelated efficiency factor (red herring)
    eff_factor = calculate_efficiency_factor(len(calibrated_data))
    
    # Step 8: Build performance metrics dictionary
    metrics = {
        'accuracy_score': sum(calibrated_data) / len(calibrated_data),
        'stability_index': report['range'],
        'consistency_score': report['median'],
        'sample_count': len(calibrated_data)
    }
    
    # Step 9: Transform metrics (intermediate step)
    transformed_metrics = transform_metrics(metrics)
    
    # Step 10: Define weighting schema
    weights = {
        'accuracy_score': 0.4,
        'stability_index': -0.2,  # Penalty for high variance
        'consistency_score': 0.3,
        'sample_count': 0.1
    }
    
    # Step 11: Evaluate final performance score
    final_score = evaluate_performance(transformed_metrics, weights)
    
    # Print result for extraction
    print(f"Target result: {final_score}")
    
    return final_score

if __name__ == "__main__":
    main()