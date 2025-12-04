def calculate_delivery_metrics(distances, traffic_factors):
    # Calculate adjusted distances based on traffic
    adjusted_distances = []
    for i, (dist, factor) in enumerate(zip(distances, traffic_factors)):
        weather_penalty = (i % 3) * 0.5  # Weather affects every third route more
        adjusted = dist * factor + weather_penalty
        adjusted_distances.append(adjusted)
    
    # Calculate fuel consumption (not used in final calculation)
    fuel_rates = [2.5, 3.2, 2.8, 3.0, 2.7]
    fuel_consumption = [d * rate for d, rate in zip(distances, fuel_rates[:len(distances)])]
    total_fuel = sum(fuel_consumption)  # Distractor calculation
    
    # Determine time estimates
    avg_speed = 50  # km/h
    time_estimates = [d / avg_speed for d in adjusted_distances]
    
    # Find routes with time less than threshold (distractor)
    quick_routes = [i for i, t in enumerate(time_estimates) if t < 0.5]
    
    # Prioritize routes based on combined score
    priority_scores = []
    for i, (dist, time) in enumerate(zip(adjusted_distances, time_estimates)):
        # Calculate a priority score - lower is better
        importance_factor = 5 if i in quick_routes else 1  # Distractor
        score = dist * 0.7 + time * 60  # Convert time to minutes
        priority_scores.append(score)
    
    # Create route options with route number and score
    route_options = [(i+1, score) for i, score in enumerate(priority_scores)]
    
    # Additional sorting for visualization (distractor)
    sorted_routes = sorted(route_options, key=lambda x: x[1])
    
    # Find the optimal route (lowest score)
    optimal_route = min(route_options, key=lambda x: x[1])[0]
    
    # Calculate efficiency ratio (distractor)
    efficiency = total_fuel / sum(adjusted_distances)
    
    print(f"Route options: {route_options}")
    print(f"Result: {optimal_route}")
    return optimal_route

# Test data
distances = [12, 8, 15, 10, 7]
traffic_factors = [1.2, 1.0, 1.5, 1.3, 1.1]

calculate_delivery_metrics(distances, traffic_factors)