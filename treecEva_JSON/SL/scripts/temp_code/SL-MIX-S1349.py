from collections import Counter
import re

recipes_log = ['flour', 'Flour ', ' sugar', 'SUGAR', 'salt ', '  Salt']
ingredient_counter = Counter()

for item in recipes_log:
    normalized = re.sub(r'[^a-zA-Z]', '', item).lower()
    ingredient_counter[normalized] += 1

total_ingredients = sum(ingredient_counter.values())
distinct_ingredients = len(ingredient_counter)

secret_ratio = total_ingredients * distinct_ingredients // 2

print(f'Result: {secret_ratio}')