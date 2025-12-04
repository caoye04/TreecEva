import itertools

def calculate_product_checksum(products):
    # Checksum is calculated as XOR of product codes multiplied by their priority
    checksum = 0
    priority_map = {}
    
    # Generate priority values (distraction - never used)
    for i, category in enumerate(['electronics', 'clothing', 'food', 'books']):
        priority_map[category] = (i * 17) % 256
    
    # Track processing metrics (distraction)
    processed_items = 0
    skipped_items = 0
    error_count = 0
    
    for product in products:
        if product['in_stock'] is False:
            skipped_items += 1
            continue
            
        # Error detection logic (distraction - always evaluates to False)
        if product['code'] < 0 or 'price' not in product:
            error_count += 1
            product['code'] = 0
        
        # Apply various modifications (most are distractions)
        modified_code = product['code']
        
        # This is relevant for the calculation
        if product['category'] == 'priority':
            modified_code = (modified_code * 3) & 0xFF
        
        # These are distractions
        if product['price'] > 500:
            temp_code = (modified_code << 2) | 0x3
            if temp_code > 1000:
                modified_code = temp_code % 256
        
        if product['name'].startswith('X'):
            # This branch is never taken (distraction)
            modified_code = (modified_code + 42) % 256
        
        # This is the actual calculation that matters
        checksum ^= modified_code
        processed_items += 1
    
    # Distraction - this value isn't used
    efficiency = (processed_items / (processed_items + skipped_items + 0.001)) * 100
    
    return checksum

# Main inventory processing
inventory = [
    {'code': 120, 'name': 'Tablet', 'category': 'regular', 'price': 299, 'in_stock': True},
    {'code': 255, 'name': 'Smartphone', 'category': 'priority', 'price': 899, 'in_stock': True},
    {'code': 34, 'name': 'Headphones', 'category': 'regular', 'price': 149, 'in_stock': True},
    {'code': 88, 'name': 'Smartwatch', 'category': 'priority', 'price': 199, 'in_stock': True},
    {'code': 42, 'name': 'Charger', 'category': 'regular', 'price': 29, 'in_stock': False},
    {'code': 75, 'name': 'Speaker', 'category': 'regular', 'price': 129, 'in_stock': True},
    {'code': 101, 'name': 'Keyboard', 'category': 'priority', 'price': 89, 'in_stock': True},
    {'code': 63, 'name': 'X-Ray Specs', 'category': 'special', 'price': 999, 'in_stock': False}
]

# Generate product combinations (distraction)
combinations = list(itertools.combinations([p['name'] for p in inventory if p['in_stock']], 2))
combination_count = len(combinations)

# Filter products based on various criteria (mostly distractions)
min_price = 50
max_price = 1000
allowed_categories = ['regular', 'priority', 'special']
restricted_codes = [42, 13, 666]

# This variable is important
filtered_products = []
for product in inventory:
    # Distraction conditions that don't filter anything in our dataset
    if product['price'] < min_price and product['category'] not in ['priority', 'special']:
        continue
    if product['price'] > max_price and product['code'] not in [101, 255]:
        continue
    if product['code'] in restricted_codes and not product['name'].startswith('X'):
        continue
        
    # The only condition that actually matters
    if product['in_stock']:
        filtered_products.append(product)

# Calculate potential permutations (distraction)
potential_arrangements = 1
for i in range(len(filtered_products)):
    potential_arrangements *= (i + 1)

# Apply a complex discount formula (distraction)
discount_factor = 0
for p in filtered_products:
    if p['price'] > 100:
        discount_factor += (p['price'] * 0.05)
discount_factor = min(discount_factor, 100)

# This is the key calculation we're asking about
actual_checksum = calculate_product_checksum(filtered_products)

# More distractions after the key calculation
modified_checksum = (actual_checksum + int(discount_factor)) % 256
total_value = sum(p['price'] for p in filtered_products)
weighted_average = total_value / len(filtered_products) if filtered_products else 0

print(f"Result: {actual_checksum}")
