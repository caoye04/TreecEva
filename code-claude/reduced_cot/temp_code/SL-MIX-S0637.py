import itertools

def analyze_product_combinations(items, target_sum):
    # Generate all possible pairs of items
    product_combinations = list(itertools.combinations(items, 2))
    
    # Check if a combination is valid (product equals target_sum)
    def is_valid(combo):
        return combo[0] * combo[1] == target_sum
    
    # Some items might not be useful for our analysis
    inventory_count = len(items)
    
    # Count combinations where product equals target_sum
    valid_combinations = len(list(filter(is_valid, product_combinations)))
    
    # Calculate average of all items (not relevant to main task)
    avg = sum(items) / inventory_count if inventory_count > 0 else 0
    
    print(f"Result: {valid_combinations}")
    return valid_combinations

# List of available items
items = [1, 2, 3, 4, 5, 6, 8, 10, 12]
# Target product value
target_value = 12

# Analyze the combinations
result = analyze_product_combinations(items, target_value)