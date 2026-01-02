def evaluate_performance(logs, conditions):
    # Irrelevant helper: counts transitions but not used in final result
    def count_state_transitions(data):
        transitions = 0
        for i in range(len(data) - 1):
            if data[i] != data[i+1]:
                transitions += 1
        return transitions

    # Distractor: processes unrelated metric
    peak_magnitude = max([abs(x['value']) for x in logs if x['active']], default=0)
    baseline_ref = sum(x['value'] for x in logs[:3]) / 3 if len(logs) > 2 else 0

    # Relevant logic begins: filter logs by active and condition match
    filtered_entries = [x for x in logs if x['active']]
    matched_conditions = [c for c in conditions if c['threshold'] < 50]

    # Bitwise analysis on entry keys (relevant)
    key_flags = [entry['id'] & 7 for entry in filtered_entries]
    flag_distribution = {}
    for f in key_flags:
        flag_distribution[f] = flag_distribution.get(f, 0) + 1

    # Distractor: unused recursive function
    def calculate_depth(n):
        if n <= 1:
            return 1
        return n + calculate_depth(n // 2)

    # Dead code path — never called
    def generate_report():
        return {"entries": len(filtered_entries), "flags": flag_distribution}

    # Character counting distractor
    tag_summary = ''.join([str(entry['id']) for entry in filtered_entries])
    digit_frequency = {d: tag_summary.count(d) for d in '0123456789'}

    # Core logic: compute weighted score based on flag occurrences and thresholds
    base_score = 0
    for cond in matched_conditions:
        weight = cond['weight']
        for entry in filtered_entries:
            if entry['value'] > cond['threshold']:
                base_score += weight * (entry['value'] % 4)

    # Additional relevant computation: adjust by XOR of all flag keys
    adjustment_key = 0
    for k in flag_distribution.keys():
        adjustment_key ^= k

    # Final computation chain
    intermediate = base_score + adjustment_key
    penalty = len([x for x in filtered_entries if x['value'] < 0])
    bonus = len(matched_conditions) * 3

    # Critical execution point
    final_score = intermediate - penalty + bonus

    # Red herring: complex slicing with no impact
    shadow_slice = logs[::2][1:5]
    temp_result = [x['value'] * 2 for x in shadow_slice if x['value'] > baseline_ref]

    return final_score

# Setup input data
import json

daily_logs = [
    {'id': 123, 'value': 15, 'active': True},
    {'id': 124, 'value': -5, 'active': True},
    {'id': 125, 'value': 42, 'active': False},  # inactive
    {'id': 126, 'value': 33, 'active': True},
    {'id': 127, 'value': 8, 'active': True},
    {'id': 128, 'value': 55, 'active': True}
]

target_conditions = [
    {'threshold': 25, 'weight': 4},
    {'threshold': 60, 'weight': 2},  # will be filtered out (threshold >= 50)
    {'threshold': 10, 'weight': 5}
]

# Execution
final_score = evaluate_performance(daily_logs, target_conditions)
print(f"Result: {final_score}")