def process_inventory(items, modifier):
    # Distractor: Unused lambda that looks relevant
    calculate_discount = lambda x: x * 0.9 if x > 100 else x
    
    # Distractor: Misleading intermediate calculations
    temp_sum = sum(items.values()) + modifier * 2
    avg_weight = temp_sum / len(items) if items else 0
    
    # Relevant logic with distraction
    filtered_items = {k: v for k, v in items.items() if v > 15}
    
    # Distractor: Dead code path
    if len(filtered_items) > 5:
        bonus_adjustment = modifier * 3
    else:
        bonus_adjustment = modifier - 2
    
    # Core computation with interference
    value_map = {
        'A': lambda x: x * 1.5,
        'B': lambda x: x + 8,
        'C': lambda x: x // 2,
        'D': lambda x: x ^ 3
    }
    
    processed_values = []
    for item_code, quantity in filtered_items.items():
        if item_code in value_map:
            processed_values.append(value_map[item_code](quantity))
        else:
            processed_values.append(quantity * modifier)
    
    # Distractor: Unused variable
    max_possible = max(processed_values) * 2 if processed_values else 0
    
    # Actual answer computation
    final_result = sum(processed_values) - modifier
    return final_result

# Main execution
inventory_data = {'A': 12, 'B': 25, 'C': 18, 'D': 30, 'E': 8}
adjustment_factor = 7

# Distractor: Misleading variable assignment
initial_estimate = sum(inventory_data.values()) * adjustment_factor
secondary_calc = initial_estimate // len(inventory_data)

final_computation = process_inventory(inventory_data, adjustment_factor)

# Distractor: Unused operation that looks important
quality_check = (final_computation + secondary_calc) % 17

print(f"Target result: {final_computation}")