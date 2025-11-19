def calculate_potency(ingredients):
    if not ingredients:
        return 0
    if len(ingredients) == 1:
        return ingredients[0]
    return ingredients[0] + calculate_potency(ingredients[1:])

recipe_ingredients = [3, -1, 4, -2, 5]
prefix_potencies = []
for i in range(1, len(recipe_ingredients) + 1):
    prefix = recipe_ingredients[:i]
    potency = calculate_potency(prefix)
    prefix_potencies.append(potency)
    if potency > 10:
        break

max_potency = max(prefix_potencies)
print(f"Result: {max_potency}")