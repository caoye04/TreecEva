def analyze_document_tags(doc1_tags, doc2_tags, priority_tags=None):
    # Convert input lists to sets for efficient operations
    tags1 = set(doc1_tags)
    tags2 = set(doc2_tags)
    
    # Calculate basic similarity metrics
    common_elements = tags1.intersection(tags2)
    unique_to_doc1 = tags1.difference(tags2)
    unique_to_doc2 = tags2.difference(tags1)
    
    # Initialize tracking variables
    word_length_sum = 0
    longest_tag = ""
    
    # Process common tags for additional metrics
    for tag in common_elements:
        if len(tag) > len(longest_tag):
            longest_tag = tag
        word_length_sum += len(tag)
    
    # Calculate average word length (not used in final calculation)
    avg_length = word_length_sum / len(common_elements) if common_elements else 0
    
    # Determine priority factor based on priority tags
    priority_factor = 1.0
    if priority_tags:
        priority_set = set(priority_tags)
        priority_matches = priority_set.intersection(common_elements)
        if priority_matches:
            # Increase factor based on priority matches
            priority_factor = 1.5
            
            # Further bonus for specific high-priority tags
            if "urgent" in priority_matches or "critical" in priority_matches:
                priority_factor = 2.0
    
    # Calculate normalized similarity score
    total_unique = len(unique_to_doc1) + len(unique_to_doc2)
    similarity_ratio = len(common_elements) / (len(common_elements) + total_unique) if (len(common_elements) + total_unique) > 0 else 0
    
    # Generate tag statistics summary (not used in final calculation)
    stats = {
        "common": len(common_elements),
        "unique_doc1": len(unique_to_doc1),
        "unique_doc2": len(unique_to_doc2),
        "longest_common": longest_tag
    }
    
    # Calculate final overlap score
    overlap_score = len(common_elements) * priority_factor
    
    # Return the target result
    print(f"Result: {overlap_score}")
    return overlap_score

# Test with sample data
doc1_tags = ["python", "programming", "development", "code", "tutorial"]
doc2_tags = ["python", "tutorial", "learning", "education"]
priority_tags = ["python", "development", "tutorial"]

result = analyze_document_tags(doc1_tags, doc2_tags, priority_tags)