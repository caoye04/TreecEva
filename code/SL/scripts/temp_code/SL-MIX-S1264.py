import math

# Ingredient calories per unit
ingredient_calories = {'flour': 364, 'sugar': 387, 'butter': 717, 'eggs': 155}

# Batch sizes for processing
batch_sizes = [2, 1, 3, 2]

# Process ingredients using list comprehension and dictionary comprehension
processed_ingredients = {ingredient: calories * batch_sizes[idx] 
                        for idx, (ingredient, calories) in enumerate(ingredient_calories.items())}

# Tokenize the ingredient names into characters
char_tokens = [list(ingredient) for ingredient in ingredient_calories.keys()]

# Flatten the tokens and count unique characters
flattened_tokens = [char for sublist in char_tokens for char in sublist]
unique_char_count = len(set(flattened_tokens))

# Calculate total calories
final_dish_calories = sum(processed_ingredients.values()) + unique_char_count * 10

print(f'Result: {final_dish_calories}')