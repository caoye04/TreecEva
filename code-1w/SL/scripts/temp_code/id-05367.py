def evaluate_performance(log, thresh):
    # Irrelevant preprocessing: case conversion and string manipulation
    actions = [entry['action'].upper() for entry in log if 'action' in entry]
    durations = [entry['duration'] for entry in log if entry['duration'] > 0]
    
    # Semi-relevant: filtering and counting
    valid_entries = [e for e in log if e['status'] == 'SUCCESS']
    failure_count = len([e for e in log if e['status'] == 'FAILURE'])  # unused later

    # Core logic begins: compute efficiency ratio using dictionary and set operations
    unique_actions = set(actions)
    action_freq = {act: actions.count(act) for act in unique_actions}
    
    total_actions = len(actions)
    distinct_action_types = len(unique_actions)
    
    # Distractor: complex but unused computation
    redundancy_score = sum(f ** 2 for f in action_freq.values()) / (total_actions + 1e-5)
    normalized_diversity = distinct_action_types / (len(action_freq) + 1) if action_freq else 0
    
    # Slicing operation on sorted duration values
    sorted_durations = sorted(durations)
    mid_segment = sorted_durations[len(sorted_durations)//4 : len(sorted_durations)*3//4]
    average_mid_duration = sum(mid_segment) / len(mid_segment) if mid_segment else 0
    
    # Key metric: compliance rate below threshold
    compliant_count = sum(1 for d in durations if d <= thresh)
    compliance_rate = compliant_count / total_actions if total_actions > 0 else 0
    
    # Secondary metric: success-to-failure ratio (only successes used)
    success_count = len(valid_entries)
    stability_index = success_count / (failure_count + 1)  # avoids division by zero
    
    # Final score calculation – only compliance_rate and stability_index are actually used
    base_score = compliance_rate * 100
    adjustment = stability_index * 10
    final_component = base_score + adjustment
    
    # Dead code path – never executed due to logic
    if len(unique_actions) > 100:
        final_component *= 1.1
    
    return int(final_component)

# Main execution
metrics_log = [
    {'action': 'read', 'duration': 12, 'status': 'SUCCESS'},
    {'action': 'write', 'duration': 8, 'status': 'SUCCESS'},
    {'action': 'delete', 'duration': 15, 'status': 'FAILURE'},
    {'action': 'read', 'duration': 5, 'status': 'SUCCESS'},
    {'action': 'write', 'duration': 20, 'status': 'SUCCESS'},
    {'action': 'read', 'duration': 7, 'status': 'SUCCESS'},
    {'action': 'execute', 'duration': 3, 'status': 'FAILURE'},
    {'action': 'read', 'duration': 9, 'status': 'SUCCESS'},
    {'action': 'write', 'duration': 11, 'status': 'SUCCESS'},
    {'action': 'create', 'duration': 6, 'status': 'SUCCESS'}
]
threshold = 10

final_score = evaluate_performance(metrics_log, threshold)
print(f"Result: {final_score}")