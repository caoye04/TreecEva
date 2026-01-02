from collections import Counter, defaultdict
import math

def analyze_user_engagement(timestamps, actions):
    duration = max(timestamps) - min(timestamps)
    action_freq = Counter(actions)
    unique_actions = len(action_freq)
    avg_interval = duration / len(timestamps) if timestamps else 0
    return unique_actions, avg_interval

def compute_stability_factor(metrics):
    raw_stability = sum([abs(metrics[i] - metrics.get(i-1, 0)) for i in range(1, len(metrics))])
    normalized = raw_stability / (len(metrics) + 1)
    return round(normalized * 100, 2)

def aggregate_performance(counter, base):
    bonus = 0
    if counter['positive'] > counter['negative']:
        bonus += 15
    if 'neutral' in counter:
        bonus -= 5
    total_interactions = sum(counter.values())
    efficiency = counter['positive'] / total_interactions if total_interactions else 0
    scaled_efficiency = math.floor(efficiency * 100)
    return base + scaled_efficiency + bonus

# Simulated user interaction data
timestamps = [100, 105, 112, 120, 135, 140]
user_actions = ['view', 'like', 'share', 'view', 'like', 'comment']
action_scores = {'like': 1, 'share': 2, 'comment': 1, 'view': 0}

# Irrelevant tracking variables
engagement_log = defaultdict(list)
dummy_metrics = {i: (i**2 + 3*i) % 7 for i in range(8)}

# Compute engagement features
unique_action_count, average_interval = analyze_user_engagement(timestamps, user_actions)

# Misleading stability analysis on dummy data
stability_score = compute_stability_factor(dummy_metrics)

# Core rating logic begins
base_rating = 50
feedback_counter = Counter()
for action in user_actions:
    score = action_scores.get(action, 0)
    if score > 1:
        feedback_counter['positive'] += 1
    elif score == 1:
        feedback_counter['positive'] += 1
    else:
        feedback_counter['neutral'] += 1

# Introduce dead code path (never executed)
if False:
    feedback_counter['negative'] += sum(1 for a in user_actions if a == 'report')

# Add distractor computation with no impact
penalty_adjustment = 0
for t in timestamps:
    if t % 10 == 0:
        penalty_adjustment += 2

# Key computation point
final_score = aggregate_performance(feedback_counter, base_rating)
print(f"Result: {final_score}")