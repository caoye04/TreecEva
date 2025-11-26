def analyze_product_ratings():
    product_reviews = [4, 2, 5, 3, 4, 1, 5, 4, 2, 3]
    rating_categories = {}
    
    for rating in product_reviews:
        if rating in rating_categories:
            rating_categories[rating] += 1
        else:
            rating_categories[rating] = 1
    
    temp_calc = lambda x: x * 2 - 1
    processed_values = {}
    
    for key, value in rating_categories.items():
        processed_values[key] = temp_calc(value)
    
    target_key = max(processed_values, key=processed_values.get)
    final_result = processed_values[target_key]
    
    print(f"Result: {final_result}")

analyze_product_ratings()