def analyze_efficiency(values):
    weighted = [v * (i + 1) for i, v in enumerate(values)]
    return sum(weighted) / len(weighted) if weighted else 0

# Simulate employee performance metrics across quarters
def process_performance(metrics, bonuses):
    base_scores = []
    adjustment_log = []
    total_bonus_allocated = 0
    
    for idx, (name, score) in enumerate(zip(['Q1', 'Q2', 'Q3', 'Q4'], metrics)):
        if score < 60:
            adjusted = score * 1.1
        elif score > 90:
            adjusted = score * 1.05
        else:
            adjusted = score + 3
            
        # Track adjustments for audit (some are distractions)
        adjustment_log.append(f'{name}: {score}->{adjusted:.1f}')
        base_scores.append(adjusted)
    
    # Calculate composite efficiency with weighted quarters
    efficiency = analyze_efficiency(base_scores)
    
    # Bonus logic with red herring computation
    projected_growth = 0.0
    for b in bonuses:
        projected_growth += b * 1.75  # Not actually used later
    
    # Apply only real bonus impact: count how many exceed threshold
    bonus_count = sum(1 for b in bonuses if b > 8000)
    total_bonus_allocated = sum(bonuses)  # Distractor
    
    # Final scoring with conditional modifiers
    final_score = efficiency * (1 + 0.02 * bonus_count)
    
    # Irrelevant string processing to increase cognitive load
    report_key = ''.join([s[0] for s in ['Alpha', 'Beta', 'Gamma']]).lower()
    metadata_tag = f"{report_key}_{len(bonuses)}"
    
    # Dead code branch (never executed but looks relevant)
    if len(metadata_tag) > 10:
        final_score *= 0.9
    
    return int(round(final_score))

# Input data
performance_metrics = [78, 85, 92, 73]
bonus_awards = [7500, 9200, 8800, 7900]

# Execute main logic
final_score = process_performance(performance_metrics, bonus_awards)
print(f"Result: {final_score}")