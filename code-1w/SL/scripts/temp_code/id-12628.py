from collections import defaultdict, Counter
import math

# Simulated system logs and user interaction data
timestamps = [1623456789, 1623456795, 1623456801, 1623456810, 1623456815]
user_actions = ['click', 'hover', 'scroll', 'click', 'keydown']
action_durations = [1.2, 0.8, 3.1, 0.5, 2.4]

# Irrelevant telemetry processing (distractor)
def analyze_latency(logs):
    if not logs:
        return 0.0
    total = 0.0
    for t in logs:
        total += (t % 100) * 0.01
    return round(total, 3)

latency_report = analyze_latency(timestamps)

# Core evaluation data
feedback_sequence = [4, 5, 3, 5, 4, 2, 5, 4, 4, 5]
metric_weights = {'consistency': 0.4, 'accuracy': 0.35, 'responsiveness': 0.25}

def count_transitions(seq):
    transitions = 0
    for i in range(len(seq) - 1):
        if seq[i] != seq[i+1]:
            transitions += 1
    return transitions

def compute_entropy(seq):
    freq = Counter(seq)
    total = len(seq)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 6)

def calculate_streaks(seq):
    max_streak = current = 1
    for i in range(1, len(seq)):
        if seq[i] == seq[i-1]:
            current += 1
            max_streak = max(max_streak, current)
        else:
            current = 1
    return max_streak

def normalize_scores(raw_scores):
    mean = sum(raw_scores) / len(raw_scores)
    variance = sum((x - mean) ** 2 for x in raw_scores) / len(raw_scores)
    std_dev = math.sqrt(variance)
    if std_dev == 0:
        return [1.0] * len(raw_scores)
    return [(x - mean) / std_dev for x in raw_scores]

# Misleading auxiliary function (dead code path)
def deprecated_evaluation(data):
    score = 0
    for x in data:
        if x > 4:
            score += 2
        elif x == 4:
            score += 1
    return score // len(data) if data else 0

# Complex weight adjustment based on behavioral heuristics
def adjust_weights_by_context(base_weights, sequence):
    transition_count = count_transitions(sequence)
    entropy_val = compute_entropy(sequence)
    streak = calculate_streaks(sequence)
    
    adjusted = base_weights.copy()
    
    # Artificial adjustments with red herring logic
    if transition_count > 5:
        adjusted['consistency'] *= 0.9
    if entropy_val > 2.0:
        adjusted['accuracy'] *= 1.1
    if streak < 3:
        adjusted['responsiveness'] *= 0.85
    
    # Renormalize weights
    total_weight = sum(adjusted.values())
    for k in adjusted:
        adjusted[k] /= total_weight
    
    return adjusted

# Unused diagnostic function (distractor)
def generate_diagnostic_profile(seq):
    profile = defaultdict(int)
    profile['length'] = len(seq)
    profile['unique_values'] = len(set(seq))
    profile['peak'] = max(seq)
    profile['valley'] = min(seq)
    return dict(profile)

diag = generate_diagnostic_profile(feedback_sequence)

# Recursive smoothing filter (actually used)
def smooth_recursive(data, alpha=0.3, axis=None):
    if axis is None:
        axis = len(data) - 1
    if axis == 0:
        return [data[0]]
    prev_smooth = smooth_recursive(data, alpha, axis-1)
    if len(prev_smooth) < len(data):
        smoothed_val = alpha * data[axis] + (1 - alpha) * prev_smooth[-1]
        prev_smooth.append(smoothed_val)
    return prev_smooth

smoothed_feedback = smooth_recursive(feedback_sequence)

# Final performance evaluator
def evaluate_performance(seq, weights):
    raw_mean = sum(seq) / len(seq)
    entropy_bonus = 5 - compute_entropy(seq)  # Higher consistency → higher bonus
    transition_penalty = count_transitions(seq) * 0.1
    
    # Apply recursive smoothing result as offset
    smoothing_offset = abs(smoothed_feedback[-1] - raw_mean) * 0.5
    
    base_score = raw_mean + entropy_bonus - transition_penalty + smoothing_offset
    
    # Weighted aggregation (weights are modified by context)
    adjusted_weights = adjust_weights_by_context(weights, seq)
    
    final_component = base_score
    for w in adjusted_weights.values():
        final_component *= 1.05  # Compound effect per metric
    
    return int(round(final_component * 100))  # Scale up for precision tracking

# Critical execution point
final_score = evaluate_performance(feedback_sequence, metric_weights)
print(f"Target result: {final_score}")