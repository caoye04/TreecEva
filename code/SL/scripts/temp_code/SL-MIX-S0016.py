def process_items(item_list):
    enumerated_values = []
    for index, item in enumerate(item_list):
        processed = len(item) * (index + 1)
        enumerated_values.append(processed)
    
    # Calculate final result
    total_sum = sum(enumerated_values)
    print(f"Result: {total_sum}")

# Main execution
items = ["apple", "banana", "cherry", "date"]
process_items(items)