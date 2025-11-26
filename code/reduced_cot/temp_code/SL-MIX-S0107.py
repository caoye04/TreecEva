import itertools

def analyze_data_patterns(data_points):
    # Initialize metrics
    primary_metric = 0
    secondary_metric = 0
    temp_buffer = []
    
    # Distractor: Calculate average but don't use it
    data_sum = sum(data_points)
    data_average = data_sum / len(data_points)
    
    # Main logic: Find combinations that sum to target
    target_sum = 15
    valid_combinations = []
    
    for r in range(2, 4):
        for combo in itertools.combinations(data_points, r):
            if sum(combo) == target_sum:
                valid_combinations.append(combo)
                # Distractor: Store in buffer but don't use
                temp_buffer.append(combo[0] if len(combo) > 0 else 0)
    
    # Primary metric: Count valid combinations
    primary_metric = len(valid_combinations)
    
    # Secondary metric: Calculate weighted score
    weight_factor = 3
    secondary_metric = sum(len(combo) * weight_factor for combo in valid_combinations)
    
    # Distractor: Calculate unused metric
    unused_metric = max(data_points) - min(data_points)
    
    # Final calculation
    final_solution = primary_metric - secondary_metric
    
    return final_solution

# Sample data
measurement_data = [3, 5, 7, 8, 10, 2]
final_result = analyze_data_patterns(measurement_data)
print(f"Target result: {final_result}")