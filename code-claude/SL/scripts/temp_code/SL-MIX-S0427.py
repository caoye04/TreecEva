from collections import Counter, defaultdict

def analyze_text_metrics(document):
    # Count word frequencies
    words = document.lower().split()
    word_count = Counter(words)
    
    # Calculate average word length (distractor)
    avg_length = sum(len(word) for word in words) / len(words) if words else 0
    
    # Count sentences (distractor)
    sentence_count = document.count('.') + document.count('!') + document.count('?')
    
    # Extract keywords based on frequency
    keywords = {word: count for word, count in word_count.items() if count > 1 and len(word) > 3}
    
    # Generate text complexity score (distractor)
    complexity = (avg_length * 1.5) + (sentence_count * 0.5)
    
    return {
        'word_count': len(words),
        'unique_words': len(word_count),
        'keywords': keywords,
        'avg_word_length': avg_length,
        'sentences': sentence_count,
        'complexity': complexity
    }

def generate_keyword_weights(keywords):
    # Create baseline weights
    weights = defaultdict(float)
    
    # Apply various weighting strategies (mostly distractors)
    for keyword, count in keywords.items():
        # Length-based weight (distractor)
        length_factor = len(keyword) / 10
        
        # Position-based weight (distractor)
        position_factor = 1.2 if keyword[0] in 'aeiou' else 0.9
        
        # Frequency weight (relevant)
        frequency_factor = count * 0.75
        
        # Combined weight with misleading calculation
        combined = length_factor + position_factor + frequency_factor
        
        # Final weight calculation (only frequency matters)
        weights[keyword] = count
        
        # Misleading update (distractor)
        if len(keyword) > 6:
            weights[keyword] += 0.5
    
    return weights

def calculate_priority(stats, weights):
    # Distracting variables
    text_density = stats['word_count'] / (stats['sentences'] + 1)
    semantic_richness = stats['unique_words'] / max(1, stats['word_count']) * 100
    content_quality = min(stats['complexity'] * 2, 95)
    
    # Misleading intermediate calculation
    base_score = text_density * 0.3 + semantic_richness * 0.4 + content_quality * 0.1
    
    # The actual relevant calculation
    keyword_score = 0
    for keyword, count in stats['keywords'].items():
        if keyword in weights and len(keyword) > 3:
            # This is the only part that matters
            keyword_score += weights[keyword]
    
    # More distraction
    adjusted_score = base_score * 0.2 + keyword_score * 0.8
    normalized_score = min(adjusted_score / 10, 100)
    
    # The actual result is just the sum of weights for keywords
    return keyword_score

# Sample document
document = "Python is a versatile programming language. Python supports multiple paradigms including object-oriented and functional programming. Many developers prefer Python for its readability and simplicity."

# Analyze document
document_stats = analyze_text_metrics(document)

# Generate misleading statistics (distractors)
readability_index = document_stats['avg_word_length'] * 4.71 + document_stats['sentences'] * 0.5 - 21.43
engagement_score = 87.5 - (document_stats['complexity'] * 0.5)
quality_rating = min(document_stats['unique_words'] / document_stats['word_count'] * 100, 95)

# Generate keyword weights
keyword_weights = generate_keyword_weights(document_stats['keywords'])

# Calculate priority score - this is what we need to track
priority_score = calculate_priority(document_stats, keyword_weights)

# Apply misleading normalization (distractor)
if priority_score > 20:
    priority_score = priority_score * 0.95
elif priority_score < 10:
    priority_score = priority_score * 1.05

# More distraction with unused variables
final_quality_index = (priority_score + readability_index + engagement_score) / 3
recommendation_threshold = final_quality_index > 75

print(f"Result: {priority_score}")