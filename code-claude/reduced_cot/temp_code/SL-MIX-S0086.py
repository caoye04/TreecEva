def text_preprocessing(text):
    # Remove punctuation and convert to lowercase
    import string
    text = text.lower()
    for char in string.punctuation:
        text = text.replace(char, '')
    return text

def calculate_word_complexity(word):
    # Calculate complexity score based on length and unique characters
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonants = {c for c in 'abcdefghijklmnopqrstuvwxyz' if c not in vowels}
    
    vowel_count = sum(1 for char in word if char in vowels)
    consonant_count = sum(1 for char in word if char in consonants)
    
    complexity = (len(word) * 0.4) + (len(set(word)) * 0.6)
    if vowel_count > consonant_count:
        complexity *= 0.8  # Reduce complexity for vowel-heavy words
    return complexity

def analyze_sentiment(text):
    # Dummy sentiment analysis using word-based scoring
    positive_words = {'good', 'great', 'excellent', 'positive', 'happy', 'love'}
    negative_words = {'bad', 'terrible', 'awful', 'negative', 'sad', 'hate'}
    neutral_words = {'the', 'and', 'is', 'at', 'on', 'it'}
    
    words = text.split()
    sentiment_score = 0
    
    # This is a distractor calculation
    average_word_length = sum(len(word) for word in words) / max(1, len(words))
    lexical_diversity = len(set(words)) / max(1, len(words))
    readability_score = average_word_length * 1.8 - lexical_diversity * 2.7
    
    for word in words:
        if word in positive_words:
            sentiment_score += 1
        elif word in negative_words:
            sentiment_score -= 1.5
        elif len(word) > 8:  # Assume longer words are more impactful
            sentiment_score += 0.2
        elif word in neutral_words:
            # Neutral words have minimal impact
            sentiment_score += 0.01
            
    return sentiment_score

def calculate_sentiment_score(text):
    # Calculate final sentiment score with normalization
    words = text.split()
    if not words:
        return 0
    
    base_sentiment = analyze_sentiment(text)
    
    # Misleading calculations that don't affect the result
    word_complexities = {word: calculate_word_complexity(word) for word in set(words)}
    avg_complexity = sum(word_complexities.values()) / max(1, len(word_complexities))
    max_complexity_word = max(word_complexities.items(), key=lambda x: x[1])[0] if word_complexities else ''
    
    # This branch is never taken with our input
    if 'excellent' in words and 'terrible' in words:
        return base_sentiment * 0.5  # Conflicting sentiment reduces impact
    
    # Distractor calculations
    word_frequency = {}
    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1
    most_common_word = max(word_frequency.items(), key=lambda x: x[1])[0] if word_frequency else ''
    most_common_count = word_frequency.get(most_common_word, 0)
    
    # These operations don't affect the final result
    sentiment_modifier = 1.0
    if len(words) > 20:  # This condition is false with our input
        sentiment_modifier = 1.2
    if len(set(words)) < 10:  # This condition is true with our input
        sentiment_modifier = 0.9
    
    # Normalize the sentiment score based on text length
    normalized_sentiment = base_sentiment / (len(words) ** 0.5)
    
    # Apply bitwise operations as distraction
    binary_factor = 0
    for i, word in enumerate(words):
        if i < 32:  # Limit to avoid overflow
            binary_factor |= (1 << (i % 8))
    
    # This has no effect as binary_factor & 0 is always 0
    if binary_factor & 0:
        normalized_sentiment *= 1.5
    
    # Final calculation - this is what actually matters
    return round(normalized_sentiment * sentiment_modifier, 2)

# Main processing
input_text = "good movie great acting but terrible ending"
processed_text = text_preprocessing(input_text)

# Calculate additional metrics (distractors)
word_count = len(processed_text.split())
unique_chars = len(set(processed_text))
char_frequency = {}
for char in processed_text:
    if char != ' ':
        char_frequency[char] = char_frequency.get(char, 0) + 1

# These variables are never used
most_common_char = max(char_frequency.items(), key=lambda x: x[1])[0] if char_frequency else ''
least_common_char = min(char_frequency.items(), key=lambda x: x[1])[0] if char_frequency else ''

# This is the key calculation
final_sentiment_score = calculate_sentiment_score(processed_text)

# Distractor calculations after the key calculation
average_sentiment = final_sentiment_score / word_count if word_count > 0 else 0
weighted_score = final_sentiment_score * (unique_chars / 26)

print(f"Result: {final_sentiment_score}")