def evaluate_performance(revenue_str, target_revenue, team_size):
    base_score = 100
    revenue = int(revenue_str.replace(',', ''))
    achievement_rate = revenue / target_revenue
    
    # Determine adjustment based on achievement rate
    adjustment = 20 if achievement_rate >= 1.1 else (10 if achievement_rate >= 0.9 else 0)
    adjusted_base = base_score * (1 + adjustment / 100)
    
    # Performance bonus based on team efficiency
    efficiency_factor = 1.5 if team_size <= 5 else 1.2
    raw_bonus = 15 * efficiency_factor
    performance_bonus = int(raw_bonus) if achievement_rate > 1.0 else 0
    
    final_score = adjusted_base + performance_bonus
    return final_score

# Execute with realistic input
team_revenue = "1,150,000"
result = evaluate_performance(team_revenue, 1000000, 4)
print(f"Result: {result}")