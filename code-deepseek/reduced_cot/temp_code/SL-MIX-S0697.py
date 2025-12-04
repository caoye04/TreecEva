original_data = [10, 25, 8, 42, 17, 33, 56, 91, 14, 29]
processed_items = original_data[3:8]
processed_items.sort()
processed_items.append(processed_items[1] * 2)
intermediate_calc = len(processed_items) - 2
final_result = sum(processed_items[1:4]) * 2
print(f"Target result: {final_result}")