inventory_items = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
processed_items = len([item for item in inventory_items if item.startswith('a') or item.startswith('b')])
remaining_items = len([item for item in inventory_items if not item.startswith('a') and not item.startswith('b')])
final_count = processed_items + remaining_items
print(f"Result: {final_count}")