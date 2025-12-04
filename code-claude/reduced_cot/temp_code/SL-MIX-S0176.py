from collections import Counter

def analyze_text(text):
    # Remove spaces and convert to lowercase
    processed_text = text.lower()
    
    # Count character frequencies
    char_counts = Counter(processed_text)
    
    # Track some metrics (distractors)
    word_count = len(text.split())
    unique_chars = len(set(processed_text))
    digits_count = sum(c.isdigit() for c in processed_text)
    
    # Define letter values based on modified alphabet position
    letter_values = {}
    for i, char in enumerate('abcdefghijklmnopqrstuvwxyz'):
        # Assign values with some mathematical transformation
        letter_values[char] = (i + 1) % 10
    
    # Calculate some metrics that won't affect final result
    avg_word_length = sum(len(word) for word in text.split()) / max(1, word_count)
    longest_word = max(text.split(), key=len, default='')
    consonant_count = sum(1 for c in processed_text if c.isalpha() and c not in 'aeiou')
    
    # Calculate frequency score - this is our target calculation
    frequency_score = sum(letter_values[c] * count for c, count in char_counts.items() if c.isalpha())
    
    # Additional calculations that don't affect the result
    complexity_index = (unique_chars / len(processed_text)) * 100 if processed_text else 0
    vowel_ratio = sum(char_counts[v] for v in 'aeiou') / max(1, len(processed_text))
    
    return frequency_score, word_count, avg_word_length, complexity_index

# Sample text for analysis
sample = "Hello, Python 3.9!"

# Run the analysis
result, words, avg_len, complexity = analyze_text(sample)

print(f"Result: {result}")