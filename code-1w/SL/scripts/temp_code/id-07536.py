from collections import defaultdict

# Simulated user activity logs with redundant and irrelevant fields
timestamps = [1623456000, 1623456060, 1623456120, 1623456180, 1623456240]
user_actions = ['click', 'scroll', 'click', 'hover', 'click']
duration_ms = [1200, 300, 900, 450, 600]
irrelevant_flags = [False, True, False, True, False]
payload_size_kb = [12.5, 3.2, 8.7, 1.9, 5.4]

# Data processing pipeline with mixed relevance
action_counts = defaultdict(int)
duration_by_action = {}
score_weights = {'click': 3, 'scroll': 2, 'hover': 1, 'keypress': 4}

for i in range(len(user_actions)):
    action = user_actions[i]
    action_counts[action] += 1
    
    # Accumulate durations per action type
    if action not in duration_by_action:
        duration_by_action[action] = 0
    duration_by_action[action] += duration_ms[i]

    # Irrelevant computation: simulating network overhead (not used later)
    overhead = payload_size_kb[i] * 0.05
    adjusted_time = duration_ms[i] - int(overhead * 10)  # Dead code path

# Secondary processing with red herring variables
average_durations = {}
total_interactions = sum(action_counts.values())
fake_normalization_factor = 1.0 / (total_interactions + 1e-8)

for act in action_counts:
    avg_dur = duration_by_action[act] / action_counts[act]
    average_durations[act] = round(avg_dur, 2)

# Compute engagement score with weighted logic
base_engagement = 0
for act, count in action_counts.items():
    base_engagement += score_weights.get(act, 1) * count

# Dummy transformation: unused metrics
unused_peak_load = max(duration_ms) * 1.5
unused_variance = sum((x - sum(duration_ms)/len(duration_ms))**2 for x in duration_ms)

# Final scoring logic dependent on multiple steps
def calculate_final_score(data_dict):
    temp_score = 0
    for key, val in data_dict.items():
        if key == 'click':
            temp_score += val * 3
        elif key == 'scroll':
            temp_score += val * 2
        elif key == 'hover':
            temp_score += val * 1
    # Apply artificial decay based on total actions
    total_actions = sum(data_dict.values())
    decayed_score = temp_score * (0.95 ** (total_actions - 1)) if total_actions > 0 else 0
    return int(round(decayed_score))

processed_data = dict(action_counts)
final_score = calculate_final_score(processed_data)

# Misleading post-processing block (no effect on final_score)
if final_score > 10:
    bonus = 5
    final_score_adjustment = bonus * 0.1  # Not applied

print(f"Result: {final_score}")