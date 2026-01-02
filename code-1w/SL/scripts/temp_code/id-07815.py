def evaluate_performance(records, importance):
    base_score = 0
    penalty_adjustment = 0
    temp_sum = 0
    outlier_count = 0

    # Irrelevant pre-scan: counts string lengths (distractor)
    metadata = [len(str(r)) for r in records]
    avg_metadata = sum(metadata) / len(metadata) if metadata else 0

    # Real logic begins: classify and score based on thresholds
    high_performers = 0
    for value in records:
        if value > 85:
            base_score += value * importance.get('high', 1.2)
            high_performers += 1
        elif value > 60:
            base_score += value * importance.get('medium', 1.0)
        else:
            penalty_adjustment -= 5
            outlier_count += 1  # Tracked but only partially used

    # Secondary adjustment using lambda (required feature)
    volatility_filter = list(map(lambda x: abs(x - 75)**0.5, records))
    stability_bonus = 10 if sum(volatility_filter) < 40 else 0

    # Complex conditional with nested structure (3 levels deep)
    if high_performers >= 3:
        tier_bonus = 25
        if outlier_count == 0:
            tier_bonus += 10
        else:
            # Dead code path: won't execute due to conditions above
            if avg_metadata > 100:
                tier_bonus += 5  # Never reached
    else:
        tier_bonus = 0

    # Additional distraction: unused intermediate calculation
    projected_next = (sum(records) / len(records)) * 1.05 + penalty_adjustment

    # Final score computation (key line)
    final_score = base_score + penalty_adjustment + stability_bonus + tier_bonus
    
    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Input data
data = [90, 88, 92, 76, 55]
weights = {'high': 1.2, 'medium': 1.0}

# Execute
final_score = evaluate_performance(data, weights)