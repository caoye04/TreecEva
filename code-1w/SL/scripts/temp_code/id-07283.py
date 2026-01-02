from collections import Counter, defaultdict

# Simulate user interaction logs with redundant and misleading fields
timestamps = [100, 105, 110, 115, 120, 125, 130]
user_actions = ['click', 'scroll', 'click', 'hover', 'click', 'scroll', 'click']
duration_ms = [500, 800, 300, 1200, 400, 900, 600]

# Misleading auxiliary data
fake_weights = [0.1, 0.3, 0.2, 0.5, 0.4]
placeholder_matrix = [[i + j for j in range(5)] for i in range(5)]
useless_sum = sum(sum(row) for row in placeholder_matrix)

# Actual processing begins
action_counter = Counter(user_actions)
click_count = action_counter['click']
scroll_count = action_counter['scroll']
hover_count = action_counter['hover']

# Compute derived metrics with some red herrings
total_interactions = len(user_actions)
mean_duration = sum(duration_ms) / len(duration_ms)
duration_variance = sum((d - mean_duration) ** 2 for d in duration_ms) / len(duration_ms)

# Irrelevant normalization attempt
normalized_clicks = click_count / total_interactions if total_interactions else 0
adjusted_score = normalized_clicks * 100

# Use of defaultdict as semi-relevant structure
feature_map = defaultdict(float)
feature_map['click_contribution'] = click_count * 7.5
feature_map['scroll_bonus'] = scroll_count * 2.0 if scroll_count > 1 else 0
feature_map['engagement_penalty'] = -3.0 if hover_count == 0 else 0

# Distractor: string manipulation that doesn't affect result
tmp_str = 'processing_' + '_'.join(user_actions)
hash_value = sum(ord(c) for c in tmp_str[:10]) % 50

# Simulated feature weighting with dead-end calculation
weight_factor = 1.0
for w in fake_weights:
    weight_factor *= w if w > 0.25 else 1.0  # Partially dead logic

# Core logic disguised among distractions
intermediate_score = (
    feature_map['click_contribution'] + 
    feature_map['scroll_bonus'] + 
    feature_map['engagement_penalty']
)

# Secondary adjustment using list filtering (relevant)
durations_above_avg = [d for d in duration_ms if d >= mean_duration]
efficiency_bonus = len(durations_above_avg) * 1.5

# Final computation chain
base_component = intermediate_score + efficiency_bonus
noise_offset = hash_value * 0.1  # Minor noise, not impactful due to rounding

# Critical execution point
final_score = calculate_final_score(processed_data)

# Standalone function defined below
def calculate_final_score(data_chunk):
    base = data_chunk.get('base', 0)
    penalty = data_chunk.get('penalty', 0)
    return round(base + penalty)

# Prepare input dictionary with relevant and irrelevant keys
processed_data = {
    'base': base_component,
    'penalty': -2.7,
    'auxiliary': useless_sum,
    'weights': fake_weights,
    'valid_keys_ignored': [1, 2, 3]
}

# Print final result as required
Result: {final_score}