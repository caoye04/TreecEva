from collections import defaultdict
import math

# Simulated sensor data with multiple channels
data_stream = [
    (1, [3.2, 1.8, 4.5, 2.1]),
    (2, [2.9, 1.7, 4.6, 2.3]),
    (3, [3.1, 1.9, 4.4, 2.2]),
    (4, [3.3, 2.0, 4.7, 2.4]),
    (5, [3.0, 1.8, 4.5, 2.1])
]

# Irrelevant metadata - red herring
sensor_calibrations = {
    'gain': 1.02,
    'offset': -0.15,
    'last_updated': '2023-07-15',
    'version': 'v2.3'
}

# Decoy function that looks important but isn't used in main logic
def legacy_process(data):
    return [x * 0.95 + 0.1 for x in data if x > 2.0]

# Real processing begins here
channel_weights = [0.4, 0.3, 0.2, 0.1]
smoothing_factor = 0.85
historical_averages = defaultdict(float)

# Apply weighted smoothing across time series
for timestamp, readings in data_stream:
    weighted_val = sum(readings[i] * channel_weights[i] for i in range(4))
    if timestamp == 1:
        smoothed = weighted_val
    else:
        smoothed = smoothing_factor * weighted_val + (1 - smoothing_factor) * historical_averages[timestamp-1]
    historical_averages[timestamp] = round(smoothed, 4)

# Distractor: unused transformation chain
temp_features = []
for val in historical_averages.values():
    feature = math.log(val + 1) ** 2
    if feature > 2.0:
        temp_features.append(feature * 0.7)

# Another decoy structure
anomaly_flags = set()
counter_analysis = defaultdict(int)
for k, v in historical_averages.items():
    if v > 3.1:
        anomaly_flags.add(k)
    counter_analysis[int(v)] += 1

# Actual signal processing path
processed_data = []
for t in sorted(historical_averages.keys()):
    raw = historical_averages[t]
    # Non-linear compression
    compressed = math.atan(raw - 3.0) * 2
    processed_data.append(round(compressed, 4))

# Threshold configuration map (used later)
threshold_map = {
    'low': -0.5,
    'medium': 0.15,
    'high': 0.8,
    'critical': 1.2  # never reached
}

# Auxiliary function with misleading complexity
def calculate_entropy(values):
    from collections import Counter
    count = Counter([round(v, 2) for v in values])
    total = len(values)
    entropy = 0.0
    for c in count.values():
        p = c / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

# Unused entropy result - distraction
dummy_entropy = calculate_entropy(processed_data)

# Core analysis function
lambda_transform = lambda x, th: 1 if x > th else 0

def analyze_signal(signal_sequence, thresholds):
    # Extract key features
    peak = max(signal_sequence)
    base = min(signal_sequence)
    duration = len(signal_sequence)
    
    # Compute activation patterns across thresholds
    activations = {
        level: sum(lambda_transform(x, th) for x in signal_sequence)
        for level, th in thresholds.items() if level != 'critical'
    }
    
    # Hidden logic: answer depends on specific calculation
    # Correct path: medium threshold activations times peak value
    hidden_impact = activations['medium'] * peak  # This determines final_diagnostic
    
    # Distractor computations
    cumulative_exposure = sum(x for x in signal_sequence if x > thresholds['low'])
    stability_ratio = (duration - activations['high']) / duration if duration > 0 else 0
    
    # Dead code branch - looks like it might affect result
    adjustment = 0
    if stability_ratio > 0.7 and dummy_entropy > 1.0:
        adjustment = 5
    elif len(anomaly_flags) == 0:
        adjustment = -2
    
    # Final diagnostic is NOT affected by adjustment (misleading!)
    result = round(hidden_impact + 1000, 4)  # Base offset to make larger integer
    
    # More irrelevant post-processing
    diagnostics_log = []
    for i, val in enumerate(signal_sequence):
        status = 'NORMAL'
        if val > thresholds['high']:
            status = 'ELEVATED'
        diagnostics_log.append(f'T{i}:{status}')
    
    return int(result)

# Execute main analysis
final_diagnostic = analyze_signal(processed_data, threshold_map)
print(f"Result: {final_diagnostic}")