from collections import Counter

def analyze_text(text):
    # Remove punctuation and convert to lowercase
    cleaned_text = ''.join(c.lower() if c.isalpha() or c.isspace() else ' ' for c in text)
    
    # Split into words
    words = cleaned_text.split()
    
    # Count word occurrences
    word_counts = Counter(words)
    
    # Calculate statistics
    total_words = len(words)
    unique_words = len(word_counts)
    
    # Count how many distinct characters are used across all words
    all_chars = ''.join(words)
    char_count = len(set(all_chars))
    
    # Get words that appear exactly once
    singleton_words = [word for word, count in word_counts.items() if count == 1]
    
    # Calculate a special metric: number of unique character occurrences
    unique_count = len(set(word_counts.elements()))
    
    # This is a distractor - not used in final calculation
    avg_word_length = sum(len(word) for word in words) / total_words if total_words > 0 else 0
    
    return {
        "total": total_words,
        "unique": unique_words,
        "chars": char_count,
        "singletons": len(singleton_words),
        "special": unique_count
    }

# Sample text for analysis
sample = "The quick brown fox jumps over the lazy dog. The dog stays lazy."
result = analyze_text(sample)
print(f"Result: {result['special']}")