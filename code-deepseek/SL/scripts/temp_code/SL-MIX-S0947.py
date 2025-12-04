from collections import Counter

def process_text(text):
    # Analyze character frequencies and patterns
    char_counter = Counter(text.lower())
    
    # Calculate vowel distribution (distractor - not used in final answer)
    vowels = 'aeiou'
    vowel_count = sum(char_counter[vowel] for vowel in vowels if vowel in char_counter)
    
    # Process consonant frequencies
    consonants = ''.join(c for c in 'abcdefghijklmnopqrstuvwxyz' if c not in vowels)
    consonant_freq = {c: char_counter[c] for c in consonants if c in char_counter}
    
    # Filter consonants with multiple occurrences (key logic)
    filtered_consonants = {char: count for char, count in consonant_freq.items() if count > 1}
    
    # Calculate total count of repeated consonants
    final_count = sum(filtered_consonants.values())
    
    # Additional intermediate calculations (distractors)
    total_chars = len(text)
    unique_consonants = len(consonant_freq)
    
    return final_count

# Sample text data
text_data = "Programming challenges require systematic analysis and methodical approaches"

# Process the text data
processed = process_text(text_data)

# Print the target result
print(f"Result: {processed}")