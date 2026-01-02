def analyze_user_behavior(logs):
    duration_sum = 0
    invalid_entries = 0
    action_counter = {}

    for log in logs:
        action = log.get('action')
        time_spent = log.get('duration', 0)
        
        # Irrelevant string processing (distractor)
        normalized_action = action.strip().lower() if action else ''
        if 'click' in normalized_action:
            duration_sum += time_spent * 0.8  # partial weighting
        elif 'scroll' in normalized_action:
            duration_sum += time_spent * 0.3
        else:
            invalid_entries += 1
            
        # Semi-relevant tracking (not used later)
        if action not in action_counter:
            action_counter[action] = 0
        action_counter[action] += 1

    return duration_sum


def calculate_rating(data):
    base_score = 0
    bonus_factor = 1.0
    penalty = 0
    
    # Dictionary-based threshold mapping (meaningful)
    thresholds = {
        'low': 100,
        'medium': 300,
        'high': 600
    }
    
    # Real computation path
    total_engagement = analyze_user_behavior(data)
    
    # Conditional expression chain with distractors
    adjustment = 5 if total_engagement > thresholds['medium'] else 2
    extra_weight = len([x for x in data if 'session_id' in x])  # counts something irrelevant
    
    base_score += total_engagement / 10
    
    # Multiple nested conditionals (2-3 levels)
    if total_engagement > thresholds['high']:
        bonus_factor = 1.5
        if extra_weight > 4:
            bonus_factor += 0.2
    elif total_engagement > thresholds['low']:
        bonus_factor = 1.1
    else:
        penalty = 10

    # Final calculation with misleading but unused variables
    debug_info = f"Score computed at {base_score:.2f} with factor {bonus_factor}"  # unused
    temp_result = base_score * bonus_factor - penalty  # intermediate
    final_score = int(temp_result + adjustment)  # actual answer
    
    # Dead code path (distractor)
    if False:
        fallback = sum(thresholds.values()) // 100
        final_score = fallback
        
    return final_score

# Simulated dataset (real input)
engagement_data = [
    {'action': 'click_button   ', 'duration': 40, 'session_id': 'A1'},
    {'action': 'scroll_page', 'duration': 120, 'session_id': 'A2'},
    {'action': 'hover_menu', 'duration': 30, 'session_id': 'A3'},
    {'action': 'click_link', 'duration': 60, 'session_id': 'A4'},
    {'action': 'keypress', 'duration': 25, 'session_id': 'A5'},
    {'action': 'click_overlay', 'duration': 35, 'session_id': 'A6'},
    {'action': 'scroll_footer', 'duration': 90, 'session_id': 'A7'}
]

# Execution point of interest
final_score = calculate_rating(engagement_data)
print(f"Result: {final_score}")