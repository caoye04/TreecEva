data_records = "apple,banana,,cherry,date,,"
items_list = data_records.split(",")
filtered_items = [item for item in items_list if item]
valid_items = [item.upper() if len(item) > 5 else item for item in filtered_items]
final_result = len(valid_items)
print(f"Result: {final_result}")