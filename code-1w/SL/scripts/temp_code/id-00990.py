from collections import defaultdict, Counter
from math import log, ceil

# Simulated sensor data processing with performance evaluation
def analyze_sensor_readings(readings):
    stats = defaultdict(float)
    anomalies = []
    total = 0
    valid_count = 0

    for i, val in enumerate(readings):
        if val < 0:
            anomalies.append(i)
            continue
        if val > 1000:
            # Irrelevant saturation check
            stats['saturation_events'] += 1
            continue
        total += val
        valid_count += 1
        stats['sum_squares'] += val * val

    if valid_count > 0:
        mean = total / valid_count
        stats['mean'] = mean
        stats['variance'] = (stats['sum_squares'] / valid_count) - (mean ** 2)
        stats['signal_strength'] = ceil(mean / (1 + stats['variance'] ** 0.5))

    return dict(stats), anomalies

def calculate_entropy(data):
    # Decoy function – not used in main logic
    freqs = Counter(data)
    entropy = 0
    n = len(data)
    for count in freqs.values():
        p = count / n
        entropy -= p * log(p)
    return entropy

def normalize_vector(vec):
    # Dead code path – never called
    mag = sum(x**2 for x in vec) ** 0.5
    return [x/mag for x in vec] if mag else vec

def evaluate_consistency(trends):
    trend_scores = []
    for i in range(1, len(trends)):
        if trends[i] >= trends[i-1]:
            trend_scores.append(1.1)
        else:
            trend_scores.append(0.9)
    return sum(trend_scores) / len(trend_scores) if trend_scores else 0

# Main pipeline
sensor_data = [105, 200, -5, 340, 450, 1005, 670, 890, -12, 910, 1001, 730]

# Step 1: Basic filtering and statistics
primary_stats, outliers = analyze_sensor_readings(sensor_data)

# Irrelevant transformations
shifted_data = [x >> 2 for x in sensor_data if x > 0]  # Bit manipulation red herring
hex_codes = [hex(x << 1)[:5] for x in shifted_data[:3]]  # Unused string formatting

# Step 2: Simulate multiple metric evaluations
temporal_trends = [primary_stats['mean'] * 0.9, primary_stats['mean'], primary_stats['mean'] * 1.1]
consistency = evaluate_consistency(temporal_trends)

# Dummy weight initialization (some are unused)
weights = {
    'mean': 0.4,
    'variance': -0.1,  # Will be clamped
    'signal_strength': 0.3,
    'consistency': 0.2,
    'entropy': 0.1  # Not available, ignored
}

# Compute actual metrics used in scoring
metrics = defaultdict(float)
metrics['mean'] = primary_stats.get('mean', 0)
metrics['signal_strength'] = primary_stats.get('signal_strength', 0)
metrics['consistency'] = consistency
metrics['variance'] = primary_stats.get('variance', 0)

# Apply clamping and scaling
for k in weights:
    if k not in ['variance', 'entropy']:
        metrics[k] = max(0, min(metrics[k], 100))  # Normalize to 0-100
    elif k == 'variance':
        metrics[k] = abs(metrics[k])  # Make positive

# Weight clamping
for k in weights:
    weights[k] = max(0, weights[k])  # Remove negative weights

# Final aggregation (key statement)
final_score = 0
weight_sum = sum(weights[k] for k in weights)
if weight_sum > 0:
    for k in metrics:
        if k in weights and weights[k] > 0:
            final_score += metrics[k] * weights[k] / weight_sum

# Debugging leftovers (irrelevant prints commented out)
# print(f'Outliers at indices: {outliers}')
# print(f'Shifted data: {shifted_data}')
# print(f'Hex codes: {hex_codes}')

# Correct output format
print(f"Target result: {final_score}")