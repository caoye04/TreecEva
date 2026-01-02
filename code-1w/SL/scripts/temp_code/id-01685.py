from collections import defaultdict
import math

# Simulate system performance metrics over time
telemetry_data = [
    {'cpu': 75, 'memory': 80, 'latency_ms': 45, 'requests': 230},
    {'cpu': 60, 'memory': 65, 'latency_ms': 30, 'requests': 190},
    {'cpu': 90, 'memory': 85, 'latency_ms': 120, 'requests': 250},
    {'cpu': 45, 'memory': 50, 'latency_ms': 20, 'requests': 180}
]

# Irrelevant baseline for distraction
baseline_thresholds = defaultdict(lambda: 50)
baseline_thresholds['latency_ms'] = 35
baseline_thresholds['requests'] = 200

# Extract and transform metrics
metrics = defaultdict(float)
total_entries = len(telemetry_data)
dummy_accumulator = 0

for entry in telemetry_data:
    dummy_accumulator += entry['cpu'] * 0.01  # Distractor computation
    for k in ['cpu', 'memory', 'latency_ms', 'requests']:
        metrics[k] += entry[k] / total_entries

# Normalize latency (inverse score: lower latency = higher score)
metrics['latency_norm'] = 100 * (50 / (metrics['latency_ms'] + 1e-5))

# Artificial penalty factor based on memory fluctuations (semi-relevant)
memory_vals = [d['memory'] for d in telemetry_data]
memory_variance = sum((v - sum(memory_vals)/len(memory_vals))**2 for v in memory_vals) / len(memory_vals)
fluctuation_penalty = max(0, memory_variance / 10 - 2)

# Weight assignment with red herring weights
weights = {
    'cpu': 0.2,
    'memory': 0.2,
    'latency_norm': 0.3,
    'requests': 0.25,
    'placeholder': 0.05  # Unused weight — misleading
}

# Fake aggregation to simulate complexity
temp_aggr = lambda w: sum(w.values()) * 0.95  # Distractor function
scaling_factor = temp_aggr(weights)  # Not actually used later

# Evaluate composite performance score
def evaluate_performance(m, w):
    score = 0.0
    relevance_map = {
        'cpu': 1, 'memory': 1, 'latency_norm': 1, 'requests': 1, 'placeholder': 0
    }
    
    # Additional internal distraction
    debug_info = []
    for key in m:
        if key == 'latency_ms':
            continue  # Already normalized
        norm_key = 'latency_norm' if key == 'latency_ms' else key
        weight = w.get(norm_key, 0)
        contribution = m.get(norm_key, 0) * weight
        debug_info.append(contribution)  # Collected but unused
    
    # Actual scoring logic
    score += m['cpu'] * w['cpu']
    score += m['memory'] * w['memory']
    score += m['latency_norm'] * w['latency_norm']
    score += m['requests'] * w['requests']
    
    # Apply fluctuation penalty from outer scope
    score -= fluctuation_penalty * 5
    
    # Final adjustment based on hidden rule: cap at 85 if avg CPU > 70
    if m['cpu'] > 70:
        score = min(score, 85)
    
    return round(score, 4)

# Execute main logic
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Result: {final_score}")