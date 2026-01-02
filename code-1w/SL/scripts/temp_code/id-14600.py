def analyze_feedback(text_data):
    words = text_data.lower().split()
    word_freq = {}
    for word in words:
        cleaned = ''.join(ch for ch in word if ch.isalnum())
        if cleaned:
            word_freq[cleaned] = word_freq.get(cleaned, 0) + 1

    sentiment_keywords = {'good': 1, 'excellent': 2, 'poor': -1, 'bad': -2, 'average': 0}
    total_sentiment = 0
    keyword_count = 0
    for w in word_freq:
        if w in sentiment_keywords:
            total_sentiment += sentiment_keywords[w] * word_freq[w]
            keyword_count += word_freq[w]

    avg_sentiment = total_sentiment / keyword_count if keyword_count else 0
    return {'sentiment': total_sentiment, 'density': keyword_count / len(words), 'length_penalty': len(words) > 50}


def calculate_threshold(base, adjustment_factor=0.75):
    temp_result = 0
    for i in range(1, 10):
        temp_result += (base % i) if i % 2 == 0 else 0  # Irrelevant accumulation
    meaningful_adjustment = base * adjustment_factor
    return int(meaningful_adjustment)


def evaluate_performance(log_entries, min_threshold):
    aggregated = []
    noise_counter = 0
    for entry in log_entries:
        analysis = analyze_feedback(entry)
        score = analysis['sentiment']
        
        # Distractor: complex but unused computation
        if analysis['density'] > 0.1:
            penalty = 1 if analysis['length_penalty'] else 0
            noise_counter += penalty
        
        if abs(score) >= min_threshold:
            adjusted = score * 2 if score > 0 else score * 1.5
            aggregated.append(adjusted)
    
    final_score = sum(aggregated)
    return final_score

# Main execution
feedback_strings = [
    "The service was excellent and really good, very good experience",
    "Poor and bad attitude from staff, poor overall",
    "Average performance, nothing special but not bad either",
    "Excellent work! Everything was perfect and excellent again",
    "Good, good, good – consistently good service"
]

base_metric = 3
threshold = calculate_threshold(base_metric)
feedback_log = feedback_strings

# Key statement
final_score = evaluate_performance(feedback_log, threshold)
print(f"Result: {final_score}")