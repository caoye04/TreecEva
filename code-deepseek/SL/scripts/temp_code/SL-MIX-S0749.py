import itertools

def calculate_inventory_value():
    # Core inventory data
    item_quantities = [8, 12, 5, 9, 7]
    item_values = [25, 18, 42, 31, 29]
    
    # Calculate total inventory value
    inventory_total = sum(qty * val for qty, val in zip(item_quantities, item_values))
    
    # Distraction: Process combinations that won't affect final result
    combination_data = list(itertools.combinations(item_quantities, 2))
    combination_sum = sum(min(pair) for pair in combination_data)
    
    # Distraction: Additional processing that's ultimately unused
    processed_values = [val * 1.1 for val in item_values if val > 20]
    value_adjustment = len(processed_values) * 5
    
    # Core calculation
    base_calculation = inventory_total // 10
    adjustment_factor = len([qty for qty in item_quantities if qty > 7]) * 3
    
    # Final result computation
    primary_sum = base_calculation + adjustment_factor
    adjustment = (sum(item_quantities[:3]) - 10) * 2
    final_result = primary_sum + adjustment
    
    # Distraction: Final calculations that don't impact result
    dummy_metric = combination_sum % 50
    verification_check = dummy_metric + value_adjustment
    
    print(f"Result: {final_result}")
    return final_result

if __name__ == "__main__":
    calculate_inventory_value()