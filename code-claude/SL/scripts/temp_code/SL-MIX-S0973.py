def calculate_word_score(word):
    # Calculate a score based on character positions and frequencies
    char_values = {chr(i + 97): i + 1 for i in range(26)}  # a=1, b=2, ..., z=26
    
    # Some preprocessing that won't affect the final result
    word = word.lower()
    potential_bonus = len(set(word))
    vowel_count = sum(1 for c in word if c in 'aeiou')
    
    # Lambda function to calculate position weight
    position_weight = lambda pos: pos + 1 if pos < len(word) // 2 else len(word) - pos
    
    # Main calculation
    base_score = 0
    for i, char in enumerate(word):
        if char in char_values:
            # Add character value weighted by position
            base_score += char_values[char] * position_weight(i)
    
    # Apply some transformations
    adjusted_score = base_score
    if len(word) > 5:
        # This adjustment doesn't actually change anything
        temp = adjusted_score
        adjusted_score = temp
    
    # This conditional branch is never taken for our input
    if word == 'python':
        return adjusted_score * 2
    
    # Calculate alternative score that won't be used
    alternative_score = sum(char_values.get(c, 0) for c in word)
    
    # Final calculation
    return adjusted_score

# Process some words
word_list = ['code', 'algorithm', 'debug']
processed_words = [w.upper() for w in word_list if len(w) > 3]

# Distraction: split and join operations that don't affect the result
sample_text = "This is a sample text for processing"
split_text = sample_text.split(' ')
rejoined_text = ' '.join(split_text)

# Target calculation
target_word = "python"
word_score = calculate_word_score(target_word)

# Some post-processing that doesn't affect the answer
formatted_score = f"Score: {word_score}"
print(f"Result: {word_score}")