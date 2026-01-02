def analyze_trend(data, threshold=0.5):
    above_threshold = [x for x in data if x > threshold]
    below_threshold = [x for x in data if x <= threshold]
    trend_ratio = len(above_threshold) / len(below_threshold) if below_threshold else float('inf')
    return trend_ratio

# Simulate sensor readings over time
readings = [0.62, 0.48, 0.71, 0.33, 0.54, 0.82, 0.29, 0.67]

# Misleading transformation (not used in final result)
transformed = list(map(lambda x: round(x ** 2 + 0.1, 3), readings))

# Secondary analysis with red herring variables
total_fluctuation = sum(abs(readings[i] - readings[i-1]) for i in range(1, len(readings)))
avg_reading = sum(readings) / len(readings)
median_reading = sorted(readings)[len(readings)//2]

# Conditional expression to determine processing mode
dynamic_mode = 'adaptive' if avg_reading > 0.5 else 'conservative'

# Core logic disguised among auxiliary calculations
def evaluate_performance(logs, method='hybrid'):
    if method == 'hybrid':
        valid_logs = [x for x in logs if 0.3 <= x <= 0.7]
        outlier_count = len([x for x in logs if x < 0.3 or x > 0.7])
        base_efficiency = len(valid_logs) / len(logs)
        
        # Nested conditional with distractor branches
        adjustment_factor = 0.9 if outlier_count > 2 else (0.95 if dynamic_mode == 'adaptive' else 0.85)
        
        # Complex but partially irrelevant computation
        cumulative_drift = 0.0
        for i in range(1, len(logs)):
            drift = logs[i] - logs[i-1]
            cumulative_drift += abs(drift) * 0.1
        smoothness_score = max(0, 1 - cumulative_drift)
        
        # Key calculation step
        raw_score = base_efficiency * adjustment_factor
        final_score = round(raw_score + smoothness_score * 0.3, 4)
        
        # Dead code path (never executed under current conditions)
        if len(logs) < 5:
            fallback = sum(logs) % 1
            final_score = fallback
        
        return final_score

# Unused helper function (adds interference)
def normalize_signal(signal):
    min_val, max_val = min(signal), max(signal)
    return [(x - min_val) / (max_val - min_val) for x in signal]

# Unused statistical measures
variance_proxy = sum((x - avg_reading)**2 for x in readings) / len(readings)
std_deviation = variance_proxy ** 0.5

# Key execution point
final_score = evaluate_performance(readings, method='hybrid')

# Print result as required
print(f"Result: {final_score}")