def calculate_fruit_shipping_cost():
    fruit_names = ['apple', 'banana', 'cherry']
    fruit_weights = [0.2, 0.3, 0.1]
    price_per_kg = 15.0
    
    # Convert names to uppercase for database consistency
    upper_names = [name.upper() for name in fruit_names]
    
    # Simulate sensor readings (irrelevant to final result)
    temperature_readings = [22.5, 23.1, 21.9]
    avg_temp = sum(temperature_readings) / len(temperature_readings)
    
    # Core computation
    total_weight = sum(fruit_weights)
    shipping_cost = total_weight * price_per_kg
    
    # Dummy operation using enumerate and zip
    indexed_data = list(enumerate(zip(fruit_names, fruit_weights)))
    
    # Lambda function for scaling (not used in main logic)
    scale_weight = lambda w: w * 1000
    scaled_weights = [scale_weight(w) for w in fruit_weights]
    
    # Print target result
    print(f"Result: {total_weight}")

calculate_fruit_shipping_cost()