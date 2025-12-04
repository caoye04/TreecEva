def calculate_delivery_efficiency(distances, traffic_factors):
    # Initialize efficiency metrics
    fuel_consumption = [12, 15, 10, 18, 14]
    route_popularity = [0.8, 0.5, 0.9, 0.3, 0.6]
    environmental_impact = [3, 5, 2, 7, 4]
    
    # Process traffic conditions
    adjusted_traffic = []
    for idx, factor in enumerate(traffic_factors):
        # Apply time-of-day adjustment
        hour_modifier = (idx * 3) % 24
        rush_hour_penalty = 1.5 if 7 <= hour_modifier <= 9 or 16 <= hour_modifier <= 18 else 1.0
        weather_condition = idx % 3  # 0:clear, 1:rain, 2:snow
        weather_multiplier = 1.0 if weather_condition == 0 else 1.2 if weather_condition == 1 else 1.4
        
        adjusted_value = factor * rush_hour_penalty * weather_multiplier
        adjusted_traffic.append(adjusted_value)
    
    # Calculate route scores - lower is better
    route_scores = []
    for i in range(len(distances)):
        # Primary calculation
        base_score = distances[i] * adjusted_traffic[i]
        
        # Apply efficiency modifiers
        eco_factor = fuel_consumption[i] / 10
        popularity_bonus = 1 - (route_popularity[i] if route_popularity[i] < 0.7 else 0.7)
        environmental_penalty = environmental_impact[i] * 0.5
        
        # Irrelevant calculations for distraction
        potential_savings = (fuel_consumption[i] * distances[i]) // 100
        driver_preference = (i * 7 + 3) % 10 / 10
        scenic_rating = (i ** 2 + 1) % 5
        
        # Final score calculation (only some factors actually matter)
        route_score = base_score * eco_factor + environmental_penalty
        if i % 2 == 0:  # This condition is actually relevant
            route_score += 2  # Small penalty for even-indexed routes
        
        # More distractions that don't affect the result
        if scenic_rating > 3:
            potential_alternate = base_score * 0.9
        else:
            potential_alternate = base_score * 1.1
            
        route_scores.append(route_score)
    
    return route_scores

# Main delivery planning
def optimize_delivery_route():
    # Initialize route data
    city_distances = [45, 32, 18, 55, 27]
    current_traffic = [1.2, 0.8, 1.5, 0.9, 1.1]
    
    # Distracting variables and calculations
    package_counts = [12, 8, 15, 10, 5]
    customer_priority = [2, 1, 3, 1, 2]  # 3 highest, 1 lowest
    time_windows = [(9, 12), (10, 14), (13, 16), (14, 17), (9, 11)]
    
    # Process package weights - distraction
    total_weight = 0
    for count in package_counts:
        weight_per_package = count * 0.5 + 2
        total_weight += count * weight_per_package
    
    # Calculate delivery time windows - distraction
    delivery_minutes = []
    for start, end in time_windows:
        window_size = end - start
        minutes = window_size * 60
        delivery_minutes.append(minutes)
    
    # Get route scores
    route_scores = calculate_delivery_efficiency(city_distances, current_traffic)
    
    # Apply priority adjustments - this doesn't actually affect the result
    priority_adjusted = []
    for i in range(len(route_scores)):
        # This looks important but doesn't change the optimal route
        if customer_priority[i] == 3:
            adjusted = route_scores[i] * 0.9
        elif customer_priority[i] == 1:
            adjusted = route_scores[i] * 1.1
        else:
            adjusted = route_scores[i]
        priority_adjusted.append(adjusted)
    
    # More distraction calculations
    estimated_profits = []
    for i in range(len(city_distances)):
        base_profit = 100 - city_distances[i] * 0.5
        # These complex calculations don't matter for the final result
        volume_factor = (package_counts[i] ** 2) / 100
        time_efficiency = delivery_minutes[i] / 120
        potential_profit = base_profit * (1 + volume_factor - time_efficiency)
        estimated_profits.append(potential_profit)
    
    # Calculate possible routes (the actual answer comes from here)
    possible_routes = []
    for i in range(len(route_scores)):
        # Only these two factors actually matter
        real_score = city_distances[i] * current_traffic[i]
        if i % 2 == 0:
            real_score += 2
        possible_routes.append(real_score)
    
    # Find the optimal route (lowest score)
    optimal_route = min(possible_routes)
    
    # Distracting final calculations that aren't used
    alternative_route = sum(possible_routes) / len(possible_routes)
    max_profit_route = max(estimated_profits)
    
    print(f"Result: {optimal_route}")
    return optimal_route

# Execute the optimization
final_route = optimize_delivery_route()