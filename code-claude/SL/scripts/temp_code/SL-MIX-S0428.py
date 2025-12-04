def process_documents(doc1, doc2):
    # Convert documents to lowercase and split into words
    words1 = doc1.lower().split()
    words2 = doc2.lower().split()
    
    # Create sets for faster operations
    unique_words1 = set(words1)
    unique_words2 = set(words2)
    
    # Find common words between documents
    common_words = unique_words1.intersection(unique_words2)
    
    # Count occurrences of each word in both documents
    word_counts = {}
    for i, word in enumerate(words1):
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1
    
    # Track words that appear exactly once in either document
    singleton_words = set()
    for word, count in word_counts.items():
        if count == 1:
            singleton_words.add(word)
    
    # Process second document word counts
    doc2_counts = {}
    for word in words2:
        if word not in doc2_counts:
            doc2_counts[word] = 0
        doc2_counts[word] += 1
    
    # Calculate average word length in both documents
    total_length = sum(len(word) for word in words1) + sum(len(word) for word in words2)
    total_words = len(words1) + len(words2)
    avg_word_length = total_length / total_words if total_words > 0 else 0
    
    # Count unique words in each document
    unique_count1 = len(unique_words1)
    unique_count2 = len(unique_words2)
    
    # Find words that are in doc1 but not in doc2
    words_only_in_doc1 = unique_words1 - unique_words2
    
    # Calculate the number of common words
    common_word_count = len(common_words)
    
    return common_word_count, avg_word_length, unique_count1, unique_count2

# Test with sample documents
document1 = "The quick brown fox jumps over the lazy dog"
document2 = "A quick dog jumps higher than the brown fox"

result, avg_length, unique1, unique2 = process_documents(document1, document2)
print(f"Result: {result}")