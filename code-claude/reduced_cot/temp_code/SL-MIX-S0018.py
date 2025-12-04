# Word scoring system for a simple word game
# Each letter has a point value, and some special rules apply

# Points for each letter
points = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
         'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10,
         'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}

# Player information
player_name = "Alex"
bonus_multiplier = 1.5  # Unused in this calculation

# The word being scored
word = "python"

# Calculate word score - this is what we're interested in
total_score = sum(map(lambda x: points.get(x, 0), word))

# Apply bonus (not part of the question)
final_score = int(total_score * (2 if len(word) > 6 else 1))

print(f"Word: {word}")
print(f"Base score: {total_score}")
print(f"Final score: {final_score}")
