import itertools

def analyze_user_behavior(session_data, threshold=3):
    counts = {}
    for event in session_data:
        if event not in counts:
            counts[event] = 0
        counts[event] += 1
    return {k: v for k, v in counts.items() if v >= threshold}

# Irrelevant utility function (dead code path)
def encrypt_string(s):
    return ''.join(chr((ord(c) + 3) % 128) for c in s)

# Misleading data processing chain
temp_results = [x**2 for x in range(15) if x % 3 == 0]
decoys = {f'key_{i}': i * 17 for i in range(10)}
shadow_value = sum(decoys.values()) // 5  # Red herring

# Real data pipeline starts here
raw_logs = 'click,scroll,click,hover,click,scroll,scroll,hover,click'
session_events = raw_logs.split(',')

# Apply filtering based on frequency
filtered_actions = analyze_user_behavior(session_events, threshold=2)

# Augment with time-series weights (simulated)
timing_weights = {event: len(event) * 1.5 for event in filtered_actions}
weighted_metrics = {
    k: v * timing_weights[k] for k, v in filtered_actions.items()
}

# Simulate configuration overlay
benchmark_config = {
    'scaling_factor': 2.1,
    'penalty_rate': 0.95,
    'activation_threshold': 6.0,
    'legacy_mode': False
}

# Complex conditional transformation
processed_values = []
for key, value in weighted_metrics.items():
    if len(key) > 5:
        processed_values.append(value * benchmark_config['penalty_rate'])
    else:
        processed_values.append(value * benchmark_config['scaling_factor'])

# Decoy list comprehension with no downstream use
dummy_aggregation = [
    x * y for x, y in itertools.product([1, 2], [10, 20])
    if x + y > 15
]

# Core logic buried among distractions
metrics_log = {
    'base_score': sum(processed_values),
    'adjustment': len(filtered_actions.keys()) * 1.1,
    'mode_flag': benchmark_config['legacy_mode'] and len(dummy_aggregation) > 0
}

# Critical computation with multiple dependencies
def evaluate_performance(log, config):
    score = log['base_score']
    if log['mode_flag']:
        score *= 0.8
    else:
        score += log['adjustment']
    
    # Additional condition using string logic
    action_keys = ''.join(filtered_actions.keys())
    if action_keys.upper().replace('_', '').isalpha():
        score *= 1.05
    
    # Final scaling
    return int(score * config['scaling_factor']) if score > config['activation_threshold'] else 0

# Execute main evaluation
final_score = evaluate_performance(metrics_log, benchmark_config)

# Print result as required
print(f"Result: {final_score}")