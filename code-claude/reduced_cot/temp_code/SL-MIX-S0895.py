def calculate_weighted_checksum(product_data, weights):
    """Calculate a weighted checksum for product verification."""
    valid_items = 0
    invalid_items = 0
    checksum = 0
    
    # Tracking system for debugging
    debug_values = {}
    error_codes = [404, 500, 302, 200, 403]
    
    # Process each product entry
    for idx, product in enumerate(product_data):
        # Extract product code and quantity
        code, quantity = product
        
        # Store debug information
        debug_values[f"product_{idx}"] = (code, quantity)
        
        # Apply weight factor if available, otherwise use default
        weight = weights.get(code % 10, 1)
        
        # Complex validation logic (distraction)
        validation_score = sum(int(digit) for digit in str(code)) * 0.1
        if validation_score > 5:
            valid_items += 1
            potential_value = error_codes[valid_items % len(error_codes)]
        else:
            invalid_items += 1
            potential_value = -1 * (code % 100)
        
        # Calculate contribution to checksum
        if code > 1000 and quantity > 0:
            contribution = (code % 100) * weight * (1 if quantity > 10 else quantity / 10)
            checksum += contribution
    
    # Alternative calculation path (distraction)
    alternative_sum = sum(p[0] for p in product_data if p[1] > 5)
    recovery_factor = (valid_items - invalid_items) * 2
    
    # Apply final transformations
    checksum = checksum * (1 + 0.01 * (valid_items % 3))
    
    # Format debug output (distraction)
    debug_output = {
        "valid": valid_items,
        "invalid": invalid_items,
        "alt_sum": alternative_sum,
        "recovery": recovery_factor
    }
    
    return int(checksum) if checksum > 0 else 0

# Main processing
def process_inventory():
    # Product inventory: (product_code, quantity)
    inventory = [(1234, 5), (5678, 15), (9012, 3), (3456, 0), (7890, 20)]
    
    # Potential inventory updates (distraction)
    pending_orders = {
        1234: 10,
        5678: -5,
        9999: 15
    }
    
    # Weight factors based on product category (last digit of code)
    weight_factors = {
        4: 1.5,  # Electronics
        8: 2.0,  # Furniture
        2: 0.8,  # Clothing
        6: 1.2   # Books
    }
    
    # Apply pending orders (distraction)
    updated_inventory = []
    for item in inventory:
        code, qty = item
        if code in pending_orders:
            new_qty = max(0, qty + pending_orders[code])
            updated_inventory.append((code, new_qty))
        else:
            updated_inventory.append(item)
    
    # Calculate inventory metrics (distraction)
    total_items = sum(item[1] for item in inventory)
    avg_quantity = total_items / len(inventory) if inventory else 0
    
    # Process original inventory data
    product_data = [(item[0], item[1]) for item in inventory]
    
    # Calculate the actual checksum
    actual_checksum = calculate_weighted_checksum(product_data, weight_factors)
    
    # Generate verification code (distraction)
    verification_code = sum(code % 1000 for code, _ in updated_inventory)
    security_hash = verification_code ^ (total_items * 10)
    
    # Final reporting
    report = {
        "inventory_count": total_items,
        "average_qty": avg_quantity,
        "security_code": security_hash,
        "checksum": actual_checksum
    }
    
    print(f"Result: {actual_checksum}")
    return report

# Run the process
process_inventory()