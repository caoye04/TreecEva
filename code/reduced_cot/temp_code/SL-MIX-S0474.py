from collections import Counter

# Warehouse inventory analysis
warehouse_stock = {'A': 150, 'B': 200, 'C': 175, 'D': 90}
recent_transactions = [('A', 25), ('B', 30), ('A', 15), ('C', 20), ('B', 10)]

# Calculate current stock levels after transactions
transaction_counts = Counter()
for warehouse, quantity in recent_transactions:
    transaction_counts[warehouse] += quantity

stock_levels = {}
for warehouse, initial_stock in warehouse_stock.items():
    stock_levels[warehouse] = initial_stock - transaction_counts[warehouse]

# Process warehouse B
warehouse_id = 'B'
pending_orders = 45
final_quantity = stock_levels[warehouse_id] - pending_orders

print(f"Target result: {final_quantity}")