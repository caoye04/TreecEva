daily_ingredients = {
    'monday': {'flour': 5, 'eggs': 12, 'butter': 2},
    'tuesday': {'flour': 3, 'sugar': 4, 'eggs': 6},
    'wednesday': {'milk': 3, 'flour': 2, 'eggs': 4},
    'thursday': {'butter': 1, 'sugar': 2, 'flour': 4},
    'friday': {'eggs': 8, 'milk': 2, 'butter': 3}
}

# Get all unique ingredients used during the week
all_ingredients = set().union(*[set(day.keys()) for day in daily_ingredients.values()])

# Calculate total quantity per ingredient using dictionary comprehension
ingredient_totals = {ingredient: sum(daily_ingredients[day].get(ingredient, 0) for day in daily_ingredients) for ingredient in all_ingredients}

# Sum all ingredient totals
total_quantity = sum(ingredient_totals.values())

print(f"Result: {total_quantity}")