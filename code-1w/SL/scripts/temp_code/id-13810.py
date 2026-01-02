items = [
    {'name': 'apple', 'weight': 2.5, 'category': 'fruit'},
    {'name': 'carrot', 'weight': 1.2, 'category': 'vegetable'},
    {'name': 'banana', 'weight': 3.0, 'category': 'fruit'},
    {'name': 'potato', 'weight': 1.8, 'category': 'vegetable'},
    {'name': 'grape', 'weight': 0.5, 'category': 'fruit'}
]

# Extract weights of items in 'fruit' category using list comprehension
fruit_weights = [item['weight'] for item in items if item['category'] == 'fruit']

# Apply filtering condition: only fruits heavier than 1.0
filtered_weights = [w for w in fruit_weights if w > 1.0]

# Compute total weight of filtered fruits
total_weight = sum(filtered_weights)

# Print result
print(f"Result: {total_weight}")