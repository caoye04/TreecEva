from collections import Counter

def calculate_weighted_score(frequencies, bonus):
    # Base calculation
    letter_values = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1,
                    'b': 2, 'c': 2, 'd': 2, 'f': 2, 'g': 2,
                    'h': 3, 'j': 3, 'k': 3, 'l': 3, 'm': 3,
                    'n': 4, 'p': 4, 'q': 4, 'r': 4, 's': 4,
                    't': 5, 'v': 5, 'w': 5, 'x': 8, 'y': 8, 'z': 10}
    
    # Calculate preliminary score
    preliminary_score = sum(frequencies[letter] * letter_values.get(letter, 0) for letter in frequencies)
    
    # Potential multipliers (not all used)
    vowel_multiplier = 1.5 if sum(frequencies.get(v, 0) for v in 'aeiou') > 10 else 1.0
    consonant_bonus = sum(frequencies.get(c, 0) for c in 'bcdfghjklmnpqrstvwxyz') // 5
    
    # Check for special combinations
    has_special = any(frequencies.get(letter, 0) >= 3 for letter in 'xyz')
    special_modifier = 1.25 if has_special else 1.0
    
    # Calculate challenge words (distractor calculation)
    challenge_words = ['python', 'algorithm', 'benchmark', 'language']
    challenge_points = sum(len(word) for word in challenge_words if sum(c in frequencies for c in word) > 4)
    
    # Apply modifiers selectively
    modified_score = preliminary_score * special_modifier
    
    # Apply bonus points with a cap
    bonus_cap = min(bonus, 50)
    final_score = modified_score + bonus_cap + consonant_bonus
    
    return int(final_score)

# Analyze text sample
sample_text = "programming challenges require logical thinking and problem solving skills"

# Process the text
word_frequencies = Counter(sample_text.lower().replace(" ", ""))

# Calculate metrics (some are distractors)
num_words = len(sample_text.split())
average_word_length = sum(len(word) for word in sample_text.split()) / num_words
unique_letters = len(set(sample_text.lower().replace(" ", "")))

# Set bonus points based on some metrics
bonus_points = int(unique_letters * 1.5)

# Apply penalties for common letters (distractor)
penalty = 0
for common in 'etaoin':
    if word_frequencies.get(common, 0) > 5:
        penalty += 2

# This is the key calculation
total_score = calculate_weighted_score(word_frequencies, bonus_points)

# Final adjustments (distractor)
adjusted_score = total_score - penalty
if 'z' in word_frequencies or 'x' in word_frequencies:
    adjusted_score += 15

print(f"Result: {total_score}")