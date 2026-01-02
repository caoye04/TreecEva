import math

def preprocess_signal(raw_samples):
    # Irrelevant preprocessing (distractor)
    normalized = [x / max(raw_samples) for x in raw_samples]
    smoothed = [sum(normalized[i:i+3]) / 3 for i in range(len(normalized)-2)]
    return smoothed  # This return is never used in relevant logic

def calculate_entropy(data):
    # Dead function - looks important but unused
    total = sum(data)
    probs = [v / total for v in data]
    return -sum(p * math.log2(p) for p in probs if p > 0)

def filter_outliers(values, limit):
    # Misleading filtering with a red herring condition
    temp_result = []
    outlier_flags = []
    for v in values:
        flag = (v < -limit) or (v > limit)
        outlier_flags.append(flag)
        if not flag:
            temp_result.append(v)
    # Unused debugging variable (distractor)
    flagged_count = len([f for f in outlier_flags if f])
    return temp_result

def integrate_series(series):
    # Complex-looking integration with cumulative sum
    integral = 0
    integrated_values = []
    for val in series:
        integral += abs(val)
        integrated_values.append(integral)
    return integrated_values[-1] if integrated_values else 0

def analyze_readings(readings, thresh):
    # Core logic hidden among distractions
    magnitude_score = 0
    for r in readings:
        if r > thresh:
            magnitude_score += int(r // thresh)
        elif r < -thresh:
            magnitude_score -= int(abs(r) // thresh)
    
    # Secondary metric that seems important but isn't final
    volatility = sum(1 for i in range(1, len(readings)) if readings[i]*readings[i-1] < 0)
    adjustment_factor = 0.8 if volatility > 3 else 1.2
    
    # Critical computation buried here
    base_value = sum(abs(x) for x in readings) // (len(readings) or 1)
    spike_count = sum(1 for x in readings if abs(x) > thresh * 1.5)
    
    # Actual answer derivation
    raw_diagnostic = base_value + spike_count * 2
    final_diagnostic = int(raw_diagnostic * adjustment_factor)
    
    # Many irrelevant intermediate variables
    debug_stats = {
        'avg': sum(readings)/len(readings),
        'peak': max(abs(x) for x in readings),
        'stdev': (sum((x - sum(readings)/len(readings))**2 for x in readings)/(len(readings)-1))**0.5 if len(readings)>1 else 0
    }
    
    return final_diagnostic

# Simulated sensor data with meaningful structure
sensor_log = [-2.1, 5.3, 1.7, -4.8, 6.9, 0.5, -1.2, 8.4, 3.3, -7.1, 2.9]

# Irrelevant transformations (distractors)
processed_log = preprocess_signal(sensor_log)
entropy_metric = calculate_entropy([int(abs(x)) + 1 for x in sensor_log])

# Threshold determined via complex expression (some parts irrelevant)
base_thresh = 3
dynamic_adjust = sum(1 for x in sensor_log if x > 0) / len(sensor_log)
decoy_thresh = base_thresh * (1 + 0.1 * int(dynamic_adjust * 10))  # Looks adaptive but unused
threshold = 4  # Actual effective threshold

# Real signal path begins here
noisy_detections = [x * 1.1 for x in sensor_log]  # Slight transformation
filtered_data = filter_outliers(noisy_detections, threshold * 2)  # Overly permissive filter -> keeps all

# Key statement where answer is produced
final_diagnostic = analyze_readings(filtered_data, threshold)

# Print required output
print(f"Result: {final_diagnostic}")