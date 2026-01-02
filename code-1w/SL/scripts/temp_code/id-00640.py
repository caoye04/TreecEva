import math

# Simulated sensor data processing for environmental monitoring system
def collect_sensor_data():
    raw_values = [23.4, 19.8, 20.1, 25.3, 18.7, 21.0, 22.5, 19.3, 20.8]
    timestamps = list(range(1000, 1009))
    metadata = {'unit': 'Celsius', 'location': 'Zone B7', 'version': '2.1'}
    return list(zip(timestamps, raw_values))


def filter_outliers(data, threshold=2.0):
    values = [d[1] for d in data]
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    filtered = [d for d in data if abs(d[1] - mean_val) <= threshold * std_dev]
    # Distractor: unused computation
    anomaly_score = sum(1 for v in values if v > mean_val + 1.5 * std_dev)
    return filtered


def smooth_signal(data, window=3):
    smoothed = []
    padded = [data[0]] * (window // 2) + data + [data[-1]] * (window // 2)
    for i in range(len(data)):
        window_vals = [padded[i + j][1] for j in range(window)]
        smoothed.append((data[i][0], round(sum(window_vals) / window, 2)))
    # Distractor: irrelevant transformation
    inverted = [(t, 1.0 / (v + 1e-5)) for t, v in smoothed]
    return smoothed


def extract_trend_segments(data):
    segments = []
    current_segment = [data[0]]
    for i in range(1, len(data)):
        if data[i][1] >= data[i-1][1]:
            current_segment.append(data[i])
        else:
            if len(current_segment) > 1:
                segments.append(current_segment)
            current_segment = [data[i]]
    if len(current_segment) > 1:
        segments.append(current_segment)
    # Distractor: dead-end analysis
    flat_segments = [s for s in segments if all(abs(s[j][1] - s[j+1][1]) < 0.1 for j in range(len(s)-1))]
    return segments or [[data[0], data[-1]]]


def compress_data(segments):
    compressed = []
    for seg in segments:
        start, end = seg[0], seg[-1]
        duration = end[0] - start[0]
        delta = round(end[1] - start[1], 2)
        if duration > 0:
            rate = round(delta / duration, 4)
        else:
            rate = 0.0
        compressed.append({'start_temp': start[1], 'end_temp': end[1], 'rate': rate})
    # Distractor: unused compression format
    legacy_format = [f'{c['start_temp']:.1f},{c['end_temp']:.1f}' for c in compressed]
    return compressed


def calculate_stability_index(compressed_segments):
    if not compressed_segments:
        return 0.0
    rates = [abs(seg['rate']) for seg in compressed_segments]
    max_rate = max(rates)
    avg_rate = sum(rates) / len(rates)
    stability = round((1 / (1 + avg_rate)) * 100, 2) if max_rate < 5.0 else round((1 / (1 + max_rate)) * 50, 2)
    # Distractor: alternative index calculation
    volatility = sum(r ** 2 for r in rates) / len(rates) if rates else 0
    return stability


def assess_calibration_status(stability):
    return "CALIBRATED" if stability > 75.0 else "REVIEW_NEEDED"


def generate_diagnostics(stability, status, segments):
    peak_duration = max([len(s) for s in segments]) if segments else 1
    complexity_score = len(segments) * peak_duration
    base_risk = 100 - stability
    adjusted_risk = base_risk * (1 + 0.1 * complexity_score)
    final_risk = min(max(round(adjusted_risk, 1), 0), 100)
    # Distractor: alternate risk model
    conservative_risk = base_risk * (1.5 if complexity_score > 10 else 1.0)
    return {
        'risk_level': final_risk,
        'status': status,
        'complexity': complexity_score
    }


def analyze_readings(data_package):
    # Main processing pipeline
    raw_data = data_package.get('readings', [])
    config = data_package.get('config', {})
    
    # Step 1: Filter outliers
    clean_data = filter_outliers(raw_data)
    
    # Step 2: Smooth signal
    smoothed_data = smooth_signal(clean_data)
    
    # Step 3: Extract trend segments
    trend_segments = extract_trend_segments(smoothed_data)
    
    # Step 4: Compress into analytical units
    compressed_analysis = compress_data(trend_segments)
    
    # Step 5: Calculate stability index
    stability_index = calculate_stability_index(compressed_analysis)
    
    # Step 6: Assess calibration
    calibration_status = assess_calibration_status(stability_index)
    
    # Step 7: Generate full diagnostics
    diagnostics = generate_diagnostics(stability_index, calibration_status, trend_segments)
    
    # Key computation: final diagnostic score
    adjustment_factor = config.get('adjustment', 1.0)
    base_score = diagnostics['risk_level']
    penalty = 0
    
    # Conditional expression and slicing used here
    if len(smoothed_data) > 5:
        recent_trend = smoothed_data[-3:]
        if any(t[1] > 22.0 for t in recent_trend):
            penalty += 5
    else:
        penalty += 10
    
    # Final computation with distractors
    temp_baseline = sum(d[1] for d in smoothed_data[:min(3, len(smoothed_data))]) / min(3, len(smoothed_data))
    decay_correction = math.exp(-temp_baseline / 100)
    unadjusted_result = base_score + penalty
    final_diagnostic = int(round(unadjusted_result * adjustment_factor * decay_correction))
    
    # Irrelevant post-processing (dead code path)
    if final_diagnostic < 0:
        final_diagnostic = 0
    elif final_diagnostic > 200:
        audit_flag = True
        normalized = 200
    
    return final_diagnostic

# Simulate data package
sensor_readings = collect_sensor_data()
data_package = {
    'readings': sensor_readings,
    'config': {'adjustment': 1.1},
    'timestamp': 20240517,
    'source_id': 'SEN-B7-042'
}

# Additional distractor variables
baseline_stats = {
    'initial_mean': sum(r[1] for r in sensor_readings[:3]) / 3,
    'total_points': len(sensor_readings),
    'version': 'A'
}

historical_ref = [20.5, 21.3, 19.9, 22.1, 20.7]
consistency_check = all(abs(h - baseline_stats['initial_mean']) < 2.0 for h in historical_ref)

# Unused function - red herring
def legacy_analysis(data):
    return sum(d[1] * 0.95 for d in data[:5]) / 5

# Main execution point
processed_data = {
    'readings': data_package['readings'],
    'config': data_package['config']
}

final_diagnostic = analyze_readings(processed_data)
print(f"Result: {final_diagnostic}")