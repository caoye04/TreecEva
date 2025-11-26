from collections import Counter

inventory_list = ['laptop', 'mouse', 'keyboard', 'monitor', 'laptop', 'mouse', 'headphones']
sold_items_list = ['laptop', 'monitor', 'webcam']

inventory_counter = Counter(inventory_list)
inventory_set = set(inventory_list)
sold_items = set(sold_items_list)

remaining_products = len(inventory_set - sold_items)
print(f"Result: {remaining_products}")