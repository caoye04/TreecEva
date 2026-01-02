from collections import Counter, defaultdict

# Simulate user interaction logs with redundant metadata
timestamps = [100, 105, 110, 115, 120, 125, 130]
actions = ['click', 'scroll', 'hover', 'click', 'click', 'scroll', 'click']
duration_log = {ts: (ts + 5) for ts in timestamps}

# Track action frequency - relevant
action_counter = Counter(actions)

click_count = action_counter['click']
scroll_count = action_counter['scroll']
hover_count = action_counter['hover']

# Dummy transformation - misleading
transformed_metrics = [x * 1.5 for x in action_counter.values()]
scaled_clicks = click_count * 0.8  # Not used later

# Feedback loop simulation with nested logic
event_feedback = []
for i, act in enumerate(actions):
    if act == 'click' and i % 2 == 0:
        event_feedback.append('positive')
    elif act == 'scroll':
        event_feedback.append('neutral')
    else:
        event_feedback.append('negative')

feedback_counter = Counter(event_feedback)

# Irrelevant histogram creation - distractor code
dist_map = defaultdict(int)
for val in range(1, 6):
    dist_map[val] = val ** 2 + 2 * val - 1

# Red herring calculation
phantom_score = sum(dist_map[k] for k in [2, 4]) / 3  # Unused

# Conditional adjustment based on feedback ratios
positive_fb = feedback_counter['positive']
negative_fb = feedback_counter['negative']

if positive_fb > negative_fb:
    adjustment_factor = 1.2
elif positive_fb == negative_fb:
    adjustment_factor = 1.0
else:
    adjustment_factor = 0.8

# Auxiliary tracking - partially relevant
status_tracker = {}
status_tracker['last_action'] = actions[-1]
status_tracker['total_events'] = len(actions)
status_tracker['peak_load'] = max(duration_log.values())  # Distractor

# Core evaluation logic
def evaluate_performance(feedback_hist, adj_factor):
    base_score = feedback_hist['positive'] * 10
    penalty = feedback_hist['negative'] * 3
    net_score = base_score - penalty
    adjusted_score = net_score * adj_factor
    
    # Extra computation to increase nesting
    if adjusted_score > 50:
        bonus = 5
        if adj_factor >= 1.2:
            bonus += 3
        adjusted_score += bonus
    return int(adjusted_score)

# Critical execution point
final_score = evaluate_performance(feedback_counter, adjustment_factor)

# Output result as required
print(f"Target result: {final_score}")