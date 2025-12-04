def analyze_inventory(products):
    # Process inventory data
    product_codes = [p['code'] for p in products if p['stock'] > 0]
    
    # Calculate total stock (distractor - not used in final result)
    total_stock = sum(p['stock'] for p in products)
    
    # Filter products based on multiple conditions
    high_demand = [p for p in products if p['demand'] > 50 and p['price'] < 100]
    low_supply = [p for p in products if p['stock'] < 20]
    
    # Perform intermediate calculations (some are distractors)
    avg_price = sum(p['price'] for p in products) / len(products) if products else 0
    max_stock = max(p['stock'] for p in products) if products else 0
    
    # Critical logic: count products meeting specific criteria
    filtered_products = len([p for p in products 
                           if p['category'] == 'electronics' 
                           and p['price'] >= 50 
                           and p['stock'] > 10])
    
    # Final assignment
    final_count = filtered_products
    print(f"Result: {final_count}")
    return final_count

# Test data
products = [
    {'code': 'A001', 'category': 'electronics', 'price': 75, 'stock': 15, 'demand': 60},
    {'code': 'A002', 'category': 'electronics', 'price': 45, 'stock': 25, 'demand': 40},
    {'code': 'B001', 'category': 'furniture', 'price': 120, 'stock': 8, 'demand': 30},
    {'code': 'A003', 'category': 'electronics', 'price': 90, 'stock': 5, 'demand': 80},
    {'code': 'C001', 'category': 'clothing', 'price': 35, 'stock': 30, 'demand': 70},
    {'code': 'A004', 'category': 'electronics', 'price': 150, 'stock': 12, 'demand': 45}
]

analyze_inventory(products)