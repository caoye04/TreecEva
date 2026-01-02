from collections import defaultdict

# Simulate user interaction logs with various actions
def collect_user_actions():
    actions = [
        'click', 'scroll', 'hover', 'click', 'click',
        'keypress', 'scroll', 'click', 'hover', 'hover',
        'scroll', 'scroll', 'click', 'click', 'keypress'
    ]
    return actions

# Analyze frequency of each action
def analyze_action_frequency(actions):
    freq = defaultdict(int)
    for act in actions:
        freq[act] += 1
    return freq

# Compute baseline engagement metric (irrelevant distractor)
def compute_engagement_index(freq_dict):
    weights = {'click': 3, 'scroll': 1, 'hover': 0.5, 'keypress': 2}
    index = 0
    for act, count in freq_dict.items():
        index += weights.get(act, 0) * count
    return index * 0.75  # Arbitrary scaling (distractor)

# Apply cognitive load adjustment based on repeated patterns (semi-relevant)
def calculate_repetition_penalty(actions):
    penalty = 0
    for i in range(1, len(actions)):
        if actions[i] == actions[i-1]:
            penalty += 0.1
    return max(0.5, 1.0 - penalty)  # Normalize to [0.5, 1.0]

# Core evaluation logic depending on feedback and adjustment
def evaluate_performance(feedback, adj_factor):
    base = sum(feedback.values())
    multiplier = 1.0
    
    # Conditional adjustments based on feedback distribution
    if feedback['click'] > 4:
        multiplier *= 1.2
    if feedback['hover'] >= 3:
        multiplier *= 1.1
    if feedback['keypress'] < 2:
        multiplier *= 0.9
    
    adjusted_base = base * multiplier * adj_factor
    
    # Additional noise that doesn't affect final result
    temp_debug = adjusted_base * 0.01  # Logging placeholder (dead code)
    log_entry = f'DEBUG: Intermediate trace = {temp_debug:.3f}'  # Unused
    
    return int(round(adjusted_base))

# Main execution flow
if __name__ == '__main__':
    # Step 1: Collect raw interaction data
    user_actions = collect_user_actions()
    
    # Step 2: Build action frequency map
    feedback_counter = analyze_action_frequency(user_actions)
    
    # Step 3: Compute irrelevant engagement index (distractor)
    engagement_score = compute_engagement_index(feedback_counter)
    engagement_score += 10  # Fake adjustment to make it seem relevant
    
    # Step 4: Calculate repetition behavior penalty (semi-relevant but not used directly)
    cognitive_load = calculate_repetition_penalty(user_actions)
    
    # Step 5: Derive adjustment factor from cognitive load and hover frequency
    adjustment_factor = cognitive_load * (1.05 if feedback_counter['hover'] >= 3 else 1.0)
    
    # Step 6: Evaluate final performance score (key statement)
    final_score = evaluate_performance(feedback_counter, adjustment_factor)
    
    # Print result as required
    print(f"Target result: {final_score}")