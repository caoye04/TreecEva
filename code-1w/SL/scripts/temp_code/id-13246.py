from collections import defaultdict

# Simulate system performance metrics
def analyze_metrics(data_log):
    counts = defaultdict(int)
    efficiency = 0.0
    temp_buffer = []
    total_entries = len(data_log)
    
    for entry in data_log:
        category = entry['type']
        status = entry['status']
        counts[category] += 1
        
        if status == 'success':
            efficiency += 1.5
        elif status == 'warning':
            efficiency += 0.5
        else:
            efficiency -= 0.3

        temp_buffer.append(category)

    # Irrelevant aggregation
    unique_categories = set(temp_buffer)
    avg_per_category = total_entries / max(len(unique_categories), 1)
    spike_count = sum(1 for x in temp_buffer if 'critical' in x)

    efficiency /= total_entries
    return efficiency, counts

def calculate_baseline(reference_data):
    # Distractor function: computes unused baseline stats
    base_mean = sum(reference_data) / len(reference_data)
    variance = sum((x - base_mean) ** 2 for x in reference_data) / len(reference_data)
    adjusted_scores = [x * 0.95 for x in reference_data if x > base_mean]
    return base_mean, variance, len(adjusted_scores)

def evaluate_performance(efficiency, error_list):
    penalty = 0
    severity_map = {'minor': 1, 'major': 3, 'critical': 7}
    
    for err in error_list:
        level = err['level']
        timestamp = err['ts']  # Unused field (distraction)
        penalty += severity_map.get(level, 0)
    
    raw_score = efficiency * 100
    final_score = int(raw_score - penalty)
    
    # Additional irrelevant transformation
    normalized = (final_score + 100) / 200
    capped = min(max(final_score, 0), 100)
    
    return final_score  # This is the actual output used

# Main execution
if __name__ == '__main__':
    log_data = [
        {'type': 'io_read', 'status': 'success'},
        {'type': 'compute_task', 'status': 'success'},
        {'type': 'network_fetch', 'status': 'warning'},
        {'type': 'io_read', 'status': 'success'},
        {'type': 'compute_task', 'status': 'error'},
        {'type': 'cache_lookup', 'status': 'success'},
        {'type': 'network_fetch', 'status': 'success'},
        {'type': 'compute_task', 'status': 'warning'}
    ]
    
    reference_values = [85, 90, 88, 92, 87]
    
    # Call analysis (relevant)
    efficiency, category_breakdown = analyze_metrics(log_data)
    
    # Call baseline (completely irrelevant - distractor)
    baseline, var, count_above = calculate_baseline(reference_values)
    
    # Error logs (semi-relevant preprocessing)
    errors = [
        {'level': 'minor', 'ts': 1680000001},
        {'level': 'major', 'ts': 1680000005},
        {'level': 'minor', 'ts': 1680000010},
        {'level': 'critical', 'ts': 1680000015}
    ]
    
    # Key statement
    final_score = evaluate_performance(efficiency, errors)
    
    # Print result as required
    print(f"Result: {final_score}")