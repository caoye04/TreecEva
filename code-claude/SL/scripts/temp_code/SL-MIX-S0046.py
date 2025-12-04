from collections import Counter

def analyze_text(text):
    # Remove punctuation and convert to lowercase
    cleaned_text = ''.join(c.lower() for c in text if c.isalnum() or c.isspace())
    
    # Count word occurrences
    words = cleaned_text.split()
    word_counts = Counter(words)
    
    # Find most common word
    most_common = word_counts.most_common(1)[0][0] if words else ""
    
    # Count letter frequencies
    letter_counts = Counter(cleaned_text.replace(" ", ""))
    
    # Calculate average word length
    avg_word_len = sum(len(word) for word in words) / len(words) if words else 0
    potential_factor = int(avg_word_len * 2) if avg_word_len > 0 else 1
    
    # Identify vowels and consonants
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    
    # This is our target - vowels that appear in the most common word
    target_chars = [char for char in most_common if char in vowels]
    
    # Calculate various metrics (some are distractors)
    vowel_count = sum(letter_counts[v] for v in vowels)
    consonant_count = sum(letter_counts[c] for c in consonants)
    consonant_ratio = consonant_count / vowel_count if vowel_count > 0 else 0
    
    # This is what we're looking for
    filtered_frequency = sum(letter_counts[char] for char in target_chars)
    
    # More distractor calculations
    weighted_score = filtered_frequency * potential_factor
    normalized_score = weighted_score / len(text) if text else 0
    
    return {
        "most_common": most_common,
        "vowel_count": vowel_count,
        "consonant_count": consonant_count,
        "filtered_frequency": filtered_frequency,
        "weighted_score": weighted_score
    }

# Sample text for analysis
sample_text = "The quick brown fox jumps over the lazy dog. The dog remains lazy while the fox continues to be quick."

result = analyze_text(sample_text)
print(f"Result: {result['filtered_frequency']}")