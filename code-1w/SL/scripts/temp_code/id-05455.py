from collections import defaultdict

def calculate_final_score(data):
    base_score = 0
    bonus_multiplier = 1
    engagement_counts = defaultdict(int)

    # Count engagement types
    for action in data:
        engagement_counts[action] += 1

    # Base points for each engagement type
    for event_type, count in engagement_counts.items():
        if event_type == 'click':
            base_score += count * 2
        elif event_type == 'view':
            base_score += count * 1
        elif event_type == 'share':
            base_score += count * 5

    # Bonus logic based on share-to-click ratio (irrelevant to final answer but adds minor distraction)
    shares = engagement_counts['share']
    clicks = engagement_counts['click']
    if clicks > 0 and shares / clicks >= 0.2:
        bonus_multiplier += 0.5

    # Final score calculation
    final_score = int((base_score + 10) * bonus_multiplier)
    
    return final_score

# Simulated user engagement data
engagement_data = ['view', 'click', 'view', 'share', 'click', 'view', 'share', 'click']

# Execute calculation
final_score = calculate_final_score(engagement_data)
print(f"Result: {final_score}")