from collections import defaultdict
import math

# Simulate sensor data aggregation and performance scoring in an autonomous drone system
def collect_diagnostics():
    # Real data: flight stability metrics
    return [0.88, 0.91, 0.85, 0.93, 0.87]

def analyze_redundancy(layers):
    # Irrelevant helper: calculates redundant processing paths (not used in final score)
    redundancy_score = 0
    for i in range(layers):
        for j in range(i + 1, layers):
            redundancy_score += (i * j) % 5
    return redundancy_score

def preprocess_metrics(raw):
    # Normalize and filter relevant metrics
    filtered = [x for x in raw if x > 0.8]
    mean_val = sum(filtered) / len(filtered) if filtered else 0
    return [math.sqrt(x * mean_val) for x in filtered]

def calculate_robustness(metrics):
    # Compute variance-based robustness score
    mean_metric = sum(metrics) / len(metrics)
    variance = sum((x - mean_metric) ** 2 for x in metrics) / len(metrics)
    return 1.0 / (1.0 + variance)

def generate_synthetic_features(base):
    # Distractor function: generates unused synthetic features
    synth = defaultdict(float)
    for i, val in enumerate(base):
        synth[f'feat_{i}'] = val ** 2 + 0.1 * i
    return dict(synth)

def evaluate_outlier_impact(data):
    # Dead code path — never called
    z_scores = [(x - sum(data)/len(data)) / (sum((x - sum(data)/len(data))**2 for x in data)/len(data))**0.5 for x in data]
    return sum(1 for z in z_scores if abs(z) > 1.5)

# Main execution flow
raw_readings = collect_diagnostics()
processed_metrics = preprocess_metrics(raw_readings)

# Irrelevant computations (distractors)
processing_layers = 4
redundancy_index = analyze_redundancy(processing_layers)
synthetic_data = generate_synthetic_features(processed_metrics)

# Core weighting logic
metric_weights = {
    'stability': 0.6,
    'consistency': 0.4
}

# Secondary derived values (some irrelevant)
raw_outcomes = {
    'stability': calculate_robustness(processed_metrics),
    'consistency': sum(processed_metrics) / len(processed_metrics),
    'timestamp': 1712345678,
    'version': 'v2.3'
}

# Unused lambda – misleading but syntactically valid
debug_validator = lambda x: all(v > 0.5 for v in x.values())

# Critical computation
final_score = evaluate_performance(metric_weights, raw_outcomes)

# Helper used only here
def evaluate_performance(weights, outcomes):
    score = 0.0
    # Only two keys are relevant; others ignored
    for key in weights:
        if key in outcomes:
            score += weights[key] * outcomes[key]
    # Apply non-linear sensitivity boost
    boosted_score = 100 * (1 - math.exp(-score))
    
    # Extra distracting calculation (no effect)
    temp_adjustment = 0
    for k in outcomes:
        if isinstance(outcomes[k], float) and k.startswith('extra'):
            temp_adjustment += outcomes[k]
    
    return int(boosted_score)  # Final answer as integer

print(f"Result: {final_score}")