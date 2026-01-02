import math

# Simulated sensor array data (irrelevant in part)
sensor_offsets = [0.1, -0.3, 0.4, 0.05, -0.15]
base_frequency = 440
calibration_lookup = {i: round(math.sin(i * 0.1) * 100, 2) for i in range(10)}

# Core data structures for analysis
trend_series = [12, 15, 22, 28, 31, 35, 38, 40, 39, 37, 36, 38, 42, 45, 47]
outlier_flags = [x < 10 or x > 50 for x in trend_series]  # unused distractor

# Mapping thresholds by category (used later)
threshold_map = {
    'low_risk': (0, 25),
    'moderate': (25, 40),
    'high_alert': (40, float('inf'))
}

# Auxiliary transformation (partially irrelevant)
def apply_digital_filter(signal):
    filtered = []
    for i in range(len(signal)):
        window = signal[max(0, i-2):i+1]
        filtered.append(sum(window) / len(window))
    return [round(x, 1) for x in filtered]

# Unused recursive function (red herring)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Data categorization with side effects
risk_categories = []
def classify_trend(value, boundaries):
    global risk_categories
    if value < boundaries['moderate'][0]:
        cat = 'low_risk'
    elif value < boundaries['high_alert'][0]:
        cat = 'moderate'
    else:
        cat = 'high_alert'
    risk_categories.append(cat)
    return cat

# Complex aggregation with list comprehensions and filtering
def aggregate_metrics(data, thresholds):
    # Apply filter (result not directly used in final logic)
    smoothed = apply_digital_filter(data)
    
    # Key computation path
    categorized = [classify_trend(x, thresholds) for x in data]
    
    # Count transitions between states
    transitions = 0
    for i in range(1, len(categorized)):
        if categorized[i] != categorized[i-1]:
            transitions += 1
    
    # Compute volatility score (distractor)
    volatility = sum(1 for a, b in zip(data, data[1:]) if abs(b - a) > 3)
    
    # Hidden key logic: count how many values fall into 'high_alert'
    high_risk_count = len([v for v in data if v >= thresholds['high_alert'][0]])
    
    # Secondary metric (unused)
    average_jump = sum(abs(b-a) for a,b in zip(data[1:], data[:-1])) / (len(data)-1) if len(data) > 1 else 0
    
    # Decoy calculation with bit manipulation (misleading)
    decoy_flag = (volatility << 2) ^ int(average_jump)
    
    # Final diagnostic is based on transition count multiplied by high-risk occurrences
    if high_risk_count > 0:
        result = transitions * high_risk_count * 100
    else:
        result = len(data) // 2
    
    return int(result)

# Extraneous pre-processing (distractor block)
processed_series = []
for val in trend_series:
    adjusted = val
    if val % 2 == 0:
        adjusted = int(val * 1.1)
    else:
        adjusted = int(val * 0.9)
    processed_series.append(adjusted)

# Irrelevant string processing (dead code path)
status_tags = ['OK', 'WARN', 'ALERT']
label_map = {i: tag for i, tag in enumerate(status_tags)}
joined_labels = '-'.join([label_map[i % 3] for i in range(len(trend_series))])
segmented = joined_labels.split('WARN')
reconstructed = ' '.join([part.strip('-') for part in segmented])

# Critical execution point
trend_data = trend_series.copy()
final_diagnostic = aggregate_metrics(trend_data, threshold_map)
print(f"Result: {final_diagnostic}")