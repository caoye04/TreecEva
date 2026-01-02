def calculate_rating(data):
    base_score = 0
    penalty_adjustment = 0
    bonus_multiplier = 1.0
    
    # Irrelevant distraction: initialize unused metrics
    avg_latency = sum(data.get('latency_history', [0])) / len(data.get('latency_history', [1]))
    peak_load = max(data.get('system_load', [1]))

    # Real logic begins: analyze engagement trends
    views = data['views']
    likes = data['likes']
    shares = data['shares']
    duration = data['avg_watch_time']

    if views > 10000:
        base_score += 25
        if likes > 500:
            base_score += 15
            if likes / views > 0.05:
                bonus_multiplier *= 1.2
    
    if shares > 0:
        base_score += 10
        if shares / views > 0.02:
            bonus_multiplier *= 1.15

    # Distractor: complex but unused calculation
    predicted_growth = 0
    for i in range(3):
        predicted_growth += views * (1.05 ** i)
    predicted_growth = int(predicted_growth / 3)

    # Duration-based tier evaluation
    if duration >= 180:
        base_score += 20
    elif duration >= 90:
        base_score += 10
    else:
        penalty_adjustment -= 5

    # Unused helper structure
    status_flags = {
        'high_engagement': views > 5000 and likes > 250,
        'viral_potential': shares > 0 and (shares / views) > 0.03,
        'at_risk': duration < 60 and likes < 100
    }

    # Final score computation - only base_score and bonus_multiplier matter
    raw_score = base_score + penalty_adjustment
    final_score = raw_score * bonus_multiplier

    return int(final_score)

# Main execution
engagement_data = {
    'views': 15000,
    'likes': 900,
    'shares': 450,
    'avg_watch_time': 210,
    'latency_history': [120, 135, 110, 150],
    'system_load': [0.7, 0.8, 0.75]
}

final_score = calculate_rating(engagement_data)
print(f"Result: {final_score}")