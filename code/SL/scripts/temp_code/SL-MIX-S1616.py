ingredients = ['flour', 'eggs', 'butter', 'sugar', 'vanilla']
ingredient_ids = {name: (lambda s: hash(s) % 1000)(name) for name in ingredients}
checksum = sum(ingredient_ids.values()) % 1000
print(f"Result: {checksum}")