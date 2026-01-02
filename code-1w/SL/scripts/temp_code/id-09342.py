def calculate_surplus():
    needed_items = {f'part_{i}' for i in range(1, 18) if i % 3 != 0}
    available_items = {f'part_{i}' for i in range(1, 25) if i % 4 != 0}
    temp_log = [f'missing_{x}' for x in needed_items - available_items]
    inventory_surplus = len(available_items - needed_items)
    return inventory_surplus

result = calculate_surplus()
print(f"Target result: {result}")