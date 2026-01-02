from collections import Counter

def calculate_final_score(log_entries):
    # Parse log entries and count action frequencies
    action_counts = Counter()
    for entry in log_entries:
        action = entry.strip().lower().split()[0]  # Extract first word as action
        if action in ['click', 'scroll', 'hover']:
            action_counts[action] += 1

    # Compute weighted engagement score
    weights = {'click': 3, 'scroll': 2, 'hover': 1}
    base_score = sum(weights[action] * count for action, count in action_counts.items())
    
    # Apply bonus for diverse actions (at least one of each)
    unique_actions = len([a for a in ['click', 'scroll', 'hover'] if action_counts[a] > 0])
    diversity_bonus = 5 if unique_actions == 3 else 0
    
    # Normalize by total interactions
    total_interactions = sum(action_counts.values())
    normalized_score = base_score / total_interactions if total_interactions > 0 else 0
    final_score = round(normalized_score + diversity_bonus, 3)
    
    return final_score

# Simulated user interaction logs
raw_logs = [
    'Click on banner',
    'Scroll down page',
    'Hover over menu',
    'CLICK item',
    'Scroll to top',
    'HOVER tooltip',
    'Click submit button'
]

# Process logs and compute final score
processed_logs = [log.upper() for log in raw_logs]  # Preprocessing step (irrelevant case change)
case_adjusted_logs = [log.replace('CLICK', 'click') for log in processed_logs]  # Normalize clicks

# Final computation
final_score = calculate_final_score(case_adjusted_logs)
print(f"Result: {final_score}")