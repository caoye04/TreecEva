from collections import Counter

recipes_text = [
    "flour eggs butter sugar",
    "flour milk sugar eggs",
    "butter flour sugar",
    "eggs flour milk"
]

ingredient_tokens = []
for recipe in recipes_text:
    tokens = recipe.split()
    ingredient_tokens.extend(tokens)

ingredient_counter = Counter(ingredient_tokens)
flour_count = ingredient_counter['flour']

print(f"Result: {flour_count}")