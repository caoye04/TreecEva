from collections import Counter

def analyze_inventory(items, sizes):
    # Track item frequencies
    item_counts = Counter(items)
    most_common = item_counts.most_common(3)
    
    # Process size information
    size_distribution = {}
    for i, size in enumerate(sizes):
        if size not in size_distribution:
            size_distribution[size] = 0
        size_distribution[size] += 1
        
        # Unnecessary calculation that isn't used
        avg_so_far = sum(sizes[:i+1]) / (i+1)
    
    # Find sizes that appear multiple times
    common_sizes = [size for size, count in size_distribution.items() if count >= 3]
    common_sizes.sort(reverse=True)
    
    # Some distracting calculations
    total_items = len(items)
    unique_items = len(set(items))
    diversity_ratio = unique_items / total_items if total_items > 0 else 0
    
    # Calculate storage efficiency
    efficiency_factor = 0.85
    base_capacity = 50
    
    # More distraction - this doesn't affect the final calculation
    adjusted_capacity = base_capacity * (1 + diversity_ratio)
    
    # Calculate threshold based on most common item
    if most_common and most_common[0][1] > 5:
        popularity_bonus = most_common[0][1] * 0.5
    else:
        popularity_bonus = 0
    
    # Set threshold
    threshold = int(base_capacity * efficiency_factor + popularity_bonus)
    
    # Find optimal size
    if not common_sizes:
        optimal_size = threshold // 2
    else:
        # This is the key statement
        optimal_size = min(common_sizes[0], threshold)
    
    return optimal_size

# Test data
items = ['shirt', 'pants', 'shirt', 'hat', 'pants', 'shirt', 'scarf', 'hat']
sizes = [42, 36, 40, 22, 38, 42, 18, 22]

result = analyze_inventory(items, sizes)
print(f"Result: {result}")