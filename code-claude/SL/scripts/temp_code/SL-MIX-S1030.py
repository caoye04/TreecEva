import itertools

# Inventory management system for a small shop
def process_inventory(products, categories):
    # Map product categories to their minimum stock thresholds
    category_thresholds = {'electronics': 5, 'books': 10, 'toys': 7, 'groceries': 15}
    
    # Sort products by name (for display purposes)
    sorted_products = sorted(products, key=lambda x: x[0].lower())
    
    # Calculate average price across all products (for reporting)
    total_price = sum(price for _, price, _ in products)
    avg_price = total_price / len(products) if products else 0
    
    # Group products by their categories
    product_groups = {}
    for cat in categories:
        product_groups[cat] = [p for p in products if p[2] == cat]
    
    # Find products that need restocking
    restock_needed = []
    for cat, threshold in category_thresholds.items():
        for prod in products:
            if prod[2] == cat and prod[1] < threshold:
                restock_needed.append(prod[0])
    
    # Create combinations of products (for bundle offers)
    bundles = list(itertools.combinations([p[0] for p in products[:3]], 2))
    
    # Filter products with valid prices (price > 0)
    filtered_products = [(name, price, category) for name, price, category in products]
    
    # Count products with valid prices
    valid_items = len([prod for prod in filtered_products if prod[1] > 0])
    
    # Calculate total inventory value
    inventory_value = sum(price for _, price, _ in filtered_products)
    
    print(f"Result: {valid_items}")
    return valid_items

# Sample inventory data: (name, price, category)
products = [
    ("Smartphone", 499.99, "electronics"),
    ("Laptop", 899.50, "electronics"),
    ("Headphones", 59.99, "electronics"),
    ("Novel", 12.95, "books"),
    ("Textbook", 75.00, "books"),
    ("Action Figure", 19.99, "toys"),
    ("Board Game", 29.95, "toys"),
    ("Apples", 0, "groceries")  # Free promotion item
]

categories = ["electronics", "books", "toys", "groceries"]
result = process_inventory(products, categories)