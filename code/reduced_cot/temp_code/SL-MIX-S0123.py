def process_inventory_data(items):
    base_values = [item * 2 for item in items]
    adjustment_factor = 7
    
    # Intermediate calculation (not used in final result)
    temp_sum = sum(base_values) + adjustment_factor
    
    processed_values = [value - 5 for value in base_values]
    
    # Lambda function with filter for divisibility check
    result_filter = list(filter(lambda x: x % 3 == 0, processed_values))
    
    # Semi-relevant operation (doesn't affect final result)
    max_value = max(processed_values) if processed_values else 0
    
    # Final calculation
    final_result = len(result_filter) * adjustment_factor
    
    print(f"Target result: {final_result}")

# Main execution
inventory_items = [8, 12, 5, 9, 15, 3]
process_inventory_data(inventory_items)