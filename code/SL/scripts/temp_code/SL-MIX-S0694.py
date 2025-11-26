# Inventory management system
product_catalog = {"A101": 25, "B205": 18, "C309": 42}
inventory_count = sum(product_catalog.values())
backorder_items = len(product_catalog) * 7
final_quantity = inventory_count - backorder_items
print(f"Result: {final_quantity}")