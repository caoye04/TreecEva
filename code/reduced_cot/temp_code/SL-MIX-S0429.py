def compute_final_result():
    inventory_values = {'item_a': 45, 'item_b': 67, 'item_c': 23, 'item_d': 89}
    threshold_check = lambda x: x > 50
    
    relevant_items = {k: v for k, v in inventory_values.items() if threshold_check(v)}
    irrelevant_calc = sum(inventory_values.values()) * 2 - 150
    
    processed_values = [v * 1.1 for v in relevant_items.values()]
    adjustment_factor = len(inventory_values) - len(relevant_items)
    
    base_result = sum(processed_values)
    final_calculation = base_result - adjustment_factor * 5
    
    return round(final_calculation, 2)

final_solution = compute_final_result()
print(f"Result: {final_solution}")