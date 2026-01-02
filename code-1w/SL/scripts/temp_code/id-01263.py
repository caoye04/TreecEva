from collections import Counter, defaultdict

# Simulate user interaction logs with various actions
def generate_interaction_logs():
    logs = [
        'click:start', 'hover:menu', 'click:save', 'keypress:ctrl+s',
        'click:export', 'click:save', 'hover:settings', 'click:start',
        'keypress:enter', 'click:export', 'click:save', 'hover:menu'
    ]
    return logs

# Process raw logs into action categories
def parse_logs(logs):
    parsed = []
    action_stats = defaultdict(int)
    
    for log in logs:
        if ':' in log:
            action_type, detail = log.split(':', 1)
            parsed.append((action_type, detail))
            action_stats[action_type] += 1
    
    # Irrelevant computation: counts per detail (not used later)
    detail_counter = Counter([detail for _, detail in parsed])
    total_hovers = action_stats.get('hover', 0)  # Used in distraction
    
    # Misleading metric
    redundancy_score = sum(v ** 0.5 for v in detail_counter.values() if v > 1)
    
    return parsed, action_stats

# Analyze frequency of critical actions
def extract_feedback_patterns(parsed_actions):
    critical_actions = ['save', 'export', 'start']
    feedback_sequence = []
    
    for action_type, detail in parsed_actions:
        if action_type == 'click' and detail in critical_actions:
            feedback_sequence.append(detail)
    
    # Count occurrences of each feedback event
    feedback_counter = Counter(feedback_sequence)
    
    # Distractor variables
    total_interactions = len(parsed_actions)
    unique_actions = len(set(feedback_sequence))
    
    # Extra logic that doesn't affect final result
    if unique_actions >= 3:
        bonus_multiplier = 1.5
    else:
        bonus_multiplier = 1.0
    
    return feedback_counter, total_interactions

# Core evaluation logic
def evaluate_performance(counter, threshold):
    base_value = 0
    adjustment = 2
    
    # Only 'save' and 'export' contribute to score
    if 'save' in counter:
        base_value += counter['save'] * 3
    if 'export' in counter:
        base_value += counter['export'] * 5
    
    # Apply threshold penalty if save count is below threshold
    save_count = counter.get('save', 0)
    if save_count < threshold:
        base_value -= 4
    
    # Dead code branch - never executed due to fixed data
    if 'print' in counter:
        base_value += 10
    
    return base_value

# Main execution flow
if __name__ == '__main__':
    # Step 1: Generate logs
    raw_logs = generate_interaction_logs()
    
    # Step 2: Parse logs
    parsed_actions, stats = parse_logs(raw_logs)
    
    # Step 3: Extract feedback pattern
    feedback_counter, total_events = extract_feedback_patterns(parsed_actions)
    
    # Step 4: Set threshold based on statistical artifact (fixed due to deterministic input)
    max_threshold = max(stats.get('click', 1), stats.get('keypress', 1)) // 2
    
    # Step 5: Compute auxiliary metric (distractor)
    avg_length = sum(len(log) for log in raw_logs) / len(raw_logs)
    
    # Step 6: Evaluate performance - key statement
    final_score = evaluate_performance(feedback_counter, max_threshold)
    
    # Step 7: Print result
    print(f"Result: {final_score}")