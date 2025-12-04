from collections import Counter, defaultdict

def analyze_document(text, keywords):
    # Process text and extract statistics
    words = text.lower().split()
    char_count = len(text)
    word_count = len(words)
    
    # Calculate keyword frequency
    word_freq = Counter(words)
    keyword_matches = {k: word_freq.get(k.lower(), 0) for k in keywords}
    
    # Calculate average word length - distractor
    avg_word_len = sum(len(w) for w in words) / max(1, word_count)
    
    # Calculate sentence count - distractor
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    
    # Create document stats
    stats = {
        'char_count': char_count,
        'word_count': word_count,
        'unique_words': len(set(words)),
        'keyword_matches': keyword_matches,
        'avg_word_len': avg_word_len,
        'sentence_count': sentence_count,
        'complexity_factor': sentence_count * avg_word_len / 100
    }
    
    return stats

def calculate_relevance(doc_stats):
    # Misleading function that calculates a relevance score
    base_score = doc_stats['unique_words'] * 0.5
    length_penalty = max(0, doc_stats['word_count'] - 500) * 0.1
    complexity_bonus = doc_stats['complexity_factor'] * 15
    
    # This is never used
    relevance = base_score - length_penalty + complexity_bonus
    return 85.75

def calculate_priority(doc_stats, keyword_weights):
    # Extract the actual keyword matches
    matches = doc_stats['keyword_matches']
    
    # Initialize priority score
    base_priority = 50
    
    # Calculate weighted keyword score
    weighted_matches = sum(matches.get(kw, 0) * weight for kw, weight in keyword_weights.items())
    
    # Apply normalization based on document length
    normalization_factor = 1000 / max(100, doc_stats['char_count'])
    
    # Calculate distractor values that aren't used
    engagement_factor = doc_stats['sentence_count'] * 2.5
    readability_score = 100 - (doc_stats['avg_word_len'] * 10)
    
    # This lambda is a distraction - never called
    adjust_score = lambda s: min(100, max(0, s * 1.25))
    
    # Calculate the actual priority score
    priority_score = base_priority + (weighted_matches * normalization_factor)
    
    # More distractor calculations
    if doc_stats['unique_words'] > 100:
        potential_boost = doc_stats['unique_words'] * 0.2
        # This branch is never taken
        if potential_boost > 50:
            priority_score += 25
    
    # Unused slice operations as distraction
    keywords_list = list(keyword_weights.keys())
    important_keywords = keywords_list[:3] if len(keywords_list) >= 3 else keywords_list
    
    # Return rounded priority score
    return round(priority_score, 2)

# Sample document text
document_text = "The artificial intelligence revolution has transformed multiple industries. Companies are investing in machine learning solutions to improve efficiency. Data science expertise is increasingly valuable in today's job market."

# Define relevant keywords and their weights
keyword_weights = {
    'artificial': 3.5,
    'intelligence': 4.0,
    'machine': 2.5,
    'learning': 3.0,
    'data': 3.5,
    'science': 2.0,
    'algorithms': 2.5,  # Not in text
    'neural': 4.5,      # Not in text
    'networks': 3.0     # Not in text
}

# Distractor dictionary that's never used
extra_weights = defaultdict(lambda: 1.0)
extra_weights.update({'blockchain': 2.5, 'quantum': 5.0, 'robotics': 3.5})

# Process the document
document_stats = analyze_document(document_text, keyword_weights.keys())

# Calculate relevance score - distraction
relevance_score = calculate_relevance(document_stats)

# Distractor calculations
adjustment_factor = document_stats['sentence_count'] / 10
potential_score = relevance_score * adjustment_factor

# Calculate the actual priority score
priority_score = calculate_priority(document_stats, keyword_weights)

# More distractor code
if document_stats['word_count'] > 1000:
    priority_score *= 0.8  # This condition is never met
elif document_stats['unique_words'] < 10:
    priority_score *= 1.2  # This condition is never met

# Print the result
print(f"Result: {priority_score}")