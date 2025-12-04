def analyze_package_combinations(items, weight_limit):
    # Process item weights
    processed_weights = [w for w in items if w > 0]
    
    # Some statistics about weights (not used in final calculation)
    avg_weight = sum(processed_weights) / len(processed_weights) if processed_weights else 0
    weight_variance = sum((w - avg_weight) ** 2 for w in processed_weights) / len(processed_weights) if processed_weights else 0
    
    # Generate all possible combinations of items (pairs)
    combinations = []
    for i in range(len(processed_weights)):
        for j in range(i+1, len(processed_weights)):
            # Create pairs and track their indices
            item_pair = (processed_weights[i], processed_weights[j])
            index_pair = (i, j)
            combinations.append(item_pair)
    
    # Set maximum allowed weight
    max_weight = weight_limit
    
    # Filter combinations based on weight limit
    valid_combinations = len(list(filter(lambda x: sum(x) <= max_weight, combinations)))
    
    # Calculate a priority score (not used in final result)
    priority_score = valid_combinations * 2 - len(combinations)
    
    # Slice operations on the original list (not affecting the result)
    heaviest_items = sorted(processed_weights, reverse=True)[:3]
    lightest_items = sorted(processed_weights)[:2]
    
    print(f"Result: {valid_combinations}")
    return valid_combinations

# Test with sample data
item_weights = [2, 3, 4, 5, 6]
max_allowed_weight = 8
result = analyze_package_combinations(item_weights, max_allowed_weight)