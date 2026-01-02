from collections import Counter, defaultdict

# Simulate user interaction logs with various actions
def process_user_actions(log_entries):
    action_count = Counter()
    temporal_gaps = []
    prev_timestamp = 0

    for entry in log_entries:
        action, timestamp = entry['action'], entry['time']
        action_count[action] += 1
        if prev_timestamp:
            gap = timestamp - prev_timestamp
            temporal_gaps.append(gap)
        prev_timestamp = timestamp

    avg_gap = sum(temporal_gaps) / len(temporal_gaps) if temporal_gaps else 0
    return action_count, avg_gap

# Analyze feedback patterns and compute adjustment factors
def analyze_feedback(feedback_list):
    sentiment_tally = defaultdict(int)
    total_entries = 0
    neutral_count = 0

    for fb in feedback_list:
        sentiment = fb['sentiment']
        sentiment_tally[sentiment] += 1
        total_entries += 1
        if sentiment == 'neutral':
            neutral_count += 1

    # Misleading distraction: unused transformation
    transformed_scores = [sentiment_tally[s] ** 0.5 for s in sentiment_tally]
    adjusted_total = sum(transformed_scores) + 1e-8

    consistency_ratio = (sentiment_tally['positive'] + sentiment_tally['negative']) / total_entries if total_entries else 0
    return sentiment_tally, consistency_ratio, neutral_count

# Core evaluation logic
def evaluate_performance(feedback_counter, adjustment_factor):
    base_score = 0
    penalty = 0

    # Weighted scoring based on feedback frequency
    for sentiment, count in feedback_counter.items():
        if sentiment == 'positive':
            base_score += count * 3
        elif sentiment == 'negative':
            penalty += count * 2
        elif sentiment == 'neutral':
            base_score += count * 1

    raw_score = base_score - penalty
    
    # Apply non-linear adjustment
    adjusted_score = raw_score * (1 + adjustment_factor)
    
    # Final thresholding
    if adjusted_score > 100:
        adjusted_score = 95 + (adjusted_score - 100) * 0.5
    elif adjusted_score < 0:
        adjusted_score = max(-10, adjusted_score - 5)
    
    return int(adjusted_score)

# Simulated dataset
log_data = [
    {'action': 'click', 'time': 10},
    {'action': 'scroll', 'time': 15},
    {'action': 'click', 'time': 22},
    {'action': 'hover', 'time': 28},
    {'action': 'click', 'time': 35}
]

feedback_data = [
    {'sentiment': 'positive'},
    {'sentiment': 'positive'},
    {'sentiment': 'neutral'},
    {'sentiment': 'negative'},
    {'sentiment': 'positive'},
    {'sentiment': 'neutral'},
    {'sentiment': 'positive'}
]

# Process action logs (distractor: not directly used in final score)
actions, avg_interval = process_user_actions(log_data)
distraction_multiplier = len(actions) * avg_interval

# Analyze feedback
feedback_counter, consistency, neutral_total = analyze_feedback(feedback_data)

# Compute adjustment factor based on consistency
if consistency > 0.7:
    adjustment_factor = 0.2
elif consistency > 0.5:
    adjustment_factor = 0.1
else:
    adjustment_factor = 0.05

# Introduce irrelevant state tracking
state_tracker = defaultdict(list)
for k, v in feedback_counter.items():
    state_tracker[k].append(v * 2)  # No impact on result

# Critical execution point
final_score = evaluate_performance(feedback_counter, adjustment_factor)

# Print result
print(f"Target result: {final_score}")