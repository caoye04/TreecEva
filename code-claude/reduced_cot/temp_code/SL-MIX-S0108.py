# Calculate inventory value based on product quantities and prices

# Product prices (in dollars)
product_prices = {
    'apple': 1.20,
    'banana': 0.50,
    'orange': 0.75,
    'grape': 2.50,
    'mango': 1.80
}

# Current inventory quantities
inventory_count = {
    'apple': 25,
    'banana': 40,
    'orange': 30,
    'grape': 15,
    'mango': 20
}

# Store information
store_name = "Fresh Fruits Market"
store_location = "123 Orchard Street"
store_rating = 4.8

# Calculate value of each product in inventory
inventory_value = {}
for product, price in product_prices.items():
    if product in inventory_count:
        inventory_value[product] = price * inventory_count[product]

# Calculate total inventory value
total_value = sum(inventory_value.values())

# Display results
print(f"Store: {store_name}")
print(f"Total inventory value: ${total_value}")