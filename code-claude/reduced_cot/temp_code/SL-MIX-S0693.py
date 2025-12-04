import itertools

def calculate_word_value(word, multipliers):
    # Letter values based on Scrabble-like scoring
    letter_values = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
        'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
        's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }
    
    value = 0
    for i, char in enumerate(word):
        # Apply position multipliers if available
        if i < len(multipliers):
            value += letter_values.get(char.lower(), 0) * multipliers[i]
        else:
            value += letter_values.get(char.lower(), 0)
    
    # Bonus for words of certain lengths
    length_bonus = max(0, len(word) - 4)
    
    return value + length_bonus

# Process text input
text = "programming puzzles are challenging and fun"
words = text.split()

# Distractor: Generate combinations that aren't used
combos = list(itertools.combinations(words, 2))
combo_lengths = [len(w1) + len(w2) for w1, w2 in combos]

# Filter words based on length
min_length = 5
max_length = 10
filtered_words = [word for word in words if min_length <= len(word) <= max_length]

# Distractor: Calculate average word length
avg_length = sum(len(word) for word in words) / len(words)

# Choose a specific word for processing
word_index = 2 % len(filtered_words)
filtered_word = filtered_words[word_index]

# Create letter position multipliers
base_multipliers = [1, 2, 1, 3, 1]
multiplier_cycles = itertools.cycle(base_multipliers)
multipliers = [next(multiplier_cycles) for _ in range(len(filtered_word))]

# Distractor: Create a different set of multipliers
alternate_multipliers = [2, 1, 2, 1, 2]

# Calculate the word value
word_score = calculate_word_value(filtered_word, multipliers)

# Distractor: Calculate another value that isn't used
alternate_score = sum(ord(c) % 26 for c in filtered_word)

print(f"Result: {word_score}")