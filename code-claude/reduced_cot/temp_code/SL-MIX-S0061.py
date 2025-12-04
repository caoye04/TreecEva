from collections import Counter

# Processing text data for sentiment analysis
def process_text_data(text_samples, sentiment_threshold):
    # Initialize variables
    word_freq = Counter()
    total_chars = 0
    max_length = 0
    sentiment_scores = []
    
    # Process each text sample
    for idx, sample in enumerate(text_samples):
        # Track character statistics
        sample_len = len(sample)
        total_chars += sample_len
        max_length = max(max_length, sample_len)
        
        # Simple sentiment calculation (just for demonstration)
        sentiment = (idx % 3) - 1  # Values: -1, 0, 1
        sentiment_scores.append(sentiment)
        
        # Count word frequencies
        words = sample.lower().split()
        word_freq.update(words)
    
    # Calculate average sample length
    avg_length = total_chars / len(text_samples) if text_samples else 0
    
    # Process sentiment data
    positive_count = sentiment_scores.count(1)
    negative_count = sentiment_scores.count(-1)
    neutral_count = sentiment_scores.count(0)
    
    # Generate numerical values based on text properties
    text_values = [len(word) * (i+1) for i, word in enumerate(word_freq.keys())]
    
    # Apply filtering based on sentiment threshold
    sentiment_ratio = positive_count / len(sentiment_scores) if sentiment_scores else 0
    adjustment_factor = sentiment_ratio * 2
    
    # Extract values with specific properties
    valid_values = [val for val in text_values[2:8] if val > sentiment_threshold]
    filtered_sum = sum(valid_values)
    
    # Calculate alternative metrics (not used in final result)
    alternative_metric = avg_length * adjustment_factor
    weighted_score = (positive_count * 1) + (negative_count * -1)
    
    print(f"Result: {filtered_sum}")
    return filtered_sum

# Test with sample data
text_samples = [
    "The weather is nice today",
    "I didn't enjoy that movie",
    "This product works as expected",
    "The service was excellent"
]

result = process_text_data(text_samples, 5)