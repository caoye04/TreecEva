from collections import Counter

# Simulate user interaction logs with action types
actions = [
    'click', 'scroll', 'click', 'hover', 'click',
    'scroll', 'click', 'hover', 'hover', 'scroll',
    'click', 'click', 'hover', 'scroll', 'scroll'
]

# Count frequency of each action
rank_counter = Counter(actions)

# Calculate weights for each action type
weight_click = 1
weight_scroll = 2
weight_hover = 1.5

# Compute weighted score based on frequencies
weighted_clicks = rank_counter['click'] * weight_click
weighted_scrolls = rank_counter['scroll'] * weight_scroll
weighted_hovers = rank_counter['hover'] * weight_hover

# Intermediate metric: total activity score
total_activity_score = weighted_clicks + weighted_scrolls + weighted_hovers

# Bonus threshold logic
bonus_eligible = rank_counter['click'] > 4
bonus_points = 10 if bonus_eligible else 0

# Final scoring calculation
def calculate_final_score(counter):
    base = (counter['click'] * weight_click) + (counter['scroll'] * weight_scroll)
    base += (counter['hover'] * weight_hover)
    return base + bonus_points

final_score = calculate_final_score(rank_counter)
print(f"Result: {final_score}")