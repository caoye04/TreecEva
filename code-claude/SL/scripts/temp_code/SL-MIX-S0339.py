import itertools

def analyze_data_sequences(values, target_sum=10, filter_value=3):
    # Generate all possible permutations of the values
    all_permutations = list(itertools.permutations(values))
    
    # Filter permutations based on multiple criteria
    filtered_permutations = []
    for perm in all_permutations:
        # Calculate various metrics for analysis
        sum_value = sum(perm)
        product_value = 1
        for val in perm:
            product_value *= val
        
        # Track elements that meet certain thresholds
        elements_above_threshold = [x for x in perm if x > filter_value]
        threshold_count = len(elements_above_threshold)
        
        # Apply primary filtering criteria
        if sum_value >= target_sum and threshold_count >= 1:
            filtered_permutations.append(perm)
    
    # Calculate some statistics on the filtered permutations
    avg_first_element = sum(p[0] for p in filtered_permutations) / len(filtered_permutations) if filtered_permutations else 0
    max_last_element = max(p[-1] for p in filtered_permutations) if filtered_permutations else 0
    
    # Count permutations where first element doesn't match last element
    valid_permutation_count = len([p for p in filtered_permutations if p[0] != p[-1]])
    
    # Additional metrics calculation (not directly used for final result)
    total_unique_elements = len(set(values))
    theoretical_max = total_unique_elements * (total_unique_elements - 1)
    
    return valid_permutation_count, avg_first_element, max_last_element

# Test with sample data
test_values = [2, 4, 5, 3]
result, avg_first, max_last = analyze_data_sequences(test_values, target_sum=12, filter_value=2)

# Display the results
print(f"Result: {result}")