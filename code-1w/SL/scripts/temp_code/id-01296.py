from collections import Counter

def analyze_text_patterns(input_str):
    words = input_str.lower().split()
    word_counter = Counter(words)
    unique_count = len(word_counter)
    total_length = sum(len(word) for word in words)
    avg_word_len = total_length / len(words) if words else 0
    
    # Distractor: irrelevant transformation
    reversed_map = {word: word[::-1] for word in words}
    palindrome_count = sum(1 for w in words if w == w[::-1])
    
    return unique_count, avg_word_len

def extract_keywords(text, min_len=4):
    filtered = [word.strip('.,!?"') for word in text.split() if len(word.strip('.,!?"')) >= min_len]
    freq_dist = {}
    for word in filtered:
        freq_dist[word] = freq_dist.get(word, 0) + 1
    
    # Dead code path (never used)
    if False:
        temp_result = [w.upper() for w in filtered if 'e' in w]
        return temp_result
    
    return list(set(filtered))

def calculate_entropy(values):
    from math import log2
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        p = v / total
        if p > 0:
            entropy -= p * log2(p)
    return round(entropy, 4)

def evaluate_performance(feedbacks, keywords):
    scores = []
    seen_keywords = set()
    keyword_hits = 0
    
    for fb in feedbacks:
        fb_lower = fb.lower()
        # Check for keyword matches
        for kw in keywords:
            if kw.lower() in fb_lower:
                keyword_hits += 1
                seen_keywords.add(kw)
                break  # Count only first match per feedback
        
        # Extract sentiment clues (simplified heuristic)
        positive_clues = sum(fb.count(w) for w in ['good', 'excellent', 'great', 'well'])
        negative_clues = sum(fb.count(w) for w in ['poor', 'bad', 'terrible', 'awful'])
        net_sentiment = positive_clues - negative_clues
        
        # Use lambda to compute weighted contribution
        weight_fn = lambda x, y: x + 2 * y if x > 0 else max(0, y)
        base_score = weight_fn(net_sentiment, keyword_hits)
        scores.append(base_score)
    
    # Intermediate distractor: unused statistical measure
    mean_score = sum(scores) / len(scores) if scores else 0
    score_variance = sum((s - mean_score) ** 2 for s in scores) / len(scores) if scores else 0
    
    # Real computation path
    adjustment_factor = len(seen_keywords) * 3
    penalty = 2 * (len(feedbacks) - keyword_hits)
    raw_total = sum(scores)
    final_score = raw_total + adjustment_factor - penalty
    
    # Additional red herring
    debug_info = {'raw': raw_total, 'adjust': adjustment_factor, 'penalty': penalty}
    
    return int(final_score)

# Main execution block
if __name__ == "__main__":
    user_feedback = [
        "The system performed excellently and handled requests well.",
        "Poor response time, but good documentation helped.",
        "Great overall experience, especially the excellent interface.",
        "Bad design choices, though implementation was great.",
        "Well executed, great work on performance optimization."
    ]
    
    # Extract meaningful terms (distractor usage)
    all_text = ' '.join(user_feedback)
    _, _ = analyze_text_patterns(all_text)  # Results ignored
    
    # Core keyword list
    target_words = ['excellent', 'great', 'well', 'good']
    
    # Evaluate performance based on keyword presence and sentiment
    final_score = evaluate_performance(user_feedback, target_words)
    
    # Print result as required
    print(f"Target result: {final_score}")