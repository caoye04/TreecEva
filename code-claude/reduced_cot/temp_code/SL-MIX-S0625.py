def calculate_word_value(word):
    # Calculate base value based on character positions
    base_value = sum(ord(c) - ord('a') + 1 for c in word.lower() if c.isalpha())
    
    # Apply multiplier for words with special patterns
    multiplier = 1
    if len(set(word)) == len(word):  # All unique characters
        multiplier = 1.5
    elif any(word.count(c) > 2 for c in word):  # Any character appears more than twice
        multiplier = 0.8
    
    # This calculation doesn't affect the final result
    potential_bonus = len(word) * 0.25
    
    return int(base_value * multiplier)

def analyze_text(text):
    # Remove punctuation and convert to lowercase
    cleaned_text = ''
    for char in text.lower():
        if char.isalnum() or char.isspace():
            cleaned_text += char
    
    # Split into words
    words = cleaned_text.split()
    
    # Count word frequencies
    frequencies = {}
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    
    # Calculate some statistics that won't be used
    avg_word_length = sum(len(word) for word in words) / len(words) if words else 0
    unique_ratio = len(frequencies) / len(words) if words else 0
    
    return frequencies

def calculate_final_score(word_frequencies, target_words):
    base_score = 0
    bonus_points = 0
    penalty = 0
    
    # Process each target word
    for word in target_words:
        if word in word_frequencies:
            # Add points based on frequency and word value
            word_score = word_frequencies[word] * calculate_word_value(word)
            base_score += word_score
            
            # Add bonus for high-frequency words
            if word_frequencies[word] > 2:
                bonus_points += 15
        else:
            # Apply penalty for missing target words
            penalty += 10
    
    # Calculate unused sentiment score
    sentiment_score = len(target_words) * 2
    
    # Apply modifiers to get final score
    return base_score + bonus_points - penalty

# Sample text for analysis
sample_text = "The quick brown fox jumps over the lazy dog. The fox was quick and brown."

# Generate word frequencies
word_frequencies = analyze_text(sample_text)

# Define target words to look for
target_words = ["quick", "fox", "elephant", "brown"]

# Calculate the score
total_score = calculate_final_score(word_frequencies, target_words)
print(f"Result: {total_score}")