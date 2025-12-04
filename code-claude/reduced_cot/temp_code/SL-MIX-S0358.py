import itertools

def calculate_letter_value(letter):
    # Calculate value based on position in alphabet (a=1, b=2, etc.)
    base_value = ord(letter.lower()) - ord('a') + 1
    # Bonus for vowels
    vowel_bonus = 5 if letter.lower() in 'aeiou' else 0
    # Penalty for letters after 'm'
    late_penalty = 2 if letter.lower() > 'm' else 0
    return base_value + vowel_bonus - late_penalty

def calculate_word_score(word):
    # Calculate base score for the word
    letter_scores = [calculate_letter_value(letter) for letter in word if letter.isalpha()]
    
    # Distractor calculation that doesn't affect result
    alternate_score = sum(ord(c) for c in word) % 10
    potential_multiplier = len(set(word.lower())) / len(word) if word else 1
    
    # Actual scoring logic
    if not letter_scores:
        return 0
    
    base_score = sum(letter_scores)
    # Bonus for words with more than 5 letters
    length_bonus = len(word) * 2 if len(word) > 5 else 0
    
    return base_score + length_bonus

# Sample text with various words
text = "Programming puzzles are both challenging and rewarding for developers."

# Processing the text
words = text.split()
distractor_list = words[::-1]  # Reversed list not used in final calculation

# Create a dictionary of word lengths (distractor)
word_lengths = {word: len(word) for word in words}

# Filter words based on certain criteria
filtered_words = []
for word in words:
    cleaned_word = word.strip('.,!?').lower()
    if len(cleaned_word) >= 4:  # Keep words with 4+ letters
        filtered_words.append(cleaned_word)
    elif cleaned_word.startswith('a') or cleaned_word.startswith('r'):
        # Special case for words starting with 'a' or 'r'
        filtered_words.append(cleaned_word)

# Another distractor - grouping by first letter (not used)
word_groups = {}
for word in filtered_words:
    first_letter = word[0] if word else ''
    if first_letter not in word_groups:
        word_groups[first_letter] = []
    word_groups[first_letter].append(word)

# Calculate intermediate scores
intermediate_scores = [calculate_word_score(word) for word in filtered_words]

# Some words get bonus points based on position
for i, score in enumerate(intermediate_scores):
    if i % 3 == 0:  # Every third word gets a bonus
        intermediate_scores[i] += 10

def calculate_final_score(word_list):
    # Calculate individual word scores
    word_scores = [calculate_word_score(word) for word in word_list]
    
    # Apply position-based adjustments
    adjusted_scores = []
    for i, score in enumerate(word_scores):
        if i % 3 == 0:  # Every third word gets a bonus
            adjusted_scores.append(score + 10)
        else:
            adjusted_scores.append(score)
    
    # Distractor calculation
    max_score = max(adjusted_scores) if adjusted_scores else 0
    min_score = min(adjusted_scores) if adjusted_scores else 0
    score_range = max_score - min_score
    
    # Calculate the actual total
    return sum(adjusted_scores)

total_score = calculate_final_score(filtered_words)
print(f"Result: {total_score}")