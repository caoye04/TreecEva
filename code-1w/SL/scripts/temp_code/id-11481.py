from collections import defaultdict

# Simulate system benchmark data with noise and auxiliary metrics
def generate_test_data():
    raw_metrics = [
        (1, {'ops': 85, 'latency': 12, 'power': 45}),
        (2, {'ops': 90, 'latency': 14, 'power': 50}),
        (3, {'ops': 95, 'latency': 11, 'power': 48}),
        (4, {'ops': 88, 'latency': 13, 'power': 46}),
        (5, {'ops': 92, 'latency': 10, 'power': 52})
    ]
    return {k: v for k, v in raw_metrics}

# Auxiliary function to compute secondary diagnostic stats
def analyze_stability(data):
    stability_log = defaultdict(int)
    drift_counter = 0
    for idx, (key, values) in enumerate(data.items()):
        ops = values['ops']
        if idx > 0 and abs(ops - prev_ops) > 3:
            drift_counter += 1
        prev_ops = ops
        # Misleading computation: rarely affects final result
        adjusted_latency = (values['latency'] + 0.5) ** 0.5
        stability_log[f'entry_{key}'] = int(adjusted_latency * 10)
    return drift_counter

# Core performance calculation with embedded distractions
def calculate_performance(raw_data):
    base_weight = 0.6
    latency_factor = 0.3
    power_penalty = 0.1
    
    # Irrelevant aggregation (distractor)
    historical_trends = [0] * len(raw_data)
    temp_offset = 0
    for i in range(len(raw_data)):
        if i % 2 == 0:
            temp_offset += i * 0.05
        historical_trends[i] = round(temp_offset, 2)
    
    # Real computation begins
    total_ops = sum(entry['ops'] for entry in raw_data.values())
    avg_latency = sum(entry['latency'] for entry in raw_data.values()) / len(raw_data)
    avg_power = sum(entry['power'] for entry in raw_data.values()) / len(raw_data)
    
    # Secondary irrelevant list comprehension (distractor)
    efficiency_flags = [1 if entry['ops'] > 90 else 0 for entry in raw_data.values()]
    high_perf_count = sum(efficiency_flags)
    
    # Key distraction: unused bitwise analysis
    bitmask = 0
    for entry in raw_data.values():
        op_val = entry['ops']
        latency_val = entry['latency']
        # XOR pattern that doesn't influence final score
        bitmask ^= (op_val & 255) | (latency_val << 2)
    
    # Actual scoring logic (depends only on averages)
    performance_component = total_ops * base_weight
    latency_component = (100 - avg_latency * 5) * latency_factor
    power_component = (50 - avg_power) * power_penalty
    
    preliminary_score = performance_component + latency_component + power_component
    
    # Final adjustment based on hidden rule: only use floor if drift is low
    drift_count = analyze_stability(raw_data)
    if drift_count < 2:
        final_score = int(preliminary_score)
    else:
        final_score = int(preliminary_score * 0.95)
    
    return final_score

# Main execution flow
benchmark_data = generate_test_data()

# Dead code path (never executed but looks relevant)
def deprecated_normalization(x):
    return [val / max(x) for val in x] if max(x) > 0 else x

# Trigger the actual computation
dummy_list = [x for x in range(5)]
side_metric = sum(dummy_list) * 0.1  # Unused variable

final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")