def analyze_frequency(text, threshold=3):
    # Count character frequencies
    char_freq = {}
    for char in text.lower():
        if char.isalpha():
            char_freq[char] = char_freq.get(char, 0) + 1
    
    # Get characters above threshold (unused)
    frequent_chars = {c for c, count in char_freq.items() if count >= threshold}
    return char_freq, frequent_chars

def calculate_word_priority(text):
    # Extract unique words
    words = text.split()
    unique_words = set(words)
    
    # Calculate word metrics
    word_lengths = [len(word) for word in unique_words]
    avg_length = sum(word_lengths) / len(word_lengths) if word_lengths else 0
    
    # Priority calculation based on several metrics
    vowel_count = sum(1 for char in text.lower() if char in 'aeiou')
    consonant_count = sum(1 for char in text.lower() if char.isalpha() and char not in 'aeiou')
    
    # This is the core calculation
    priority = (vowel_count * 2) - (consonant_count // 3) + int(avg_length)
    
    return priority

# Sample text for analysis
sample_text = "The quick brown fox jumps over the lazy dog and runs away happily"

# Process text in different ways
char_stats, frequent_chars = analyze_frequency(sample_text, 2)

# Extract important segments
segment_1 = sample_text[4:14]  # "quick brow"
segment_2 = sample_text[16:30]  # "fox jumps over"

# Create alternative text versions
reversed_text = sample_text[::-1]  # Reverse the text
upper_text = sample_text.upper()  # Convert to uppercase

# Calculate misleading metrics
entropy_score = len(char_stats) * 0.5  # Misleading entropy calculation
complexity_index = len(sample_text) / len(set(sample_text.lower()))  # Text complexity

# Process segments with different approaches
processed_segments = []
for i, segment in enumerate([segment_1, segment_2]):
    if i % 2 == 0:  # Even index segments
        processed_segments.append(segment.replace('o', 'X'))
    else:  # Odd index segments
        processed_segments.append(segment.upper())

# Combine processed segments
combined_segments = ' '.join(processed_segments)

# Filter text for analysis - this is what affects the final result
filtered_text = ''
for i, char in enumerate(sample_text):
    # Keep only characters at even indices plus vowels
    if i % 2 == 0 or char.lower() in 'aeiou':
        filtered_text += char

# Calculate priority score based on filtered text
priority_score = calculate_word_priority(filtered_text)

# Additional calculations that don't affect the result
bonus_factor = len(set(filtered_text)) / len(filtered_text) if filtered_text else 0
adjusted_score = priority_score * bonus_factor  # Misleading adjustment

# Apply different weighting schemes (unused)
weighted_scores = {
    'standard': priority_score,
    'enhanced': priority_score * 1.5,
    'conservative': priority_score * 0.8
}

# Final output
print(f"Text complexity: {complexity_index:.2f}")
print(f"Character diversity: {entropy_score}")
print(f"Result: {priority_score}")