def process_inventory(items):
    temp_analysis = [item * 2 for item in items]
    intermediate_check = sum(temp_analysis)  # Not used in final calculation
    filtered_items = [x for x in temp_analysis if x % 3 != 0]
    backup_storage = len(filtered_items) * 5  # Distractor variable
    processed_items = [val + 10 for val in filtered_items]
    final_prep = max(processed_items) - min(processed_items)  # Irrelevant computation
    final_value = processed_items[-1]
    print(f"Result: {final_value}")

initial_stock = [7, 12, 5, 18, 9]
process_inventory(initial_stock)