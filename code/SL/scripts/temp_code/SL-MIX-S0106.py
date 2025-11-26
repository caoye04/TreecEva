items_data = "apple,banana,,cherry,date,elderberry,,"
item_list = items_data.split(",")
valid_items = [item for item in item_list if item]
final_count = len(valid_items)
print(f"Result: {final_count}")