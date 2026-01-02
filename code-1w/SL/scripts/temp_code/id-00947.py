import math

# Simulated system metrics from a distributed computing environment
def collect_metrics():
    raw_data = {
        'cpu_load': [0.65, 0.82, 0.73, 0.91, 0.67],
        'memory_usage_gb': [12.4, 14.1, 13.8, 15.2, 11.9],
        'network_latency_ms': [23, 45, 31, 29, 37],
        'disk_iops': [1200, 980, 1340, 1150, 1020],
        'temperature_c': [67, 72, 69, 75, 68]
    }

    # Irrelevant transformation (distractor)
    processed = {k: [round(v * 1.05, 2) for v in values] for k, values in raw_data.items()}

    # Decoy function that's never called
    def analyze_anomaly(data):
        return sum(1 for x in data if x > 1.0)  # nonsense logic

    # Actual metric aggregation
    metrics = {
        'throughput': sum(raw_data['disk_iops']) / len(raw_data['disk_iops']),
        'avg_latency': sum(raw_data['network_latency_ms']) / len(raw_data['network_latency_ms']),
        'stability': 100 - (max(raw_data['cpu_load']) - min(raw_data['cpu_load'])) * 50,
        'efficiency': (sum(raw_data['memory_usage_gb']) / 5) * 0.1,
        'thermal_safe': int(all(t < 75 for t in raw_data['temperature_c']))
    }

    # Dead code path - never executed
    if False:
        dummy = [math.sin(x) for x in range(100)]
        metrics['fake_metric'] = sum(dummy) // 10

    return metrics

# Weighting schema for evaluation (some weights are misleading)
def get_weights():
    base_weights = {
        'throughput': 0.30,
        'avg_latency': -0.15,  # negative weight (penalty)
        'stability': 0.25,
        'efficiency': 0.10,
        'redundant_factor': 0.20,  # unused in calculation
        'thermal_safe': 0.20
    }

    # Distractor: complex lambda-based normalization (not used)
    normalize = lambda w: {k: v / sum(w.values()) for k, v in w.items()}
    adjusted = {k: v * 1.1 for k, v in base_weights.items() if k != 'redundant_factor'}

    # Return only relevant weights
    return {k: v for k, v in base_weights.items() if k in ['throughput', 'avg_latency', 'stability', 'efficiency', 'thermal_safe']}

# Core evaluation logic
def evaluate_performance(metrics, weights):
    # Initialize with irrelevant intermediate values
    temp_results = {}
    debug_logs = []

    # Real computation begins
    score_components = {}

    # Throughput: higher is better
    score_components['throughput'] = metrics['throughput'] * weights['throughput']

    # Latency: lower is better, so invert and apply negative weight intentionally
    latency_score = (100 / (metrics['avg_latency'] + 1)) * abs(weights['avg_latency'])
    score_components['latency_adj'] = -latency_score  # double-negative logic path

    # Stability: already in percentage form
    score_components['stability'] = metrics['stability'] * weights['stability']

    # Efficiency: penalize high memory usage
    efficiency_score = (15 - metrics['efficiency']) * weights['efficiency']
    score_components['efficiency'] = efficiency_score

    # Thermal safety: binary bonus
    thermal_bonus = 10 if metrics['thermal_safe'] else -5
    score_components['thermal_safe'] = weights['thermal_safe'] * thermal_bonus

    # Hidden correction factor (critical but non-obvious)
    correction_map = {k: 1.05 if 'adj' in k else 1.0 for k in score_components}
    corrected_scores = {k: v * correction_map[k] for k, v in score_components.items()}

    # Final aggregation
    total = sum(corrected_scores.values())

    # Distractor: unused alternative scoring method
    alt_score = 0
    for i, (k, v) in enumerate(score_components.items()):
        if i % 2 == 0:
            alt_score += v * 0.9
        else:
            alt_score += v * 1.1

    # Unused debugging artifact
    debug_snapshot = [
        f"{k}: {v:.3f}" for k, v in corrected_scores.items()
    ]

    return round(total, 4)

# Irrelevant helper class (red herring)
class PerformanceLogger:
    def __init__(self):
        self.entries = []
    def log(self, msg):
        self.entries.append(msg)
    def export(self):
        return '\n'.join(self.entries)

# Unused cryptographic hash (misleading security context)
def generate_proof_of_work(data):
    h = 0
    for c in str(data):
        h = (h * 31 + ord(c)) % (10**9 + 7)
    return h

# Main execution flow
if __name__ == "__main__":
    # Collect system metrics
    metrics = collect_metrics()
    
    # Retrieve weighting schema
    weights = get_weights()
    
    # Evaluate overall performance
    final_score = evaluate_performance(metrics, weights)
    
    # Print result as required
    print(f"Target result: {final_score}")