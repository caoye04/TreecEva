def evaluate_performance(log, base):
    cumulative = 0
    penalty = 0
    bonus_tracker = []
    
    for entry in log.values():
        if 'response_time' in entry:
            cumulative += entry['response_time']
        
        if 'errors' in entry:
            if entry['errors'] > base['max_errors']:
                penalty += 2
        
        if 'throughput' in entry:
            bonus_tracker.append(entry['throughput'])
    
    avg_throughput = sum(bonus_tracker) / len(bonus_tracker) if bonus_tracker else 0
    throughput_bonus = int(avg_throughput // 10)

    # Distractor: irrelevant computation on metadata
    meta_sum = 0
    for k in log.keys():
        meta_sum += len(k)
    dummy_offset = meta_sum % 7

    # Another distractor: unused function definition
    def adjust_for_latency(val, factor=1.1):
        return val * factor

    # Unused list accumulation
    temp_history = []
    for i in range(len(log)):
        temp_history.append(i * 2)

    final_score = cumulative - penalty + throughput_bonus
    return final_score

# Baseline configuration
current_baseline = {
    'max_errors': 3,
    'threshold': 0.85,
    'grace_period': 10
}

# Simulated system metrics over time
metrics_log = {
    'node_01': {
        'response_time': 12,
        'throughput': 23,
        'errors': 2
    },
    'node_02': {
        'response_time': 15,
        'throughput': 31,
        'errors': 4
    },
    'node_03': {
        'response_time': 18,
        'throughput': 27,
        'errors': 1
    },
    'node_04': {
        'response_time': 14,
        'throughput': 35,
        'errors': 5
    }
}

# Key execution point
final_score = evaluate_performance(metrics_log, current_baseline)
print(f"Result: {final_score}")