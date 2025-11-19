ingredients_scores = [84, 92, 76, 99, 88]

# Sort the scores in descending order using Python's built-in sorted function
sorted_scores = sorted(ingredients_scores, reverse=True)

# Extract the second highest score
second_highest_score = sorted_scores[1]

print(f"Result: {second_highest_score}")