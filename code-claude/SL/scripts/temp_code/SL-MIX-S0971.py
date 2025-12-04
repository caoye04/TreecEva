from collections import Counter

def analyze_text(text):
    # Count all characters in the text
    character_freq = Counter(text.lower())
    
    # Some processing metrics (not directly relevant to final answer)
    total_chars = sum(character_freq.values())
    avg_freq = total_chars / len(character_freq) if character_freq else 0
    
    # Characters to potentially ignore
    punctuation = ",.!?;:'\""
    spaces = " \t\n"
    digits = "0123456789"
    
    # Track characters seen in specific positions
    position_tracker = {}
    for i, char in enumerate(text):
        if i % 3 == 0 and char not in position_tracker:
            position_tracker[char] = i
    
    # Characters we decide to ignore (punctuation and whitespace)
    ignored_chars = set()
    for char in character_freq:
        if char in punctuation or char in spaces:
            ignored_chars.add(char)
    
    # Calculate metrics
    alpha_count = sum(character_freq[c] for c in character_freq if c.isalpha())
    digit_count = sum(character_freq[c] for c in character_freq if c in digits)
    
    # This is our target calculation
    unique_chars = len(character_freq) - len(ignored_chars)
    
    # Some additional metrics (not directly relevant)
    unique_ratio = unique_chars / total_chars if total_chars else 0
    complexity_score = alpha_count * 0.8 + digit_count * 0.2
    
    return unique_chars

# Sample text for analysis
sample_text = "Hello, World! This is a test string with numbers: 12345."

# Process the text and get the result
result = analyze_text(sample_text)
print(f"Result: {result}")