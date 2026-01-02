from collections import defaultdict

# Simulate system event logging with priority tagging
def analyze_events(event_stream, min_priority):
    priority_count = defaultdict(int)
    temp_magnitude = 0
    total_entries = 0

    for event in event_stream:
        code = event['code']
        level = event['level']
        priority_count[level] += 1
        total_entries += 1
        
        # Irrelevant magnitude accumulation (distractor)
        temp_magnitude += len(code) * level

    # Misleading intermediate calculation
    avg_code_length = temp_magnitude / total_entries if total_entries else 0
    high_priority = priority_count.get('critical', 0) + priority_count.get('high', 0)

    # This function is never used (dead code - distractor)
    def normalize_value(x):
        return (x ** 0.5) if x > 0 else 0

    return high_priority, avg_code_length

# Evaluate data processing performance with scoring logic
def evaluate_performance(logs, thresh):
    score = 0
    penalty = 0
    event_categories = defaultdict(list)
    cumulative_weight = 0  # Unused accumulator (distractor)

    # Categorize logs by type (semi-relevant grouping)
    for entry in logs:
        event_categories[entry['type']].append(entry['value'])

    # Real scoring logic based on threshold crossing
    for values in event_categories.values():
        above_threshold = [v for v in values if v > thresh]
        count = len(above_threshold)
        
        if count > 3:
            score += 15
        elif count > 1:
            score += 8
        else:
            penalty += 5
    
    # Apply penalty (actual impact on result)
    final = score - penalty
    
    # Red herring computation (no effect)
    for k in event_categories:
        cumulative_weight += len(k) * 0.3

    return final

# Main execution
if __name__ == '__main__':
    # Sample system data stream
    data_log = [
        {'type': 'sensor_a', 'value': 23},
        {'type': 'sensor_b', 'value': 45},
        {'type': 'sensor_a', 'value': 67},
        {'type': 'sensor_c', 'value': 12},
        {'type': 'sensor_b', 'value': 89},
        {'type': 'sensor_a', 'value': 55},
        {'type': 'sensor_c', 'value': 78},
        {'type': 'sensor_b', 'value': 33},
        {'type': 'sensor_a', 'value': 91}
    ]

    config_threshold = 40

    # Analyze events (result not used - distraction)
    high_count, average_length = analyze_events([
        {'code': 'ERR01', 'level': 1},
        {'code': 'CRIT3', 'level': 5},
        {'code': 'WARN2', 'level': 3},
        {'code': 'CRIT5', 'level': 5},
        {'code': 'INFO1', 'level': 1}
    ], min_priority=3)

    # Key statement determining final answer
    final_score = evaluate_performance(data_log, config_threshold)
    
    # Print result as required
    print(f"Target result: {final_score}")