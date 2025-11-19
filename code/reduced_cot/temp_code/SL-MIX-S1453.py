from dataclasses import dataclass

ingredients_data = [
    {'name': 'saffron', 'flavor': 10, 'cost': 5},
    {'name': 'vanilla', 'flavor': 6, 'cost': 3},
    {'name': 'cardamom', 'flavor': 4, 'cost': 2},
    {'name': 'cinnamon', 'flavor': 8, 'cost': 4}
]

@dataclass
class Ingredient:
    name: str
    flavor: int
    cost: int
    ratio: float = 0.0

budget = 15
ingredients = [Ingredient(**item) for item in ingredients_data]
for ing in ingredients:
    ing.ratio = ing.flavor / ing.cost

sorted_ingredients = sorted(ingredients, key=lambda x: x.ratio, reverse=True)

total_flavor = 0
remaining_budget = budget
for ing in sorted_ingredients:
    if ing.cost <= remaining_budget:
        total_flavor += ing.flavor
        remaining_budget -= ing.cost

print(f"Result: {total_flavor}")