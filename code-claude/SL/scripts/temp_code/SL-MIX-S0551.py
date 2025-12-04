import itertools

def calculate_frequency(word_list):
    # Count letter frequencies across all words
    all_letters = ''.join(word_list)
    letter_counts = {}
    
    for letter in all_letters:
        if letter.isalpha():
            letter_counts[letter.lower()] = letter_counts.get(letter.lower(), 0) + 1
    
    # Find most common letter
    most_common = max(letter_counts.items(), key=lambda x: x[1])
    return most_common[1] * 2 - len(letter_counts)

# Text analysis for environmental research papers
document_text = "climate change impact forest ecosystems water cycle"
words = document_text.split()

# Create some alternative words for analysis
alternate_terms = [word.upper() for word in words if len(word) > 5]

# Track word positions for potential mapping
positions = list(enumerate(words))

# Apply filters to words
def apply_filters(text_list):
    # Filter words by length and content
    primary_filter = [word for word in text_list if 'a' in word or 'e' in word]
    
    # Track metrics that won't affect final result
    avg_word_length = sum(len(word) for word in text_list) / max(1, len(text_list))
    consonant_count = sum(1 for word in text_list for char in word if char.lower() not in 'aeiou')
    
    # Secondary filter based on word length
    return [word for word in primary_filter if len(word) >= 6]

# Process words with different methods
processed_words = [word.replace('c', 'k') for word in words]
zipped_data = list(zip(words, processed_words))

# Extract words that meet our criteria
filtered_words = apply_filters(words)

# Calculate the frequency score based on filtered words
frequency_score = calculate_frequency(filtered_words)

# Additional metrics calculation that doesn't affect the result
total_chars = sum(len(word) for word in filtered_words)
max_length = max(len(word) for word in filtered_words) if filtered_words else 0

print(f"Result: {frequency_score}")