from functools import reduce

# Chef's original list of ingredients
ingredients = ['salt', 'pepper', 'garlic', 'oregano', 'basil', 'thyme', 'parsley', 'rosemary']

# Tokenize by taking first letter of each ingredient
tokenized = list(map(lambda x: x[0], ingredients))

# Divide the tokens into two halves using slicing (divide and conquer approach)
midpoint = len(tokenized) // 2
first_half_tokens = tokenized[:midpoint]
second_half_tokens = tokenized[midpoint:]

# Convert to sets for efficient intersection operation
first_set = set(first_half_tokens)
second_set = set(second_half_tokens)

# Find common elements between the two sets
common_ingredients_count = len(first_set & second_set)

print(f'Result: {common_ingredients_count}')