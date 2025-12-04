def process_inventory(products):
    # Inventory processing system with security encoding
    inventory_stats = {'total': 0, 'categories': set()}
    product_codes = {}
    
    # Process each product
    for product in products:
        name, category, price = product
        inventory_stats['total'] += 1
        inventory_stats['categories'].add(category)
        
        # Generate product code (not used in final calculation)
        code = f"{name[:2].upper()}{len(category)}"
        product_codes[name] = code
    
    # Calculate category distribution (not directly used)
    category_counts = {}
    for product in products:
        category = product[1]
        if category in category_counts:
            category_counts[category] += 1
        else:
            category_counts[category] = 1
    
    # Security encoding for inventory value
    base_value = len(products) * 42  # Base value from inventory count
    validation_sum = sum(len(p[0]) for p in products)  # Checksum from product names
    
    # Apply security transformation
    bitwise_key = 0xA5  # Binary: 10100101
    mask = 0xFF  # Limit to 8 bits (0-255 range)
    
    # This is the critical security encoding step
    encrypted_value = (base_value ^ bitwise_key) & mask
    
    # Additional validation steps (not affecting encrypted_value)
    verification_code = validation_sum % 10
    secure_tuple = (encrypted_value, verification_code)
    
    print(f"Processed {len(products)} products in {len(inventory_stats['categories'])} categories")
    print(f"Result: {encrypted_value}")
    return secure_tuple

# Test with sample inventory
products = [
    ("Laptop", "Electronics", 1200),
    ("Headphones", "Electronics", 150),
    ("Desk", "Furniture", 350),
    ("Chair", "Furniture", 200)
]

process_inventory(products)