import math

def analyze_trend(data, window):
    # Irrelevant function - never called
    return [sum(data[i:i+window]) / window for i in range(len(data) - window + 1)]

def preprocess_signal(signal_input):
    # Distractor: signal processing that isn't used in main logic
    filtered = []
    for x in signal_input:
        if x > 0:
            filtered.append(math.log(x) * 1.5)
    return filtered

def calculate_entropy(sequence):
    # Dead function - looks important but unused
    from collections import Counter
    counts = Counter(sequence)
    total = len(sequence)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

def accumulate_weighted_sum(items, weights):
    # Unused helper with misleading relevance
    weighted_sum = 0
    for i in range(min(len(items), len(weights))):
        weighted_sum += items[i] * weights.get(i, 1)
    return weighted_sum

def simulate_feedback_loop(initial, iterations):
    # Red herring: complex recursion not tied to final result
    if iterations == 0:
        return initial
    return simulate_feedback_loop(initial * 0.9 + 2.5, iterations - 1)

# Global decoy variables
temp_cache = {i: i**2 for i in range(100)}
running_stats = {'mean': 0, 'variance': 0, 'peak': None}
placeholder_data = [x % 7 for x in range(50)]

# Key data structures with mixed relevant and irrelevant content
metrics_log = {
    'response_times': [120, 145, 130, 95, 160, 110],
    'error_count': 3,
    'throughput': 88,
    'priority_flags': [1, 0, 1, 1, 0],
    'timestamp_sequence': [1623456789 + i*60 for i in range(6)],  # unused
    'debug_info': {'level': 'verbose', 'triggers': 7}  # unused
}

baseline_metrics = {
    'thresholds': {
        'latency': 135,
        'errors': 5,
        'volume': 80
    },
    'weights': {'speed': 0.5, 'accuracy': 0.3, 'load': 0.2},  # unused in final calc
    'history': [0.87, 0.82, 0.91, 0.76]  # unused
}

base_threshold = 100
adjustment_factor = 1.1  # unused directly

# Misleading intermediate calculations
candidate_scores = []
for rt in metrics_log['response_times']:
    if rt < 100:
        candidate_scores.append(10)
    elif rt < 130:
        candidate_scores.append(7)
    else:
        candidate_scores.append(4)

# Simulate false dependency
aggregate_latency = sum(metrics_log['response_times']) / len(metrics_log['response_times'])
penalty_rate = 0
if aggregate_latency > 130:
    penalty_rate = 0.8

# Real logic buried among distractions
consecutive_good = 0
max_consecutive = 0
for rt in metrics_log['response_times']:
    if rt <= base_threshold:
        consecutive_good += 1
        max_consecutive = max(max_consecutive, consecutive_good)
    else:
        consecutive_good = 0

bonus_awarded = False
if max_consecutive >= 3:
    bonus_awarded = True

# Core scoring logic
base_score = 0
for rt in metrics_log['response_times']:
    if rt <= base_threshold:
        base_score += 10
    elif rt <= base_threshold + 20:
        base_score += 6
    else:
        base_score += 3

# Apply error deduction
error_penalty = metrics_log['error_count'] * 4
adjusted_score = base_score - error_penalty

# Incorporate throughput bonus
if metrics_log['throughput'] > 85:
    adjusted_score += 15

# Final adjustment based on bonus condition
if bonus_awarded:
    adjusted_score += 12

# Critical assignment point
final_score = adjusted_score

# Distractor block: looks like logging but doesn't affect result
log_entry = {
    'score_snapshot': adjusted_score,
    'flags_active': sum(metrics_log['priority_flags']),
    'anomaly_detected': False
}

# Unused accumulator
rolling_total = 0
for i, rt in enumerate(metrics_log['response_times']):
    rolling_total += rt * (0.9 ** i)

# Output the actual answer
print(f"Result: {final_score}")