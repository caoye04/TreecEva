import itertools

# Track player scores in a word game
player_names = ['Alex', 'Blake', 'Casey']
word_lengths = [4, 7, 5]

# Calculate base points (1 point per letter)
base_points = list(map(lambda x: x, word_lengths))

# Bonus points for words with odd lengths
bonus_points = [2 if length % 2 == 1 else 0 for length in word_lengths]

# Create player dictionary with initial scores
player_scores = {}
for name, base, bonus in zip(player_names, base_points, bonus_points):
    # Score formula: base points + bonus points
    player_scores[name] = base + bonus

# Apply special bonus for player with longest word
max_length_idx = word_lengths.index(max(word_lengths))
player_scores[player_names[max_length_idx]] += 3

# Deduct points for repeated letters
repeated_letter_penalty = 1
player_with_repeated = 'Blake'  # Blake has repeated letters
player_scores[player_with_repeated] -= repeated_letter_penalty

# Calculate final score
final_score = sum(player_scores.values())

print(f"Result: {final_score}")