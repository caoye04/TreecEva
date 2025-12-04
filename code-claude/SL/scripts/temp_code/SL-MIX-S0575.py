def text_processor(raw_text):
    # Process text to remove punctuation
    import string
    text_lower = raw_text.lower()
    for char in string.punctuation:
        text_lower = text_lower.replace(char, '')
    return text_lower

def calculate_word_frequency_score(text):
    words = text.split()
    word_count = {}
    
    # Count occurrences of each word
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    # Calculate score based on unique words and their frequencies
    unique_words = set(words)
    total_unique = len(unique_words)
    max_freq = max(word_count.values()) if word_count else 0
    min_freq = min(word_count.values()) if word_count else 0
    
    # This is the actual formula we need
    return total_unique * (max_freq - min_freq)

# Alternative scoring method (unused distractor)
def sentiment_analyzer(text):
    positive_words = {'good', 'great', 'excellent', 'best', 'happy'}
    negative_words = {'bad', 'worst', 'terrible', 'sad', 'poor'}
    
    words = text.split()
    positive_count = sum(1 for word in words if word in positive_words)
    negative_count = sum(1 for word in words if word in negative_words)
    
    sentiment_score = positive_count * 10 - negative_count * 5
    return sentiment_score

# Text complexity analyzer (unused distractor)
def complexity_score(text):
    words = text.split()
    avg_word_length = sum(len(word) for word in words) / len(words) if words else 0
    unique_ratio = len(set(words)) / len(words) if words else 0
    return avg_word_length * 5 + unique_ratio * 10

# Main processing function
def analyze_text_sample(sample):
    # Process multiple text metrics
    sample_id = sample.split('-')[0]  # Extract sample ID (distractor)
    
    # Clean and prepare text
    cleaned_text = text_processor(sample)
    
    # Calculate various scores (most are distractors)
    char_count = len(cleaned_text)
    word_count = len(cleaned_text.split())
    avg_word_len = char_count / word_count if word_count > 0 else 0
    
    # Calculate readability index (distractor)
    readability = (char_count * 0.5 - word_count * 0.2) / 10
    
    # Calculate text density score (distractor)
    density = len(set(cleaned_text)) / len(cleaned_text) if cleaned_text else 0
    density_factor = density * 100
    
    # Calculate word frequency distribution
    frequency_score = calculate_word_frequency_score(cleaned_text)
    
    # Calculate final composite score (distractor)
    if sample_id.isdigit() and int(sample_id) > 100:
        composite_score = frequency_score * 0.7 + readability * 0.3
    else:
        composite_score = frequency_score * 0.6 + density_factor * 0.4
    
    return {
        'word_count': word_count,
        'char_count': char_count,
        'frequency_score': frequency_score,
        'readability': readability,
        'density_factor': density_factor,
        'composite_score': composite_score
    }

# Test with sample text
sample_text = "The quick brown fox jumps over the lazy dog. The fox was quick and brown."
results = analyze_text_sample(sample_text)
print(f"Result: {results['frequency_score']}")