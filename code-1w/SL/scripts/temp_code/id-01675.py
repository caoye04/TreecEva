from itertools import combinations

def analyze_response_time(raw_logs):
    # Irrelevant processing: logs are transformed but not used in final result
    processed = [round((t - 50) * 0.3 + 2, 2) for t in raw_logs if t > 30]
    outliers = [t for t in processed if t > 10]
    return len(outliers)


def validate_feedback_integrity(entries):
    # Semi-relevant check: counts valid entries but only some affect logic
    valid_count = 0
    for entry in entries:
        chars = set(entry)
        if '!' not in chars and len(entry) > 2:
            valid_count += 1
    return valid_count > 3

# Simulated user feedback strings
feedback_pool = ['good', 'excellent', 'poor', 'average', 'great', 'ok']

# Generate all 3-element combinations of feedback
feedback_sets = list(combinations(feedback_pool, 3))

# Misleading variable: appears important but unused in final score
response_log = [120, 45, 67, 89, 52, 110, 134]
analyze_response_time(response_log)  # Called but result discarded

# Scoring logic with distractors
base_weights = {'good': 2, 'average': 1, 'ok': 1, 'poor': -2}
bonus_triggers = {'excellent', 'great'}

scores = []
duplicate_tracker = set()

for group in feedback_sets:
    word_set = set(group)
    
    # Red herring: character counting that doesn't impact outcome
    total_chars = sum(len(w) for w in group)
    char_count_threshold = 15
    size_penalty = -1 if total_chars > char_count_threshold else 0

    base_score = sum(base_weights.get(word, 0) for word in group)
    bonus = 5 if any(word in bonus_triggers for word in group) else 0
    
    # Distractor: conditional that never triggers due to data
    if 'outstanding' in word_set:
        base_score += 10  # Dead code path
    
    # Actual key logic
    if validate_feedback_integrity(group):
        composite = base_score + bonus + size_penalty
        scores.append(composite)

# Aggregation function
aggregate_performance = lambda data: sum(filter(lambda x: x > 0, data))

# Critical execution point
final_score = aggregate_performance(scores)

print(f"Result: {final_score}")