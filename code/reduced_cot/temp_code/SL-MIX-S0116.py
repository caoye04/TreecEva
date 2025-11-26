import itertools

def process_candidates(candidates, filter_func):
    # Irrelevant processing function
    processed = [x * 2 for x in candidates if filter_func(x)]
    return sum(processed) % 100

def score_calculation(points, limit):
    # Main scoring logic with interference
    relevant_set = {x for x in points if x > limit}
    irrelevant_set = {x for x in points if x < limit}
    
    # Distractor calculations
    temp_sum = sum(points) * 2
    distractor_var = temp_sum // len(points) if points else 0
    
    # Misleading intermediate result
    dummy_result = process_candidates(points, lambda x: x % 2 == 0)
    
    # Key logic with bitwise operations
    if relevant_set:
        min_val = min(relevant_set)
        max_val = max(relevant_set)
        
        # Core calculation using itertools
        combinations = list(itertools.combinations(relevant_set, 2))
        valid_pairs = [(a, b) for a, b in combinations if (a ^ b) > 2]
        
        # Dead code path
        if len(valid_pairs) > 10:
            unused_var = len(valid_pairs) * 3
        
        # Final score calculation
        score = (min_val + max_val) * len(valid_pairs)
        score = score | 0b101  # Bitwise OR with 5
        
        # Remove misleading offset
        score = score - distractor_var
        
        return score
    else:
        return dummy_result  # Misleading return path

# Main execution
data_points = [8, 15, 3, 12, 7, 20, 5]
threshold = 6

# Irrelevant variable assignments
preliminary_check = sum(data_points) > 50
backup_data = [x - 1 for x in data_points]

# Target calculation
final_score = score_calculation(data_points, threshold)

# Print result
print(f"Result: {final_score}")