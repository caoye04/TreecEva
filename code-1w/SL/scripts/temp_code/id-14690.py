def calculate_performance(data):
    # Preprocessing: filter valid entries
    valid_entries = [x for x in data if x > 0]
    
    # Irrelevant transformation (distractor)
    squared_values = list(map(lambda x: x**2, data))
    sum_squares = sum(squared_values)  # Unused later

    # Core logic: compute weighted harmonic mean
    reciprocals = [1/x for x in valid_entries]
    total_weight = len(valid_entries)
    
    # Simulate noise with unused stats
    avg_reciprocal = sum(reciprocals) / len(reciprocals)
    max_val = max(valid_entries)
    min_val = min(valid_entries)
    dynamic_factor = (max_val - min_val) or 1
    
    # Actual performance metric
    if valid_entries:
        harmonic_sum = sum(reciprocals)
        weighted_harmonic = total_weight / harmonic_sum
    else:
        weighted_harmonic = 0
    
    # Apply arbitrary scaling based on data size (relevant)
    size_bonus = len(data) * 0.5
    
    # Secondary distractor: complex but unused structure
    derived_metrics = {
        'norm': sum([x / (weighted_harmonic + 1) for x in valid_entries]),
        'entropy': -sum([x * avg_reciprocal for x in reciprocals])
    }
    
    # Final computation
    raw_score = weighted_harmonic + size_bonus
    penalty = 0.1 * (len(data) - len(valid_entries))  # penalize invalids
    final_score = raw_score - penalty
    
    return final_score

# Input data with mixed valid/invalid values
dataset = [4, 8, 0, 12, -3, 6, 0, 10]

# Key execution point
final_score = calculate_performance(dataset)
print(f"Target result: {final_score}")