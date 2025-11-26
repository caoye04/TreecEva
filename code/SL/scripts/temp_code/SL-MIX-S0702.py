def analyze_text_similarity():
    text1 = "machine learning models require careful evaluation"
    text2 = "evaluation of machine learning requires careful models"
    
    # Extract unique words from both texts
    words1 = set(text1.split())
    words2 = set(text2.split())
    
    # Find intersection of unique words
    common_words = words1.intersection(words2)
    
    # Calculate average word length
    total_chars = sum(len(word) for word in common_words)
    avg_length = total_chars // len(common_words) if common_words else 0
    
    # Count unique words across both texts
    unique_words = len(words1.union(words2))
    
    # Final calculation
    final_count = unique_words // avg_length
    print(f"Result: {final_count}")

analyze_text_similarity()