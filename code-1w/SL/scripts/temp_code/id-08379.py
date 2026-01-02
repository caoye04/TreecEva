from collections import defaultdict, Counter

# Simulate user interaction logs with partial noise
def generate_logs():
    actions = ['click', 'hover', 'scroll', 'click', 'keystroke', 'click']
    return Counter(actions)

# Process raw interaction frequency
logs = generate_logs()
frequent_actions = {k: v for k, v in logs.items() if v > 1}

# Initialize system state with some irrelevant metrics
current_state = defaultdict(int)
current_state['timeout_count'] = 5
current_state['retry_limit'] = 3
current_state['stability_index'] = 0.87

# Core processing pipeline
action_weights = {
    'click': 1.2,
    'hover': 0.3,
    'scroll': 0.6,
    'keystroke': 1.5
}

weighted_score = 0.0
for action, count in logs.items():
    if action in action_weights:
        weighted_score += count * action_weights[action]

# Simulate multi-phase feedback accumulation
feedback_summary = []
base_penalty = 0
max_iter = 4

for i in range(max_iter + 1):
    if i == 0:
        feedback_summary.append(weighted_score * 1.1)
        continue
    
    temp_offset = 0
    if i % 2 == 0:
        temp_offset += i * 0.1
        base_penalty += 1  # Irrelevant accumulation
    else:
        temp_offset -= 0.05
    
    adjusted = feedback_summary[-1] * (0.9 + temp_offset)
    feedback_summary.append(adjusted)
    
    # Dead-end conditional with no downstream impact
    if adjusted < 5 and i > 2:
        shadow_buffer = [x * 0.1 for x in feedback_summary]
        break

# Auxiliary function with plausible but non-critical logic
def smooth_data(seq):
    smoothed = []
    for i in range(len(seq)):
        window = seq[max(0, i-1):i+2]
        smoothed.append(sum(window) / len(window))
    return smoothed

# Apply smoothing (not used in final calculation - distraction)
sentiment_trace = smooth_data(feedback_summary)
sentiment_score = sum(sentiment_trace) / len(sentiment_trace)

# Key computational branch using slicing and set operations
recent_feedback = feedback_summary[-3:]
suppressed_modes = set(['error', 'crash', 'timeout'])
active_modes = set(['click', 'hover', 'scroll'])

# Secondary score with red herring
consistency_bonus = len(active_modes & {'click', 'scroll'}) * 0.25

# Final aggregation with distractor variables
baseline_ref = recent_feedback[0]
drift_adjustment = (recent_feedback[-1] - baseline_ref) * 0.1  # Unused

final_score = 0
for val in recent_feedback:
    if val > baseline_ref * 0.95:  # Tolerance threshold
        final_score += int(val)

# Add minor correction based on control flow history
if max_iter >= 3:
    final_score += base_penalty  # base_penalty was incremented in loop

# Output result as required
print(f"Result: {final_score}")