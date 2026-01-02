from collections import defaultdict, Counter

# Simulated user interaction sequence with metadata
events = [
    {'type': 'click', 'target': 'button-a', 'time': 100, 'user': 'x1'},
    {'type': 'hover', 'target': 'nav', 'time': 120, 'user': 'x2'},
    {'type': 'click', 'target': 'button-a', 'time': 150, 'user': 'x1'},
    {'type': 'submit', 'target': 'form', 'time': 180, 'user': 'x3'},
    {'type': 'click', 'target': 'button-b', 'time': 200, 'user': 'x2'},
    {'type': 'click', 'target': 'button-a', 'time': 220, 'user': 'x3'},
    {'type': 'hover', 'target': 'sidebar', 'time': 240, 'user': 'x1'},
    {'type': 'click', 'target': 'button-b', 'time': 260, 'user': 'x3'}
]

# Preprocessing: extract click events only
click_events = [e for e in events if e['type'] == 'click']

# Track frequency of clicks per button
button_counter = Counter([e['target'] for e in click_events])

# User-specific action tracking
user_actions = defaultdict(list)
for e in click_events:
    user_actions[e['user']].append(e['target'])

# Calculate base engagement score (sum of unique buttons clicked per user)
engagement_scores = []
for user, actions in user_actions.items():
    unique_buttons = len(set(actions))
    total_clicks = len(actions)
    # Irrelevant distraction: time-based decay not actually used later
    avg_time_gap = sum([(i+1) * 10 for i in range(total_clicks)]) / total_clicks if total_clicks > 0 else 0
    engagement_scores.append(unique_buttons)

base_engagement = sum(engagement_scores)

# Distraction block: unused metrics calculation
unused_hover_count = sum(1 for e in events if e['type'] == 'hover')
duplicate_click_threshold = 2
frequent_buttons = [btn for btn, cnt in button_counter.items() if cnt >= duplicate_click_threshold]

# Simulate data transformation pipeline
processed_data = {}
for idx, (button, count) in enumerate(button_counter.items()):
    # Apply artificial weighting based on alphabetical order (real effect)
    weight = ord(button[-1]) - ord('a') + 1  # 'button-a' -> 1, 'button-b' -> 2
    normalized = count * weight
    processed_data[button] = {
        'raw_count': count,
        'weighted': normalized,
        'bonus': 5 if count >= 2 else 0,
        'rank': idx + 1
    }

# Red herring: unused transformation
legacy_mapping = {k: v['weighted'] * 0.9 for k, v in processed_data.items()}

# Core logic: calculate final score
# Only weighted values and bonus contribute
main_component = sum(v['weighted'] for v in processed_data.values())
bonus_component = sum(v['bonus'] for v in processed_data.values())

# Conditional adjustment based on button diversity
if len(processed_data) > 1 and button_counter['button-a'] >= 2:
    diversity_modifier = 1.2
else:
    diversity_modifier = 0.8

adjusted_total = (main_component + bonus_component) * diversity_modifier

# Final nonlinear transformation (simulate scoring model)
def calculate_final_score(data):
    raw_sum = sum(item['weighted'] + item['bonus'] for item in data.values())
    penalty = 0
    for item in data.values():
        if item['raw_count'] == 1:
            penalty += item['weighted'] * 0.1  # 10% penalty for single-use buttons
    return int((raw_sum - penalty) * (item['rank'] / 2))  # uses last item's rank

final_score = calculate_final_score(processed_data)

# Debug print (not counted as interference)
print(f"Target result: {final_score}")