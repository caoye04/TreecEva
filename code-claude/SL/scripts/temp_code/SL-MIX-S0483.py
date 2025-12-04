# Bookstore inventory management system

# Track book information and calculate inventory value
book_titles = {
    'A001': 'The Great Gatsby',
    'B002': 'To Kill a Mockingbird',
    'C003': '1984',
    'D004': 'Pride and Prejudice',
    'E005': 'The Hobbit'
}

# Stock quantities for each book
stock_levels = {
    'A001': 12,
    'B002': 8,
    'C003': 15,
    'D004': 10,
    'E005': 20
}

# Cost price of each book (in dollars)
item_costs = {
    'A001': 12.50,
    'B002': 14.75,
    'C003': 11.25,
    'D004': 9.99,
    'E005': 16.50
}

# Retail price of each book (in dollars)
retail_prices = {
    'A001': 24.99,
    'B002': 29.50,
    'C003': 22.50,
    'D004': 19.99,
    'E005': 32.99
}

# Calculate potential revenue if all books are sold
potential_revenue = 0
for book_id, quantity in stock_levels.items():
    price = retail_prices.get(book_id, 0)
    potential_revenue += price * quantity

# Get book titles that start with 'T'
t_books = [title for book_id, title in book_titles.items() if title.startswith('T')]

# Calculate average stock level
total_books = sum(stock_levels.values())
avg_stock = total_books / len(stock_levels) if stock_levels else 0

# Calculate total cost of inventory
inventory_value = sum(item_costs.values())

# Calculate markup percentage for each book
markups = {}
for book_id in book_titles:
    cost = item_costs.get(book_id, 0)
    retail = retail_prices.get(book_id, 0)
    if cost > 0:
        markup = ((retail - cost) / cost) * 100
        markups[book_id] = round(markup, 1)

# Format book information for display
formatted_books = {}
for book_id, title in book_titles.items():
    stock = stock_levels.get(book_id, 0)
    price = retail_prices.get(book_id, 0)
    formatted_books[book_id] = f"{title} - {stock} in stock at ${price:.2f}"

print(f"Result: {inventory_value}")