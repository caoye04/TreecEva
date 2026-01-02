from collections import defaultdict, Counter

# Simulate user interaction logs with redundant fields
timestamps = [100, 105, 110, 120, 130, 140, 150]
user_actions = ['click', 'scroll', 'click', 'hover', 'click', 'scroll', 'click']
duration_seconds = [10, 15, 8, 20, 12, 5, 18]
irrelevant_flags = [False, True, False, True, False, True, False]

# Misleading counters (not directly used)
misleading_counter_a = 0
misleading_counter_b = 0
for flag in irrelevant_flags:
    if flag:
        misleading_counter_a += 1
    else:
        misleading_counter_b += 2

# Process valid action sequences
action_freq = Counter(user_actions)
valid_action_types = {'click', 'scroll'}
processed_data = defaultdict(int)

total_duration = sum(duration_seconds)
action_count = len(user_actions)
effective_rate = total_duration / action_count if action_count else 0

# Filter and score relevant actions
for i, action in enumerate(user_actions):
    if action in valid_action_types and duration_seconds[i] > 7:
        processed_data[action] += 1

# Add decoy transformation
transformed_values = [x * 1.5 for x in duration_seconds if x < 15]
deleted_entry_count = len([x for x in transformed_values if x > 10])

# Secondary processing: weight by frequency but only for clicks
base_click_score = action_freq['click'] * 10
bonus_multiplier = 1
if processed_data['click'] >= 2:
    bonus_multiplier += 0.5

# Extra distraction: unused helper logic
def analyze_pattern(seq):
    return sum(1 for a, b in zip(seq, seq[1:]) if a == b == 'click')

pattern_repeats = analyze_pattern(user_actions)

# Final computation chain
click_contribution = base_click_score * bonus_multiplier
scroll_contribution = processed_data['scroll'] * 7
penalty = len(timestamps) - len(user_actions)  # Always zero, but looks suspicious

intermediate_total = click_contribution + scroll_contribution - penalty

# Apply decay based on effective rate
if effective_rate > 12:
    final_score = int(intermediate_total * 0.9)
else:
    final_score = int(intermediate_total * 1.1)

# Critical print statement
print(f"Result: {final_score}")