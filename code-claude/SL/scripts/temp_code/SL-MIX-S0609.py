from collections import Counter, defaultdict

def apply_discounts(prices, discount_rates):
    # Apply various discount rates to prices
    discounted = {}
    for item, price in prices.items():
        if item in discount_rates:
            discounted[item] = price * (1 - discount_rates[item])
        else:
            discounted[item] = price
    return discounted

def calculate_shipping_cost(weight, distance):
    # Calculate shipping cost based on weight and distance
    base_rate = 5.0
    weight_factor = 0.75 if weight < 10 else 1.25
    distance_factor = distance * 0.01
    return base_rate + (weight * weight_factor) + distance_factor

def calculate_inventory_value(products, price_adjustments):
    # Calculate the actual inventory value after applying adjustments
    base_value = sum(p['quantity'] * p['unit_price'] for p in products)
    
    # Apply bitwise operations for adjustment factors
    adjustment_factor = 1.0
    bit_flags = 0b1101  # Control flags for different adjustment types
    
    if bit_flags & 0b0001:  # Check if first bit is set
        adjustment_factor *= 0.95  # 5% discount
    
    if bit_flags & 0b0010:  # Check if second bit is set
        adjustment_factor *= 1.02  # 2% tax
    
    if bit_flags & 0b0100:  # Check if third bit is set
        adjustment_factor *= 1.03  # 3% market adjustment
    
    if bit_flags & 0b1000:  # Check if fourth bit is set
        adjustment_factor *= 0.98  # 2% bulk discount
    
    # Calculate actual value with adjustments
    adjustment_sum = sum(price_adjustments.values())
    
    # Lambda to filter valid adjustments
    is_valid = lambda x: -1000 < x < 1000
    valid_adjustments = list(filter(is_valid, price_adjustments.values()))
    
    # Apply only relevant adjustments
    actual_value = (base_value * adjustment_factor) + \
                   (sum(valid_adjustments) if valid_adjustments else 0)
    
    return int(actual_value)

# Main inventory tracking
products_data = [
    {'id': 'A101', 'name': 'Widget', 'quantity': 150, 'unit_price': 12.99},
    {'id': 'B205', 'name': 'Gadget', 'quantity': 200, 'unit_price': 8.50},
    {'id': 'C309', 'name': 'Tool', 'quantity': 75, 'unit_price': 19.95},
    {'id': 'D413', 'name': 'Accessory', 'quantity': 100, 'unit_price': 6.75},
    {'id': 'E517', 'name': 'Component', 'quantity': 300, 'unit_price': 4.25}
]

# Tracking metrics (not relevant to main calculation)
metrics = {
    'total_sku_count': len(products_data),
    'avg_price': sum(p['unit_price'] for p in products_data) / len(products_data),
    'total_items': sum(p['quantity'] for p in products_data)
}

# Filter products based on criteria
min_price = 7.0
max_quantity = 250
filtered_products = [p for p in products_data if p['unit_price'] > min_price and p['quantity'] < max_quantity]

# Potential shipping costs (not used in inventory calculation)
shipping_estimates = {
    'A101': calculate_shipping_cost(0.5, 100),
    'B205': calculate_shipping_cost(0.8, 150),
    'C309': calculate_shipping_cost(2.1, 75),
    'D413': calculate_shipping_cost(0.3, 200),
    'E517': calculate_shipping_cost(0.4, 125)
}

# Counter to track product categories (distraction)
product_categories = Counter({
    'Electronics': 12,
    'Tools': 8,
    'Office': 15,
    'Kitchen': 7
})

# Price adjustments to apply
price_adjustments = defaultdict(int)
price_adjustments['seasonal_discount'] = -500
price_adjustments['tax_adjustment'] = 320
price_adjustments['bulk_bonus'] = -150
price_adjustments['shipping_offset'] = 75
price_adjustments['invalid_extreme'] = 50000  # Should be filtered out

# Apply discount rates to base prices (not used in final calculation)
discount_rates = {'A101': 0.10, 'C309': 0.15, 'E517': 0.05}
product_prices = {p['id']: p['unit_price'] for p in products_data}
discounted_prices = apply_discounts(product_prices, discount_rates)

# Calculate the actual inventory value
actual_inventory = calculate_inventory_value(filtered_products, price_adjustments)

# Additional calculations for reporting (not relevant to main result)
potential_value = sum(p['quantity'] * discounted_prices[p['id']] for p in products_data)
value_difference = potential_value - actual_inventory

print(f"Result: {actual_inventory}")