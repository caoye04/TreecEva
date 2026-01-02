from itertools import combinations

# Simulate sensor data calibration and performance scoring
def collect_diagnostics():
    return [0.88, 0.91, 0.76, 0.94, 0.85]

def generate_baseline(count):
    return [0.8 for _ in range(count)]

def compute_deviation(sensor, base):
    return abs(sensor - base)

def assess_stability(readings):
    trend = [readings[i] <= readings[i+1] for i in range(len(readings)-1)]
    return sum(trend) / len(trend)

def filter_outliers(data, threshold=0.75):
    mean_val = sum(data) / len(data)
    return [x for x in data if abs(x - mean_val) / mean_val < (1 - threshold)]

def evaluate_performance(metrics, weights):
    weighted_sum = sum(m * w for m, w in zip(metrics, weights))
    adjustment = 0.05 if metrics[2] > 0.8 else -0.03
    return int((weighted_sum + adjustment) * 100)

# Main execution flow
data_stream = collect_diagnostics()
baseline = generate_baseline(len(data_stream))

# Irrelevant combination analysis (distractor)
possible_pairs = list(combinations(data_stream, 2))
pair_consistency = [abs(a - b) < 0.1 for a, b in possible_pairs]
consistency_rate = sum(pair_consistency) / len(pair_consistency)

# Compute deviations (semi-relevant)
deviations = [compute_deviation(s, b) for s, b in zip(data_stream, baseline)]
avg_deviation = sum(deviations) / len(deviations)

# Stability assessment (partially used later)
stability = assess_stability(data_stream)

# Filtered data for alternative path (dead code path)
filtered_data = filter_outliers(data_stream)
alt_stability = assess_stability(filtered_data) if filtered_data else 0.0

# Weight configuration (misleading manual override)
weights = [0.2, 0.2, 0.3, 0.15, 0.1]
weights = [w * 1.1 for w in weights]  # normalization attempt
norm_factor = sum(weights)
weights = [w / norm_factor for w in weights]  # now properly normalized

# Performance metric construction
metrics = [
    sum(data_stream) / len(data_stream),      # average accuracy
    stability,                                 # trend consistency
    data_stream[2],                          # key sensor (index 2)
    avg_deviation,                           # lower is better
    len(possible_pairs) / 100                # complexity proxy
]

# Introduce lambda-based transformation (irrelevant)
transform = lambda x: x ** 2 + 0.1
transformed_metrics = list(map(transform, metrics))

# Final evaluation using original metrics
final_score = evaluate_performance(metrics, weights)

# Additional distraction: dictionary tracking
status_log = {
    'timestamp': 12345,
    'score_level': final_score,
    'anomaly_count': len([d for d in deviations if d > 0.1]),
    'calibration_needed': False
}

# Output result as required
print(f"Result: {final_score}")