from collections import defaultdict

# Initialize store inventory tracking
price_list = {'apple': 1.25, 'banana': 0.75, 'orange': 1.50, 'grape': 2.00}
inventory = {'apple': 10, 'banana': 15, 'grape': 5}

# Track sales for the day
sales_data = {'apple': 3, 'banana': 7, 'orange': 2}

# Update inventory based on sales
for item, quantity in sales_data.items():
    if item in inventory:
        inventory[item] = max(0, inventory[item] - quantity)

# Calculate remaining inventory value
inventory_value = sum(item_price * inventory.get(item, 0) for item, item_price in price_list.items())

# Display statistics
daily_sales = sum(price_list[item] * quantity for item, quantity in sales_data.items())
print(f"Daily sales: ${daily_sales:.2f}")
print(f"Remaining inventory value: ${inventory_value:.2f}")