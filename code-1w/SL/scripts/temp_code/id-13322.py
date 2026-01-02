from collections import defaultdict

# Simulate user activity logs with action types and counts
def process_user_actions(log_entries):
    action_count = defaultdict(int)
    for entry in log_entries:
        action_type = entry.split('_')[0]
        action_count[action_type] += 1

    bonus = 0
    if action_count['click'] > 3:
        bonus += 10
    if action_count['scroll'] >= 2:
        bonus += 5

    total_interactions = sum(action_count.values())
    base_score = total_interactions * 2
    result = base_score + bonus
    return result

# Irrelevant helper (minimal distraction)
def validate_timestamp(ts):
    return isinstance(ts, str) and len(ts) == 8

# Data setup
data_log = ['click_button', 'scroll_page', 'click_link', 'scroll_footer', 'click_menu', 'keypress_enter']
rules_config = {"threshold": 3, "penalty": 0}  # Not fully used (slight interference)

# Core computation
def calculate_score(log, config):
    score = process_user_actions(log)
    threshold = config["threshold"]
    if score > threshold * 15:
        score -= config["penalty"]  # No effect, but adds slight logic branch
    return score

result = calculate_score(data_log, rules_config)
print(f"Result: {result}")