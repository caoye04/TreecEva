def analyze_text_segments():
    text_a = 'machine learning models are sensitive to input patterns'
    text_b = 'deep learning architectures detect complex input patterns'
    
    # Split texts into words and remove duplicates using sets
    words_a = set(text_a.split())
    words_b = set(text_b.split())
    
    # Identify common words between the two segments
    common_elements = words_a.intersection(words_b)
    
    # Compute overlap statistics
    total_unique_words = len(words_a.union(words_b))
    unique_to_a = len(words_a - words_b)
    unique_to_b = len(words_b - words_a)
    
    # Key computation step
    final_overlap_count = len(common_elements)
    
    # Print result for verification
    print(f"Result: {final_overlap_count}")

analyze_text_segments()