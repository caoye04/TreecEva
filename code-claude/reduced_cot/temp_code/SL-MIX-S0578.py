from collections import Counter

def analyze_text(text):
    # Clean the text by removing non-alphabetic characters and converting to lowercase
    cleaned_text = ''.join(char.lower() for char in text if char.isalpha())
    
    # Count word lengths for reference
    words = text.split()
    word_lengths = [len(word.strip('.,!?;:"\'\'')) for word in words]
    avg_word_length = sum(word_lengths) / len(word_lengths) if word_lengths else 0
    
    # Count letter frequencies
    letter_counts = Counter(cleaned_text)
    
    # Find the most common letter and its count
    most_common_letter_count = letter_counts.most_common(1)[0][1]
    
    # Some additional statistics for context
    unique_letters = len(letter_counts)
    total_letters = len(cleaned_text)
    
    return most_common_letter_count

# Sample text from a famous speech
sample_text = "We choose to go to the Moon in this decade and do the other things, not because they are easy, but because they are hard."

result = analyze_text(sample_text)
print(f"Result: {result}")