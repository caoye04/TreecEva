# Word puzzle scoring system

target_word = "lighthouse"
target_letters = set(target_word)

# Dictionary of candidate words and their respective points
word_points = {
    "house": 12,
    "light": 15,
    "ghost": 18,
    "sight": 20,
    "height": 25
}

# Sort words by their point values for display purposes
sorted_words = sorted(word_points.items(), key=lambda x: x[1], reverse=True)
top_scoring = sorted_words[0][0]

# Calculate bonus points based on word length
bonus_multiplier = 1.5
word_length_bonus = {word: len(word) * bonus_multiplier for word in word_points}

# Find candidate word that matches criteria
candidate_word = ""
for word in word_points:
    # Check if the word has more than 4 letters
    if len(word) > 4:
        # Check if the word contains the letter 'h'
        if 'h' in word:
            # Check if the word's points are above average
            avg_points = sum(word_points.values()) / len(word_points)
            if word_points[word] > avg_points:
                candidate_word = word
                break

# Calculate unused letters in target word
unused_letters = target_letters.difference(set(candidate_word))
unused_count = len(unused_letters)

# Calculate letter frequency in candidate word
letter_freq = {}
for letter in candidate_word:
    if letter in letter_freq:
        letter_freq[letter] += 1
    else:
        letter_freq[letter] = 1

# Find common letters between candidate word and target word
common_letters = len(set(candidate_word).intersection(target_letters))

# Calculate final score (not used in the answer)
final_score = word_points[candidate_word] + common_letters * 2 - unused_count

# Display some statistics (not affecting the answer)
print(f"Candidate word: {candidate_word}")
print(f"Word length: {len(candidate_word)}")
print(f"Common letters with target: {common_letters}")
