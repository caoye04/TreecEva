from collections import Counter, defaultdict

def process_text(text):
    # Count character frequencies
    char_count = Counter(text.lower())
    
    # Remove spaces from consideration
    if ' ' in char_count:
        del char_count[' ']
    
    # Create a character weight dictionary
    character_weight = defaultdict(int)
    unique_chars = set(char_count.keys())
    
    # Some preliminary calculations that won't be used
    vowel_count = sum(char_count[c] for c in 'aeiou' if c in char_count)
    consonant_count = sum(char_count[c] for c in char_count if c not in 'aeiou ')
    
    # Calculate character weights based on frequency and position
    position_multiplier = {c: i+1 for i, c in enumerate(sorted(unique_chars))}
    
    # Apply lambda function for weight calculation
    weight_calculator = lambda char, freq: freq * position_multiplier[char] if freq > 1 else position_multiplier[char] // 2
    
    for char, freq in char_count.items():
        # Skip non-alphabetic characters
        if not char.isalpha():
            continue
            
        # Calculate weight
        character_weight[char] = weight_calculator(char, freq)
    
    # This variable tracks an alternative calculation (distraction)
    alternative_score = sum(position_multiplier.values()) - len(position_multiplier)
    
    # Calculate the unique frequency
    unique_frequency = sum(character_weight.values())
    
    return unique_frequency

# Sample text to process
sample_text = "Python collections are useful"

# Process the text and get the result
result = process_text(sample_text)

print(f"Result: {result}")