from collections import defaultdict, Counter

# Simulate user interaction logs with redundant and auxiliary data
timestamps = [101, 102, 105, 106, 108, 110, 115, 120]
user_actions = ['click', 'scroll', 'click', 'hover', 'click', 'scroll', 'click', 'exit']
dummy_weights = [0.1, 0.3, 0.2, 0.5, 0.4, 0.6, 0.7, 0.9]

# Auxiliary tracking variables (some irrelevant)
action_count = defaultdict(int)
accumulated_focus = 0.0
irrelevant_sum = sum([w ** 2 for w in dummy_weights])  # Distractor computation

for action in user_actions:
    action_count[action] += 1

# Compute derived metrics
unique_actions = set(user_actions)
frequent_action_threshold = 2
common_actions = [act for act, cnt in action_count.items() if cnt >= frequent_action_threshold]

# Simulate time-based session segmentation
session_gaps = []
for i in range(1, len(timestamps)):
    gap = timestamps[i] - timestamps[i-1]
    session_gaps.append(gap)

mean_gap = sum(session_gaps) / len(session_gaps)

# Begin relevant processing chain
raw_duration = timestamps[-1] - timestamps[0]
scaled_duration = raw_duration * 0.75

# Misleading transformation (not used later)
transformed_weights = [w * 1.5 for w in dummy_weights if w > 0.4]
offset_correction = len(transformed_weights) * 0.1  # Dead-end variable

# Core logic disguised among distractions
action_counter = Counter(user_actions)
click_bonus = action_counter['click'] * 10
scroll_penalty = action_counter.get('scroll', 0) * 3
exit_severity = 1 if 'exit' in user_actions else 0

intermediate_score = click_bonus - scroll_penalty - (exit_severity * 5)

# Conditional adjustment based on session continuity
if mean_gap <= 5:
    intermediate_score += 7
else:
    adjustment_factor = max(0, 6 - (mean_gap // 2))
    intermediate_score += adjustment_factor

# Secondary validation via unique action diversity
diversity_bonus = len(unique_actions) * 2

# Another red herring: unused structure
theoretical_max = len(user_actions) * 15
efficiency_ratio = intermediate_score / theoretical_max if theoretical_max > 0 else 0

# Accumulate final components
temp_offset = sum(session_gaps[:3]) % 4  # Minor perturbation
final_score = intermediate_score + diversity_bonus + temp_offset

# Irrelevant list comprehension with side-effect-free operations
reindexed = [i * 2 + 1 for i, t in enumerate(timestamps) if t % 2 == 0]
shadow_metric = sum(reindexed) / (len(reindexed) + 1) if reindexed else 0

# Critical execution point
final_score = calculate_final_score(processed_data)

# Mock function to finalize score (defined here to avoid undefined behavior)
def calculate_final_score(data_dict):
    base = data_dict['score']
    modifier = data_dict['diversity'] * 0.5
    return int(base + modifier)

# Prepare input for function call
processed_data = {
    'score': intermediate_score,
    'diversity': len(unique_actions),
    'sequence_length': len(user_actions)
}

# Recompute final_score correctly after definition
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")