def calculate_relevance(text, keywords):
    # Calculate relevance based on keyword matches
    matches = 0
    for word in text.lower().split():
        if word in keywords:
            matches += 1
    
    # Misleading calculation that isn't used
    irrelevant_score = len(text) * 0.5
    return matches

def sort_by_importance(items):
    # This function is never actually used
    return sorted(items, key=lambda x: x[1], reverse=True)

def calculate_document_priority(doc_ids, frequencies):
    # Initialize variables
    base_score = 100
    penalty_factor = 2.5
    bonus_multiplier = 1.5
    priority_threshold = 75
    
    # These variables are distractions
    max_attempts = 3
    system_load = 0.65
    cache_hits = {}
    processing_flags = [True, False, True, False]
    
    # Process document IDs and frequencies
    valid_docs = []
    for doc_id in doc_ids:
        if doc_id % 2 == 0 and doc_id > 10:
            valid_docs.append(doc_id)
        elif doc_id % 3 == 0:
            # This branch is misleading
            cache_hits[doc_id] = doc_id * 0.1
    
    # More distraction calculations
    for flag in processing_flags:
        if flag:
            system_load += 0.05
        else:
            system_load -= 0.025
    
    # Core calculation with zip and enumerate
    doc_scores = {}
    keywords = ['important', 'urgent', 'critical']
    sample_texts = [
        'important document for review',
        'urgent notice about system',
        'regular update notification',
        'critical security patch'
    ]
    
    # This loop contains both relevant and irrelevant operations
    for i, (doc_id, freq) in enumerate(zip(valid_docs, frequencies[:len(valid_docs)])):
        # Relevant calculation
        if i < len(sample_texts):
            relevance = calculate_relevance(sample_texts[i], keywords)
        else:
            relevance = 1
        
        # Misleading calculation
        potential_score = base_score + (freq * relevance)
        if potential_score > 150:
            potential_score = 150
        
        # Another distraction
        if doc_id in cache_hits:
            cache_hits[doc_id] += 1
        
        # The actual score calculation
        doc_scores[doc_id] = base_score - (freq * penalty_factor)
        if relevance > 1:
            doc_scores[doc_id] *= bonus_multiplier
    
    # Final priority calculation
    if not doc_scores:
        return 0
    
    # More distraction
    for attempt in range(max_attempts):
        if system_load > 0.8:
            system_load -= 0.1
    
    # The actual return value calculation
    average_score = sum(doc_scores.values()) / len(doc_scores)
    if average_score >= priority_threshold:
        return int(average_score + len(valid_docs))
    else:
        return int(average_score / 2)

# Main execution
document_ids = [5, 12, 15, 9, 20, 3]
word_frequencies = [4, 2, 7, 1, 3, 5]

# Some distraction operations
filtered_ids = [x for x in document_ids if x > 10]
sorting_key = lambda x: -x
sorted_frequencies = sorted(word_frequencies, key=sorting_key)

# Calculate priority score
priority_score = calculate_document_priority(document_ids, word_frequencies)
print(f"Result: {priority_score}")
