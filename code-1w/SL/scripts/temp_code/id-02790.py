def calculate_final_score(log, weight_map):
    base_score = 0
    penalty_adjustment = 0
    bonus_tracker = []
    temp_result_cache = {}

    for entry_id, metrics in log.items():
        raw_value = metrics['base'] * weight_map['base_factor']
        if metrics['anomaly_flag']:
            penalty_adjustment += metrics['severity'] * weight_map['penalty_scale']
        else:
            if metrics['efficiency'] > 0.8:
                bonus_tracker.append(metrics['efficiency'] * weight_map['bonus_factor'])

        intermediate_key = f"{entry_id}_{metrics['category']}"
        temp_result_cache[intermediate_key] = raw_value  # stored but not used later

    # Irrelevant aggregation (dead-end computation)
    cumulative_sum = sum(temp_result_cache.values())
    average_irrelevant = cumulative_sum / len(temp_result_cache) if temp_result_cache else 0

    base_score = sum(log[k]['base'] for k in log) * weight_map['base_factor']
    total_bonus = sum(bonus_tracker)

    # Misleading complex expression that doesn't affect logic
    debug_offset = len(bonus_tracker) > 0 and average_irrelevant > 50
    if debug_offset:
        base_score += 0.001  # negligible effect, distractor

    final_score = base_score - penalty_adjustment + total_bonus
    return final_score

# Simulated input data
weights = {
    'base_factor': 3,
    'penalty_scale': 2,
    'bonus_factor': 5
}

data_log = {
    'node_01': {'base': 10, 'anomaly_flag': False, 'severity': 5, 'efficiency': 0.85, 'category': 'A'},
    'node_02': {'base': 15, 'anomaly_flag': True, 'severity': 3, 'efficiency': 0.7, 'category': 'B'},
    'node_03': {'base': 12, 'anomaly_flag': False, 'severity': 1, 'efficiency': 0.92, 'category': 'A'},
    'node_04': {'base': 8,  'anomaly_flag': False, 'severity': 0, 'efficiency': 0.65, 'category': 'C'},
    'node_05': {'base': 20, 'anomaly_flag': True, 'severity': 4, 'efficiency': 0.88, 'category': 'B'}
}

# Execution point of interest
final_score = calculate_final_score(data_log, weights)
print(f"Result: {final_score}")