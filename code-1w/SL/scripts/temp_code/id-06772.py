from collections import defaultdict

# Simulate user feedback analysis with signal filtering
def analyze_feedback(raw_logs):
    counts = defaultdict(int)
    for log in raw_logs:
        action = log.split('_')[0]
        if action in ['upvote', 'downvote', 'skip']:
            counts[action] += 1

    total_interactions = sum(counts.values())
    upvote_ratio = counts['upvote'] / total_interactions if total_interactions else 0
    downvote_ratio = counts['downvote'] / total_interactions if total_interactions else 0
    
    # Irrelevant metric (distractor)
    avg_length = sum(len(log) for log in raw_logs) / len(raw_logs) if raw_logs else 0
    normalized_bias = (upvote_ratio - downvote_ratio) * 100
    
    return upvote_ratio, normalized_bias, avg_length

# Assess content coherence across segments
def assess_coherence(text_segments):
    word_freq = {}
    for segment in text_segments:
        words = segment.lower().split()
        for word in words:
            cleaned = ''.join(filter(str.isalpha, word))
            if cleaned:
                word_freq[cleaned] = word_freq.get(cleaned, 0) + 1
    
    repeated_words = [w for w, c in word_freq.items() if c > 1]
    repetition_score = len(repeated_words) / len(word_freq) if word_freq else 0
    
    # Dead computation path (distractor)
    unique_ngrams = set()
    for segment in text_segments:
        tokens = segment.split()
        for i in range(len(tokens) - 1):
            unique_ngrams.add((tokens[i], tokens[i+1]))
    bigram_density = len(unique_ngrams) / sum(len(s.split()) for s in text_segments) if text_segments else 0
    
    return repetition_score, bigram_density

# Main evaluation logic
def evaluate_performance(feedback_seq, base_val):
    # Extract metrics
    up_ratio, bias_metric, _ = analyze_feedback(feedback_seq)
    rep_score, _ = assess_coherence([
        'the quick brown fox jumps over the lazy dog',
        'a brown fox is quick and jumps high',
        'lazy dogs lie still'
    ])
    
    # Core calculation chain
    adjustment_factor = (1 + rep_score) * (1 - abs(bias_metric) / 100)
    intermediate_score = base_val * adjustment_factor
    
    # Multiple assignment (relevant)
    alpha, beta = intermediate_score * 0.7, intermediate_score * 0.3
    
    # Misleading transformation (distractor)
    temp_buffer = []
    for i in range(5):
        temp_buffer.append((i, alpha / (i + 1), beta * (i + 1)))
    
    # Actual score refinement
    stability_penalty = 0.95 if rep_score > 0.2 else 1.0
    final_raw = (alpha + beta) * stability_penalty
    
    # Final scaling based on interaction volume
    volume_multiplier = 1.1 if len(feedback_seq) >= 8 else 1.0
    final_score = int(final_raw * volume_multiplier)
    
    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Input data
feedback_chain = [
    'upvote_action', 'upvote_submission', 'skip_navigation', 'downvote_comment',
    'upvote_refresh', 'skip_timeout', 'upvote_confirm', 'downvote_error',
    'skip_retry'
]
base_rating = 85

# Execute
final_score = evaluate_performance(feedback_chain, base_rating)