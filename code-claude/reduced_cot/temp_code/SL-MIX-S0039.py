import itertools

# Inventory management system for a bookstore
def process_inventory(book_catalog, sales_data):
    # Initial inventory counts
    fiction_books = {'novel': 45, 'poetry': 23, 'drama': 17}
    nonfiction_books = {'biography': 38, 'history': 52, 'science': 29}
    
    # Process incoming shipment
    new_shipment = {'novel': 12, 'science': 8, 'poetry': 5, 'cookbook': 15}
    
    # Combine existing inventory
    inventory = {}
    inventory.update(fiction_books)
    inventory.update(nonfiction_books)
    
    # Add new shipment to inventory
    for category, count in new_shipment.items():
        if category in inventory:
            inventory[category] += count
        else:
            inventory[category] = count
    
    # Process sales data (not relevant to final calculation)
    monthly_sales = {'novel': 22, 'biography': 18, 'history': 15, 'science': 12}
    potential_revenue = sum(price * monthly_sales.get(book, 0) 
                           for book, price in book_catalog.items())
    
    # Calculate inventory statistics
    total_books = sum(inventory.values())
    avg_per_category = total_books / len(inventory)
    
    # Find categories present in both fiction and nonfiction (distraction)
    overlap = set(fiction_books.keys()) & set(nonfiction_books.keys())
    
    # Create sets for analysis
    category_set = set(inventory.keys())
    bestseller_categories = set(['novel', 'biography', 'history'])
    low_stock_categories = {k for k, v in inventory.items() if v < 25}
    
    # Combine categories for tracking
    tracked_categories = category_set | bestseller_categories
    inventory_set = category_set - low_stock_categories
    
    # Calculate unique items for inventory report
    unique_items = len(inventory_set)
    
    # Generate combinations for display planning (distraction)
    display_options = list(itertools.combinations(bestseller_categories, 2))
    display_count = len(display_options)
    
    print(f"Result: {unique_items}")
    return unique_items

# Test the function
book_catalog = {'novel': 12.99, 'biography': 15.99, 'history': 14.99, 
                'science': 16.99, 'poetry': 9.99, 'drama': 11.99, 'cookbook': 18.99}
sales_data = [('novel', 5), ('biography', 3), ('cookbook', 2)]

result = process_inventory(book_catalog, sales_data)