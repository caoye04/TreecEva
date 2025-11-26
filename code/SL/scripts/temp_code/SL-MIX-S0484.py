product_categories = {
    'electronics': {'laptop', 'phone', 'tablet'},
    'home': {'lamp', 'chair', 'table'},
    'office': {'desk', 'chair', 'laptop'}
}

all_products = set()
for category_items in product_categories.values():
    all_products.update(category_items)

unique_products = all_products
final_count = len(unique_products)
print(f"Result: {final_count}")