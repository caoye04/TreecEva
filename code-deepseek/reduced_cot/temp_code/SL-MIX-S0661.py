raw_data = [2, 7, 4, 1, 9, 5]
processed_items = [item * 2 + 5 for item in raw_data if item > 3]
operation_count = len(processed_items)
temp_buffer = sum(processed_items)
efficiency_score = temp_buffer // operation_count
print(f"Result: {efficiency_score}")