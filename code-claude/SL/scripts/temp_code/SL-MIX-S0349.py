# Inventory management system for a bookstore

# Product catalog with book details (id: [title, price, stock])
product_catalog = {
    101: ["The Great Gatsby", 12.99, 15],
    102: ["To Kill a Mockingbird", 14.50, 8],
    103: ["1984", 11.25, 20],
    104: ["Pride and Prejudice", 9.75, 12],
    105: ["The Catcher in the Rye", 10.50, 6]
}

# Sales data (id: quantity sold)
sales_data = {
    101: 3,
    103: 5,
    104: 2,
    105: 1
}

# Discount rates for different price ranges
discount_rates = {
    "low": 0.05,     # For books under $10
    "medium": 0.10,  # For books $10-$12
    "high": 0.15     # For books over $12
}

# Calculate remaining inventory
remaining_inventory = {}
low_stock_threshold = 10
low_stock_items = set()

for book_id, details in product_catalog.items():
    title, price, stock = details
    
    # Calculate remaining stock after sales
    sold = sales_data.get(book_id, 0)
    remaining = stock - sold
    
    # Track which books are low in stock
    if remaining < low_stock_threshold:
        low_stock_items.add(book_id)
    
    remaining_inventory[book_id] = remaining

# Prepare for reordering calculation
reorder_cost = 0
potential_savings = 0

# Calculate inventory value with appropriate discounts
inventory_values = []
total_books = 0

for book_id, quantity in remaining_inventory.items():
    _, price, _ = product_catalog[book_id]
    
    # Determine discount based on price range
    if price < 10:
        discount = discount_rates["low"]
    elif price <= 12:
        discount = discount_rates["medium"]
    else:
        discount = discount_rates["high"]
    
    # Calculate discounted price
    discounted_price = price * (1 - discount)
    
    # Calculate value of remaining inventory for this book
    book_value = quantity * discounted_price
    inventory_values.append(book_value)
    
    # Track total books for inventory report
    total_books += quantity
    
    # Calculate potential reorder costs (not used in final calculation)
    if book_id in low_stock_items:
        reorder_cost += (10 - quantity) * price * 0.8  # 20% discount on bulk orders
        potential_savings += (10 - quantity) * price * 0.2

# Process inventory slices for reporting (not affecting final answer)
first_half = inventory_values[:len(inventory_values)//2]
second_half = inventory_values[len(inventory_values)//2:]

# Calculate total inventory value
total_inventory_value = sum(inventory_values)

# Calculate average book value (not used in final calculation)
average_book_value = total_inventory_value / total_books if total_books > 0 else 0

print(f"Total inventory value: {total_inventory_value:.2f}")