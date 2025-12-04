import itertools

# Function to calculate product combinations for inventory planning
def calculate_combinations(items, sizes):
    # Generate all possible item-size combinations
    all_combos = list(itertools.product(items, sizes))
    
    # Track availability status (placeholder for real inventory system)
    availability = [True, False, True, True, False, True, False, True, True]
    
    # Filter available combinations only
    available_combos = [combo for combo, avail in zip(all_combos, availability) if avail]
    
    # Count products per category
    product_count = []
    for item in items:
        count = sum(1 for combo in available_combos if combo[0] == item)
        product_count.append(count)
    
    # Calculate total available combinations
    total_combinations = sum(product_count)
    
    return total_combinations

# Main execution
items = ['shirt', 'pants', 'jacket']
sizes = ['S', 'M', 'L']

result = calculate_combinations(items, sizes)
print(f"Result: {result}")