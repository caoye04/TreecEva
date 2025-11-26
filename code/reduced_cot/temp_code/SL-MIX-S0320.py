from collections import defaultdict

def process_inventory(items):
    inventory_map = defaultdict(lambda: 0)
    
    # Distractor: complex but irrelevant inventory processing
    for idx, item in enumerate(items):
        if idx % 3 == 0:
            inventory_map[item] += 7
        elif idx % 5 == 0:
            inventory_map[item] -= 3
        else:
            inventory_map[item] += 1
    
    # More irrelevant computations
    temp_sum = sum(len(str(k)) for k in inventory_map.keys())
    cycle_count = (temp_sum * 3) % 11
    
    # Dead code path - never executed
    if cycle_count > 20:
        unused_var = inventory_map.get('phantom', 100)
        cycle_count += unused_var
    
    # Core logic starts here
    base_value = 42
    multiplier = 3
    
    # Distracting intermediate calculations
    intermediate = (base_value << 2) ^ 15
    shadow_value = intermediate % 7 + 2
    
    # Key computation chain
    if shadow_value > 4:
        target_value = base_value * multiplier - 25
    else:
        target_value = base_value // multiplier + 18
    
    # More distractions
    fake_result = target_value + 100
    misleading_counter = sum(1 for x in range(10) if x % 2 == 0)
    
    # Final transformation
    def final_transform(x):
        return (x * 2) - 7
    
    result = final_transform(target_value)
    
    print(f"Target result: {result}")
    return result

# Execute the main function
sample_items = ['apple', 'banana', 'cherry', 'apple', 'date', 'elderberry']
process_inventory(sample_items)