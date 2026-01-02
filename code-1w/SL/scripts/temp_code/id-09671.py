def evaluate_performance(convergence_set, activity_log):
    # Core logic variables
    base_points = 0
    penalty = 0
    convergence_count = len(convergence_set)

    # Irrelevant tracking (distractor)
    debug_trace = []
    temp_buffer = [0] * 10
    for i in range(len(temp_buffer) - 1):
        temp_buffer[i + 1] = temp_buffer[i] + 2

    # Semi-relevant preprocessing
    unique_actions = set(activity_log)
    action_frequency = {}
    for action in activity_log:
        action_frequency[action] = action_frequency.get(action, 0) + 1

    # Red herring computation: computes average but unused
    total_actions = len(activity_log)
    avg_frequency = total_actions / len(unique_actions) if unique_actions else 0

    # Actual scoring logic
    for action in unique_actions:
        if action in convergence_set:
            base_points += 7
        else:
            penalty += 3

    # Bonus rule: if any action occurs exactly 4 times, add bonus
    frequency_values = list(action_frequency.values())
    if 4 in frequency_values:
        base_points += 10

    # Misleading complex structure (dead end)
    snapshot = {
        'momentum': sum(frequency_values[:3]) if len(frequency_values) > 2 else 0,
        'stability': len(unique_actions) - len(convergence_set)
    }
    snapshot['adjustment'] = snapshot['momentum'] // (snapshot['stability'] + 1)

    # Final score calculation
    final_score = base_points - penalty

    return final_score

# Setup data
convergence_set = {1, 3, 5, 7, 9}
activity_log = [1, 1, 3, 3, 3, 5, 7, 9, 9, 9, 9, 2, 4, 6]

# Key statement
final_score = evaluate_performance(convergence_set, activity_log)
print(f"Target result: {final_score}")