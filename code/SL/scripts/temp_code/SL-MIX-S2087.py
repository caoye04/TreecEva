def track_unique_ingredients(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        wrapper.total += len(result)
        return result
    wrapper.total = 0
    return wrapper

@track_unique_ingredients
def process_recipe(ingredients):
    return frozenset(ingredients)

recipe_1 = ['flour', 'egg', 'sugar']
recipe_2 = ['milk', 'egg', 'butter']
recipe_3 = ['flour', 'butter', 'sugar', 'chocolate']

process_recipe(recipe_1)
process_recipe(recipe_2)
process_recipe(recipe_3)

final_ingredient_count = track_unique_ingredients.total
print(f'Result: {final_ingredient_count}')