def process_text(input_text, priority="AEIOU"):
    # Clean and normalize the text
    normalized = input_text.upper().replace(" ", "")
    
    # Extract characters that appear more than once
    char_count = {}
    for char in normalized:
        char_count[char] = char_count.get(char, 0) + 1
    
    duplicate_chars = [c for c, count in char_count.items() if count > 1]
    
    # Potential priority characters (vowels by default)
    priority_chars = priority.upper()
    
    # Statistics tracking (some not used for final answer)
    stats = {
        "total_length": len(normalized),
        "unique_chars": len(set(normalized)),
        "max_occurrences": max(char_count.values()) if char_count else 0
    }
    
    # Filter text based on position
    position_filter = [i for i in range(len(normalized)) if i % 3 != 0]
    filtered_text = ''.join([normalized[i] for i in position_filter])
    
    # Count unique priority characters in filtered text
    unique_count = len(set([char for char in filtered_text if char in priority_chars]))
    
    # Calculate alternative metrics (distractors)
    vowel_ratio = sum(1 for c in normalized if c in "AEIOU") / len(normalized) if normalized else 0
    complexity_score = stats["unique_chars"] * (1 + vowel_ratio)
    
    return unique_count

# Test with sample text
sample_text = "Programming challenges are fun and educational"
alternative_priority = "STRLNM"

# Process with default priority (vowels)
result1 = process_text(sample_text)

# Process with alternative priority (common consonants)
result2 = process_text(sample_text, alternative_priority)

# Final result uses the default priority
final_result = process_text("Hello World")
print(f"Result: {final_result}")