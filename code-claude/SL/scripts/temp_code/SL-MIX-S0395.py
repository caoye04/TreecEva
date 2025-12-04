from collections import defaultdict, Counter
import math

# Data processing for urban planning distance optimization
def calculate_city_metrics(locations, thresholds):
    # Calculate various metrics that might be useful
    density_scores = defaultdict(int)
    proximity_values = []
    
    # Process each location and threshold
    for loc in locations:
        # Extract coordinates and apply transformations
        x, y = loc
        transformed_x = x * 1.5 - 20
        transformed_y = y * 0.8 + 15
        
        # Calculate density score based on quadrant
        quadrant = 1 if x > 0 and y > 0 else 2 if x < 0 and y > 0 else 3 if x < 0 and y < 0 else 4
        density_scores[quadrant] += 1
        
        # Calculate proximity value
        proximity = math.sqrt(transformed_x**2 + transformed_y**2)
        proximity_values.append(proximity)
    
    # Find the most common quadrant
    quadrant_counts = Counter(density_scores)
    most_common = quadrant_counts.most_common(1)[0][0] if quadrant_counts else 0
    
    # Apply threshold filters
    filtered_values = [val for val in proximity_values if val > thresholds[0]]
    
    return filtered_values, most_common, density_scores

# Main urban planning optimization algorithm
def optimize_urban_distances():
    # Sample location data (x, y coordinates)
    location_data = [(5, 10), (-3, 7), (8, -4), (-2, -9), (4, 6)]
    
    # Various threshold configurations for testing
    threshold_configs = [
        [10, 20, 30],  # Standard thresholds
        [5, 15, 25],   # Lower thresholds
        [15, 25, 35]   # Higher thresholds
    ]
    
    # Track optimization metrics
    all_distances = []
    efficiency_scores = {}
    optimal_threshold = None
    
    # Process different threshold configurations
    for i, thresholds in enumerate(threshold_configs):
        # Calculate metrics for this configuration
        proximity_values, dominant_quadrant, density = calculate_city_metrics(location_data, thresholds)
        
        # Calculate distance metrics
        if dominant_quadrant in [1, 3]:  # Prioritize diagonal quadrants
            distances = [val * 0.8 for val in proximity_values]
        else:
            distances = [val * 1.2 for val in proximity_values]
        
        # Apply correction factor based on density
        correction = sum(density.values()) / len(density) if density else 1
        adjusted_distances = [d * correction for d in distances]
        
        # Store metrics
        all_distances.extend(adjusted_distances)
        efficiency_scores[i] = sum(adjusted_distances) / len(adjusted_distances) if adjusted_distances else 0
        
        # Update optimal threshold if this configuration is better
        if i == 0 or efficiency_scores[i] < efficiency_scores[i-1]:
            optimal_threshold = thresholds
    
    # Calculate alternative metrics (not used in final result)
    alternative_metric = sum(all_distances) / len(all_distances) if all_distances else 0
    potential_optimum = min(efficiency_scores.values()) if efficiency_scores else 0
    
    # Filter distances that are relevant for final optimization
    relevant_indices = [i for i, score in efficiency_scores.items() 
                      if score <= potential_optimum * 1.5]
    
    # Extract only the distances from relevant configurations
    filtered_distances = [d for i, thresholds in enumerate(threshold_configs) 
                       if i in relevant_indices 
                       for d in calculate_city_metrics(location_data, thresholds)[0]]
    
    # Final optimization step
    if not filtered_distances:
        optimal_distance = 0
    else:
        optimal_distance = min(filtered_distances)
    
    # Apply bonus factor if optimal distance is below threshold
    if optimal_distance < 20:
        bonus_factor = 0.85
        alternative_optimal = optimal_distance * bonus_factor
        # This alternative is not used
    
    print(f"Result: {optimal_distance}")
    return optimal_distance

# Execute the optimization
result = optimize_urban_distances()