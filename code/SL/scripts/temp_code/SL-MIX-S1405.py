recipes = [
    "flour,eggs,butter,sugar,vanilla",
    "eggs, milk, flour, sugar, cinnamon",
    "butter, sugar, chocolate, eggs, flour"
]

all_ingredients = []
for recipe in recipes:
    tokens = [token.strip().lower() for token in recipe.split(',')]
    all_ingredients.extend(tokens)

unique_ingredients = set(all_ingredients)
unique_ingredients_count = len(unique_ingredients)
print(f"Result: {unique_ingredients_count}")