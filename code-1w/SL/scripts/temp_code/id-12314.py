def analyze_performance(metrics, thresholds):
    # Irrelevant transformation (distractor)
    normalized = [round((m - min(metrics)) / (max(metrics) - min(metrics)) * 100) for m in metrics]
    
    # Semi-relevant pre-processing
    above_threshold = [i for i, m in enumerate(metrics) if m > thresholds[i % len(thresholds)]]
    
    # Core logic: count how many consecutive pairs pass threshold check
    streak = 0
    max_streak = 0
    for i in range(len(metrics) - 1):
        if metrics[i] >= thresholds[i % len(thresholds)] and metrics[i+1] >= thresholds[(i+1) % len(thresholds)]:
            streak += 1
        else:
            max_streak = max(max_streak, streak)
            streak = 0
    max_streak = max(max_streak, streak)
    
    # Distractor: unused complex structure
    metadata_map = {idx: {'value': val, 'index_square': idx**2, 'flagged': val < 50} for idx, val in enumerate(metrics)}
    
    return max_streak


def calculate_adjusted_score(data_log, config, mode='advanced'):
    base_score = sum([x // 2 for x in data_log if x % 2 == 0])
    
    # Misleading intermediate calculation (not used in final result)
    temp_offset = 0
    for i, val in enumerate(data_log):
        if val > config['limit']:
            temp_offset += (val - config['limit']) * (i + 1)
    
    penalty = 0
    if mode == 'advanced':
        # Real logic path
        critical_indices = [i for i, x in enumerate(data_log) if x > config['critical_floor']]
        if len(critical_indices) > 0:
            gaps = [critical_indices[i+1] - critical_indices[i] for i in range(len(critical_indices)-1)]
            if gaps:
                avg_gap = sum(gaps) / len(gaps)
                penalty = int(avg_gap // 2)
    
    # Another distractor: set operation that computes but isn't used
    unique_pairs = set(zip(data_log, [x*2 for x in data_log]))
    pair_analysis = len(unique_pairs) > len(data_log) * 0.7
    
    adjusted = base_score - penalty
    return adjusted

# Main execution block
if __name__ == '__main__':
    # Input data
    system_metrics = [45, 80, 92, 77, 61, 98, 85, 72]
    alert_levels = [50, 70, 75, 60]
    config_params = {
        'limit': 90,
        'critical_floor': 90,
        'bonus_factor': 1.5
    }
    
    # Trigger analysis (irrelevant to final answer but looks important)
    performance_peak = analyze_performance(system_metrics, alert_levels)
    
    # Key statement
    final_score = calculate_adjusted_score(system_metrics, config_params, mode='advanced')
    
    # Output result
    print(f"Result: {final_score}")