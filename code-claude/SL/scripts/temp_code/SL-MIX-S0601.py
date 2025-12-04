import itertools

def analyze_text(text, target_chars):
    # Extract characters matching target criteria
    filtered_text = ''.join(filter(lambda x: x.isalpha(), text))
    
    # Generate some statistics that aren't used in final calculation
    letter_stats = {}
    for letter in filtered_text.lower():
        letter_stats[letter] = letter_stats.get(letter, 0) + 1
    
    # Calculate average ASCII value (not used in final answer)
    avg_ascii = sum(ord(c) for c in filtered_text) / len(filtered_text) if filtered_text else 0
    
    # Process target characters
    char_counts = {}
    for char in target_chars:
        # Use XOR operation to create a unique hash for each character (not relevant to answer)
        char_hash = ord(char) ^ 42
        
        # Count occurrences using string methods
        char_counts[char] = text.lower().count(char.lower())
    
    # Additional processing with itertools (not directly relevant)
    pairs = list(itertools.combinations(target_chars, 2))
    pair_count = len(pairs)
    
    # This is the key statement for the answer
    occurrence_count = sum(char_counts.values())
    
    # Perform some bitwise operations that don't affect the result
    bit_mask = 0xFF
    encoded_val = occurrence_count & bit_mask
    
    return occurrence_count

# Sample text for analysis
sample = "Python programming is fun and rewarding!"

# Characters to track (vowels)
target = "aeiou"

# Run analysis
result = analyze_text(sample, target)
print(f"Result: {result}")