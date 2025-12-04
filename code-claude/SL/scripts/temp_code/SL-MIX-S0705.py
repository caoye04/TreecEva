def calculate_final_price(items, discounts, loyalty_points):
    # Process shopping cart items and apply discounts
    base_total = sum(price for item, price in items)
    
    # Apply discounts in order of priority
    sorted_discounts = sorted(discounts.items(), key=lambda x: x[1]['priority'])
    
    # Track applied discounts for reporting
    applied_discount_names = []
    discount_amount = 0
    
    # Process potential loyalty discount
    loyalty_discount = 0
    if loyalty_points > 500:
        loyalty_discount = min(loyalty_points * 0.01, 50)  # Max $50 discount
        applied_discount_names.append('Loyalty')
    
    # Apply item discounts
    for discount_name, details in sorted_discounts:
        if details['active'] and base_total >= details['min_purchase']:
            if details['type'] == 'percentage':
                current_discount = base_total * (details['value'] / 100)
            else:  # Fixed amount
                current_discount = details['value']
            
            # Some discounts can't be combined
            if details.get('exclusive', False) and discount_amount > 0:
                continue
                
            discount_amount += current_discount
            applied_discount_names.append(discount_name)
            
            # Early termination if we hit max discount
            if discount_amount >= base_total * 0.5:  # Max 50% total discount
                discount_amount = base_total * 0.5
                break
    
    # Calculate shipping based on subtotal (before loyalty)
    subtotal = base_total - discount_amount
    shipping_cost = 0
    if subtotal < 50:
        shipping_cost = 10
    elif subtotal < 100:
        shipping_cost = 5
    
    # Generate receipt data (not used in final calculation)
    receipt = {
        "items": len(items),
        "subtotal": base_total,
        "discounts": applied_discount_names,
        "discount_amount": discount_amount,
        "loyalty_applied": loyalty_discount > 0,
        "shipping": shipping_cost
    }
    
    # Calculate final price
    total_price = base_total - discount_amount - loyalty_discount + shipping_cost
    
    # Apply tax (fixed 8%)
    tax = (base_total - discount_amount - loyalty_discount) * 0.08
    total_with_tax = total_price + tax
    
    # Round to 2 decimal places
    return round(total_price, 2)

# Test data
cart_items = [('Shirt', 25.99), ('Pants', 34.50), ('Shoes', 89.99)]
discounts = {
    'SUMMER': {'priority': 2, 'active': True, 'type': 'percentage', 'value': 15, 'min_purchase': 100},
    'WELCOME': {'priority': 1, 'active': True, 'type': 'fixed', 'value': 10, 'min_purchase': 50, 'exclusive': True},
    'CLEARANCE': {'priority': 3, 'active': False, 'type': 'percentage', 'value': 25, 'min_purchase': 150}
}
loyalty_points = 600

# Calculate price with discounts and loyalty points
total_price = calculate_final_price(cart_items, discounts, loyalty_points)
print(f"Result: {total_price}")