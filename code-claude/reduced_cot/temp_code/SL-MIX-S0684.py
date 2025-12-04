# Product inventory analysis system
# Analyzing overlapping product categories between stores

def analyze_inventory(store_a, store_b):
    # Track processing metrics
    comparison_count = 0
    duplicate_items = {}
    
    # Convert lists to sets for efficient operations
    set_a = set(store_a)
    set_b = set(store_b)
    
    # Find items that appear in both stores
    common_elements = set_a.intersection(set_b)
    
    # Calculate size metrics
    total_unique = len(set_a.union(set_b))
    overlap_size = len(common_elements)
    
    # Calculate potential revenue impact (not needed for this analysis)
    potential_impact = overlap_size * 1.5
    market_saturation = (overlap_size / total_unique) if total_unique > 0 else 0
    
    # Count frequency of each item across both stores
    for idx, item in enumerate(store_a + store_b):
        comparison_count += 1
        if item in duplicate_items:
            duplicate_items[item] += 1
        else:
            duplicate_items[item] = 1
    
    # Alternative calculation method (not used in final result)
    alt_overlap = sum(1 for item, count in duplicate_items.items() if count > 1)
    
    # Calculate a different metric (not related to final answer)
    exclusive_items = total_unique - overlap_size
    
    return overlap_size, market_saturation

# Store inventory data
store_1 = ["milk", "eggs", "bread", "cheese", "yogurt", "butter"]
store_2 = ["eggs", "bread", "cereal", "milk", "pasta"]
store_3 = ["bread", "meat", "cheese", "pasta"]

# Analyze overlap between store 1 and store 2
overlap, saturation = analyze_inventory(store_1, store_2)

# Check overlap with store 3 (not used in final result)
_, _ = analyze_inventory(store_2, store_3)

# Print result
print(f"Result: {overlap}")