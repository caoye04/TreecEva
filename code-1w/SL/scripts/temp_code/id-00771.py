from collections import defaultdict, Counter
from itertools import zip_longest

# Simulated sensor readings over time (timestamp -> reading)
sensor_log = [
    (1001, 4.5), (1002, 4.7), (1003, 4.6), (1004, 4.8), (1005, 5.0),
    (1006, 5.2), (1007, 5.3), (1008, 5.5), (1009, 5.4), (1010, 5.6)
]

# Irrelevant backup log (distractor)
backup_status = ['ok', 'ok', 'failed', 'ok']
last_backup = 998

# Noise filter threshold (unused in final calculation)
filter_threshold = 0.15

# Extract trend using sliding window (relevant)
def extract_trend(readings, window=3):
    trend = []
    for i in range(len(readings) - window + 1):
        window_avg = sum(r[1] for r in readings[i:i+window]) / window
        trend.append(round(window_avg, 2))
    return trend

trend_data = extract_trend(sensor_log)

# Decoy function: appears useful but unused
def smooth_signal(signal, factor=0.3):
    smoothed = [signal[0]]
    for val in signal[1:]:
        smoothed.append(round(smoothed[-1] * (1 - factor) + val * factor, 2))
    return smoothed

# Unused intermediate transformation
temp_shifted = [x - 4.0 for x in trend_data if x > 4.5]

# Weight assignment with red herring elements
weight_map = defaultdict(float)
for i in range(len(trend_data)):
    base_weight = 0.5 + (i * 0.1)
    weight_map[i] = min(base_weight, 1.0)

# Include dummy entries that don't align with data length (misleading)
weight_map[15] = 0.9
weight_map[20] = 1.2  # Invalid index

# Correct weights list (aligned with trend_data)
weights = [weight_map[i] for i in range(len(trend_data))]

# Spurious counter for unrelated categories (distractor)
event_counter = Counter(['sensor', 'sensor', 'calibration', 'sensor'])

def aggregate_metrics(trends, wts):
    # Misleading initialization
    baseline = trends[0] if trends else 0
    adjustment = 0.0
    
    # Fake correction pass
    for t in trends:
        if t > 5.0:
            adjustment += 0.05  # Never actually applied
    
    # Real computation hidden among distractions
    weighted_sum = sum(t * w for t, w in zip(trends, wts))
    total_weight = sum(wts)
    
    # Extra logic that looks important but doesn't affect result
    if len(trends) % 2 == 0:
        weighted_sum += 0.0  # No-op
    
    # Actual result calculation
    raw_result = weighted_sum / total_weight if total_weight != 0 else 0
    
    # Final processing step
    diagnostic_score = round(raw_result * 1.05, 4)
    
    # Dead code branch (never reached due to prior logic)
    if False and diagnostic_score < 0:
        diagnostic_score = abs(diagnostic_score)
    
    return diagnostic_score

# Secondary decoy: complex but unused data structure
config_profile = {
    'version': '2.1',
    'filters': [
        {'type': 'moving_avg', 'window': 5},
        {'type': 'outlier', 'threshold': 2.0}
    ],
    'scaling': (1.0, 0.5)
}

# Key statement
final_diagnostic = aggregate_metrics(trend_data, weights)

# Additional irrelevant slicing operation (to satisfy language feature)
recent_trend_slice = trend_data[-3:]  # Not used

# Another decoy using itertools
paired_gaps = list(zip_longest(trend_data, trend_data[1:], fillvalue=0))

dummy_aggregate = [abs(a - b) for a, b in paired_gaps[:3]]

# Output the target result
print(f"Result: {final_diagnostic}")