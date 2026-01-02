import itertools

def analyze_sentiment(tone_profile):
    sentiment_sum = 0
    for tone in tone_profile:
        if tone == 'positive':
            sentiment_sum += 1
        elif tone == 'negative':
            sentiment_sum -= 0.5
    return sentiment_sum

def compute_stability_index(pattern):
    stability = 0
    for i in range(len(pattern) - 1):
        if pattern[i] == pattern[i + 1]:
            stability += 0.1
    return stability

def evaluate_performance(feedbacks, metrics):
    # Irrelevant preprocessing: reverse and slice (distractor)
    processed = feedbacks[::-1][:len(feedbacks)]
    
    # Real computation starts here
    base_score = metrics['initial'] * 0.3
    adjustment = 0
    
    # Count positive feedback streaks using itertools
    streaks = [len(list(group)) for key, group in itertools.groupby(feedbacks) if key == 'positive']
    max_streak = max(streaks) if streaks else 0
    adjustment += max_streak * 2
    
    # Misleading intermediate calculation (not used in final score)
    avg_gap = 0
    positions = [i for i, f in enumerate(feedbacks) if f == 'positive']
    if len(positions) > 1:
        gaps = [positions[i+1] - positions[i] for i in range(len(positions)-1)]
        avg_gap = sum(gaps) / len(gaps) if gaps else 0
    
    # Another distractor: stability index (computed but not impactful)
    _ = compute_stability_index(feedbacks)
    
    # Key logic: sentiment analysis contributes to adjustment
    sentiment_value = analyze_sentiment(feedbacks)
    if sentiment_value > 2:
        adjustment += 3
    
    # Conditional bonus based on length pattern
    if len(feedbacks) % 4 == 0:
        bonus_factor = 1.5
    else:
        bonus_factor = 1.0
    
    # Final score calculation
    final_score = base_score + adjustment
    final_score *= bonus_factor  # Apply bonus
    
    # Dead code path (never executed due to prior logic)
    if False:
        final_score = abs(final_score) * 0.1
    
    return int(final_score)

# Main execution
feedback_sequence = ['positive', 'positive', 'negative', 'positive', 'positive', 'positive', 'neutral']
base_metrics = {
    'initial': 50,
    'weight': 0.7,
    'offset': 12
}

intermediate_total = sum(1 for f in feedback_sequence if f == 'neutral')  # Distractor
shadow_copy = feedback_sequence[:]  # Irrelevant copy

final_score = evaluate_performance(feedback_sequence, base_metrics)
print(f"Target result: {final_score}")