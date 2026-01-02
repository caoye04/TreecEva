def analyze_pattern(seq):
    return sum(x * (i + 1) for i, x in enumerate(seq))

# Simulated sensor data stream (irrelevant to final result)
sensor_log = [127, 89, 103, 115, 98, 107]
baseline_offset = 100
adjusted_readings = [abs(x - baseline_offset) for x in sensor_log]
count_above_threshold = len([x for x in adjusted_readings if x > 15])

# Data transformation pipeline (partial red herring)
transform = lambda x: (x ** 0.5) * 2
mapped_values = list(map(transform, adjusted_readings))

# Core health monitoring data (only this matters)
health_data = [85, 92, 78, 96, 88]
thresh_map = {'low': 80, 'high': 95}

# Misleading diagnostic using wrong logic (dead path)
def false_alarm(data):
    risk_score = 0
    for val in data:
        if val < 82:
            risk_score += 10
        elif val > 94:
            risk_score += 5
    return risk_score // 2

# Unused but plausible-looking function (decoy)
def evaluate_stability(metrics):
    diffs = [abs(metrics[i] - metrics[i+1]) for i in range(len(metrics)-1)]
    return sum(diffs) / len(diffs) if diffs else 0

# Real processing with distractor-heavy context
def process_metrics(readings, limits):
    alert_count = 0
    trend_boost = 0
    
    # Real logic embedded in noise
    for idx, level in enumerate(readings):
        if level < limits['low']:
            alert_count += 1
        elif level > limits['high']:
            # Apply bonus based on position via enumerate
            trend_boost += idx % 3  # Only indices matter here
    
    # Irrelevant smoothing operation (distractor)
    smoothed = [readings[i] for i in range(0, len(readings), 2]]
    fallback_index = sum(smoothed) // len(smoothed)
    
    # Critical calculation hidden among side computations
    raw_alerts = alert_count * 7
    boost_factor = analyze_pattern([trend_boost, 2, trend_boost + 1])
    
    # Final result combines correct and misleading paths
    temp_diagnostic = raw_alerts + boost_factor
    secondary_check = false_alarm(readings)  # Computed but unused
    final_diagnostic = temp_diagnostic - fallback_index  # Final answer
    
    # Dead code block (never executed)
    if False:
        backup = evaluate_stability(readings)
        final_diagnostic = backup * 2
    
    return final_diagnostic

# Execute main logic
diagnostic_code = 42
initial_scan = sum(sensor_log) % 100

# Key execution point
final_diagnostic = process_metrics(health_data, thresh_map)

# Print required output
print(f"Result: {final_diagnostic}")