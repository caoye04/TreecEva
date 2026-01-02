def compute_weather_score():
    temperatures = [23, 18, 27, 32, 15]
    city_codes = ['NYC', 'LAX', 'CHI', 'MIA', 'SEA']
    
    # Create dictionary mapping city codes to adjusted temperatures
    temperature_map = {}
    for i in range(len(city_codes)):
        temperature_map[city_codes[i]] = temperatures[i] + 2

    city_key = 'MIA'
    base_value = temperature_map[city_key]
    
    # Logical flag and numeric adjustments
    is_coastal = True
    is_valid = is_coastal and (base_value > 30)
    adjustment_factor = 1.5 if is_valid else 0.8
    offset = 5

    # Key computation step
    final_score = temperature_map[city_key] * adjustment_factor + (is_valid and offset)
    
    # Irrelevant tracking variable (minor distraction)
    record_count = len(temperature_map)
    
    print(f"Result: {final_score}")

compute_weather_score()