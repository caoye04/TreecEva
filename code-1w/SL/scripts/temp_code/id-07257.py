from collections import defaultdict, Counter

# Simulate employee review data across departments
def generate_feedback():
    raw_scores = [4.2, 3.8, 4.5, 4.0, 3.9, 4.3, 4.1, 3.7]
    comments = [
        'excellent teamwork', 'good initiative', 'needs improvement',
        'strong leadership', 'reliable performer', 'innovative thinking',
        'consistent quality', 'average contribution'
    ]
    
    feedback = defaultdict(list)
    for i, score in enumerate(raw_scores):
        category = 'positive' if score >= 4.0 else 'developmental'
        sentiment_words = set(comment.lower().split() for comment in comments)[i]
        word_count = len(sentiment_words)
        adjusted = round(score * (1 + 0.05 * (word_count - 2)), 2)  # minor adjustment
        feedback[category].append(adjusted)
    
    return feedback

# Analyze textual trends (distractor function - not directly used)
def analyze_sentiment_trends(texts):
    word_freq = Counter()
    for text in texts:
        words = text.lower().replace(',', '').split()
        word_freq.update(words)
    
    top_words = [w for w, c in word_freq.most_common(3)]
    distraction_value = sum(ord(c) for w in top_words for c in w) % 7  # irrelevant
    return distraction_value

# Core evaluation logic
def evaluate_performance(feedback_map):
    base_values = []
    temp_offsets = []
    
    for category, scores in feedback_map.items():
        avg_score = sum(scores) / len(scores)
        count = len(scores)
        
        # Apply conditional weighting
        if category == 'positive':
            weight = 1.1
        else:
            weight = 0.9
            
        weighted_avg = avg_score * weight
        base_values.append(weighted_avg)
        
        # Some red herring computation
        for s in scores:
            temp_offsets.append((s ** 2) % 3)  # unused later
    
    # Real logic path
    aggregate = sum(base_values)
    penalty = 0
    
    # Additional interference: unrelated bitwise check
    flag_state = 0b1010
    for val in temp_offsets[:3]:
        flag_state ^= int(val)
        if flag_state & 0b100:  # early trigger condition (irrelevant)
            penalty += 0.05

    final_aggregate = aggregate - penalty
    rounded_result = round(final_aggregate, 2)
    
    # Key assignment point
    final_score = int(rounded_result * 100)  # scale to integer for reporting
    
    return final_score

# Main execution flow
data = generate_feedback()
feedback_summary = dict(data)  # snapshot for analysis

# Distractor: analyze comments (not affecting main result)
distraction_comments = [
    'excellent teamwork', 'good initiative', 'needs improvement',
    'strong leadership', 'reliable performer', 'innovative thinking',
    'consistent quality', 'average contribution'
]
noise_level = analyze_sentiment_trends(distraction_comments)
status_flag = (noise_level ^ 5) | 2

# Critical statement
final_score = evaluate_performance(feedback_summary)

print(f"Result: {final_score}")