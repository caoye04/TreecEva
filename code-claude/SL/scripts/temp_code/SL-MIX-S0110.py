from collections import Counter

def calculate_word_score(word, values):
    # Calculate score based on letter values
    score = 0
    letter_counts = Counter(word.lower())
    
    # Track unique vowels for potential bonus
    vowels = set()
    consonant_score = 0
    
    for letter, count in letter_counts.items():
        if letter in values:
            # Add letter value multiplied by its count
            score += values[letter] * count
            
            # Track vowels for bonus calculation
            if letter in 'aeiou':
                vowels.add(letter)
            else:
                consonant_score += count
    
    # Apply vowel bonus if at least 3 unique vowels
    vowel_bonus = 15 if len(vowels) >= 3 else 0
    
    # Apply consonant penalty - not used in final calculation
    consonant_penalty = consonant_score * 0.5
    
    # Calculate potential multiplier - not used in final score
    potential_multiplier = len(set(word)) / len(word) if len(word) > 0 else 0
    
    # Apply length modifier
    if len(word) >= 8:
        score += 10
    elif len(word) <= 3:
        score -= 5
    
    # Add vowel bonus to score
    score += vowel_bonus
    
    return int(score)

# Define letter values
letter_values = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# Process some sample words - these don't affect the final result
sample_words = ["hello", "python", "algorithm"]
sample_scores = {}

for word in sample_words:
    # Calculate but don't use these scores
    temp_score = calculate_word_score(word, letter_values)
    sample_scores[word] = temp_score

# Target word to evaluate
target_word = "education"

# Calculate the score for the target word
word_score = calculate_word_score(target_word, letter_values)

# Display the result
print(f"Result: {word_score}")