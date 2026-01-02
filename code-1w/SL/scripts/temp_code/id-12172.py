from collections import Counter

# Simulate user interaction logs with various actions
def collect_feedback(actions):
    feedback = []
    action_count = Counter(actions)
    for act in actions:
        if act == 'like':
            feedback.append(1)
        elif act == 'dislike':
            feedback.append(-1)
        else:
            feedback.append(0)
    return feedback, action_count

# Process system events and extract relevant metrics
def analyze_events(event_log):
    event_stats = {}
    total_events = len(event_log)
    error_count = 0
    warning_count = 0
    for event in event_log:
        if 'error' in event:
            error_count += 1
        elif 'warning' in event:
            warning_count += 1
    event_stats['errors'] = error_count
    event_stats['warnings'] = warning_count
    event_stats['total'] = total_events
    return event_stats

# Core evaluation logic
def compute_baseline(feedback_values):
    raw_total = sum(feedback_values)
    count_valid = len([v for v in feedback_values if v != 0])
    if count_valid == 0:
        return 0.0
    return raw_total / count_valid

# Apply dynamic adjustment based on system health
def calculate_health_penalty(events_data):
    err_penalty = events_data['errors'] * 0.1
    warn_penalty = events_data['warnings'] * 0.05
    return err_penalty + warn_penalty

# Final performance scoring with multiple factors
def evaluate_performance(counter_obj, factor):
    likes = counter_obj.get('like', 0)
    dislikes = counter_obj.get('dislike', 0)
    neutrals = counter_obj.get('neutral', 0)
    total = likes + dislikes + neutrals
    
    # Irrelevant computation: track ratio (not used in final score)
    positive_ratio = likes / total if total > 0 else 0
    negative_ratio = dislikes / total if total > 0 else 0
    
    base = likes - dislikes
    adjusted = base * factor
    
    # Distractor: unused intermediate calculations
    dummy_metric = (positive_ratio ** 2) - (negative_ratio * 0.5)
    shadow_value = adjusted + dummy_metric  # Not used
    
    return int(adjusted + 0.5)  # Final deterministic integer score

# Main execution flow
if __name__ == '__main__':
    user_actions = ['like', 'like', 'dislike', 'neutral', 'like', 'like', 'dislike']
    system_events = ['info: startup', 'warning: disk', 'info: processing', 'error: timeout', 'warning: memory', 'info: done']
    
    # Step 1: Collect and process feedback
    feedback_vals, feedback_counter = collect_feedback(user_actions)
    
    # Step 2: Analyze system event log
    event_analysis = analyze_events(system_events)
    
    # Step 3: Compute baseline metric (not directly used but part of reasoning chain)
    baseline_score = compute_baseline(feedback_vals)
    
    # Step 4: Calculate penalty from system health
    penalty = calculate_health_penalty(event_analysis)
    
    # Step 5: Determine adjustment factor (based on health)
    adjustment_factor = 1.0 - penalty
    if adjustment_factor < 0.5:
        adjustment_factor = 0.5
    
    # Step 6: Evaluate final performance score
    final_score = evaluate_performance(feedback_counter, adjustment_factor)
    
    # Irrelevant block: simulate logging (dead code path)
    debug_mode = False
    if debug_mode:
        print(f'Debug: {feedback_vals}')
        print(f'Stats: {event_analysis}')
    
    # Output result
    print(f"Result: {final_score}")