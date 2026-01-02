import itertools

def analyze_metrics(data, thresholds):
    # Irrelevant aggregation (distractor)
    avg_val = sum(data) / len(data) if data else 0
    peak = max(data) if data else 0
    
    # Semi-relevant transformation
    normalized = [x / (peak or 1) for x in data]
    
    # Conditional filtering based on threshold (actual logic path)
    passed = [n for n in normalized if n >= thresholds.get('min_norm', 0.5)]
    return len(passed), sum(normalized)


def evaluate_performance(logs):
    # Extract time-series signals (real data)
    signal_a = [x['value'] for x in logs if x['sensor'] == 'A']
    signal_b = [x['value'] for x in logs if x['sensor'] == 'B']
    
    # Misleading preprocessing (dead code path)
    temp_offset = 0
    for val in signal_a:
        if val > 100:
            temp_offset += 1  # Unused variable
    
    # Actual computation begins
    combined = list(itertools.chain(signal_a[:5], signal_b[:5]))
    
    # Slice manipulation with conditional logic
    filtered = [x for x in combined if x % 2 == 1]  # Keep odd values
    squared_filtered = [x**2 for x in filtered]
    
    # Distractor: unused intermediate stats
    mean_filtered = sum(squared_filtered) / len(squared_filtered) if squared_filtered else 0
    variance_proxy = sum(abs(x - mean_filtered) for x in squared_filtered)  # Not used
    
    # Key logic step: count how many exceed dynamic threshold
    dynamic_threshold = len(combined) * 2.5
    count_above = len([x for x in squared_filtered if x > dynamic_threshold])
    
    # Final score computed from multiple reasoning steps
    base_score = sum(squared_filtered) // (count_above or 1)
    adjustment = len(filtered) * 3
    final_score = base_score - adjustment
    
    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Simulated sensor log input
log_data = [
    {'sensor': 'A', 'value': 7}, {'sensor': 'B', 'value': 4},
    {'sensor': 'A', 'value': 9}, {'sensor': 'B', 'value': 11},
    {'sensor': 'A', 'value': 6}, {'sensor': 'B', 'value': 13},
    {'sensor': 'A', 'value': 5}, {'sensor': 'B', 'value': 8},
    {'sensor': 'A', 'value': 3}, {'sensor': 'B', 'value': 15}
]

# Threshold config (some keys unused)
config = {
    'min_norm': 0.4,
    'max_gap': 10,
    'debug_mode': False
}

# Execute analysis (triggers distractor computations)
analyze_metrics([12, 15, 7, 22, 18], config)

# Main call that produces the answer
evaluate_performance(log_data)