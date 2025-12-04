def process_text(text):
    # Convert text to lowercase for processing
    processed = text.lower()
    
    # Remove punctuation (not actually used)
    punctuation = '.,;:!?'
    for p in punctuation:
        processed = processed.replace(p, '')
    
    # Split into words
    return processed.split()

def calculate_score(words):
    # Initialize score
    score = 0
    
    # Count vowels in each word
    vowel_counts = []
    for word in words:
        vowels = 0
        for char in word:
            if char in 'aeiou':
                vowels += 1
        vowel_counts.append(vowels)
    
    # Calculate base score (sum of vowel counts)
    base_score = sum(vowel_counts)
    
    # Apply multiplier based on word lengths
    length_multiplier = 1.0
    if len(words) > 0:
        avg_length = sum(len(word) for word in words) / len(words)
        length_multiplier = min(2.0, avg_length / 3)
    
    # Calculate alternative score (not used in final calculation)
    alt_score = max(vowel_counts) * 2 if vowel_counts else 0
    
    # Final calculation
    return int(base_score * length_multiplier)

# Sample text for analysis
sample_text = "The quick brown fox jumps over the lazy dog"
all_words = process_text(sample_text)

# Filter words based on length
min_length = 3
max_length = 5
filtered_words = [word for word in all_words if min_length <= len(word) <= max_length]

# Calculate score based on filtered words
final_score = calculate_score(filtered_words)
print(f"Result: {final_score}")