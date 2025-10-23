import re

dish_ingredients = [
    "flour, eggs, sugar, butter",
    "flour, milk, eggs, cheese",
    "sugar, butter, chocolate, flour",
    "milk, sugar, eggs, vanilla",
    "butter, chocolate, sugar, nuts"
]

# Parse ingredients using regex and store as sets
parsed_dishes = [set(re.split(r',\s*', dish)) for dish in dish_ingredients]

# Count occurrences of each ingredient across all dishes
ingredient_count = {}
for dish in parsed_dishes:
    for ingredient in dish:
        ingredient_count[ingredient] = ingredient_count.get(ingredient, 0) + 1

# Count how many ingredients appear in exactly two dishes
dual_ingredient_count = sum(1 for count in ingredient_count.values() if count == 2)

print(f"Result: {dual_ingredient_count}")