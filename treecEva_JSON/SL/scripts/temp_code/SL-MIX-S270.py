from collections import defaultdict
import math

def calculate_route_efficiency(packages, distances, priorities):
    weight_score = 0
    distance_score = 0
    priority_bonus = 0
    
    # Calculate weight score with dynamic programming approach
    weight_dp = defaultdict(int)
    for i, pkg in enumerate(packages):
        weight_dp[i] = weight_dp[i-1] + (pkg ** 2) if i > 0 else pkg ** 2
        weight_score += pkg * (i + 1)
    
    # Calculate distance score with sorting and bit operations
    sorted_distances = sorted(distances, reverse=True)
    for i, dist in enumerate(sorted_distances):
        # Use bit shifting for efficient calculation
        distance_score += dist << (i % 3)
    
    # Calculate priority bonus with set operations
    unique_priorities = frozenset(priorities)
    priority_levels = {1, 2, 3, 4, 5}
    missing_priorities = priority_levels - unique_priorities
    
    # Bonus is inversely proportional to missing priorities count
    priority_bonus = 100 >> len(missing_priorities) if len(missing_priorities) < 5 else 0
    
    # Apply logical conditions with short-circuit evaluation
    base_score = weight_score and distance_score and (weight_score | distance_score)
    
    # Final efficiency calculation with conditional logic
    if weight_score > 1000 or (distance_score > 5000 and priority_bonus > 0):
        final_efficiency_score = base_score ^ priority_bonus
    elif weight_score < 500 and distance_score < 2000:
        final_efficiency_score = base_score & priority_bonus
    else:
        final_efficiency_score = base_score + priority_bonus
    
    return final_efficiency_score

# Route parameters
shipment_weights = [15, 22, 8, 31, 17, 12]
delivery_distances = [120, 85, 210, 65, 175, 95]
priority_levels = [1, 3, 5, 3, 2, 1]

# Calculate efficiency
final_efficiency_score = calculate_route_efficiency(shipment_weights, delivery_distances, priority_levels)
print(f"Result: {final_efficiency_score}")