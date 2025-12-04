def process_text(raw_text):
    # Remove special characters and convert to lowercase
    processed = ''.join(c.lower() if c.isalpha() or c.isspace() else ' ' for c in raw_text)
    return processed

def extract_letter_frequencies(words):
    # Count letter frequencies across all words
    frequencies = {}
    for word in words:
        for letter in word:
            if letter.isalpha():
                frequencies[letter] = frequencies.get(letter, 0) + 1
    
    # Sort by frequency (not used in final calculation)
    sorted_freq = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    return sorted_freq

def calculate_valid_words(text, required_letter, min_length):
    # Process the input text
    clean_text = process_text(text)
    
    # Split into words and filter by criteria
    words = clean_text.split()
    
    # Initialize tracking variables
    valid_count = 0
    potential_count = 0
    discarded_words = []
    
    # Check each word against criteria
    for word in words:
        # Track words of sufficient length
        if len(word) >= min_length:
            potential_count += 1
            
            # Count words containing the required letter
            if required_letter in word:
                valid_count += 1
            else:
                discarded_words.append(word)
    
    # Calculate letter frequencies (not used in final result)
    letter_stats = extract_letter_frequencies(words)
    
    # Apply bonus multiplier (distraction - not actually used)
    bonus_multiplier = 1.5 if potential_count > 10 else 1.0
    adjusted_count = int(valid_count * bonus_multiplier)
    
    return valid_count

# Input text
text = "The quick brown fox jumps over the lazy dog. Python programming is fun and rewarding!"

# Set parameters
required_letter = 'o'
min_length = 4
preferred_letter = 'p'  # Distraction - not used

# Calculate result
valid_word_count = len([w for w in text.split() if len(w) > 2])  # Distraction
final_count = calculate_valid_words(text, required_letter, min_length)

print(f"Result: {final_count}")