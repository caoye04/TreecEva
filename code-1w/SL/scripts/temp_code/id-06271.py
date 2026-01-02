def calculate_final_score(data, weights):
    # Initialize tracking variables
    temp_sum = 0
    running_product = 1
    count_valid = 0
    
    # Secondary metric (not used in final score) — distraction
    anomaly_count = 0
    debug_trace = []
    
    for key in data:
        if key not in weights:
            continue
        
        value = data[key]
        weight = weights[key]
        
        # Core computation branch
        if value > 0:
            temp_sum += value * weight
            running_product *= weight  # irrelevant accumulation
            count_valid += 1
        else:
            # Negative values trigger fake diagnostic path
            anomaly_count += 1
            debug_trace.append(f"Anomaly at {key}")
            continue

    # Distractor: unused normalization attempts
    avg_correction = 0
    if count_valid > 0:
        avg_correction = temp_sum / count_valid
    
    smoothed_score = avg_correction * 0.9 + 10  # red herring
    
    # Real scoring logic buried here
    base_score = 0
    for i in range(len(weights)):
        base_score += (i + 1) * (i + 1)  # sum of squares: 1 + 4 + 9 + 16 + ...
    
    # Only this line matters
    final_score = temp_sum - base_score
    
    # Dead code path — misleading
    if final_score < 0:
        final_score = abs(final_score)
    
    return final_score

# Main execution
if __name__ == "__main__":
    data = {"x": 50, "y": 30, "z": -5, "w": 20}
    weights = {"x": 2, "y": 3, "w": 4, "v": 1}  # v not in data
    
    # Unused intermediate calculations — distraction
    total_potential = sum(data.values()) * max(weights.values())
    scaling_factor = len(data) / (len(weights) + 1)
    
    final_score = calculate_final_score(data, weights)
    
    print(f"Result: {final_score}")