inventory = {"widgets": 45, "gadgets": 23, "tools": 78, "parts": 12}
key_item = "tools"
temp_count = inventory["widgets"] + inventory["gadgets"]
sorted_items = sorted(inventory.items(), key=lambda x: x[1])
sorted_inventory = dict(sorted_items)
result = sorted_inventory[key_item]
final_result = result * 2 + 10
print(f"Result: {final_result}")