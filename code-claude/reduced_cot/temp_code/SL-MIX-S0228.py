from collections import Counter, defaultdict

def analyze_inventory(products, categories):
    # Track product metrics
    inventory_value = 0
    category_counts = defaultdict(int)
    product_combinations = []
    
    # Process each product
    for product, details in products.items():
        # Calculate product value
        price = details['price']
        quantity = details['quantity']
        product_value = price * quantity
        
        # Track category information
        category = details['category']
        category_counts[category] += quantity
        
        # Potential discount tracking (not used in final calculation)
        discount_eligible = quantity > 10 or price > 50
        potential_savings = price * 0.15 if discount_eligible else 0
        
        # Add to inventory value
        inventory_value += product_value
        
        # Create product combinations for analysis
        if category in categories:
            for other_product in products:
                if other_product != product and products[other_product]['category'] == category:
                    # Store as tuple with alphabetical sorting for set deduplication
                    combo = tuple(sorted([product, other_product]))
                    product_combinations.append(combo)
    
    # Find most common category
    category_items = Counter(category_counts).most_common()
    top_category = category_items[0][0] if category_items else None
    
    # Calculate unique product combinations
    unique_pairs = len(set(product_combinations))
    
    # Calculate alternative metric (not used in final result)
    category_diversity = len(category_counts) * 10
    
    print(f"Result: {unique_pairs}")
    return unique_pairs

# Test data
product_data = {
    'laptop': {'price': 800, 'quantity': 5, 'category': 'electronics'},
    'phone': {'price': 500, 'quantity': 10, 'category': 'electronics'},
    'headphones': {'price': 100, 'quantity': 15, 'category': 'electronics'},
    'desk': {'price': 300, 'quantity': 7, 'category': 'furniture'},
    'chair': {'price': 150, 'quantity': 12, 'category': 'furniture'},
    'lamp': {'price': 50, 'quantity': 20, 'category': 'lighting'}
}

relevant_categories = ['electronics', 'furniture']

# Run analysis
result = analyze_inventory(product_data, relevant_categories)
