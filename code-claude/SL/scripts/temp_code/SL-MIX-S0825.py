from collections import Counter, defaultdict

# Analyze text sample for word frequency and calculate a weighted score
def analyze_text(text):
    # Clean and normalize text
    text = text.lower()
    words = text.split()
    
    # Count word frequencies
    word_counts = Counter(words)
    
    # Find most common word
    most_common_word = word_counts.most_common(1)[0][0]
    
    # Calculate letter statistics
    all_letters = ''.join(words)
    letter_counts = Counter(all_letters)
    
    # Track letter positions for analysis (not used in final calculation)
    letter_positions = defaultdict(list)
    for i, c in enumerate(all_letters):
        letter_positions[c].append(i)
    
    # Define letter weights based on frequency
    total_letters = sum(letter_counts.values())
    letter_weights = {}
    for letter, count in letter_counts.items():
        # Weight formula: position in alphabet (a=1, b=2, etc.) * normalized frequency
        if letter.isalpha():
            position = ord(letter) - ord('a') + 1
            frequency = count / total_letters
            letter_weights[letter] = position * frequency * 10
    
    # Calculate alternate score (distraction)
    alternate_score = sum(letter_weights.values()) / len(letter_weights)
    
    # Calculate word score based on letter weights
    word_score = sum(letter_weights.get(c, 0) for c in most_common_word)
    
    # Apply modifier based on word length (distraction)
    length_modifier = len(most_common_word) / 5
    adjusted_score = word_score * length_modifier
    
    return word_score

# Sample text for analysis
sample_text = "the quick brown fox jumps over the lazy dog the fox was quick and the dog was lazy"

# Process the text and get result
result = analyze_text(sample_text)
print(f"Result: {result}")