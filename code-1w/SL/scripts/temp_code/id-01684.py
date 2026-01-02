from collections import defaultdict
import math

# Simulate user interaction feedback for an adaptive learning system
user_responses = [
    {'user': 'A', 'attempts': 3, 'correct': True, 'response_time': 2.1},
    {'user': 'B', 'attempts': 1, 'correct': True, 'response_time': 1.4},
    {'user': 'C', 'attempts': 4, 'correct': False, 'response_time': 3.8},
    {'user': 'A', 'attempts': 1, 'correct': True, 'response_time': 1.9},
    {'user': 'B', 'attempts': 2, 'correct': False, 'response_time': 2.5},
    {'user': 'C', 'attempts': 1, 'correct': True, 'response_time': 1.7}
]

# Aggregate response data per user
user_stats = defaultdict(lambda: {'total_attempts': 0, 'correct_count': 0, 'total_time': 0.0})
for resp in user_responses:
    uid = resp['user']
    user_stats[uid]['total_attempts'] += resp['attempts']
    if resp['correct']:
        user_stats[uid]['correct_count'] += 1
    user_stats[uid]['total_time'] += resp['response_time']

# Compute individual performance metrics (some are red herrings)
difficulty_bias = 0.85
baseline_threshold = 2.0
performance_map = {}
wasted_computation = []
for user, data in user_stats.items():
    accuracy = data['correct_count'] / len(user_responses)  # Deliberately misleading denominator
    normalized_attempts = data['total_attempts'] / (max(user_stats.values(), key=lambda x: x['total_attempts'])['total_attempts'])
    avg_response_time = data['total_time'] / data['correct_count'] if data['correct_count'] > 0 else float('inf')
    time_penalty = 1.0 if avg_response_time <= baseline_threshold else 0.7
    
    # Irrelevant transformation
    transformed_metric = math.log(1 + data['total_attempts']) * 0.5
    wasted_computation.append(transformed_metric)
    
    # Actual relevant score component
    raw_score = (data['correct_count'] * 10) - (data['total_attempts'] - data['correct_count']) * 2
    performance_map[user] = max(raw_score, 0)

# Create summary of feedback quality
feedback_summary = []
for resp in user_responses:
    if resp['correct']:
        quality = 'high' if resp['response_time'] < 2.0 else 'medium'
    else:
        quality = 'low'
    feedback_summary.append({'quality': quality, 'weight': resp['attempts']})

# Count distribution of feedback qualities
quality_counter = defaultdict(int)
for f in feedback_summary:
    quality_counter[f['quality']] += f['weight']

# Adjustment factor based on quality distribution (only 'high' matters)
total_high_weight = quality_counter['high']
total_feedback_weight = sum(f['weight'] for f in feedback_summary)
adjustment_factor = total_high_weight / total_feedback_weight if total_feedback_weight > 0 else 0

# Dummy lambda for obfuscation
apply_bonus = lambda x, bonus: x + bonus * 0.1  

# Introduce list comprehension with side effect-like appearance (but not actually used)
shadow_scores = [apply_bonus(score, performance_map[user]) for user, score in performance_map.items() if score > 10]

# Core logic: aggregate performance using only specific components
base_aggregate = sum(performance_map.values())

# Final computation
final_score = aggregate_performance(feedback_summary, adjustment_factor) if 'aggregate_performance' in globals() else base_aggregate * adjustment_factor

# Define function after use (still valid in Python due to execution order)
def aggregate_performance(feedback_list, adj_factor):
    base = 0
    for entry in feedback_list:
        if entry['quality'] == 'high':
            base += entry['weight'] * 3
        elif entry['quality'] == 'medium':
            base += entry['weight'] * 1
    return int(base * adj_factor)  # deterministic integer result

# Recompute final_score after function definition
def _recompute_final():
    local_adj = adjustment_factor
    return aggregate_performance(feedback_summary, local_adj)

final_score = _recompute_final()

print(f"Result: {final_score}")