products = ['laptop', 'mouse', 'keyboard', 'monitor', 'headphones', 'laptop', 'tablet', 'laptop', 'keyboard']
target_product = 'laptop'
item_counter = 0
for product in products:
    if product == target_product:
        item_counter += 1
modifier = 3
final_count = item_counter * modifier
print(f"Result: {final_count}")