from collections import defaultdict

# Simulate system performance evaluation with multiple metrics
def analyze_response_times(logs):
    stats = defaultdict(int)
    temp_aggregates = []
    outlier_count = 0

    for entry in logs:
        duration = entry['time']
        category = entry['type']
        stats[category] += duration
        
        if duration > 500:
            outlier_count += 1
            
        temp_aggregates.append(duration ** 0.5)  # Irrelevant transformation

    avg_duration = sum(temp_aggregates) / len(temp_aggregates) if temp_aggregates else 0
    return dict(stats), avg_duration, outlier_count

def compute_efficiency_ratio(raw_values):
    total_ops = 0
    total_energy = 0
    energy_footprint = []

    for val in raw_values:
        op_weight = (val % 7) + 1
        energy_cost = (val // 10) * 0.3
        total_ops += op_weight
        total_energy += energy_cost
        energy_footprint.append(energy_cost * op_weight)

    # Dead code branch — never used later
    if total_energy == 0:
        efficiency = 0
    else:
        efficiency = total_ops / total_energy if total_energy != 0 else 0

    return efficiency, energy_footprint

def evaluate_performance(metrics, threshold):
    score = 0
    penalty_adjustment = 0
    bonus_tracker = []

    for key, value in metrics.items():
        if 'api' in key:
            if value > threshold * 1.5:
                penalty_adjustment += 5
        elif 'db' in key:
            if value < threshold:
                score += 10
            else:
                score += 3
        elif 'cache' in key:
            score += 7
            bonus_tracker.append(value)

    final_bonus = sum(bonus_tracker) / len(bonus_tracker) if bonus_tracker else 0
    score -= penalty_adjustment
    score += int(final_bonus // 10)

    return score

# Main execution
if __name__ == '__main__':
    # Real input data
    system_logs = [
        {'time': 120, 'type': 'api_call'},
        {'time': 80, 'type': 'db_query'},
        {'time': 60, 'type': 'cache_fetch'},
        {'time': 40, 'type': 'api_call'},
        {'time': 90, 'type': 'db_query'},
        {'time': 70, 'type': 'cache_fetch'},
        {'time': 520, 'type': 'api_call'},
        {'time': 55, 'type': 'db_query'}
    ]

    metric_summary, mean_sqrt, outliers = analyze_response_times(system_logs)

    # Unused derived values (distractors)
    operation_data = [10, 21, 32, 43, 54]
    efficiency, footprint = compute_efficiency_ratio(operation_data)
    normalized_efficiency = round(efficiency * 100, 2)

    base_threshold = 85
    final_score = evaluate_performance(metric_summary, base_threshold)
    
    # Additional irrelevant computation
    cumulative_load = sum(v for v in metric_summary.values())
    load_factor = cumulative_load / (base_threshold * 2) if cumulative_load > 0 else 0

    print(f"Result: {final_score}")