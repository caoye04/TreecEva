from math import sqrt

def calculate_route_efficiency(distances, traffic_factors, priorities):
    if len(distances) != len(traffic_factors) or len(traffic_factors) != len(priorities):
        return 0
    
    weighted_scores = []
    for i in range(len(distances)):
        # Distance factor (inverse relationship)
        dist_factor = 1000 / (distances[i] + 1)
        
        # Traffic penalty (exponential decay)
        traffic_penalty = 2 ** (-traffic_factors[i]/10)
        
        # Priority multiplier
        priority_mult = priorities[i]
        
        score = dist_factor * traffic_penalty * priority_mult
        weighted_scores.append(score)
    
    # Sort scores in descending order using a custom lambda
    weighted_scores.sort(key=lambda x: -x)
    
    # Apply divide and conquer approach to calculate final score
    def divide_conquer(scores):
        n = len(scores)
        if n == 0:
            return 0
        if n == 1:
            return scores[0]
        mid = n // 2
        left = divide_conquer(scores[:mid])
        right = divide_conquer(scores[mid:])
        return (left + right) / 2
    
    return divide_conquer(weighted_scores)

def process_routes(route_data):
    scores = []
    for route in route_data:
        match route['type']:
            case 'local':
                efficiency = calculate_route_efficiency(route['distances'], route['traffic'], route['priorities'])
                scores.append(efficiency * 1.0)
            case 'regional':
                efficiency = calculate_route_efficiency(route['distances'], route['traffic'], route['priorities'])
                scores.append(efficiency * 1.2)
            case 'national':
                efficiency = calculate_route_efficiency(route['distances'], route['traffic'], route['priorities'])
                scores.append(efficiency * 1.5)
            case _:
                scores.append(0)
                break
    
    # Early return if no valid routes
    if not scores:
        return 0
    
    # Calculate average score
    total = sum(scores)
    avg_score = total / len(scores)
    
    # Apply bonus based on number of routes
    bonus = 0
    if len(route_data) >= 5:
        bonus = 10
    elif len(route_data) >= 3:
        bonus = 5
    
    return avg_score + bonus

# Main execution
routes = [
    {'type': 'local', 'distances': [5, 10, 15], 'traffic': [2, 4, 3], 'priorities': [1, 2, 1]},
    {'type': 'regional', 'distances': [50, 60, 45], 'traffic': [5, 6, 4], 'priorities': [2, 2, 3]},
    {'type': 'national', 'distances': [200, 250, 180], 'traffic': [8, 9, 7], 'priorities': [3, 3, 3]},
    {'type': 'local', 'distances': [8, 12, 10], 'traffic': [3, 3, 2], 'priorities': [1, 1, 2]},
    {'type': 'regional', 'distances': [75, 80, 70], 'traffic': [6, 7, 5], 'priorities': [2, 3, 2]}
]

with open('temp_log.txt', 'w') as f:
    f.write("Processing routes\n")
    final_score = process_routes(routes)
    f.write(f"Final score: {final_score}\n")

print(f"Result: {final_score}")