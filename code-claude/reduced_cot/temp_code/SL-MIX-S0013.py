def calculate_document_signature(document, prime):
    # Document integrity verification system
    # Calculates a unique hash based on character positions and a prime factor
    
    word_counts = {}
    char_weights = {}
    
    # Initialize character weights based on position
    for i, char in enumerate(document):
        if char.isalpha():
            char_weights[char.lower()] = char_weights.get(char.lower(), 0) + (i % 7)
    
    # Count words for potential use in verification (unused)
    potential_words = document.lower().split()
    for word in potential_words:
        if len(word) > 2:
            word_counts[word] = word_counts.get(word, 0) + 1
    
    # Calculate preliminary hash value (misleading)
    misleading_hash = sum(ord(c) * 31 for c in document) % 10000
    
    # Extract special characters for secondary verification (distractor)
    special_chars = [c for c in document if not c.isalnum() and not c.isspace()]
    special_value = len(special_chars) * 17
    
    # Actual signature calculation
    base_value = 0
    for char in document:
        if char.isalnum():
            char_code = ord(char.lower()) - 96 if char.isalpha() else int(char) if char.isdigit() else 0
            # Use conditional expression for position weighting
            weight = char_code * 2 if char.isupper() else char_code
            base_value = (base_value * prime + weight) % 997
    
    # Apply transformation based on document properties
    vowels = sum(1 for c in document.lower() if c in 'aeiou')
    consonants = sum(1 for c in document.lower() if c.isalpha() and c.lower() not in 'aeiou')
    
    # Misleading transformation calculation (not used)
    transform_factor = lambda v, c: (v * 3 + c * 2) % 100
    unused_factor = transform_factor(vowels, consonants)
    
    # Actual final transformation
    if vowels > consonants:
        signature = (base_value + vowels) * 7 % 997
    else:
        signature = (base_value - consonants) % 997
        if signature < 0:
            signature += 997
    
    # Secondary checks that don't affect the result
    if misleading_hash > 5000 and special_value > 100:
        potential_modifier = (misleading_hash // 1000) + special_value
        # This condition is intentionally crafted to always be False
        if potential_modifier > 10000 and len(document) < 5:
            return (signature + potential_modifier) % 997
    
    return signature

# Main execution flow
text = "The quick brown fox jumps over 13 lazy dogs!"
prime_factor = 31

# Misleading calculations
checksum = sum(ord(c) for c in text) % 256
encryption_key = (checksum * prime_factor) % 100
verification_code = lambda t, p: sum(ord(c) * p for c in t[:5]) % 1000

# More distractions
if len(text) > 10:
    token = text[3:8].upper()
    token_value = sum(ord(c) - ord('A') for c in token if c.isalpha())
else:
    token = "NONE"
    token_value = -1

# These operations lead nowhere
reversed_text = text[::-1]
if "fox" in text and "dog" in text:
    animal_index = text.find("fox") * text.find("dog")
else:
    animal_index = -1

# The actual important calculation
final_hash = calculate_document_signature(text, prime_factor)

# More distractions after the result is calculated
verified = (final_hash * checksum) % 1000
integrity_level = "High" if verified > 500 else "Medium" if verified > 200 else "Low"

print(f"Document analysis complete")
print(f"Verification: {integrity_level}")
print(f"Target result: {final_hash}")