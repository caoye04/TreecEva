from collections import Counter

def calculate_sentiment(text):
    positive_words = ['good', 'great', 'excellent', 'amazing', 'fantastic']
    negative_words = ['bad', 'poor', 'terrible', 'awful', 'horrible']
    
    words = text.lower().split()
    sentiment_value = 0
    
    for word in words:
        if word in positive_words:
            sentiment_value += 1
        elif word in negative_words:
            sentiment_value -= 1
    
    return sentiment_value

def process_text(raw_text):
    # Remove punctuation and normalize
    cleaned = ''
    for char in raw_text:
        if char.isalnum() or char.isspace():
            cleaned += char.lower()
    
    # This doesn't affect the final result but adds complexity
    word_lengths = [len(word) for word in cleaned.split()]
    avg_length = sum(word_lengths) / len(word_lengths) if word_lengths else 0
    
    return cleaned

def calculate_popularity(text):
    words = text.split()
    word_count = len(words)
    
    # Count word frequencies
    word_freq = Counter(words)
    unique_words = len(word_freq)
    
    # Calculate redundancy factor (not used in final calculation)
    redundancy = word_count - unique_words
    
    # Get most common words (limited relevance to final result)
    common_words = word_freq.most_common(3)
    most_common_count = common_words[0][1] if common_words else 0
    
    # Track engagement metrics
    engagement_factor = most_common_count * 2
    diversity_score = (unique_words / word_count) * 10 if word_count > 0 else 0
    
    # Calculate popularity (this is the key calculation)
    base_score = unique_words * 5
    adjustment = engagement_factor - diversity_score
    
    return base_score + adjustment

# Main execution
raw_text = "The conference was fantastic! Many great speakers and excellent topics."
processed_text = process_text(raw_text)

# This sentiment calculation doesn't affect popularity score
sent_score = calculate_sentiment(processed_text)
relevance_factor = len(processed_text) % 10  # Distractor calculation

popularity_score = calculate_popularity(processed_text)

# Some additional distracting calculations
modified_score = popularity_score + sent_score
final_rating = (popularity_score / 10) * relevance_factor if relevance_factor > 0 else popularity_score

print(f"Result: {popularity_score}")