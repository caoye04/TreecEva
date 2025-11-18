import math

def recipe_encoder(ingredient_count):
    return math.log(2 ** ingredient_count)

# Baker's popular cake recipes ingredient counts
ingredient_counts = [5, 3, 7, 2, 4]

# Calculate encodings for all recipes
encodings = [recipe_encoder(count) for count in ingredient_counts]

# Sort encodings to find the most balanced one
sorted_encodings = sorted(encodings)

# Select the middle encoding (median)
selected_encoding = sorted_encodings[len(sorted_encodings) // 2]

print(f"Result: {selected_encoding}")