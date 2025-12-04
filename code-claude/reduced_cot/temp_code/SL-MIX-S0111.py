from collections import Counter, defaultdict
import math

def extract_keywords(text):
    # Extract potential keywords from text
    words = [word.lower() for word in text.split() if len(word) > 3]
    return Counter(words)

def calculate_sentiment(text):
    # Mock sentiment analysis (distractor)
    positive = sum(1 for word in text.lower().split() if word in ['good', 'great', 'excellent'])
    negative = sum(1 for word in text.lower().split() if word in ['bad', 'poor', 'terrible'])
    sentiment_score = positive - negative
    return max(-5, min(5, sentiment_score))

def analyze_readability(text):
    # Mock readability score calculation (distractor)
    sentences = text.count('.') + text.count('!') + text.count('?')
    words = len(text.split())
    if sentences == 0:
        return 50  # Default for short texts
    return 100 - min(100, 10 * (words / sentences))

def calculate_document_priority(text, sensitive_terms):
    # Extract basic metrics
    word_count = len(text.split())
    char_count = len(text)
    
    # Track metrics in a defaultdict (mostly distractors)
    metrics = defaultdict(int)
    metrics['length'] = word_count
    metrics['density'] = char_count / max(1, word_count)
    
    # Calculate keyword frequency (relevant)
    keywords = extract_keywords(text)
    total_keywords = sum(keywords.values())
    
    # Calculate readability score (distractor)
    readability = analyze_readability(text)
    metrics['readability'] = readability
    
    # Calculate sentiment (distractor)
    sentiment = calculate_sentiment(text)
    metrics['sentiment'] = sentiment
    
    # Track sensitive term occurrences (relevant)
    sensitive_count = 0
    for term in sensitive_terms:
        term_lower = term.lower()
        if term_lower in text.lower():
            sensitive_count += text.lower().count(term_lower)
            # Apply weighting based on term position
            if text.lower().startswith(term_lower):
                metrics['priority_boost'] = 15
    
    # Calculate urgency factor (distractor)
    urgency_terms = ['urgent', 'immediately', 'asap', 'critical']
    urgency_factor = sum(2 for term in urgency_terms if term in text.lower())
    metrics['urgency'] = urgency_factor
    
    # Complex priority calculation with bit operations (relevant but with distractors)
    base_priority = 10
    if sensitive_count > 0:
        # Bit shift operation (relevant)
        base_priority = base_priority << 1
        if sensitive_count > 2:
            # More shifting (relevant)
            base_priority = base_priority << 1
    
    # Apply sentiment modifier (distractor)
    sentiment_modifier = sentiment * 2
    potential_priority = base_priority + sentiment_modifier
    
    # Apply length penalty for very short documents (distractor)
    if word_count < 20:
        potential_priority = potential_priority // 2
    
    # Calculate priority score with XOR operation (relevant)
    priority_score = (base_priority ^ 15) + sensitive_count * 5
    
    # Apply keyword density factor (distractor)
    keyword_density = total_keywords / max(1, word_count) * 100
    if keyword_density > 30:
        metrics['keyword_alert'] = True
    
    return priority_score

# Main processing
document_text = "This confidential document contains sensitive financial information. \
Please review the security protocol before accessing these classified files."

# Define sensitive terms
sensitive_terms = ['confidential', 'classified', 'security', 'sensitive']

# Process document (this is the key statement)
priority_score = calculate_document_priority(document_text, sensitive_terms)

# Additional processing (distractor)
readability_score = analyze_readability(document_text)
sentiment_value = calculate_sentiment(document_text)
combined_metric = (readability_score + sentiment_value) / 2

# Apply additional transforms (distractor)
transformed_priority = priority_score
if sentiment_value > 0:
    transformed_priority += 5
else:
    transformed_priority -= 3

print(f"Result: {priority_score}")