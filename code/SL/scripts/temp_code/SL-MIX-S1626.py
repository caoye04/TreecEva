ingredients_popularity = [7, 7, 5, 5, 3, 3, 2]
threshold = 15
selected_ingredients = []
selected_popularity = 0
for popularity in sorted(ingredients_popularity, reverse=True):
    if selected_popularity + popularity <= threshold:
        selected_ingredients.append(popularity)
        selected_popularity += popularity
print(f"Result: {selected_popularity}")