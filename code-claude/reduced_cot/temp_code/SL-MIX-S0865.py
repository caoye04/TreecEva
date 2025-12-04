# Inventory management system with product filtering
inventory = {
    'apple': {'price': 0.75, 'quantity': 20, 'organic': True},
    'banana': {'price': 0.60, 'quantity': 15, 'organic': True},
    'orange': {'price': 0.80, 'quantity': 10, 'organic': False},
    'pear': {'price': 0.90, 'quantity': 5, 'organic': True},
    'grape': {'price': 2.50, 'quantity': 8, 'organic': False}
}

# Calculate inventory value for items meeting specific criteria
def calculate_inventory_value(items):
    total_value = 0
    for item_data in items.values():
        item_value = item_data['price'] * item_data['quantity']
        total_value += item_value
    return total_value

# Filter function to select only organic products with quantity > 10
filter_func = lambda inv: [item['price'] * item['quantity'] 
                         for item_name, item in inv.items() 
                         if item['organic'] and item['quantity'] > 10]

# Apply the filter and calculate sum
filtered_sum = sum(filter_func(inventory))

# Display results
print(f"Total filtered inventory value: {filtered_sum}")