import itertools

def analyze_text(text):
    # Convert text to lowercase for consistent counting
    text = text.lower()
    
    # Remove spaces and punctuation
    cleaned_text = ''.join(c for c in text if c.isalpha())
    
    # Count occurrences of each vowel
    vowels = 'aeiou'
    letter_counts = {vowel: cleaned_text.count(vowel) for vowel in vowels}
    
    # Calculate some statistics about the text
    char_count = len(cleaned_text)
    word_count = len(text.split())
    avg_word_length = char_count / word_count if word_count > 0 else 0
    
    # Get the total number of vowels
    total_vowels = sum(letter_counts.values())
    
    # Calculate vowel percentage
    vowel_percentage = (total_vowels / char_count) * 100 if char_count > 0 else 0
    
    return total_vowels, vowel_percentage

# Sample text for analysis
sample = "The quick brown fox jumps over the lazy dog."

# Perform the analysis
total_vowels, vowel_percent = analyze_text(sample)

print(f"Result: {total_vowels}")