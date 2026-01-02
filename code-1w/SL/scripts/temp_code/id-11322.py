def analyze_text_overlap(text_a, text_b):
    words_a = set(text_a.lower().split())
    words_b = set(text_b.lower().split())
    
    # Remove common stop words as part of filtering
    stop_words = {'the', 'and', 'or', 'in', 'of', 'a', 'is', 'it'}
    filtered_a = words_a - stop_words
    filtered_b = words_b - stop_words
    
    shared_elements = filtered_a.intersection(filtered_b)
    final_overlap_count = len(shared_elements)
    return final_overlap_count

result = analyze_text_overlap(
    "The quick brown fox jumps over the lazy dog", 
    "A quick movement of the enemy will jeopardize six gunboats"
)
print(f"Result: {result}")