import itertools

def analyze_inventory(products):
    # Extract categories and prices
    categories = {p['category'] for p in products}
    price_range = (min(p['price'] for p in products), max(p['price'] for p in products))
    
    # Filter products by condition
    in_stock_items = [p for p in products if p['stock'] > 0]
    premium_items = [p for p in products if p['price'] > 50]
    
    # Calculate average price (not used in final result)
    avg_price = sum(p['price'] for p in products) / len(products)
    
    # Find items that meet promotion criteria
    promotion_candidates = {}
    for p in products:
        if p['rating'] >= 4.0 and p['stock'] >= 5:
            promotion_candidates[p['id']] = p['category']
    
    # Generate all possible category pairs (distraction)
    category_pairs = list(itertools.combinations(categories, 2))
    
    # Check which products have discount applied
    discount_flag = any(p.get('discount', False) for p in products)
    
    # Count items that meet our target criteria
    valid_items = [p for p in in_stock_items 
                  if (p['category'] in ['electronics', 'books']) 
                  and (p['price'] < 100 or p['rating'] > 4.5)]
    
    result_count = len(valid_items)
    
    # Additional calculations that don't affect the result
    potential_revenue = sum(p['price'] * p['stock'] for p in products)
    category_counts = {cat: sum(1 for p in products if p['category'] == cat) for cat in categories}
    
    print(f"Target result: {result_count}")
    return result_count

# Test data
product_inventory = [
    {'id': 101, 'category': 'electronics', 'price': 120, 'stock': 10, 'rating': 4.7},
    {'id': 102, 'category': 'books', 'price': 15, 'stock': 25, 'rating': 4.2},
    {'id': 103, 'category': 'clothing', 'price': 35, 'stock': 5, 'rating': 3.8},
    {'id': 104, 'category': 'electronics', 'price': 85, 'stock': 8, 'rating': 4.5},
    {'id': 105, 'category': 'books', 'price': 45, 'stock': 0, 'rating': 4.9},
    {'id': 106, 'category': 'electronics', 'price': 65, 'stock': 12, 'rating': 4.0},
    {'id': 107, 'category': 'books', 'price': 25, 'stock': 15, 'rating': 3.7}
]

analyze_inventory(product_inventory)