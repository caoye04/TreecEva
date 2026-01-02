from collections import defaultdict
import math

# Simulated system telemetry data
telemetry_logs = [
    {'cpu': 78, 'mem': 65, 'disk': 40, 'net_in': 230, 'net_out': 190},
    {'cpu': 85, 'mem': 70, 'disk': 45, 'net_in': 240, 'net_out': 200},
    {'cpu': 90, 'mem': 75, 'disk': 55, 'net_in': 250, 'net_out': 210},
    {'cpu': 88, 'mem': 73, 'disk': 50, 'net_in': 245, 'net_out': 205}
]

# Irrelevant baseline thresholds (distractor)
baseline_thresholds = defaultdict(lambda: 50)
baseline_thresholds['cpu'] = 80
baseline_thresholds['mem'] = 70
baseline_thresholds['disk'] = 60

# Weight configuration for performance scoring (critical)
weights = {
    'efficiency': 0.4,
    'throughput': 0.35,
    'stability': 0.25
}

# Auxiliary mapping (partially used, partial red herring)
sensor_map = {'c': 'cpu', 'm': 'mem', 'd': 'disk'}

# Historical averages (unused - dead code path)
historical_avg = {}
for key in telemetry_logs[0].keys():
    historical_avg[key] = sum(log[key] for log in telemetry_logs) / len(telemetry_logs)

# Derived metrics computation
def compute_derived_metrics(logs):
    derived = []
    for i, log in enumerate(logs):
        # Efficiency score: inverse relationship with CPU and memory
        efficiency = 100 - ((log['cpu'] * 0.6) + (log['mem'] * 0.4))

        # Throughput score: based on network activity
        throughput = (log['net_in'] + log['net_out']) / 5

        # Stability penalty: rapid disk growth indicator
        stability = 100
        if i > 0 and logs[i-1]['disk'] > 0:
            growth_rate = (log['disk'] - logs[i-1]['disk']) / logs[i-1]['disk']
            if growth_rate > 0.1:
                stability -= 10

        derived.append({
            'efficiency': round(efficiency, 2),
            'throughput': round(throughput, 2),
            'stability': stability
        })
    return derived

# Misleading auxiliary function (never called)
def calculate_anomaly_score(data):
    anomaly = 0
    for entry in data:
        if entry['cpu'] > 95:
            anomaly += 3
        elif entry['mem'] > 85:
            anomaly += 2
    return anomaly

# Another decoy: bit manipulation for 'data integrity' (unused)
integrity_mask = 0b101010
scrambled = [hash(str(log)) ^ integrity_mask for log in telemetry_logs]

# Core evaluation logic
def evaluate_performance(metrics, weights):
    total_score = 0.0
    raw_components = defaultdict(float)

    # Aggregate across all time points
    for m in metrics:
        raw_components['efficiency'] += m['efficiency']
        raw_components['throughput'] += m['throughput']
        raw_components['stability'] += m['stability']

    # Normalize
    n = len(metrics)
    for k in raw_components:
        raw_components[k] /= n

    # Apply weights
    weighted_efficiency = raw_components['efficiency'] * weights['efficiency']
    weighted_throughput = raw_components['throughput'] * weights['throughput']
    weighted_stability = raw_components['stability'] * weights['stability']

    total_score = weighted_efficiency + weighted_throughput + weighted_stability

    # Final nonlinear adjustment: sigmoid-like compression
    final = 50 + (total_score / 2) * (1 / (1 + math.exp(-0.1 * total_score)))
    return round(final, 4)

# Secondary transformation chain (irrelevant)
lambda_transform = lambda x: x ** 0.5 if x > 0 else 0
transformed_signals = {k: lambda_transform(v) for k, v in historical_avg.items()}

# Actual processing pipeline
metrics = compute_derived_metrics(telemetry_logs)
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Result: {final_score}")