from collections import Counter

def analyze_text(text):
    # Remove spaces and convert to lowercase
    processed_text = text.lower().replace(' ', '')
    
    # Count character frequency
    character_frequency = Counter(processed_text)
    
    # Find characters that appear exactly once
    unique_appearances = {char for char, count in character_frequency.items() if count == 1}
    singleton_count = len(unique_appearances)
    
    # Calculate some statistics (not used in final answer)
    avg_frequency = sum(character_frequency.values()) / len(character_frequency) if character_frequency else 0
    max_char = character_frequency.most_common(1)[0][0] if character_frequency else ''
    
    # Find characters that appear more than average (not used in final answer)
    above_average = {char for char, count in character_frequency.items() if count > avg_frequency}
    
    # Calculate a ratio (not used in final answer)
    popularity_score = len(above_average) / len(character_frequency) if character_frequency else 0
    
    # Return the number of unique characters
    unique_characters = len(character_frequency)
    return unique_characters, singleton_count, popularity_score

# Sample text from a famous pangram
text = "The quick brown fox jumps over the lazy dog"

# Calculate metrics
unique_chars, single_occurrence, popularity = analyze_text(text)

# Create a set for additional analysis (not affecting the answer)
alphabet = set('abcdefghijklmnopqrstuvwxyz')
missing_letters = alphabet - set(text.lower())

# Print results
print(f"Result: {unique_chars}")