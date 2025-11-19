def calculate_fleet_performance():
    regions = [
        {'name': 'northeast', 'vehicles': 12, 'fuel_efficiency': [8.2, 7.9, 9.1, 8.7, 7.5, 8.3, 9.0, 8.8, 7.6, 8.4, 9.2, 8.1]},
        {'name': 'southwest', 'vehicles': 8, 'fuel_efficiency': [9.5, 10.2, 9.8, 10.1, 9.3, 9.7, 10.0, 9.6]},
        {'name': 'midwest', 'vehicles': 15, 'fuel_efficiency': [7.8, 8.0, 7.9, 8.2, 8.1, 7.7, 8.3, 8.4, 7.6, 8.5, 7.9, 8.0, 8.2, 8.1, 7.8]}
    ]
    
    regional_scores = {}
    for region in regions:
        avg_efficiency = sum(region['fuel_efficiency']) / len(region['fuel_efficiency'])
        utilization_rate = min(1.0, region['vehicles'] / 10.0)
        regional_scores[region['name']] = avg_efficiency * utilization_rate
    
    # Apply penalty for underperforming regions
    penalties = {name: 0.9 if score < 8.0 else 1.0 for name, score in regional_scores.items()}
    adjusted_scores = {name: score * penalties[name] for name, score in regional_scores.items()}
    
    # Calculate weighted average based on vehicle count
    total_vehicles = sum(region['vehicles'] for region in regions)
    weighted_sum = sum(adjusted_scores[region['name']] * region['vehicles'] for region in regions)
    
    # Short-circuit evaluation for bonus calculation
    has_bonus = total_vehicles > 30 and weighted_sum > 250
    bonus_factor = 1.1 if has_bonus else 1.0
    
    base_performance = weighted_sum / total_vehicles
    final_performance_score = int(base_performance * bonus_factor * 100)
    
    return final_performance_score

result = calculate_fleet_performance()
print(f"Result: {result}")