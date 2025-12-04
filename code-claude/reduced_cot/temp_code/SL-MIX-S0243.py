def process_word(word, multipliers):
    if not word:
        return 0
    
    # Calculate base value from first and last characters
    first_char = word[0].lower()
    last_char = word[-1].lower()
    
    # Track position values
    char_values = {}
    for i, c in enumerate('abcdefghijklmnopqrstuvwxyz'):
        char_values[c] = i + 1
    
    # Calculate primary score
    primary = 0
    if first_char in char_values:
        primary += char_values[first_char]
    if last_char in char_values:
        primary += char_values[last_char]
    
    # Apply length factor
    length_factor = len(word) % 5 + 1
    
    return primary * length_factor

def analyze_keywords(text):
    # Split text into words
    words = text.split()
    
    # Define keyword importance multipliers
    keyword_multipliers = {
        'urgent': 3,
        'important': 2,
        'critical': 4,
        'review': 1,
        'pending': 1
    }
    
    # Count keywords
    keyword_count = {k: 0 for k in keyword_multipliers}
    for word in words:
        clean_word = ''.join(c for c in word.lower() if c.isalpha())
        if clean_word in keyword_multipliers:
            keyword_count[clean_word] += 1
    
    # Calculate decoy metrics that aren't used
    avg_word_length = sum(len(word) for word in words) / max(1, len(words))
    unique_chars = len(set(''.join(words)))
    
    return keyword_count, keyword_multipliers

def calculate_priority(document_text):
    # Process keywords
    keyword_count, keyword_multipliers = analyze_keywords(document_text)
    
    # Calculate base priority
    base_priority = sum(count * keyword_multipliers[keyword] for keyword, count in keyword_count.items())
    
    # Process individual words for additional scoring
    words = document_text.split()
    word_processors = [
        lambda w: process_word(w, keyword_multipliers),
        lambda w: len(w) // 2  # This processor isn't actually used
    ]
    
    # Calculate supplementary score from first and last words
    supplementary = 0
    if words:
        first_word = words[0]
        last_word = words[-1]
        
        # Only the first processor is used
        supplementary += word_processors[0](first_word)
        supplementary += word_processors[0](last_word)
    
    # Apply final calculation
    priority_score = base_priority + supplementary
    
    # Apply normalization factor that doesn't change the result
    normalization = 1.0
    priority_score = priority_score * normalization
    
    return priority_score

# Document to analyze
document_text = "Urgent review required for critical project documentation"

# Calculate priority score
priority_score = calculate_priority(document_text)
print(f"Result: {priority_score}")