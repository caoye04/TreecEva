def analyze_text_properties(text):
    # Calculate various text statistics
    char_count = len(text)
    word_count = len(text.split())
    special_chars = sum(1 for c in text if not c.isalnum() and not c.isspace())
    
    # Process text for analysis (not relevant to main task)
    processed = ''.join(c.lower() if c.isalpha() else ' ' for c in text)
    words = [w for w in processed.split() if len(w) > 2]
    
    # Calculate word length distribution (distractor)
    length_dist = {}
    for word in words:
        length = len(word)
        length_dist[length] = length_dist.get(length, 0) + 1
    
    # Return comprehensive text statistics
    return {
        'length': char_count,
        'words': word_count,
        'special': special_chars,
        'distribution': length_dist
    }

def letter_frequency(text):
    # Track letter frequencies
    freq = {}
    for char in text.lower():
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
    
    # Calculate additional metrics (mostly distractors)
    total_letters = sum(freq.values())
    vowels = sum(freq.get(v, 0) for v in 'aeiou')
    consonants = total_letters - vowels
    
    # Sort letters by frequency (distractor operation)
    sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    
    return {
        'frequencies': freq,
        'total': total_letters,
        'vowels': vowels,
        'consonants': consonants,
        'most_common': sorted_freq[:5] if sorted_freq else []
    }

def cipher_key(stats, shift):
    # Extract letter frequency data
    letter_data = stats.get('letter_stats', {})
    frequencies = letter_data.get('frequencies', {})
    
    # Apply various transformations to find encryption key
    text_length = stats.get('basic_stats', {}).get('length', 0)
    word_count = stats.get('basic_stats', {}).get('words', 0)
    
    # Calculate primary factors (distractors)
    factor_a = sum(ord(c) * frequencies.get(c, 0) for c in 'etaoin')
    factor_b = sum(frequencies.get(c, 0) for c in 'zqxjk')
    
    # Apply bitwise operations (distractor)
    binary_factor = (factor_a & 0xFF) | (factor_b << 8)
    
    # Calculate the actual cipher key (the target value)
    common_letters = [k for k, v in frequencies.items() if v > 5]
    key_value = len(common_letters) * shift
    
    # Apply modular arithmetic to get final key
    if key_value > 0:
        return (key_value * 7) % 26
    else:
        return 13  # Default fallback

# Sample text for analysis
text = "The quick brown fox jumps over the lazy dog. Python programming is fun and rewarding!"

# Perform initial analysis
basic_stats = analyze_text_properties(text)
print(f"Basic stats: {len(basic_stats['distribution'])} different word lengths")

# Calculate letter statistics
letter_stats = letter_frequency(text)
print(f"Found {letter_stats['total']} letters with {letter_stats['vowels']} vowels")

# Prepare combined statistics for cipher generation
text_stats = {
    'basic_stats': basic_stats,
    'letter_stats': letter_stats
}

# Calculate encryption factors (distractors)
encryption_factors = []
for i in range(1, 6):
    # This loop creates distractor values
    factor = (i * letter_stats['vowels']) % (letter_stats['consonants'] or 1)
    encryption_factors.append(factor)
    
# Find special characters ratio (distractor)
special_ratio = basic_stats['special'] / basic_stats['length'] if basic_stats['length'] > 0 else 0
print(f"Special character ratio: {special_ratio:.4f}")

# Process potential cipher keys (more distractors)
potential_keys = list(map(lambda x: (x * 3) % 26, encryption_factors))
print(f"Potential keys: {potential_keys}")

# Calculate target frequency using the cipher key function
target_frequency = cipher_key(text_stats, 3)

# Apply additional transformations (distractors)
modified_frequency = (target_frequency + sum(potential_keys)) % 26
final_key = (modified_frequency * 2) % 26

# Print the result
print(f"Target result: {target_frequency}")