from collections import Counter
import itertools

def analyze_document_similarity(doc1, doc2):
    # Count word frequencies in both documents
    words1 = doc1.lower().split()
    words2 = doc2.lower().split()
    
    # Create word frequency counters
    counter1 = Counter(words1)
    counter2 = Counter(words2)
    
    # Calculate unique words in each document
    unique_words1 = set(counter1.keys())
    unique_words2 = set(counter2.keys())
    
    # Find words that appear in both documents
    common_elements = unique_words1.intersection(unique_words2)
    
    # Calculate similarity metrics
    total_unique = len(unique_words1.union(unique_words2))
    overlap = len(common_elements)
    
    # Calculate Jaccard similarity (not used in final result)
    jaccard = overlap / total_unique if total_unique > 0 else 0
    
    # Calculate a weighted score based on frequency (distraction)
    weighted_score = 0
    for word in common_elements:
        # Add the minimum frequency of each common word
        weighted_score += min(counter1[word], counter2[word])
    
    # Generate all possible word pairs (distraction)
    all_pairs = list(itertools.combinations(common_elements, 2))
    pair_count = len(all_pairs)
    
    # Calculate potential metric (distraction)
    potential = (overlap * pair_count) // 3 if pair_count > 0 else overlap
    
    return overlap

# Test documents
doc1 = "The quick brown fox jumps over the lazy dog"
doc2 = "A quick brown dog jumps over the fence"

# Calculate result
result = analyze_document_similarity(doc1, doc2)
print(f"Result: {result}")