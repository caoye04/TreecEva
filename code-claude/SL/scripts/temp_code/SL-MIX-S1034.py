import itertools

def analyze_text(text):
    # Count character frequencies
    char_count = {}
    for char in text.lower():
        if char.isalnum():
            char_count[char] = char_count.get(char, 0) + 1
    
    # Find most and least common characters
    most_common = max(char_count.items(), key=lambda x: x[1])[0] if char_count else ''
    least_common = min(char_count.items(), key=lambda x: x[1])[0] if char_count else ''
    
    # Extract numbers from text
    numbers = [int(c) for c in text if c.isdigit()]
    sum_numbers = sum(numbers) if numbers else 0
    
    # Generate all possible character pairs
    all_chars = [c for c in text if c.isalpha()]
    all_pairs = list(itertools.combinations(all_chars, 2))
    
    # Process pairs based on conditions
    filtered_pairs = []
    vowels = 'aeiou'
    
    for pair in all_pairs:
        # Check if pair contains a vowel
        has_vowel = pair[0].lower() in vowels or pair[1].lower() in vowels
        
        # Check if pair contains the most common character
        has_common = pair[0].lower() == most_common or pair[1].lower() == most_common
        
        # Add pair if it has a vowel but not the most common character
        if has_vowel and not has_common:
            filtered_pairs.append(pair)
    
    # Calculate metrics
    vowel_count = sum(1 for c in text.lower() if c in vowels)
    consonant_count = sum(1 for c in text.lower() if c.isalpha() and c.lower() not in vowels)
    
    # This is the key statement
    unique_pairs = len(set(filtered_pairs))
    
    # Additional calculations that don't affect the result
    ratio = vowel_count / consonant_count if consonant_count else 0
    complexity_score = (len(char_count) * ratio) if ratio else 0
    
    return unique_pairs

# Sample text for analysis
sample = "Hello Python 3!"
result = analyze_text(sample)
print(f"Result: {result}")