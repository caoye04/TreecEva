from collections import defaultdict
import math

# Simulate sensor data processing with performance evaluation
def collect_diagnostics(data_stream):
    diagnostics = defaultdict(int)
    temp_log = []
    cumulative = 0

    for val in data_stream:
        if val > 25:
            diagnostics['over_threshold'] += 1
            temp_log.append(math.sqrt(val))
        elif val < 0:
            diagnostics['negative_spikes'] += 1
            temp_log.append(-val * 0.1)
        else:
            diagnostics['normal_range'] += 1

        cumulative += abs(val)

    # Irrelevant transformation
    transformed = list(map(lambda x: round(x, 2), temp_log))
    avg_magnitude = cumulative / len(data_stream) if data_stream else 0

    return diagnostics, avg_magnitude, transformed


def compute_efficiency_index(values):
    peak = max(values) if values else 1
    base = sum(1 for v in values if v > 10) / len(values) if values else 0
    penalty = sum([v for v in values if v < 0])
    efficiency = (base * 100) - abs(penalty)
    return round(efficiency, 3)


def evaluate_performance(metrics, weights):
    score = 0.0
    components = defaultdict(float)

    # Relevant scoring logic
    components['stability'] = metrics.get('normal_range', 0) * weights[0]
    components['alert_penalty'] = metrics.get('over_threshold', 0) * -weights[1]
    components['anomaly_cost'] = metrics.get('negative_spikes', 0) * -weights[2]

    for k, v in components.items():
        score += v

    # Distractor computation - looks relevant but unused
    auxiliary_score = 0
    for i, w in enumerate(weights):
        auxiliary_score += math.log(abs(w) + 1) * (i + 1)

    final_adjustment = math.sin(len(metrics) * weights[0])
    score += final_adjustment  # Only this part uses a trigonometric function meaningfully

    return int(round(score))

# Main execution
if __name__ == '__main__':
    raw_data = [12, -5, 30, 18, 26, -3, 14, 8, 35, 22, 40, 6, -8, 19, 27]
    
    # Step 1: Collect diagnostic metrics
    diag_metrics, average_level, logs = collect_diagnostics(raw_data)
    
    # Step 2: Compute auxiliary efficiency (not used in final score, red herring)
    efficiency = compute_efficiency_index(raw_data)
    
    # Step 3: Prepare weighting scheme
    weights_config = [1.8, 0.9, 1.2]  # Stability weight, alert penalty, anomaly cost
    
    # Step 4: Evaluate overall performance - KEY STATEMENT
    final_score = evaluate_performance(diag_metrics, weights_config)
    
    # Print result for extraction
    print(f"Result: {final_score}")