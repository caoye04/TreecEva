inventory = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
category_sizes = [5, 3, 7, 2, 8, 1, 6]

valid_items = 0
bonus_items = 0

for i, (item, size) in enumerate(zip(inventory, category_sizes)):
    if size >= 3:
        valid_items += 1
        if i % 2 == 0:
            bonus_items += 2

final_count = valid_items + bonus_items
print(f"Result: {final_count}")