import itertools

# Text analysis function
def analyze_text(text):
    # Remove punctuation and normalize
    punctuation = '.,!?;:"()'
    cleaned_text = ''.join(c for c in text if c not in punctuation)
    processed_text = cleaned_text.strip()
    
    # Some basic text metrics
    char_count = len(processed_text)
    word_count = len(processed_text.split())
    
    # Count vowels
    vowels = 'aeiou'
    vowel_count = len([c for c in processed_text if c.lower() in vowels])
    
    # Calculate consonant ratio
    letter_count = sum(1 for c in processed_text if c.isalpha())
    consonant_count = letter_count - vowel_count
    vowel_ratio = vowel_count / char_count if char_count > 0 else 0
    
    return vowel_count

# Sample text to analyze
sample = "Hello world! This is a sample text."
result = analyze_text(sample)
print(f"Result: {result}")