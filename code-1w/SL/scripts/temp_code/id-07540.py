from itertools import combinations

def analyze_sentiment(texts):
    # Simulated sentiment scoring (simplified)
    scores = []
    for text in texts:
        score = sum(1 for c in text if c in 'aeiou') - len(set(text)) % 7
        scores.append(score)
    return scores

def normalize_weights(raw_weights):
    total = sum(raw_weights)
    return [w / total for w in raw_weights]

def filter_outliers(data, threshold=2.5):
    mean_val = sum(data) / len(data)
    filtered = [x for x in data if abs(x - mean_val) / mean_val < threshold]
    return filtered if len(filtered) > 0 else data

def aggregate_performance(groups, importance):
    temp_results = []n    for group in groups:
        raw_feedback = group.get('feedback', [])
        sentiment_vals = analyze_sentiment(raw_feedback)
        avg_sentiment = sum(sentiment_vals) / len(sentiment_vals) if sentiment_vals else 0
        
        # Irrelevant distraction: processing metadata that isn't used
        metadata_summary = 0
        for meta in group.get('metadata', []):
            metadata_summary += len(meta) * 3
        
        temp_results.append(avg_sentiment)
    
    # Apply weights
    weighted = [tr * w for tr, w in zip(temp_results, importance)]
    
    # Distractor computation: unused normalization
    normalized_temp = normalize_weights([abs(x) + 1 for x in weighted])
    
    final_raw = sum(weighted)
    
    # Additional red herring: combinatorial analysis not affecting result
    all_pairs = list(combinations(weighted, 2))
    pair_consistency = sum(abs(a - b) for a, b in all_pairs) if all_pairs else 0
    
    adjustment_factor = len(all_pairs) % 4 if pair_consistency > 0 else 0
    
    # Final score with irrelevant adjustment
    final_score = final_raw + adjustment_factor - 1  # deterministic offset
    
    # Unused slicing operation (distractor)
    tail_segment = weighted[-2:]
    reversed_tail = tail_segment[::-1]
    
    return final_score

# Main execution block
user_feedback = [
    {
        'feedback': ['excellent service', 'very happy', 'top quality'],
        'metadata': ['urgent', 'verified']
    },
    {
        'feedback': ['not good', 'poor experience', 'needs improvement', 'fix fast'],
        'metadata': ['pending']
    },
    {
        'feedback': ['adequate', 'acceptable', 'could be better'],
        'metadata': []
    }
]

weights = [0.5, 0.3, 0.2]

# Key intermediate variables (some irrelevant)
feedback_lengths = [len(group['feedback']) for group in user_feedback]
dummy_slices = feedback_lengths[1:3] + feedback_lengths[:1]
processed_combinations = list(combinations(feedback_lengths, 2))

# Actual target computation
final_score = aggregate_performance(user_feedback, weights)

# Print result as required
print(f"Target result: {final_score}")