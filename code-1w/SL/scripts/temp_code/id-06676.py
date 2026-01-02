from itertools import combinations

def analyze_workload(levels):
    total_load = sum([l * (i + 1) for i, l in enumerate(levels)])
    avg_load = total_load / len(levels) if levels else 0
    peak_load = max(levels) if levels else 0
    normalized_peak = peak_load / (avg_load or 1)
    return avg_load, normalized_peak

def simulate_latency(batches):
    delay_sequence = [b % 7 + 2 for b in batches]
    total_delay = sum(delay_sequence)
    effective_rate = len(batches) / (total_delay or 1)
    return total_delay, effective_rate

def calculate_efficiency(log_entries):
    raw_metrics = [entry['value'] for entry in log_entries]
    filtered_metrics = [v for v in raw_metrics if v > 0]
    
    # Irrelevant transformation: reversing but not using
    reversed_copy = filtered_metrics[::-1]
    temp_sum = sum(filtered_metrics)
    
    # Distractor: complex unused combinatorics
    unused_pairs = list(combinations(filtered_metrics, 2))
    pair_count = len(unused_pairs)
    dummy_score = sum((a - b) ** 2 for a, b in unused_pairs) if pair_count > 0 else 0
    
    # Actual computation path
    base_effort = sum(m for m in filtered_metrics if m % 2 == 1)
    bonus_factor = len([m for m in filtered_metrics if m > 50])
    adjustment = 0.1 * bonus_factor if base_effort > 0 else 0
    
    # Simulate auxiliary processes (some used, some not)
    aux_data = [base_effort + i * 10 for i in range(3)]
    _, derived_scale = analyze_workload(aux_data)
    
    # Red herring: latency simulation with partial use
    delay_val, rate = simulate_latency([int(base_effort % 100)])
    scaling_hint = rate * 1.5 if rate > 0.5 else 1.0  # Not actually used
    
    # Final efficiency formula
    raw_efficiency = base_effort * (1 + adjustment)
    normalized_efficiency = raw_efficiency / (derived_scale or 1)
    
    # Key assignment point
    efficiency_ratio = normalized_efficiency
    
    # Unused debug print
    # print(f'Debug: {dummy_score}, {pair_count}')
    
    return efficiency_ratio

def main():
    performance_log = [
        {'timestamp': 1001, 'value': 45},
        {'timestamp': 1002, 'value': 67},
        {'timestamp': 1003, 'value': 23},
        {'timestamp': 1004, 'value': 89},
        {'timestamp': 1005, 'value': 12},
        {'timestamp': 1006, 'value': 55}
    ]
    
    # Spurious preprocessing
    sorted_log = sorted(performance_log, key=lambda x: x['timestamp'])
    valid_log = [entry for entry in sorted_log if entry['value'] >= 10]
    
    # Critical execution point
    efficiency_ratio = calculate_efficiency(valid_log)
    
    # Output result
    print(f"Result: {efficiency_ratio}")

if __name__ == "__main__":
    main()