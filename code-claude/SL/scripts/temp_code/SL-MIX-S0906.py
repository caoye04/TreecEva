import itertools

def analyze_text(text):
    # Remove spaces and convert to lowercase for consistent analysis
    cleaned_text = text.lower().replace(' ', '')
    
    # Calculate the length of the text for potential use
    text_length = len(cleaned_text)
    
    # Generate some statistical values about the text
    unique_chars = len(set(cleaned_text))
    vowel_count = sum(1 for char in cleaned_text if char in 'aeiou')
    consonant_count = sum(1 for char in cleaned_text if char in 'bcdfghjklmnpqrstvwxyz')
    
    # Create frequency map of characters
    frequency_map = {}
    for char in cleaned_text:
        if char.isalpha():
            frequency_map[char] = frequency_map.get(char, 0) + 1
    
    # Find most common character pairs (digrams)
    digrams = list(itertools.pairwise(cleaned_text))
    digram_count = len(digrams)
    
    # Calculate a weighted score based on character frequencies
    weighted_score = sum(ord(char) * count for char, count in frequency_map.items())
    normalized_score = weighted_score / text_length if text_length > 0 else 0
    
    # Determine character diversity ratio
    diversity_ratio = unique_chars / text_length if text_length > 0 else 0
    adjusted_ratio = diversity_ratio * 100
    
    # Count total characters that appear in the frequency map
    total_frequency = sum(frequency_map.values())
    
    # Calculate some additional metrics that aren't used in the final result
    vowel_ratio = vowel_count / text_length if text_length > 0 else 0
    consonant_ratio = consonant_count / text_length if text_length > 0 else 0
    special_char_count = text_length - vowel_count - consonant_count
    
    return {
        'total_chars': total_frequency,
        'unique_chars': unique_chars,
        'vowel_count': vowel_count,
        'consonant_count': consonant_count,
        'weighted_score': weighted_score,
        'diversity_score': adjusted_ratio
    }

# Sample text for analysis
sample_text = "Python programming is fun and rewarding!"
results = analyze_text(sample_text)
print(f"Result: {results['total_chars']}")