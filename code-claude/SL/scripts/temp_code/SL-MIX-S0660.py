import itertools

def analyze_product_inventory(warehouse_a, warehouse_b):
    # Track warehouse inventory details
    inventory_stats = {
        'total_unique': 0,
        'warehouse_a_only': 0,
        'warehouse_b_only': 0,
        'both_locations': 0
    }
    
    # Convert to sets for efficient operations
    products_a = set(warehouse_a)
    products_b = set(warehouse_b)
    
    # Find products in both warehouses
    common_elements = products_a.intersection(products_b)
    
    # Calculate overlap size
    overlap_size = len(common_elements)
    
    # Calculate other statistics (not directly relevant to answer)
    inventory_stats['total_unique'] = len(products_a.union(products_b))
    inventory_stats['warehouse_a_only'] = len(products_a - products_b)
    inventory_stats['warehouse_b_only'] = len(products_b - products_a)
    inventory_stats['both_locations'] = overlap_size
    
    # Calculate some logistics metrics (distractors)
    shipping_routes = list(itertools.product(['North', 'South'], ['East', 'West']))
    route_count = len(shipping_routes)
    
    # Calculate theoretical distribution capacity (distractor)
    distribution_capacity = route_count * overlap_size // 2
    
    # Track potential product combinations (distractor)
    sample_combinations = list(itertools.combinations(list(common_elements)[:3] if len(common_elements) >= 3 else common_elements, 
                                                    min(2, len(common_elements))))
    
    return overlap_size, inventory_stats, distribution_capacity

# Main warehouse inventories
warehouse_a = [101, 103, 105, 106, 107, 108, 110, 115, 118]
warehouse_b = [102, 104, 106, 108, 109, 110, 111, 115, 117]

# Process inventory data
overlap, stats, capacity = analyze_product_inventory(warehouse_a, warehouse_b)

# Display results
print(f"Result: {overlap}")