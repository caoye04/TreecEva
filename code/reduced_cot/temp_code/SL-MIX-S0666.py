inventory_items = ['apple', 'banana', 'orange', 'apple', 'grape', 'banana', 'apple', 'kiwi']
item_categories = {'apple': 'fruit', 'banana': 'fruit', 'orange': 'fruit', 'grape': 'fruit', 'kiwi': 'fruit', 'carrot': 'vegetable'}

fruit_count = {}
for item in inventory_items:
    if item in item_categories and item_categories[item] == 'fruit':
        fruit_count[item] = fruit_count.get(item, 0) + 1

# Distractor operations
category_sizes = {item: len(item) for item in set(inventory_items)}
total_letters = sum(category_sizes.values())

primary_count = fruit_count.get('apple', 0) + fruit_count.get('orange', 0)
secondary_count = fruit_count.get('banana', 0) + fruit_count.get('grape', 0)

# More distractor calculations
average_length = total_letters / len(set(inventory_items)) if inventory_items else 0
unused_calculation = primary_count * secondary_count - total_letters

final_result = primary_count - secondary_count
print(f"Result: {final_result}")