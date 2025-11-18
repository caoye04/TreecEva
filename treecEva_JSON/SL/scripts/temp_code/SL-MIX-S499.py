import re

def adjust_quantities(recipe, factor):
    if not recipe:
        return {}
    return {k: v * factor if isinstance(v, (int, float)) else adjust_quantities(v, factor) for k, v in recipe.items()}

base_recipe = {'flour': 2, 'sugar': 1, 'eggs': 3}
special_additions = {'chocolate_chips': 0.5, 'vanilla_extract': 0.2}

updated_recipe = {**base_recipe, **special_additions}
adjusted_recipe = adjust_quantities(updated_recipe, 2)

pattern = r'^(chocolate|vanilla).*'
final_quantity = sum(v for k, v in adjusted_recipe.items() if re.match(pattern, k))

print(f"Result: {final_quantity}")