import itertools

# Simulate user feedback analysis for a product review system
def analyze_sentiment(text):
    words = text.lower().split()
    positive = ['good', 'great', 'excellent', 'amazing', 'love']
    negative = ['bad', 'terrible', 'awful', 'hate', 'worst']
    score = 0
    for word in words:
        cleaned = word.strip('.,!?:;')
        if cleaned in positive:
            score += 1
        elif cleaned in negative:
            score -= 2
    return max(-3, min(3, score))

# Extract key phrases using sliding window
def extract_phrases(text, n=2):
    words = text.lower().strip('.,!').split()
    phrases = [' '.join(words[i:i+n]) for i in range(len(words)-n+1)]
    return set(phrases)

# Main processing function with distraction
def process_ratings(feedback_list, importance_weights):
    raw_scores = []
    temp_aggregates = []
    phrase_pool = set()

    # Real computation: sentiment scoring
    for entry in feedback_list:
        sentiment = analyze_sentiment(entry['comment'])
        multiplier = entry['verified'] * 0.5 + 1  # Boost verified users
        adjusted = sentiment * multiplier
        raw_scores.append(adjusted)
        
        # Distractor: collect phrases (semi-relevant but unused later)
        phrases = extract_phrases(entry['comment'])
        phrase_pool.update(phrases)

    # Distractor: complex but irrelevant pairing logic
    paired_combinations = list(itertools.combinations(raw_scores, 2))
    pair_sums = [abs(a - b) for a, b in paired_combinations]
    if pair_sums:
        avg_deviation = sum(pair_sums) / len(pair_sums)
        temp_aggregates.append(avg_deviation * 0.1)

    # Real path: weighted average computation
    total_weighted = 0
    sum_of_weights = 0
    
    for i, score in enumerate(raw_scores):
        weight = importance_weights[i % len(importance_weights)]
        # Artificial complexity: filter extremes that don't trigger
        if abs(score) == 3 and '!' not in feedback_list[i]['comment']:
            continue  # Rare condition, mostly skipped
        total_weighted += score * weight
        sum_of_weights += weight
    
    normalized_avg = total_weighted / sum_of_weights if sum_of_weights else 0
    
    # Secondary adjustment based on length distribution (distractor calculation)
    lengths = [len(entry['comment'].split()) for entry in feedback_list]
    median_length = sorted(lengths)[len(lengths)//2]
    length_bias = (median_length - 5) * 0.05  # Irrelevant to final result
    
    # Final computation chain
    base_result = round(normalized_avg * 10) / 10
    stability_factor = 1 + (0.01 * len(paired_combinations))  # Negligible effect
    final_score = int((base_result + 10) * 5 + 0.5)  # Scale to 0-100 range
    
    # This print is required
    print(f"Result: {final_score}")
    return final_score

# Input data
user_feedback = [
    {'comment': 'This is excellent! I love the design.', 'verified': True},
    {'comment': 'Terrible quality, hate it.', 'verified': False},
    {'comment': 'Amazing value for money, great product.', 'verified': True},
    {'comment': 'Not bad, pretty good overall.', 'verified': True},
    {'comment': 'Worst purchase ever!', 'verified': False}
]

weights = [0.8, 1.2, 1.0, 0.9]

# Key execution point
final_score = process_ratings(user_feedback, weights)