def calculate_final_score(records, importance_weights):
    base_score = 0
    penalty_adjustment = 0
    bonus_tracker = []
    temp_result_cache = {}

    for i, record in enumerate(records):
        if i % 2 == 0:
            raw_value = record['value'] * importance_weights.get(record['type'], 1.0)
            smoothed = int(raw_value // 1.5)  # Distractor: integer division not used later
            temp_result_cache[i] = smoothed

        if record['type'] == 'critical':
            base_score += record['value'] * 3
        elif record['type'] == 'standard':
            base_score += record['value'] * 1.5
        else:
            base_score += record['value'] * 0.8

        # Conditional expression (Python idiom)
        anomaly_flag = 'yes' if record['value'] < 0 else 'no'
        if anomaly_flag == 'yes':
            penalty_adjustment -= 1

        # Bitwise tracking of even/odd indices (semi-relevant)
        parity_mask = i & 1
        if parity_mask == 0:
            bonus_tracker.append(record['value'])

    # Irrelevant aggregation
    avg_bonus = sum(bonus_tracker) / len(bonus_tracker) if bonus_tracker else 0
    max_cached = max(temp_result_cache.values()) if temp_result_cache else 0

    # Core logic hidden among distractions
    adjustment_factor = 1 + (len([b for b in bonus_tracker if b > 10]) * 0.1)
    final_score = int(base_score * adjustment_factor) + penalty_adjustment

    # Unused diagnostic variables
    debug_info = {
        'cached_count': len(temp_result_cache),
        'total_bonus': sum(bonus_tracker),
        'max_raw': max(r['value'] for r in records)
    }

    return final_score

# Input data
input_records = [
    {'type': 'critical', 'value': 25},
    {'type': 'standard', 'value': 12},
    {'type': 'standard', 'value': 18},
    {'type': 'enhancement', 'value': 8},
    {'type': 'critical', 'value': 30},
    {'type': 'standard', 'value': 14}
]

weights = {'critical': 1.2, 'standard': 1.1}

# Execution
final_score = calculate_final_score(input_records, weights)
print(f"Result: {final_score}")