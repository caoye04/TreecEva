def analyze_performance(records):
    base_modifier = 0.85
    temp_adjustment = 0
    cumulative_shift = 0

    for record in records:
        if record['status'] == 'active':
            temp_adjustment += record['weight'] * base_modifier
            if record['flagged']:
                temp_adjustment -= 0.5

    return int(temp_adjustment)


def evaluate_conditions(values):
    result_set = []
    for v in values:
        result_set.append(v ** 2 if v > 0 else abs(v))
    return sum(result_set) // len(result_set) if result_set else 0


def process_outcomes(outcomes, limits):
    score = 0
    penalty_offset = 10
    debug_trace = []

    for entry in outcomes:
        raw_value = entry['value']
        category = entry['type']
        
        # Key logic branch
        if category == 'A':
            contribution = raw_value * 1.2
        elif category == 'B':
            contribution = raw_value * 0.75 if raw_value < limits['B_max'] else raw_value * 0.4
        else:
            contribution = max(raw_value - 3, 0)

        # Conditional expression (Python feature)
        adjustment = contribution * 1.1 if entry.get('boost', False) else contribution * 0.95
        
        score += int(adjustment)
        debug_trace.append(adjustment)  # Distractor: collected but not used

    # Additional irrelevant computation
    outlier_count = 0
    for d in debug_trace:
        if d > 50:
            outlier_count += 1

    final_penalty = penalty_offset - outlier_count
    score -= final_penalty  # Only this line uses final_penalty

    return score

# Main execution block
input_records = [
    {'status': 'active', 'weight': 10, 'flagged': True},
    {'status': 'inactive', 'weight': 5, 'flagged': False},
    {'status': 'active', 'weight': 8, 'flagged': False}
]

numerical_values = [4, -7, 9, 0, -3]

results = [
    {'value': 25, 'type': 'A', 'boost': True},
    {'value': 40, 'type': 'B'},
    {'value': 15, 'type': 'C', 'boost': True},
    {'value': 30, 'type': 'B'}
]

targets = {
    'B_max': 35
}

# Irrelevant function call (distractor)
analyze_performance(input_records)
evaluate_conditions(numerical_values)

# Key statement
final_score = process_outcomes(results, targets)

print(f"Target result: {final_score}")