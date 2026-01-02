from collections import defaultdict, Counter

# Simulate user interaction logs with redundant metadata
timestamps = [100, 105, 110, 115, 120, 130, 140, 150]
user_actions = ['click', 'scroll', 'click', 'hover', 'click', 'scroll', 'click', 'exit']
duration_per_action = [2, 5, 1, 3, 2, 6, 4, 10]

# Irrelevant tracking variables (distractors)
irrelevant_counter = 0
placeholder_data = []
for t in timestamps:
    placeholder_data.append(f'tick_{t}')
    irrelevant_counter += 1

# Misleading preprocessing (not used in final logic)
action_frequencies_raw = {}
for action in user_actions:
    action_frequencies_raw[action] = action_frequencies_raw.get(action, 0) + 1

# Actual relevant processing begins
action_duration_map = defaultdict(list)
for i, action in enumerate(user_actions):
    action_duration_map[action].append(duration_per_action[i])

# Compute average duration per action type
avg_durations = {act: sum(durs) / len(durs) for act, durs in action_duration_map.items()}

# Focus on 'click' interactions for scoring
click_durations = action_duration_map['click']
click_count = len(click_durations)
click_total_time = sum(click_durations)

# Secondary distraction: analyze scroll patterns even though unused
scroll_avg = avg_durations.get('scroll', 0)
theoretical_engagement = scroll_avg * 1.5 if scroll_avg > 4 else scroll_avg * 0.8

# Build frequency profile using Counter (relevant)
frequency_profile = Counter(user_actions)
unique_actions = len(frequency_profile)

def calculate_click_efficiency(count, total_time):
    if count == 0:
        return 0.0
    # Artificial complexity: diminishing returns formula
    return (total_time * 1.2) / (count ** 0.5)

def calculate_final_score(click_eff, diversity, base_actions):
    # Core formula
    raw_score = click_eff * (diversity / 2.0)
    penalty = 0
    if base_actions > 6:
        penalty = 1.5
    elif base_actions < 4:
        penalty = 0.8
    adjusted = raw_score - penalty
    return int(adjusted) if adjusted > 0 else 0

# Misleading intermediate calculation (dead path)
if len(user_actions) % 2 == 0:
    dummy_score = click_count * 2.5
    # This score is never used

# Key computation
click_efficiency = calculate_click_efficiency(click_count, click_total_time)
final_score = calculate_final_score(click_efficiency, unique_actions, len(user_actions))

# Output result as required
print(f"Result: {final_score}")