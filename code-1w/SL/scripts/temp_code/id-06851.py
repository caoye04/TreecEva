def analyze_sentiment(text):
    positive_words = {'great', 'good', 'excellent', 'outstanding'}
    negative_words = {'bad', 'poor', 'terrible', 'awful'}
    words = text.lower().split()
    pos_count = len([w for w in words if w in positive_words])
    neg_count = len([w for w in words if w in negative_words])
    return (pos_count - neg_count) * 10

employee_data = [
    {'name': 'alice', 'rating': 4.2, 'review': 'great work and excellent attitude'},
    {'name': 'bob', 'rating': 3.8, 'review': 'good effort but bad time management'},
    {'name': 'carol', 'rating': 4.6, 'review': 'outstanding performance overall'}
]

summary_stats = {}
total_rating = 0
high_performers = 0
sentiment_shift = 0

for emp in employee_data:
    emp_id = emp['name']
    base_score = emp['rating'] * 100
    sentiment_bonus = analyze_sentiment(emp['review'])
    adjusted_score = base_score + sentiment_bonus
    
    if emp['rating'] >= 4.5:
        high_performers += 1
        adjusted_score += 20
    elif emp['rating'] >= 3.5:
        adjusted_score += 5
    else:
        adjusted_score -= 10
    
    # Track stats (some used later)
    summary_stats[emp_id] = {
        'base': base_score,
        'bonus': sentiment_bonus,
        'final': adjusted_score
    }
    total_rating += emp['rating']

# Compute averages (distractor computations)
avg_rating = total_rating / len(employee_data)
dummy_variance = sum((emp['rating'] - avg_rating)**2 for emp in employee_data) / len(employee_data)

# Simulate feedback aggregation
text_corpus = ' '.join([e['review'] for e in employee_data])
word_frequency = {}
for word in text_corpus.lower().split():
    word_frequency[word] = word_frequency.get(word, 0) + 1

frequent_words = {w: c for w, c in word_frequency.items() if c > 1}
feedback_summary = {
    'sentiment_shift': sum(analyze_sentiment(e['review']) for e in employee_data),
    'dominant_review': 'positive' if len(frequent_words) > 3 else 'neutral',
    'high_performer_count': high_performers,
    'total_base_score': sum(s['base'] for s in summary_stats.values())
}

# Misleading normalization step (not affecting final answer)
normalized_shift = feedback_summary['sentiment_shift'] / max(1, len(employee_data))
scaling_factor = 1.0 if feedback_summary['dominant_review'] == 'positive' else 0.8

# Key evaluation function
def evaluate_performance(feedback):
    base = feedback['total_base_score']
    shift = feedback['sentiment_shift']
    count = feedback['high_performer_count']
    
    # Complex conditional logic with red herring variables
    multiplier = 1.1 if count >= 2 else 1.0
    adjustment = 50 if shift > 20 else 0
    
    # Core calculation
    preliminary = base + shift + adjustment
    
    # Distractor branch (never taken due to data)
    if feedback['dominant_review'] == 'negative':
        preliminary *= 0.9
    
    # Final score computation
    result = int(preliminary * multiplier)
    
    # Dead code path (irrelevant)
    if result < 0:
        return 0
        extra_penalty = result * 0.1  # unreachable
    
    return result

# Execution point of interest
final_score = evaluate_performance(feedback_summary)
print(f"Result: {final_score}")