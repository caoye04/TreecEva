from collections import Counter
import math

def analyze_text_pattern(text):
    # Process text and extract features
    char_count = Counter(text)
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Calculate vowel statistics (distraction)
    vowel_stats = {v: char_count.get(v, 0) for v in vowels}
    vowel_total = sum(vowel_stats.values())
    consonant_total = sum(char_count[c] for c in char_count if c.isalpha() and c.lower() not in vowels)
    
    # Create bit patterns based on character positions (distraction)
    bit_patterns = {}
    for i, char in enumerate(text[:15]):
        if char in bit_patterns:
            bit_patterns[char] |= (1 << (i % 5))
        else:
            bit_patterns[char] = (1 << (i % 5))
    
    # Find the most common character and its frequency
    most_common = char_count.most_common(3)
    most_common_char = most_common[0][0] if most_common else ''
    
    # Calculate various metrics (some are distractions)
    entropy = -sum((count / len(text)) * math.log2(count / len(text)) for char, count in char_count.items())
    diversity_score = len(char_count) / len(text) if text else 0
    complexity_index = entropy * diversity_score * 10
    
    # Apply transformations to frequencies
    actual_frequencies = {}
    for char, count in char_count.items():
        if char.isalpha():
            # Complex transformation with bitwise operations
            base_value = ord(char.lower()) - ord('a') + 1
            if char.isupper():
                actual_frequencies[char] = (count << 1) | base_value
            else:
                actual_frequencies[char] = count ^ base_value
        elif char.isdigit():
            actual_frequencies[char] = int(char) * count
        else:
            actual_frequencies[char] = count
    
    # More distraction calculations
    weighted_sum = sum(count * (i + 1) for i, (char, count) in enumerate(most_common))
    potential_key = (weighted_sum % 256) ^ (len(text) % 32)
    
    # Apply bitmask based on text properties
    if vowel_total > consonant_total:
        bit_mask = 0x3F  # 00111111 in binary
    else:
        bit_mask = 0x1F  # 00011111 in binary
    
    # Calculate the final frequency using bitwise AND
    final_frequency = actual_frequencies[most_common_char] & bit_mask
    
    # Distraction calculations that don't affect the result
    if complexity_index > 3.0:
        adjusted_frequency = final_frequency * 2
    else:
        adjusted_frequency = final_frequency + 5
    
    normalized_value = (adjusted_frequency / bit_mask) * 100
    
    return {
        "most_common": most_common_char,
        "entropy": entropy,
        "final_frequency": final_frequency,
        "normalized": normalized_value
    }

# Sample text for analysis
sample_text = "Python programming is fun and educational!"
result = analyze_text_pattern(sample_text)
print(f"Result: {result['final_frequency']}")