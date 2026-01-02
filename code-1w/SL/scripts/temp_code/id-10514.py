def analyze_feedback(reviews):
    word_counts = {}
    total_chars = 0
    for review in reviews:
        words = review.lower().split()
        for word in words:
            cleaned = word.strip('.,!?"')
            word_counts[cleaned] = word_counts.get(cleaned, 0) + 1
        total_chars += len(review)

    avg_length = total_chars / len(reviews) if reviews else 0
    return word_counts, avg_length


def filter_sensitive_terms(word_freq, blocklist):
    filtered = {}
    removed_count = 0
    for term, freq in word_freq.items():
        if all(b not in term for b in blocklist):
            filtered[term] = freq
        else:
            removed_count += freq
    return filtered, removed_count

def compute_sentiment_bias(words):
    positive = ['good', 'excellent', 'great', 'well']
    negative = ['bad', 'poor', 'terrible', 'awful']
    pos_score = sum(words.get(p, 0) for p in positive)
    neg_score = sum(words.get(n, 0) for n in negative)
    return (pos_score - neg_score) / (pos_score + neg_score + 1)

def evaluate_performance(feedback, limit):
    temp_data = []
    for entry in feedback:
        temp_data.append(len(entry))
    sorted_data = sorted(temp_data)
    median_len = sorted_data[len(sorted_data)//2]

    if median_len > limit:
        adjustment = 1.1
    else:
        adjustment = 0.9

    base_score = 0
    for entry in feedback:
        if 'excellent' in entry.lower():
            base_score += 3
        elif 'good' in entry.lower():
            base_score += 2
        elif 'poor' in entry.lower():
            base_score -= 2

    final_score = int(base_score * adjustment)
    
    # Distractor variables
    outlier_count = 0
    cumulative_sum = 0
    for val in temp_data:
        cumulative_sum += val
        if val > 2 * median_len:
            outlier_count += 1

    return final_score

# Main execution
feedback_list = [
    "The service was excellent and very well executed.",
    "Good effort overall, but could improve timing.",
    "Poor communication led to confusion.",
    "Great work on coordination!",
    "Excellent delivery, good team alignment."
]

block_terms = ['spam', 'fake', 'scam']
threshold = 55

# Initial analysis (semi-relevant)
frequencies, average_length = analyze_feedback(feedback_list)
clean_frequencies, filtered_total = filter_sensitive_terms(frequencies, block_terms)sentiment_drift = compute_sentiment_bias(clean_frequencies)

# Core evaluation
final_score = evaluate_performance(feedback_list, threshold)

# Print result
print(f"Result: {final_score}")