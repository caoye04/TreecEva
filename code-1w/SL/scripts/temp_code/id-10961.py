from collections import Counter, defaultdict

def analyze_stock_gaps(inventory):
    gaps = []
    for item, count in inventory.items():
        if count < 5:
            gaps.append(item)
    return set(gaps)

def adjust_inventory_flow(inventory):
    flow_corrections = defaultdict(int)
    total_items = sum(inventory.values())
    avg = total_items / len(inventory) if inventory else 1
    for item, count in inventory.items():
        if count < avg:
            flow_corrections[item] = int(avg - count)
    # Irrelevant transformation
    temp_debug = [x * 2 for x in flow_corrections.values()]
    temp_debug = sorted(temp_debug, reverse=True)
    return flow_corrections

def optimize_distribution(inventory, threshold):
    stock_issues = analyze_stock_gaps(inventory)
    corrections = adjust_inventory_flow(inventory)
    
    # Simulate warehouse capacity adjustments
    base_capacity = 100
    adjustment_factor = 0.75
    surge_buffer = 0
    
    for item in inventory:
        if item in stock_issues:
            surge_buffer += 5
        if inventory[item] > threshold:
            surge_buffer -= 2

    # Apply corrections to estimate new load
    estimated_load = 0
    for item, needed in corrections.items():
        estimated_load += needed * 1.5
    
    # Dummy logic that doesn't affect final result
    hypothetical_scenarios = []
    for i in range(3):
        hypothetical_scenarios.append(base_capacity * (i + 1))
    
    # Actual key computation
    intermediate = base_capacity + surge_buffer
    intermediate = intermediate * adjustment_factor
    final_capacity = int(intermediate - estimated_load // 2)
    
    # Red herring: unused calculation
    unused_peak = sum(inventory.values()) * 2 if len(inventory) > 3 else 0
    
    return final_capacity

# Main execution
inventory_levels = {'widget_a': 3, 'widget_b': 8, 'widget_c': 4, 'widget_d': 12, 'widget_e': 2}
threshold = 6

# Debugging side calculations (distractors)
duplicate_count = sum(1 for x in inventory_levels.values() if x > 5)
duplicate_set = {k for k, v in inventory_levels.items() if v == 4}

final_capacity = optimize_distribution(inventory_levels, threshold)
print(f"Result: {final_capacity}")