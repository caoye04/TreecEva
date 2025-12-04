import itertools
from functools import reduce

# Customer order information
order_items = {
    'book': {'weight': 0.5, 'quantity': 3, 'fragile': False},
    'glass': {'weight': 0.3, 'quantity': 2, 'fragile': True},
    'laptop': {'weight': 2.1, 'quantity': 1, 'fragile': True}
}

# Shipping rules database
shipping_rules = {
    'base_rate': 5.00,
    'weight_factor': 2.50,
    'fragile_surcharge': 3.75,
    'discount_threshold': 50.00,
    'bulk_discount': 0.15,
    'priority_multiplier': 1.5
}

# Tax calculation helper - not actually used for shipping
def calculate_tax(subtotal, tax_rate=0.08):
    return subtotal * tax_rate

# Customer information
customer_data = {
    'name': 'John Smith',
    'tier': 'gold',  # bronze, silver, gold, platinum
    'address': '123 Main St',
    'purchase_history': [120.50, 75.25, 210.00, 45.75],
    'account_age': 731  # days
}

# Loyalty program rules - seems important but mostly unused
loyalty_tiers = {
    'bronze': {'discount': 0.00, 'free_shipping_threshold': 100.00},
    'silver': {'discount': 0.05, 'free_shipping_threshold': 75.00},
    'gold': {'discount': 0.10, 'free_shipping_threshold': 50.00},
    'platinum': {'discount': 0.15, 'free_shipping_threshold': 25.00}
}

# Marketing promotion codes - not relevant to shipping
promotion_codes = {
    'WELCOME10': {'discount': 0.10, 'expires': '2023-12-31'},
    'HOLIDAY25': {'discount': 0.25, 'expires': '2023-11-30'},
    'FREESHIP': {'free_shipping': True, 'minimum_order': 35.00}
}

# Distance zones for shipping calculation
distance_zones = {
    'local': {'factor': 1.0, 'days': 1},
    'regional': {'factor': 1.2, 'days': 2},
    'national': {'factor': 1.5, 'days': 3},
    'international': {'factor': 2.5, 'days': 7}
}

# Calculate item value for insurance purposes
def calculate_item_value(items):
    item_prices = {'book': 12.99, 'glass': 8.50, 'laptop': 899.99}
    return sum(item_prices.get(item, 0) * details['quantity'] for item, details in items.items())

# Bit flags for shipping options
EXPRESS_SHIPPING = 0b0001
INSURED_SHIPPING = 0b0010
TRACKED_SHIPPING = 0b0100
SIGNATURE_REQUIRED = 0b1000

# Binary encoding for shipping options - not used in final calculation
def encode_shipping_options(express=False, insured=False, tracked=True, signature=False):
    options = 0
    if express: options |= EXPRESS_SHIPPING
    if insured: options |= INSURED_SHIPPING
    if tracked: options |= TRACKED_SHIPPING
    if signature: options |= SIGNATURE_REQUIRED
    return options

# Main shipping cost calculation
def calculate_shipping_cost(items, rules, customer_tier):
    # Calculate total weight and check for fragile items
    total_weight = sum(item['weight'] * item['quantity'] for item in items.values())
    has_fragile = any(item['fragile'] for item in items.values())
    
    # Calculate base shipping cost
    base_cost = rules['base_rate'] + (total_weight * rules['weight_factor'])
    
    # Apply fragile surcharge if needed
    if has_fragile:
        base_cost += rules['fragile_surcharge']
    
    # Calculate potential discounts based on order value
    item_count = sum(item['quantity'] for item in items.values())
    
    # This calculation appears important but doesn't affect the result
    potential_discount = 0
    if item_count > 5:
        potential_discount = base_cost * 0.05
    
    # Apply tier discount (key calculation)
    tier_discounts = {'bronze': 0.00, 'silver': 0.05, 'gold': 0.10, 'platinum': 0.15}
    tier_discount = tier_discounts.get(customer_tier, 0.00)
    
    # Misleading calculation that doesn't contribute to final result
    priority_cost = base_cost * rules['priority_multiplier']
    insurance_cost = calculate_item_value(items) * 0.01
    
    # Another distraction: calculate shipping days using a lambda
    get_shipping_days = lambda zone: distance_zones[zone]['days']
    estimated_days = get_shipping_days('national')  # Not used
    
    # More distractions: generate shipping code
    shipping_options = encode_shipping_options(tracked=True)
    tracking_enabled = shipping_options & TRACKED_SHIPPING > 0  # Always True
    
    # Final calculation with tier discount
    shipping_cost = base_cost * (1 - tier_discount)
    
    # Round to 2 decimal places
    return round(shipping_cost, 2)

# Process the order
customer_tier = customer_data['tier']

# This appears to be used but actually isn't relevant
order_value = calculate_item_value(order_items)
qualifies_free_shipping = order_value >= loyalty_tiers[customer_tier]['free_shipping_threshold']

# Calculate final shipping cost
shipping_cost = calculate_shipping_cost(order_items, shipping_rules, customer_tier)

# Apply a promotion code if valid - not actually used
active_promo = None
if active_promo and active_promo.get('free_shipping', False) and order_value >= active_promo.get('minimum_order', 0):
    shipping_cost = 0

print(f"Result: {shipping_cost}")