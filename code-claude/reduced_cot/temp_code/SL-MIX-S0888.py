def calculate_profit(product):
    # Calculate profit margin based on cost and selling price
    cost = product['cost']
    price = product['price']
    return price - cost

def calculate_shipping_cost(weight, distance):
    # Shipping cost calculation - not relevant for final result
    base_cost = 5.0
    weight_factor = weight * 0.1
    distance_factor = distance * 0.05
    return base_cost + weight_factor + distance_factor

def get_discount_rate(customer_tier, product_category):
    # Discount rate calculation - not used in main logic flow
    if customer_tier == 'premium':
        base_discount = 0.15
    elif customer_tier == 'regular':
        base_discount = 0.05
    else:
        base_discount = 0.0
    
    category_adjustments = {'electronics': 0.02, 'clothing': 0.05, 'food': 0.03}
    category_bonus = category_adjustments.get(product_category, 0.0)
    
    return base_discount + category_bonus

# Inventory data with product information
inventory = [
    {'id': 101, 'name': 'Laptop', 'cost': 500, 'price': 950, 'weight': 2.5, 'category': 'electronics'},
    {'id': 102, 'name': 'Smartphone', 'cost': 300, 'price': 799, 'weight': 0.3, 'category': 'electronics'},
    {'id': 103, 'name': 'Headphones', 'cost': 50, 'price': 199, 'weight': 0.2, 'category': 'electronics'},
    {'id': 104, 'name': 'T-shirt', 'cost': 5, 'price': 25, 'weight': 0.1, 'category': 'clothing'},
    {'id': 105, 'name': 'Jeans', 'cost': 15, 'price': 65, 'weight': 0.6, 'category': 'clothing'},
    {'id': 106, 'name': 'Chocolate', 'cost': 2, 'price': 6, 'weight': 0.2, 'category': 'food'}
]

# Customer information - not directly relevant to final calculation
customer = {
    'name': 'John Smith',
    'tier': 'premium',
    'address': '123 Main St',
    'distance': 15.5,
    'purchase_history': [101, 103, 105]
}

# Filter settings
min_profit_threshold = 100
max_weight = 5.0
total_shipping_estimate = 0

# Apply weight filter first - misleading operation
heavy_items = [item for item in inventory if item['weight'] > max_weight]
light_items = [item for item in inventory if item['weight'] <= max_weight]

# Calculate customer discount - distractor calculation
discount_rates = {item['id']: get_discount_rate(customer['tier'], item['category']) for item in inventory}
max_discount = max(discount_rates.values()) if discount_rates else 0

# Calculate potential profit with discount - distractor
discounted_profits = []
for item in inventory:
    discount = discount_rates[item['id']]
    discounted_price = item['price'] * (1 - discount)
    potential_profit = discounted_price - item['cost']
    discounted_profits.append(potential_profit)

# Calculate shipping costs - distractor
for item in light_items:
    shipping = calculate_shipping_cost(item['weight'], customer['distance'])
    total_shipping_estimate += shipping

# Filter inventory by customer interests - not directly relevant
previous_purchases = customer['purchase_history']
recommended_items = [item for item in inventory if item['id'] not in previous_purchases]

# This is the key filtering operation that determines valid products
filtered_inventory = light_items  # All items passed weight filter
valid_products = [product for product in filtered_inventory if calculate_profit(product) > min_profit_threshold]

# Additional distracting calculation
average_profit = sum(calculate_profit(product) for product in valid_products) / len(valid_products) if valid_products else 0

# Print result
print(f"Total valid products: {len(valid_products)}")
print(f"Result: {len(valid_products)}")