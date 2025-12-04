from collections import Counter

def calculate_discounts(purchases, loyalty_points):
    # Base discount percentage
    base_discount = 5
    
    # Calculate item frequency
    item_counts = Counter(purchases)
    
    # Apply discount rules
    customer_discount = {}
    for item, count in item_counts.items():
        # Regular items get base discount
        if item.startswith('regular_'):
            customer_discount[item] = base_discount
        # Premium items get higher discount
        elif item.startswith('premium_'):
            customer_discount[item] = base_discount * 1.5
        # Sale items get conditional discount based on quantity
        elif item.startswith('sale_'):
            customer_discount[item] = base_discount * 2 if count > 1 else base_discount
    
    # Loyalty bonus (0.5% per 100 points)
    loyalty_bonus = loyalty_points // 100 * 0.5
    
    # Apply loyalty bonus to all items
    for item in customer_discount:
        customer_discount[item] += loyalty_bonus
    
    # Calculate total discount
    total_discount = sum(customer_discount.values())
    
    print(f"Total discount: {total_discount}")
    return total_discount

# Customer data
purchases = ['regular_shirt', 'premium_jeans', 'sale_socks', 'sale_socks']
loyalty_points = 250

# Process customer discounts
final_discount = calculate_discounts(purchases, loyalty_points)
