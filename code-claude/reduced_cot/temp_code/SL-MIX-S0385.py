import itertools

def calculate_valid_combinations(ingredients, allergies):
    # Calculate valid combinations of ingredients without allergens
    valid_count = 0
    total_possibilities = 0
    
    # Track nutrition values (not used in final calculation)
    nutrition_values = {
        'apple': {'calories': 95, 'protein': 0.5},
        'banana': {'calories': 105, 'protein': 1.3},
        'carrot': {'calories': 50, 'protein': 1.1},
        'date': {'calories': 282, 'protein': 2.5},
        'eggplant': {'calories': 25, 'protein': 1.0}
    }
    
    # Generate all possible combinations of 3 ingredients
    all_combinations = list(itertools.combinations(ingredients, 3))
    total_possibilities = len(all_combinations)
    
    # Calculate average nutrition (distractor calculation)
    avg_calories = sum(nutrition_values[ing]['calories'] for ing in ingredients) / len(ingredients)
    
    # Filter combinations with allergens
    safe_combinations = []
    for combo in all_combinations:
        # Check if combination contains any allergens
        is_safe = True
        allergen_count = 0
        for item in combo:
            if item in allergies:
                allergen_count += 1
                is_safe = False
                break
        
        # Track safe combinations
        if is_safe:
            safe_combinations.append(combo)
            valid_count += 1
    
    # Calculate theoretical max (distractor calculation)
    max_theoretical = total_possibilities - len(allergies)
    if max_theoretical < 0:
        max_theoretical = 0
    
    # Return number of valid combinations
    return valid_count

# Main program
ingredients = ['apple', 'banana', 'carrot', 'date', 'eggplant']
allergies = ['banana', 'eggplant']

# Calculate shopping cost (distractor calculation)
prices = {'apple': 1.20, 'banana': 0.50, 'carrot': 0.30, 'date': 2.10, 'eggplant': 1.80}
total_cost = sum(prices[item] for item in ingredients)

# Calculate valid combinations
valid_combinations = calculate_valid_combinations(ingredients, allergies)

# Calculate average price of allergens (distractor calculation)
avg_allergen_price = sum(prices[item] for item in allergies) / len(allergies)

print(f"Result: {valid_combinations}")