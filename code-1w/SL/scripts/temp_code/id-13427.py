from itertools import groupby

def analyze_sentiment(text):
    positive_words = ['good', 'excellent', 'great', 'well']
    negative_words = ['bad', 'poor', 'terrible', 'awful']
    words = text.lower().split()
    score = 0
    for word in words:
        if word in positive_words:
            score += 1
        elif word in negative_words:
            score -= 1
    return score

def count_consonants(s):
    return len([c for c in s.lower() if c in 'bcdfghjklmnpqrstvwxyz'])

def generate_metrics(data):
    # Irrelevant metric computation (distractor)
    total_chars = sum(len(entry['comment']) for entry in data)
    avg_length = total_chars / len(data) if data else 0
    return {'total_chars': total_chars, 'avg_comment_len': avg_length}

def evaluate_performance(feedback_logs, config):
    sentiment_sum = 0
    valid_entries = 0
    temp_buffer = []

    for log in feedback_logs:
        comment = log.get('comment', '')
        source = log.get('source', '')
        
        # Real processing: only internal reviews are counted
        if source != 'internal':
            # Misleading: do some irrelevant processing
            placeholder = ''.join(sorted(set(comment)))
            temp_buffer.append(placeholder)
            continue
        
        # Only process internal feedback
        sentiment = analyze_sentiment(comment)
        weighted_score = sentiment * config['weights']['sentiment']
        
        # Additional filtering: ignore neutral comments
        if sentiment == 0:
            continue
            
        sentiment_sum += weighted_score
        valid_entries += 1

    # Compute base performance
    raw_performance = sentiment_sum / valid_entries if valid_entries > 0 else 0

    # Apply bonus based on comment structure (semi-relevant)
    internal_comments = [f['comment'] for f in feedback_logs if f.get('source') == 'internal']
    consonant_total = sum(count_consonants(c) for c in internal_comments)
    
    # Bonus logic: every 10 consonants gives +0.5 bonus, capped at 5
    structural_bonus = min(consonant_total // 10 * 0.5, 5)
    
    # Final score calculation
    final_score = raw_performance + structural_bonus
    
    # Dead code path (distractor)
    if False:
        fallback = generate_metrics(feedback_logs)
        final_score = max(final_score, fallback['avg_comment_len'])

    return final_score

# Main execution
feedback_logs = [
    {'comment': 'Great job on the project!', 'source': 'external'},
    {'comment': 'Poor effort, needs improvement.', 'source': 'internal'},
    {'comment': 'Excellent work, well done!', 'source': 'internal'},
    {'comment': 'Good start but could be better.', 'source': 'internal'},
    {'comment': 'Terrible outcome, very bad.', 'source': 'internal'},
    {'comment': 'Excellent and excellent again!', 'source': 'external'}
]

benchmark_config = {
    'weights': {
        'sentiment': 2.0
    },
    'thresholds': {
        'high': 3.0,
        'low': -1.0
    }
}

# Key statement
final_score = evaluate_performance(feedback_logs, benchmark_config)

print(f"Result: {final_score}")