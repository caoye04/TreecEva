def analyze_efficiency(data, threshold=0.75):
    """Irrelevant helper function for distraction."""
    return [x * 2 for x in data if x > threshold]

# Distractor variables (unused later)
baseline = [0.5, 0.6, 0.9]
dummy_weights = (0.1, 0.1, 0.1)
scaling_factor = 1.5

# Core data structures with mixed relevance
metrics = {
    'latency': 0.3,
    'throughput': 0.85,
    'accuracy': 0.92,
    'energy': 0.68
}

weights = {
    'latency': -0.2,  # Negative weight: lower latency preferred
    'throughput': 0.4,
    'accuracy': 0.35,
    'energy': 0.15
}

# Dead code path - never executed
if False:
    for k in metrics:
        metrics[k] *= 1.1

# Misleading intermediate calculation
temp_result = sum(metrics.values()) * 0.1  # Looks important, unused

# Conditional expression with lambda abstraction (required features)
evaluate_component = lambda val, w: (val ** 2) * w if val >= 0.7 else val * w * 0.5

# Unused but plausible transformation
distorted_metrics = tuple(round(metrics[key] ** 1.1, 3) for key in metrics)

# Complex nested logic with distractors
buffer_data = []
for key in ['latency', 'throughput', 'accuracy']:
    raw_val = metrics[key]
    wt = weights[key]
    adjusted = evaluate_component(raw_val, wt)
    buffer_data.append(adjusted)

# Additional red herring: bit manipulation on float (converted to int hash)
bit_fiddle = (hash(str(metrics['energy'])) & 0xFFFF) >> 4

# Real computation chain starts here (nested logic)
def compute_stability_index(x):
    return abs(x - 0.7) < 0.15

def evaluate_performance(met, wts):
    score = 0.0
    stability_flags = {}
    
    for name in wts:
        stability_flags[name] = compute_stability_index(met[name])
        contribution = evaluate_component(met[name], wts[name])
        
        # Extra nesting level with conditional expression
        score += contribution if not (name == 'latency' and met[name] > 0.5) else contribution * 0.8
    
    # Final adjustment based on energy efficiency
    if met['energy'] < 0.7:
        penalty = (0.7 - met['energy']) * 0.2
        score -= penalty
    
    # Hidden dependency: only throughput above 0.8 gives bonus
    if met['throughput'] > 0.8:
        bonus = 0.05
        score += bonus
        
    return round(score, 6)

# Simulate prior unused processing (distraction)
sorted_keys = sorted(weights.keys(), key=lambda k: abs(weights[k]), reverse=True)

# Actual execution point
final_score = evaluate_performance(metrics, weights)

# Output requirement
print(f"Result: {final_score}")