def calculate_character_frequency(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    return char_count

def analyze_text(document):
    words = document.split()
    word_lengths = [len(word) for word in words]
    avg_length = sum(word_lengths) / len(word_lengths) if word_lengths else 0
    
    unique_words = set(word.lower().strip('.,!?') for word in words)
    word_count = len(words)
    unique_count = len(unique_words)
    
    # Analyze character distribution (not used in final calculation)
    char_freq = calculate_character_frequency(document)
    vowel_count = sum(char_freq.get(v, 0) for v in 'aeiou')
    
    return {
        'total_words': word_count,
        'unique_words': unique_count,
        'avg_word_length': avg_length,
        'vowel_count': vowel_count
    }

def calculate_weighted_average(counts, weights):
    # Extract only the metrics we need for scoring
    relevant_counts = {
        'words': counts['total_words'],
        'unique': counts['unique_words'],
        'length': counts['avg_word_length']
    }
    
    # Apply weights to each metric
    weighted_sum = 0
    for key, value in relevant_counts.items():
        if key in weights:
            weighted_sum += value * weights[key]
    
    return weighted_sum / sum(weights.values())

# Sample text from a student essay
text = "The study of history provides valuable insights into human behavior and societal patterns. Understanding our past helps us make better decisions for our future."

# Calculate text metrics
word_counts = analyze_text(text)

# Define importance weights for different metrics
weights = {
    'words': 0.3,
    'unique': 0.5,
    'length': 0.2,
    'complexity': 0.0  # This weight is not used but included as distraction
}

# Calculate the weighted score
total_score = calculate_weighted_average(word_counts, weights)

# Process some additional metrics that don't affect the final score
bonus_points = word_counts['vowel_count'] * 0.1
potential_score = total_score + bonus_points
comparison_threshold = 15.0

print(f"Text analysis complete.")
print(f"Raw metrics: {word_counts}")
print(f"Result: {total_score}")