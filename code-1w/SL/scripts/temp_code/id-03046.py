from collections import defaultdict, Counter
import itertools

# Simulated user interaction data for a code editor with multiple features
typing_events = [120, 115, 130, 125, 140, 135, 150, 160, 155, 170]
mouse_clicks = [45, 50, 40, 60, 55, 70, 65, 80, 75, 90]
feature_usage = ['autocomplete', 'linting', 'debugger', 'version_control', 'testing']

# Irrelevant transformation - red herring
shifted_events = [e - 100 for e in typing_events]
scaled_clicks = [c * 2 for c in mouse_clicks if c > 50]

# Distractor: complex but unused nested function
def analyze_productivity(data):
    def smooth_signal(signal):
        return [sum(signal[i:i+3]) / 3 for i in range(len(signal) - 2)]
    
    def detect_spike(pattern):
        return [1 if p > 2 * sum(pattern) / len(pattern) else 0 for p in pattern]
    
    trends = smooth_signal(data)
    spikes = detect_spike(trends)
    return sum(spikes)  # Dead end

# Unused recursive decoy
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Misleading intermediate metric
total_interactions = sum(typing_events) + sum(mouse_clicks)
avg_response_time = total_interactions / len(typing_events)

# Core logic disguised among distractions
user_sessions = defaultdict(lambda: {'keystrokes': 0, 'clicks': 0})
for i, event in enumerate(typing_events):
    session_id = i % 5
    user_sessions[session_id]['keystrokes'] += event
    user_sessions[session_id]['clicks'] += mouse_clicks[i]

# Data transformation with relevant and irrelevant parts
session_ranks = {}
for sid, data in user_sessions.items():
    base_rank = data['keystrokes'] / (data['clicks'] + 1)
    penalty = 0.1 * (sid % 3)  # Minor distortion
    session_ranks[f'user_{sid}'] = round(base_rank - penalty, 2)

# Decoy list comprehension with string methods
feature_caps = [f.upper() for f in feature_usage if 'e' in f]
feature_lengths = [len(f.replace('_', '')) for f in feature_usage]

# Real signal within noise: counting meaningful actions
action_log = ['edit'] * 120 + ['run'] * 45 + ['debug'] * 30 + ['commit'] * 20
action_counts = Counter(action_log)

# Filtering significant actions
significant_actions = {k: v for k, v in action_counts.items() if v >= 30}

# Bit manipulation decoy
obfuscation_key = 247
scrambled = [obfuscation_key ^ i for i in range(5)]

# Critical data for actual computation
feedback_cycles = list(itertools.accumulate([3, 5, 2, 8, 1]))  # [3, 8, 10, 18, 19]

# Another distraction: sorting irrelevant data
sorted_features = sorted(feature_usage, key=lambda x: x.count('e'), reverse=True)

# Conditional adjustment based on cycle thresholds
adjustment_factor = 1.0
for cycle in feedback_cycles:
    if cycle > 15:
        adjustment_factor *= 1.1
    elif cycle < 5:
        adjustment_factor *= 0.95

# Simulated performance metrics from sessions
raw_performances = [data['keystrokes'] * 0.7 + data['clicks'] * 0.3 for data in user_sessions.values()]
base_performance = sum(raw_performances) / len(raw_performances)

# Aggregation with distraction variables
metadata_flags = [1, 0, 1, 1, 0]
dependency_mask = 0b1101

# Real aggregation logic
def aggregate_performance(metrics, factor):
    temp = 0
    for i, val in enumerate(metrics):
        if i % 2 == 0:
            temp += val * factor
        else:
            temp += val / factor
    return int(temp // 1.5)  # Final deterministic transformation

# Critical statement
final_score = aggregate_performance(feedback_cycles, adjustment_factor)

# Output requirement
print(f"Result: {final_score}")