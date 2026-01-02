import math

# Simulated sensor data processing with diagnostic analysis
def collect_readings():
    raw_values = [i * 0.5 + math.sin(i) for i in range(15)]
    offset = 2.1
    calibrated = [v + offset for v in raw_values]
    return calibrated

# Irrelevant helper - distractor
def smooth_signal(data):
    smoothed = [data[0]]
    for i in range(1, len(data)-1):
        smoothed.append((data[i-1] + data[i] + data[i+1]) / 3)
    smoothed.append(data[-1])
    return smoothed

# Data transformation pipeline
def transform_readings(raw):
    log_scaled = [math.log(v + 10) for v in raw if v > -10]
    squared_filtered = [x**2 for x in log_scaled if x > 1.5]
    normalized = [val / max(squared_filtered) for val in squared_filtered]
    return normalized

# Threshold logic with red herring conditions
def evaluate_stability(metric, mode='strict'):
    thresholds = {'strict': 0.75, 'relaxed': 0.6}
    temp_reference = 0.45  # unused distractor
    calibration_curve = lambda x: x**2 - 0.1*x  # decoy function
    return metric > thresholds[mode]

# Core analysis function
threshold_map = {
    'low': 0.25,
    'medium': 0.5,
    'high': 0.8
}

# Misleading pre-analysis (dead path)
def legacy_diagnostic(data):
    if len(data) > 10:
        return sum([d * 0.1 for d in data]) % 7
    return -1

# Unused recursive red herring
def recursive_distractor(n):
    if n <= 1:
        return 1
    return n * recursive_distractor(n - 2) + 0.05

# Main pattern analyzer with critical logic
pattern_cache = {}  # distraction: not actually used

def analyze_pattern(data, limits):
    count_high = sum(1 for x in data if x > limits['high'])
    count_mid = sum(1 for x in data if limits['medium'] < x <= limits['high'])
    
    # Decoy aggregation
    fake_aggregate = 0
    for k in limits:
        fake_aggregate += len(k) * limits[k]
    
    # Real computation buried in noise
    weight_a = count_high * 3.1
    weight_b = count_mid * 1.2
    composite_score = weight_a + weight_b
    
    # Additional irrelevant mapping
    status_labels = {0: 'idle', 1: 'active', 2: 'critical'}
    fallback_check = [x for x in data if x < 0.1]  # never happens
    
    # Actual output calculation
    adjustment_factor = math.sqrt(2 * len(data))
    final_score = composite_score / adjustment_factor
    
    # Critical assignment point
    final_diagnostic = int(final_score * 100) / 100.0  # rounded to 2 decimal places
    return final_diagnostic

# Execution flow with distractions
if __name__ == "__main__":
    # Unused historical baseline
    baseline_snapshot = [0.1, 0.3, 0.4]
    snapshot_hash = sum(b * (i+1) for i, b in enumerate(baseline_snapshot))

    readings = collect_readings()
    processed = smooth_signal(readings)  # looks important, but not used later
    transformed_data = transform_readings(readings)  # actual input

    # Fake branching - misleading control flow
    if len(transformed_data) > 5:
        probe_test = legacy_diagnostic(transformed_data)
        verification_flag = True
    else:
        verification_flag = False

    # Real execution path
    final_diagnostic = analyze_pattern(transformed_data, threshold_map)
    
    # Distractor print statements removed
    Result: final_diagnostic