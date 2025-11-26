def process_inventory():
    # Inventory data for warehouse management
    inventory_counts = [45, 23, 67, 12, 89, 34]
    
    # Sort inventory in ascending order using lambda
    sorted_values = sorted(inventory_counts, key=lambda x: x)
    
    # Apply inventory adjustment factor
    adjustment_factor = 1.5
    processed_data = adjustment_factor * 2
    
    # Calculate final result from second smallest inventory count
    final_result = sorted_values[1] * processed_data
    
    print(f"Result: {final_result}")
    return final_result

# Execute the inventory processing
if __name__ == "__main__":
    process_inventory()