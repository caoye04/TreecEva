from collections import defaultdict
import math

def score_modifier(category):
    def decorator(func):
        def wrapper(*args, **kwargs):
            base_score = func(*args, **kwargs)
            if category == 'spice':
                return base_score * 1.5
            elif category == 'herb':
                return base_score + 10
            else:
                return base_score - 5
        return wrapper
    return decorator

ingredient_scores = {
    'basil': 20,
    'oregano': 15,
    'cinnamon': 30,
    'paprika': 25,
    'thyme': 18,
    'cardamom': 35
}

ingredient_categories = {
    'basil': 'herb',
    'oregano': 'herb',
    'cinnamon': 'spice',
    'paprika': 'spice',
    'thyme': 'herb',
    'cardamom': 'spice'
}

@score_modifier('spice')
def calculate_base_score(ingredients):
    total = 0
    for ingredient in ingredients:
        total += ingredient_scores.get(ingredient, 0)
    return total

selected_ingredients = ['basil', 'cinnamon', 'paprika', 'thyme']

# Step 1: Calculate initial modified score
initial_score = calculate_base_score(selected_ingredients)

# Step 2: Apply sorting and conditional adjustments
sorted_ingredients = sorted(selected_ingredients, key=lambda x: ingredient_scores[x], reverse=True)

bonus_points = 0
for i, ing in enumerate(sorted_ingredients):
    match ingredient_categories[ing]:  # Using structural pattern matching (switch-case)
        case 'herb' if i < 2:
            bonus_points += 5
        case 'spice' if i < 3:
            bonus_points += 7
        case _:
            bonus_points += 2

# Step 3: Aggregate scores with additional computations
aggregated_scores = defaultdict(int)
for ing in selected_ingredients:
    cat = ingredient_categories[ing]
    aggregated_scores[cat] += ingredient_scores[ing]

# Step 4: Final calculation incorporating all factors
culinary_score = initial_score + bonus_points + sum(aggregated_scores.values())
print(f'Result: {culinary_score}')