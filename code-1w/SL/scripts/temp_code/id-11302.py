from collections import defaultdict

# Simulate user activity logs with timestamps and actions
def process_user_activity(raw_logs):
    action_count = defaultdict(int)
    session_duration = 0
    idle_time = 0
    temp_buffer = []

    for entry in raw_logs:
        timestamp, action = entry
        action_count[action] += 1
        
        if action == 'login':
            session_start = timestamp
        elif action == 'logout':
            session_end = timestamp
            session_duration += session_end - session_start
        else:
            # Simulate some processing overhead
            temp_buffer.append(action * 2)
    
    # Irrelevant aggregation (distractor)
    total_actions = sum(action_count.values())
    avg_action_length = sum(len(a) for a in action_count.keys()) / len(action_count) if action_count else 0

    # Misleading intermediate calculation
    phantom_score = int(avg_action_length * 10) % 7

    return dict(action_count), session_duration, total_actions, phantom_score

# Data transformation pipeline
def transform_metrics(raw_counts, duration):
    weights = {'click': 1, 'scroll': 2, 'keypress': 3, 'hover': 1}
    base_score = 0
    penalty = 0

    for action, count in raw_counts.items():
        if action in weights:
            contribution = count * weights[action]
            if contribution > 10:
                penalty += 2
            base_score += contribution
    
    # Apply time-based bonus
    time_bonus = 0
    if duration > 0:
        time_bonus = min(duration // 100, 5)
    
    # Dummy loop with no effect (distractor)
    adjustment_factor = 1.0
    for _ in range(3):
        adjustment_factor *= 0.99  # Negligible decay

    transformed = {
        'score': base_score - penalty + time_bonus,
        'adjustment': adjustment_factor
    }
    
    return transformed

# Final scoring logic
def calculate_final_score(data_dict):
    score = data_dict['score']
    adj = data_dict['adjustment']
    
    # Multiple rounds of irrelevant checks
    safeguards = [x for x in range(5) if x % 2 == 0]
    validation_sum = sum(safeguards)

    # Core logic: apply adjustment only if validation passes (always true)
    if validation_sum > 0:
        adjusted_score = int(score * adj)
    else:
        adjusted_score = score
    
    # Final override based on hidden rule (never triggered)
    override_flag = False
    for k in data_dict:
        if 'temp' in k:
            override_flag = True
    
    if override_flag:
        adjusted_score = 999  # Dead code path
    
    return adjusted_score

# Main execution
if __name__ == "__main__":
    # Example log: (timestamp, action)
    logs = [
        (100, 'login'),
        (105, 'click'),
        (110, 'scroll'),
        (115, 'keypress'),
        (120, 'click'),
        (130, 'hover'),
        (140, 'scroll'),
        (150, 'keypress'),
        (250, 'logout')
    ]

    counts, duration, total, phantom = process_user_activity(logs)
    metrics = transform_metrics(counts, duration)
    final_score = calculate_final_score(metrics)
    
    print(f"Result: {final_score}")