from collections import Counter

recipes = [
    "flour eggs butter sugar",
    "flour milk sugar eggs",
    "butter flour sugar",
    "eggs milk flour"
]

all_ingredients = []
for recipe in recipes:
    tokens = recipe.split()
    all_ingredients.extend(tokens)

ingredient_counter = Counter(all_ingredients)
flour_count = ingredient_counter['flour']

print(f"Result: {flour_count}")