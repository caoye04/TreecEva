from collections import defaultdict

# Simulate user feedback analysis for a training module
feedback_entries = [
    {'user': 'a1', 'rating': 4, 'comments': 'clear explanation'},
    {'user': 'b2', 'rating': 5, 'comments': 'excellent pacing'},
    {'user': 'c3', 'rating': 3, 'comments': 'too fast in section 2'},
    {'user': 'd4', 'rating': 5, 'comments': 'loved the examples'},
    {'user': 'e5', 'rating': 2, 'comments': 'needed more visuals'},
    {'user': 'f6', 'rating': 5, 'comments': 'perfect structure'}
]

# Irrelevant metrics (distractor)
total_words = 0
word_frequency = defaultdict(int)
for entry in feedback_entries:
    words = entry['comments'].split()
    total_words += len(words)
    for word in words:
        cleaned = word.lower().strip('.,!')
        word_frequency[cleaned] += 1

# Relevant processing: count high vs low ratings
rating_tally = defaultdict(int)
high_rated_count = 0
low_rated_count = 0
for entry in feedback_entries:
    rating = entry['rating']
    rating_tally[rating] += 1
    if rating >= 4:
        high_rated_count += 1
    else:
        low_rated_count += 1

# Compute sentiment proxy from comment length (semi-relevant)
sentiment_proxy = 0
for entry in feedback_entries:
    length = len(entry['comments'])
    if length > 20:
        sentiment_proxy += 1
    elif length < 10:
        sentiment_proxy -= 1

# Auxiliary function to assess consistency
is_consistent = lambda rt: all(count == rt[4] for count in rt.values() if count != 0)
baseline_consistency_check = is_consistent(rating_tally)  # Always False here, distractor

# Prepare summary (key intermediate)
avg_rating = sum(entry['rating'] for entry in feedback_entries) / len(feedback_entries)
feedback_summary = {
    'average': avg_rating,
    'volume': len(feedback_entries),
    'positive_ratio': high_rated_count / len(feedback_entries),
    'sentiment_index': sentiment_proxy,
    'ratings': [e['rating'] for e in feedback_entries]
}

# Misleading complexity: entropy-like measure (not used directly)
import math
dist_entropy = 0
for count in rating_tally.values():
    p = count / len(feedback_entries)
    if p > 0:
        dist_entropy -= p * math.log(p)

# Core evaluation logic
def evaluate_performance(summary):
    score = 0
    score += summary['average'] * 10                    # Base performance
    score += summary['positive_ratio'] * 20             # Weighted boost
    if summary['volume'] >= 5:
        score += 5                                       # Sample size bonus
    if summary['sentiment_index'] > 0:
        score += 3
    return int(score)

# Final computation step
final_score = evaluate_performance(feedback_summary)
print(f"Result: {final_score}")