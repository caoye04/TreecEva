def calculate_net_sales(inventory, transactions):
    total_revenue = 0
    discount_total = 0
    tax_rate = 0.08
    
    # Calculate potential revenue based on inventory
    potential_revenue = sum(item['price'] * item['quantity'] for item in inventory.values())
    
    # Process actual transactions
    for transaction in transactions:
        product_id = transaction['product_id']
        quantity = transaction['quantity']
        
        if product_id in inventory and inventory[product_id]['quantity'] >= quantity:
            # Valid transaction
            price = inventory[product_id]['price']
            subtotal = price * quantity
            
            # Apply discount if applicable
            if transaction.get('discount_code') == 'SUMMER20':
                discount = subtotal * 0.20
                discount_total += discount
                subtotal -= discount
            
            # Track sales
            inventory[product_id]['quantity'] -= quantity
            total_revenue += subtotal
    
    # Calculate shipping costs (not affecting net sales)
    shipping_cost = 15 if total_revenue < 100 else 0
    
    # Calculate tax amount (not included in net sales)
    tax_amount = total_revenue * tax_rate
    
    # Calculate loyalty points (tracking only)
    loyalty_points = int(total_revenue / 10)
    
    return total_revenue

# Inventory with product details
inventory = {
    'P001': {'name': 'Laptop', 'price': 1200, 'quantity': 5},
    'P002': {'name': 'Headphones', 'price': 80, 'quantity': 15},
    'P003': {'name': 'Keyboard', 'price': 60, 'quantity': 10},
    'P004': {'name': 'Mouse', 'price': 25, 'quantity': 20}
}

# Customer transactions
transactions = [
    {'product_id': 'P001', 'quantity': 2, 'discount_code': 'SUMMER20'},
    {'product_id': 'P002', 'quantity': 3, 'discount_code': None},
    {'product_id': 'P003', 'quantity': 1, 'discount_code': 'SUMMER20'},
    {'product_id': 'P005', 'quantity': 2, 'discount_code': None}  # Invalid product
]

net_sales = calculate_net_sales(inventory, transactions)
print(f"Result: {net_sales}")