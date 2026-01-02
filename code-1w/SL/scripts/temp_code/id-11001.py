from itertools import combinations

# Simulate system performance metrics under varying load conditions
def collect_metrics(base_load, stress_factor):
    raw_data = {}
    temp_cache = []
    for i in range(1, 6):
        load = base_load * (1 + stress_factor * i / 10)
        throughput = (100 - load) * 0.85 if load < 100 else 10
        latency = 50 + (load ** 1.2) // 2
        errors = max(0, int((load - 90) * 0.5)) if load > 90 else 0
        
        # Store intermediate readings (some irrelevant)
        raw_data[f'phase_{i}'] = {
            't': throughput,
            'l': latency,
            'e': errors,
            'c': throughput > 70 and latency < 100
        }
        temp_cache.append(latency * 0.1)  # unused later
    
    return raw_data

# Analyze metric correlations (distractor function with partial relevance)
def find_anomalies(data_dict):
    anomaly_pairs = []
    keys = list(data_dict.keys())
    for a, b in combinations(keys, 2):
        diff_t = abs(data_dict[a]['t'] - data_dict[b]['t'])
        diff_e = abs(data_dict[a]['e'] - data_dict[b]['e'])
        if diff_t > 30 and diff_e > 2:
            anomaly_pairs.append((a, b))
    return len(anomaly_pairs) > 2

# Core evaluation logic with weighted scoring
def evaluate_performance(metrics, weights):
    score_components = {}
    phase_count = 0
    total_stability = 0.0
    
    for key, values in metrics.items():
        phase_count += 1
        base_score = values['t'] * weights['throughput']
        penalty = values['e'] * weights['error_penalty']
        latency_factor = max(0, 1 - values['l'] / 200)
        
        # Conditional expression for adaptive scoring
        adjusted = base_score * latency_factor if values['c'] else base_score * 0.5
        score_components[key] = adjusted - penalty
        
        # Track cumulative stability (semi-relevant)
        total_stability += 1 if values['c'] else 0
    
    # Compute final weighted result
    aggregate = sum(score_components.values())
    consistency_bonus = (total_stability / phase_count) * 10 if total_stability > 3 else 0
    
    # Final computation
    final_score = aggregate + consistency_bonus
    
    # Dead code branch (irrelevant but plausible)
    if False:
        debug_trace = {k: round(v, 2) for k, v in score_components.items()}
        print(f'Debug: {debug_trace}')
    
    return int(round(final_score))

# Main execution
base_load = 60
stress_factor = 0.8
weights = {
    'throughput': 1.2,
    'error_penalty': 3.0
}

# Collect system metrics
data_metrics = collect_metrics(base_load, stress_factor)

# Detect anomalies (used to distract, not directly impacting score)
detected_anomalies = find_anomalies(data_metrics)
temp_diagnostic = [v['l'] for k, v in data_metrics.items() if 'phase_3' not in k]  # unused list

# Evaluate final performance score
final_score = evaluate_performance(data_metrics, weights)

# Output result
print(f"Result: {final_score}")