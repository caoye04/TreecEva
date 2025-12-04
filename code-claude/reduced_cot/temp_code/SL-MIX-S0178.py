from collections import Counter, defaultdict

def analyze_document(text):
    """Analyzes a document and returns various metrics."""
    word_count = len(text.split())
    char_count = len(text)
    
    # Calculate average word length
    if word_count > 0:
        avg_word_length = sum(len(word) for word in text.split()) / word_count
    else:
        avg_word_length = 0
        
    # Count frequencies
    char_freq = Counter(text.lower())
    
    # Track special characters
    special_chars = sum(1 for c in text if not c.isalnum() and not c.isspace())
    
    return {
        "words": word_count,
        "chars": char_count,
        "avg_word": avg_word_length,
        "frequencies": char_freq,
        "special": special_chars
    }

def calculate_readability(metrics):
    """Calculate a readability score based on metrics."""
    if metrics["words"] < 5:
        return 0
    
    # Complex formula for readability (not actually used)
    base_score = 100 - (metrics["avg_word"] * 10)
    complexity = metrics["special"] * 2
    vocab_diversity = len(metrics["frequencies"]) / metrics["chars"] if metrics["chars"] > 0 else 0
    
    return base_score - complexity + (vocab_diversity * 100)

def sentiment_analysis(text):
    """Dummy sentiment analysis that counts positive and negative words."""
    positive_words = ["good", "great", "excellent", "best", "happy"]
    negative_words = ["bad", "worst", "terrible", "sad", "poor"]
    
    words = text.lower().split()
    positive_count = sum(1 for word in words if word in positive_words)
    negative_count = sum(1 for word in words if word in negative_words)
    
    # This isn't used in final calculation
    sentiment_score = positive_count - negative_count
    return sentiment_score

def calculate_priority(text):
    """Calculate document priority score based on various metrics."""
    # Initial setup
    metrics = analyze_document(text)
    topic_keywords = {"urgent": 5, "important": 3, "review": 2}
    
    # Calculate base priority
    base_priority = 0
    words = text.lower().split()
    
    # Priority based on keywords
    keyword_score = sum(topic_keywords.get(word, 0) for word in words)
    
    # Priority based on character patterns
    char_patterns = defaultdict(int)
    for i in range(len(text) - 1):
        char_patterns[text[i:i+2]] += 1
    
    # Get the most common digraphs (character pairs)
    common_patterns = sorted(char_patterns.items(), key=lambda x: x[1], reverse=True)
    pattern_score = 0
    for pattern, count in common_patterns[:3]:  # Only top 3 matter
        if pattern.isalpha() and pattern.islower():  # Only alphabetic patterns
            pattern_score += count
        else:
            pattern_score += count // 2  # Non-alphabetic patterns count half
    
    # Count vowels for another metric
    vowels = sum(1 for c in text.lower() if c in 'aeiou')
    consonants = sum(1 for c in text.lower() if c.isalpha() and c not in 'aeiou')
    
    # These values aren't actually used
    vowel_ratio = vowels / len(text) if len(text) > 0 else 0
    consonant_ratio = consonants / len(text) if len(text) > 0 else 0
    
    # Calculate actual priority score
    priority_score = 0
    if metrics["words"] > 0:
        # Base calculation
        priority_score = (keyword_score * 2) + (pattern_score // 3)
        
        # Apply special character modifier
        if metrics["special"] > 0:
            priority_score += metrics["special"]
        
        # Word length modifier (only words with length > 5 matter)
        long_words = sum(1 for word in text.split() if len(word) > 5)
        priority_score += long_words
    
    return priority_score

# Test document
document_text = "Please review this important document urgently! It contains critical information."

# Calculate various metrics
sentiment = sentiment_analysis(document_text)
metrics = analyze_document(document_text)
readability = calculate_readability(metrics)

# Calculate priority score
priority_score = calculate_priority(document_text)

print(f"Document metrics: {metrics['words']} words, {metrics['chars']} characters")
print(f"Sentiment score: {sentiment}")
print(f"Readability score: {readability:.2f}")
print(f"Priority score: {priority_score}")