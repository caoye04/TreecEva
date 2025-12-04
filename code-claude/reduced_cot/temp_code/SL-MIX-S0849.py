from collections import Counter, defaultdict

# Inventory management system for a repair shop
def calculate_repair_efficiency(parts_available, parts_needed, usage_history):
    # Initialize variables
    total_parts = sum(parts_available.values())
    missing_parts = 0
    excess_inventory = defaultdict(int)
    
    # Calculate parts that might be in excess
    for part, count in parts_available.items():
        if part not in parts_needed or count > parts_needed.get(part, 0):
            excess_inventory[part] = count - parts_needed.get(part, 0)
    
    # Convert dictionaries to sets for set operations
    inventory_set = set(parts_available.keys())
    required_set = set(parts_needed.keys())
    
    # Calculate missing parts
    missing_parts_set = required_set - inventory_set
    missing_parts = len(missing_parts_set)
    
    # Calculate efficiency metrics
    total_unique_parts = len(inventory_set.union(required_set))
    base_efficiency = 100 - (missing_parts * 5)
    
    # Analyze usage history to adjust efficiency
    usage_counter = Counter(usage_history)
    frequently_used = {part for part, count in usage_counter.items() if count > 2}
    rarely_used = {part for part, count in usage_counter.items() if count == 1}
    
    # Calculate efficiency factor based on inventory matching
    efficiency_factor = 2.5
    if len(frequently_used.intersection(inventory_set)) >= 3:
        efficiency_factor = 3.0
    elif len(rarely_used.intersection(missing_parts_set)) >= 2:
        efficiency_factor = 2.0
    
    # Calculate common elements between inventory and required parts
    common_elements = len(inventory_set.intersection(required_set)) * efficiency_factor
    
    # Apply additional adjustments (doesn't affect the result)
    adjusted_efficiency = base_efficiency + (len(frequently_used) - len(rarely_used))
    potential_score = total_unique_parts + common_elements
    
    return common_elements

# Test data
parts_available = {"wrench": 5, "screwdriver": 3, "pliers": 2, "hammer": 1, "drill": 2}
parts_needed = {"wrench": 2, "screwdriver": 2, "pliers": 1, "nails": 10, "screws": 20}
usage_history = ["wrench", "screwdriver", "pliers", "wrench", "hammer", "drill", "wrench"]

# Calculate and print the result
result = calculate_repair_efficiency(parts_available, parts_needed, usage_history)
print(f"Result: {result}")