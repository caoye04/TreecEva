from collections import defaultdict

# Simulate user interaction logs with action counts
def count_actions(logs):
    counter = defaultdict(int)
    for action in logs:
        counter[action] += 1
    return counter

# Determine performance score based on bonus eligibility and base scores
def calculate_performance(flags, base_list):
    total_base = sum(base_list)
    bonus_multiplier = 2 if all(flags) else 1
    return total_base * bonus_multiplier

# Main execution
user_logs = ['click', 'scroll', 'click', 'hover', 'click', 'scroll']
action_count = count_actions(user_logs)
click_count = action_count['click']
scroll_count = action_count['scroll']
hover_count = action_count['hover']

base_scores = [click_count * 10, scroll_count * 5]
bonus_flags = [click_count >= 3, hover_count > 0, scroll_count >= 2]

final_score = calculate_performance(bonus_flags, base_scores)
print(f"Result: {final_score}")