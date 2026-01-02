from collections import defaultdict

# Simulate retail inventory and transaction reconciliation
initial_stock = {'A': 50, 'B': 30, 'C': 20}
transactions = [
    ('A', 'sale', 5), ('B', 'restock', 10), ('A', 'sale', 3),
    ('C', 'sale', 8), ('B', 'sale', 12), ('A', 'restock', 20)
]
adjustments = [-2, 3, -1, 4]
daily_revenue = [250, 300, 180, 220, 240]

# Track stock changes per item
current_stock = defaultdict(int, initial_stock)
stock_movements = defaultdict(list)

for item, action, amount in transactions:
    if action == 'sale':
        current_stock[item] -= amount
        stock_movements[item].append(-amount)
    elif action == 'restock':
        current_stock[item] += amount
        stock_movements[item].append(amount)

# Irrelevant: Compute average daily revenue (not used in final result)
avg_revenue = sum(daily_revenue) / len(daily_revenue)
peak_revenue = max(daily_revenue)
revenue_variance = sum((x - avg_revenue) ** 2 for x in daily_revenue)

# Misleading: Unused adjustment tracking
temp_adjustments = [abs(x) for x in adjustments if x != 0]
adjustment_count = len(temp_adjustments)

# Core logic: Inventory change summaries
inventory_changes = {}
for item, changes in stock_movements.items():
    net_change = sum(changes)
    inventory_changes[item] = net_change

# Secondary adjustment processing (only the sum matters)
final_adjustment = sum(adjustments) * 2  # Amplify total adjustment

# Red herring: complex nested loop with no impact
phantom_balance = 0
for i in range(3):
    for j in range(2):
        phantom_balance += i * j
    phantom_balance -= i

# Key function using combined data
def calculate_net(changes, extra_adj):
    base = sum(changes.values())
    bonus = 0
    # Conditional bonus based on movement patterns
    for val in changes.values():
        if val < -5:
            bonus += 3
        elif val > 5:
            bonus += 2
    return base + bonus + extra_adj

# Execution point of interest
net_balance = calculate_net(inventory_changes, final_adjustment)

# Print result for evaluation
print(f"Result: {net_balance}")