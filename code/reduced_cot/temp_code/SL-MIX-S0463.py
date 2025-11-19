def process_document_metadata():
    document_tags = [
        {'history': 15, 'military': 8, 'europe': 12},
        {'science': 20, 'physics': 15, 'quantum': 7},
        {'literature': 25, 'poetry': 10, 'french': 5},
        {'history': 10, 'asia': 18, 'culture': 14}
    ]
    
    tag_weights = {
        'history': 3, 'military': 2, 'europe': 1,
        'science': 4, 'physics': 3, 'quantum': 2,
        'literature': 3, 'poetry': 2, 'french': 1,
        'asia': 2, 'culture': 1
    }
    
    # Initialize archival scoring system
    archival_score = 0
    unique_tag_set = frozenset()
    
    # Process each document
    for doc in document_tags:
        doc_vector = [0] * len(tag_weights)
        temp_score = 0
        
        # Calculate weighted score for current document
        for tag, frequency in doc.items():
            if tag in tag_weights and frequency > 0:
                weight = tag_weights[tag]
                temp_score += frequency * weight
                unique_tag_set |= {tag}
                
                # Update document vector representation
                tag_index = list(tag_weights.keys()).index(tag)
                doc_vector[tag_index] = frequency
        
        # Apply divide and conquer approach to normalize score
        if temp_score > 0:
            max_freq = max(doc.values()) if doc.values() else 1
            normalized_score = (temp_score // max_freq) if max_freq and temp_score >= 50 else temp_score
            archival_score += normalized_score
    
    # Final adjustment based on unique tags
    unique_bonus = len(unique_tag_set) * 2
    archival_score = (archival_score + unique_bonus) if archival_score > 0 and len(unique_tag_set) >= 8 else archival_score - 5
    
    return archival_score

archival_score = process_document_metadata()
print(f"Result: {archival_score}")