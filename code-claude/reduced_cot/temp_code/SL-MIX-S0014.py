# Function to analyze recipe ingredient commonality
def calculate_ingredient_stats(recipe_a, recipe_b):
    # Convert ingredients to sets for efficient operations
    set_a = set(recipe_a)
    set_b = set(recipe_b)
    
    # Calculate unique ingredients in each recipe
    unique_a = set_a - set_b
    unique_b = set_b - set_a
    
    # Find shared ingredients
    shared_ingredients = set_a.intersection(set_b)
    
    # Some metrics that aren't directly used in our answer
    uniqueness_score = len(unique_a) * 2 + len(unique_b) * 3
    compatibility_index = (len(shared_ingredients) / (len(set_a) + len(set_b) - len(shared_ingredients))) * 10
    
    return shared_ingredients, uniqueness_score, compatibility_index

# Recipe ingredients lists
traditional_recipe = ["flour", "sugar", "eggs", "butter", "milk", "vanilla"]
modern_variant = ["flour", "sugar", "eggs", "oil", "almond_milk", "vanilla", "cinnamon"]

# Additional recipes for comparison (not directly used in final answer)
experimental_recipe = ["coconut_flour", "honey", "eggs", "coconut_oil", "almond_milk", "vanilla", "cardamom"]

# Track ingredient frequency across all recipes
ingredient_counter = {}
for i, recipe in enumerate([traditional_recipe, modern_variant, experimental_recipe]):
    for ingredient in recipe:
        if ingredient in ingredient_counter:
            ingredient_counter[ingredient] += i + 1  # Weighted counting
        else:
            ingredient_counter[ingredient] = 1

# Process the main recipes
shared_ingredients, uniqueness, compatibility = calculate_ingredient_stats(traditional_recipe, modern_variant)

# Calculate modular sums for some common ingredients (distraction)
mod_sum = 0
for i, ingredient in enumerate(shared_ingredients):
    mod_sum = (mod_sum + (i * 7) % 11) % 20

# This is the key statement for our question
common_elements = len(shared_ingredients)

# Early return if no common elements (would never execute with our data)
if common_elements == 0:
    print("Result: 0")
    exit()

# Calculate a compatibility percentage (distraction)
compatibility_percentage = (common_elements / len(set(traditional_recipe).union(set(modern_variant)))) * 100

print(f"Result: {common_elements}")