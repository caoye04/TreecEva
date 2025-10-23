from collections import defaultdict

class DocumentMeta:
    def __init__(self, title, tags):
        self.title = title
        self.tags = tags

def calculate_complexity(doc_meta):
    # Count character frequencies
    char_freq = defaultdict(int)
    for char in doc_meta.title.lower():
        char_freq[char] += 1
    
    # Calculate base score from unique characters
    base_score = len(char_freq) << 2  # Multiply by 4 using bit shift
    
    # Apply tag multiplier using bitwise operations
    tag_multiplier = 0
    for tag in doc_meta.tags:
        tag_hash = hash(tag) & 0xF  # Get last 4 bits
        tag_multiplier |= tag_hash   # Bitwise OR to combine
    
    # String transformation: reverse and uppercase
    transformed_title = doc_meta.title[::-1].upper()
    
    # Logical conditions
    has_vowel_pattern = any(c in 'AEIOU' for c in transformed_title[:3])
    is_long_title = len(doc_meta.title) > 10
    
    # Calculate adjustment based on conditions
    adjustment = 0
    if has_vowel_pattern and is_long_title:
        adjustment = 15
    elif has_vowel_pattern or is_long_title:
        adjustment = 7
    else:
        adjustment = -5
    
    # Final score calculation
    intermediate_score = (base_score & 0xFF) ^ tag_multiplier  # Bitwise AND then XOR
    final_score = (intermediate_score + adjustment) & 0xFF     # Ensure byte-sized result
    
    return final_score

# Create document metadata
metadata = DocumentMeta(
    title="AdvancedAlgorithmicProcesses",
    tags=["technical", "research", "optimization"]
)

# Calculate complexity
final_score = calculate_complexity(metadata)
print(f"Result: {final_score}")