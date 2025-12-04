def calculate_keyword_weight(text, keywords):
    # Calculate keyword relevance weight
    word_count = len(text.split())
    keyword_matches = sum(1 for word in text.lower().split() if word in keywords)
    # This weight calculation is a distraction - not used in final result
    weight = keyword_matches * 2.5 / max(1, word_count) * 100
    return weight

def analyze_document_statistics(stats):
    # Extract document statistics with some processing
    total_chars = sum(doc.get('characters', 0) for doc in stats)
    avg_words = sum(len(doc.get('content', '').split()) for doc in stats) / len(stats) if stats else 0
    
    # Misleading metrics calculation - not used for final priority
    complexity_score = total_chars / 500 * (avg_words / 15)
    readability_index = 206.835 - 1.015 * avg_words - 84.6 * (total_chars / (avg_words * len(stats)))
    
    return {
        'total_chars': total_chars,
        'avg_words': avg_words,
        'complexity': complexity_score,
        'readability': readability_index
    }

def prioritize_documents(document_stats, keywords):
    # This is where the actual calculation happens
    if not document_stats or len(document_stats) < 2:
        return 0
    
    # Extract relevant document information
    doc_ids = [doc['id'] for doc in document_stats if 'id' in doc]
    doc_ages = [doc.get('age', 0) for doc in document_stats]
    
    # Distracting lambda functions - not used in final calculation
    age_factor = lambda x: 1.0 if x < 30 else 0.8 if x < 90 else 0.6
    content_multiplier = lambda c: len(set(c.lower().split())) / len(c.split()) if c else 1
    
    # Base score calculation
    base_score = sum(doc.get('importance', 0) for doc in document_stats)
    
    # Calculate frequency of each keyword in all documents (relevant)
    keyword_freq = {}
    for doc in document_stats:
        content = doc.get('content', '').lower()
        for keyword in keywords:
            if keyword in content:
                keyword_freq[keyword] = keyword_freq.get(keyword, 0) + 1
    
    # Dead code path - looks important but never used
    if False and any(doc.get('priority', 0) > 9 for doc in document_stats):
        urgency_factor = 1.5
        base_score *= urgency_factor
    
    # Extract the second oldest document's ID (relevant)
    sorted_docs = sorted(document_stats, key=lambda d: d.get('age', 0), reverse=True)
    second_oldest_id = sorted_docs[1]['id'] if len(sorted_docs) > 1 else 0
    
    # Calculate keyword diversity score (relevant)
    keyword_diversity = len(keyword_freq)
    
    # Misleading calculations that look important
    avg_importance = base_score / len(document_stats)
    max_age = max(doc_ages) if doc_ages else 0
    content_length_sum = sum(len(doc.get('content', '')) for doc in document_stats)
    
    # The actual priority formula (this is what matters)
    priority_score = (second_oldest_id * 2) + (keyword_diversity * 5) - 3
    
    # More distraction calculations that don't affect the result
    adjusted_score = priority_score * 1.0
    normalized_score = min(100, adjusted_score)
    
    return priority_score

# Main document processing code
document_stats = [
    {'id': 7, 'importance': 4, 'age': 45, 'characters': 1200, 
     'content': 'Annual financial report with quarterly breakdown and projections'},
    {'id': 3, 'importance': 8, 'age': 120, 'characters': 850, 
     'content': 'Strategic planning document with market analysis'},
    {'id': 9, 'importance': 6, 'age': 30, 'characters': 1500, 
     'content': 'Customer feedback summary with sentiment analysis'},
    {'id': 5, 'importance': 7, 'age': 60, 'characters': 2000, 
     'content': 'Product development roadmap with timeline milestones'}
]

keywords = ['strategic', 'analysis', 'financial', 'development', 'market']

# Distracting set operations
keyword_set = set(keywords)
unique_words = set()
for doc in document_stats:
    unique_words.update(doc.get('content', '').lower().split())

common_words = keyword_set.intersection(unique_words)

# Generate document statistics - not directly used in priority calculation
stats_analysis = analyze_document_statistics(document_stats)

# Calculate priority score - this is what we're looking for
priority_score = prioritize_documents(document_stats, keywords)

# Misleading final calculations - not the answer
final_metric = stats_analysis['complexity'] * len(common_words) / 10
adjusted_priority = priority_score * 0.8 + final_metric * 0.2

print(f"Document analysis complete")
print(f"Statistics summary: {stats_analysis}")
print(f"Common keywords found: {common_words}")
print(f"Target result: {priority_score}")