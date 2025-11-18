from functools import reduce

# Raw ingredient data with inconsistent formatting
ingredient_list = ['  salt', 'PEPPER  ', '  oLiVe Oil', 'garlic POWDER ']

# Process ingredients: strip whitespace, title case, and join with commas
processed_ingredients = ', '.join(map(lambda x: x.strip().title(), ingredient_list))

# Calculate final string length
final_length = len(processed_ingredients)

print(f'Result: {final_length}')