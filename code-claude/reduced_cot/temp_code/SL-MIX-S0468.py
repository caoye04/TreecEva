def process_text(raw_text):
    # Remove punctuation and convert to lowercase
    cleaned = ''.join(c.lower() if c.isalnum() else ' ' for c in raw_text)
    return cleaned

def meets_criteria(word):
    # Words must be at least 4 chars and contain a vowel
    vowels = 'aeiou'
    has_vowel = any(v in word for v in vowels)
    return len(word) >= 4 and has_vowel

# Sample text from a research paper
text = "Machine learning algorithms optimize performance using experience."

# Process the text
cleaned_text = process_text(text)

# Split into words and apply transformations
words = cleaned_text.split()
processed_words = []

# Track statistics (some aren't used in final calculation)
total_chars = 0
max_word_len = 0
vowel_count = 0

# Process each word
for word in words:
    # Skip words that are too short (distractor condition)
    if len(word) <= 1:
        continue
        
    # Apply transformations
    transformed = word
    if word.startswith('a') or word.startswith('e'):
        transformed = word.upper()
    elif len(word) > 9:  # This condition is never met in our sample
        transformed = word[:4]
    
    # Track statistics
    total_chars += len(word)
    max_word_len = max(max_word_len, len(word))
    vowel_count += sum(1 for c in word if c in 'aeiou')
    
    processed_words.append(transformed)

# Calculate averages (distractors)
avg_word_len = total_chars / len(words) if words else 0
vowel_ratio = vowel_count / total_chars if total_chars else 0

# Count words meeting specific criteria
valid_count = sum(1 for word in processed_words if meets_criteria(word))

# Additional processing that doesn't affect valid_count
final_text = ' '.join(processed_words)
final_chars = len(final_text)

print(f"Processed text: {final_text}")
print(f"Result: {valid_count}")