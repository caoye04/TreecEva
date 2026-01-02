from itertools import combinations

def analyze_response_time(raw_logs, threshold=100):
    # Irrelevant processing: simulates log filtering but not used in final result
    valid_entries = [log for log in raw_logs if log > threshold]
    return len(valid_entries) > 0


def compute_baseline_adjustment(config_tuple):
    base_val, mode_flag, version = config_tuple
    adjustment = base_val * 0.1 if mode_flag else base_val * 0.05
    if version == 'legacy':
        adjustment *= 0.9
    return int(adjustment)


# Main data
user_sessions = [120, 150, 98, 200, 75]
system_flags = (True, False, True)
config_settings = (50, True, 'modern')
raw_feedback = [4, 5, 3, 5, 4, 4, 5]

# Distractor: complex unused structure
session_pairs = list(combinations(user_sessions, 2))
avg_pair_gap = sum(abs(a - b) for a, b in session_pairs) / len(session_pairs) if session_pairs else 0

# Intermediate irrelevant computation
outlier_count = 0
for val in user_sessions:
    if val > 180 or val < 80:
        outlier_count += 1

# Simulated metric expansion (semi-relevant initialization)
base_metrics = {
    'response_base': analyze_response_time(user_sessions, 90),
    'consistency': len(raw_feedback) >= 5,
    'baseline_adj': compute_baseline_adjustment(config_settings)
}

# Core logic with distraction
feedback_set = set()
for rating in raw_feedback:
    if rating >= 4:
        feedback_set.add(rating)
    elif rating == 3:
        feedback_set.add(rating)

# Red herring: unused transformation
transformed = {x ** 0.5 for x in feedback_set}

# Conditional logic with distractors
if base_metrics['consistency']:
    scaling_factor = 1.2
else:
    scaling_factor = 1.0

# Unused nested loop to increase cognitive load
snapshot_buffer = []
for flag in system_flags:
    temp_row = []
    for _ in range(2):
        temp_row.append(flag ^ (len(feedback_set) > 3))
    snapshot_buffer.append(temp_row)

# Key statement with multiple concepts: sets, conditionals, tuple unpacking, arithmetic
aggregate_performance = lambda s, m: (
    len(s) * 10 + 
    m['baseline_adj'] + 
    (20 if m['response_base'] else 10) + 
    (15 if len(s) >= 3 else 5)
) * (1.2 if len(s.intersection({5})) > 0 else 1.0)

final_score = aggregate_performance(feedback_set, base_metrics)

# Print result as required
print(f"Result: {final_score}")