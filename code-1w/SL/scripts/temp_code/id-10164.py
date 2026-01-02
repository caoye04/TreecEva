import math

# Simulated system metrics with irrelevant and relevant components
def get_system_metrics():
    raw_data = [120, 85, 90, 45, 70]
    noise_floor = 5
    adjusted = [x + noise_floor for x in raw_data]
    filtered = [x for x in adjusted if x > 60]  # Only some values matter
    return {
        'latency_ms': adjusted[0],
        'throughput_ips': adjusted[1],
        'accuracy_pct': adjusted[2],
        'energy_joules': adjusted[3],
        'concurrency_level': adjusted[4],
        'dummy_pad_1': sum(adjusted) * 0.1,
        'dummy_pad_2': math.sin(len(adjusted)),
        'temporal_drift': 0.05 * adjusted[0]  # red herring
    }

# Weighting scheme – only some weights affect final result
def get_weight_profile():
    base_weights = {
        'latency_ms': -0.3,      # negative: lower is better
        'throughput_ips': 0.4,
        'accuracy_pct': 0.5,
        'energy_joules': -0.2,
        'concurrency_level': 0.1,
        'legacy_bias_factor': 0.07,  # unused
        'deprecated_offset': 0.03   # unused
    }
    
    # Apply arbitrary normalization (some distraction)
    total = sum(abs(w) for w in base_weights.values())
    normalized = {k: v / total for k, v in base_weights.items()}
    
    # Override with heuristic rules (only a subset used later)
    tuning_multipliers = {k: 1.0 + 0.1 * (hash(k) % 3) for k in normalized}
    tuned = {k: normalized[k] * tuning_multipliers[k] for k in normalized}
    
    # Return both raw and tuned (but only raw matters)
    return base_weights

# Auxiliary function – looks important but isn't directly used in final path
def calculate_efficiency_curve(data):
    curve_points = []
    for i in range(1, len(data)):
        delta = data[i] - data[i-1]
        curve_points.append(delta ** 2 if delta > 0 else 0)
    return [round(p * 0.95, 3) for p in curve_points]

# Core evaluation logic with distractors
def preprocess_metric(value, key):
    if key == 'latency_ms':
        return max(100 - value, 0)  # invert and cap
    elif key == 'accuracy_pct':
        return min(value, 100)
    elif key == 'throughput_ips':
        return value * 0.01
    elif key == 'energy_joules':
        return 100 - min(value, 100)
    elif key == 'concurrency_level':
        return value * 0.5
    else:
        return value * 0.1  # dummy fallback

def evaluate_performance(metrics, weights):
    # Irrelevant transformation block
    shadow_metrics = {k + '_copy': v * 0.99 for k, v in metrics.items()}
    temp_results = []
    for k, v in shadow_metrics.items():
        if 'copy' in k and 'dummy' not in k:
            temp_results.append(v * 1.01)
    
    # Actual computation begins here
    adjusted_metrics = {}
    for key, value in metrics.items():
        adjusted_metrics[key] = preprocess_metric(value, key)
    
    # Introduce lambda-based reducer (required Python feature)
    safe_multiply = lambda a, b: round(a * b, 4) if abs(a * b) > 1e-6 else 0
    
    weighted_sum = 0.0
    applied_weights = []
    
    # Key concept: only first four keys in sorted order contribute
    relevant_keys = sorted(weights.keys())[:4]  # ['accuracy_pct', 'concurrency_level', 'energy_joules', 'latency_ms']
    
    for key in relevant_keys:
        if key in adjusted_metrics:
            contribution = safe_multiply(adjusted_metrics[key], weights[key])
            weighted_sum += contribution
            applied_weights.append((key, contribution))
    
    # Additional distraction: unused composite score
    bonus_term = 0
    if all(metrics[k] > 70 for k in ['throughput_ips', 'accuracy_pct']):
        bonus_term = 5.0 * weights['throughput_ips']
    
    # Final nonlinear scaling (distractor but not affecting much)
    final_raw = weighted_sum + bonus_term
    saturation = math.tanh(final_raw / 10.0) * 100
    
    # BUT: actual answer is just final_raw rounded to nearest int
    final_score = int(round(final_raw))
    
    # Dead code branch (never reached due to above assignment)
    if False:
        fallback = sum(applied_weights[k][1] for k in range(len(applied_weights)))
        final_score = int(fallback * 1.1)
    
    return final_score

# Unused recursive function (red herring)
def trace_dependency_chain(level, acc):
    if level <= 0:
        return acc
    return trace_dependency_chain(level - 1, acc + [(level, hash(str(acc)) % 100)])

# Main execution flow
if __name__ == "__main__":
    # Gather metrics
    metrics = get_system_metrics()
    
    # Retrieve weight schema
    weights = get_weight_profile()
    
    # Compute efficiency curve (unused)
    _ = calculate_efficiency_curve(list(metrics.values())[:5])
    
    # Evaluate performance - critical point
    final_score = evaluate_performance(metrics, weights)
    
    # Print result as required
    print(f"Target result: {final_score}")