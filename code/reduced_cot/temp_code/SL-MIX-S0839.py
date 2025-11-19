def process_lexical_signature(documents):
    # Tokenize and hash each word
    token_hashes = [
        hash(token.lower())
        for doc in documents
        for token in doc.replace(',', '').split()
        if len(token) > 2
    ]
    
    # Apply divide-and-conquer sorting
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)
    
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    sorted_hashes = merge_sort(token_hashes)
    
    # Create signature using set operations
    unique_tokens = frozenset(sorted_hashes)
    signature_elements = [
        h for h in sorted_hashes
        if (h % 7 == 0) and (h not in set(sorted_hashes[:-3]))
    ]
    
    # Compute final signature hash
    signature_hash = sum(
        map(lambda x: x & 0xFF, signature_elements)
    ) ^ len(unique_tokens)
    
    return signature_hash

# Document corpus
archive = [
    "The quick brown fox jumps over the lazy dog",
    "Pack my box with five dozen liquor jugs",
    "How vexingly quick daft zebras jump!",
    "Bright vixens jump; dozy fowl quack"
]

# Process the documents
signature_hash = process_lexical_signature(archive)
print(f"Result: {signature_hash}")