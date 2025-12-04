def analyze_inventory(products):
    # Calculate price statistics
    total_price = 0
    max_price = 0
    discount_factor = 0.85
    premium_threshold = 50
    
    # Track product name lengths
    name_lengths = []
    categories = {}
    
    for product in products:
        name = product['name']
        price = product['price']
        category = product['category']
        
        # Process price data
        total_price += price
        if price > max_price:
            max_price = price
            premium_product = name
        
        # Process name length data
        length = len(name)
        name_lengths.append(length)
        
        # Track categories
        if category in categories:
            categories[category] += 1
        else:
            categories[category] = 1
    
    # Calculate average price
    avg_price = total_price / len(products) if products else 0
    
    # Find most frequent name length
    lengths_freq = {}
    for length in name_lengths:
        if length in lengths_freq:
            lengths_freq[length] += 1
        else:
            lengths_freq[length] = 1
    
    # Get the most common length
    most_frequent_length = lengths_freq[max(lengths_freq, key=lengths_freq.get)]
    
    # Calculate potential discount savings (not used in final result)
    potential_savings = total_price * (1 - discount_factor)
    
    # Count premium products (not used in final result)
    premium_count = sum(1 for product in products if product['price'] > premium_threshold)
    
    # Find most popular category (not used in final result)
    most_popular_category = max(categories, key=categories.get)
    
    print(f"Result: {most_frequent_length}")
    return most_frequent_length

inventory = [
    {'name': 'Laptop', 'price': 999, 'category': 'Electronics'},
    {'name': 'Headphones', 'price': 99, 'category': 'Electronics'},
    {'name': 'Mouse', 'price': 25, 'category': 'Electronics'},
    {'name': 'Keyboard', 'price': 60, 'category': 'Electronics'},
    {'name': 'Monitor', 'price': 300, 'category': 'Electronics'},
    {'name': 'Mouse Pad', 'price': 15, 'category': 'Accessories'},
    {'name': 'USB Cable', 'price': 10, 'category': 'Accessories'},
    {'name': 'Webcam', 'price': 80, 'category': 'Electronics'}
]

result = analyze_inventory(inventory)