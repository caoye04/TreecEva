ingredients = 'oregano basil thyme oregano parsley thyme'

tokens = ingredients.split()
unique_tokens = set(tokens)

flavor_count = 0
for token in unique_tokens:
    flavor_count += 1

print(f'Result: {flavor_count}')