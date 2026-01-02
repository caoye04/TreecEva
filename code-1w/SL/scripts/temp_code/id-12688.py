import math

# Simulated sensor data processing with performance evaluation
raw_readings = [0.85, 0.92, 0.78, 0.96, 0.88]
timestamps = [1634567890, 1634567895, 1634567900, 1634567905, 1634567910]

def normalize(value, min_val=0.5, max_val=1.0):
    return (value - min_val) / (max_val - min_val)

def moving_average(data, window=3):
    smoothed = []
    for i in range(len(data)):
        if i < window - 1:
            smoothed.append(data[i])
        else:
            window_avg = sum(data[i - window + 1:i + 1]) / window
            smoothed.append(window_avg)
    return smoothed

# Irrelevant transformation - red herring
transformed = [math.sin(x * math.pi) for x in raw_readings]
decoys = {f"dummy_{i}": transformed[i] * 100 for i in range(len(transformed))}

# Actual preprocessing
filtered = [x for x in raw_readings if x >= 0.75]
normalized = [normalize(x) for x in filtered]
smoothed_data = moving_average(normalized, 2)

# Weight configuration (misleading alternate weights included)
weights = {
    'precision': 0.4,
    'stability': 0.3,
    'responsiveness': 0.2,
    'redundancy': 0.1,  # unused weight - distractor
    'fallback_mode': 0.0  # dead weight - decoy
}

# False metric calculations - dead paths
legacy_metric = sum([x**2 for x in normalized]) / len(normalized)
placeholder_value = math.log(legacy_metric + 1)
dummy_tracker = {'count': 0, 'total': 0.0}

# Auxiliary function that looks important but isn't used in final path
def calculate_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

def assess_stability(readings):
    diffs = [abs(readings[i] - readings[i-1]) for i in range(1, len(readings))]
    return 1 - sum(diffs) / len(diffs)

# Complex dictionary-based metric processor
metric_data = {
    'base_values': tuple(round(x, 3) for x in smoothed_data),
    'size': len(smoothed_data),
    'meta': {
        'source': 'sensor_array',
        'version': '2.1',
        'calibration': 0.987
    }
}

# Decoy structure - looks like it should be used
aux_data = {
    'readings': raw_readings.copy(),
    'flags': [False] * len(raw_readings),
    'checksum': sum(int(x * 100) for x in raw_readings)
}

# Core evaluation logic buried among distractions
def evaluate_performance(metrics, weight_map):
    values = metrics['base_values']
    n = metrics['size']
    
    # Simulated multi-factor scoring
    precision_score = sum(values) / n
    stability_score = assess_stability(list(values))
    
    # Responsiveness based on last value growth pattern
    if n > 1:
        growth_rate = (values[-1] - values[0]) / values[0]
        responsiveness_score = math.exp(-abs(0.1 - growth_rate))
    else:
        responsiveness_score = 0.5
    
    # Final weighted combination (ignoring decoy weights)
    w_p = weight_map['precision']
    w_s = weight_map['stability']
    w_r = weight_map['responsiveness']
    
    total_weight = w_p + w_s + w_r  # Note: not using all defined weights
    
    composite = (
        w_p * precision_score + 
        w_s * stability_score + 
        w_r * responsiveness_score
    ) / total_weight
    
    # Final nonlinear calibration
    calibrated = 100 * (1 - math.exp(-2 * composite))
    
    # Dead code branch - misleading
    if calibrated > 95:
        dummy_tracker['count'] += 1  # never accessed later
    
    return round(calibrated, 4)

# Execution point of interest
final_score = evaluate_performance(metric_data, weights)

# Irrelevant post-processing
summary_tuple = ('final', 'score', final_score)
log_entry = f"Result processed at {timestamps[-1]}: {final_score:.2f}%"

# Output required format
print(f"Target result: {final_score}")