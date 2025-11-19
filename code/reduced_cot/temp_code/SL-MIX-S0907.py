def analyze_collection():
    # Digital archive categories with document hashes
    archive_categories = [
        [frozenset({1024, 2048, 4096}), frozenset({8192, 16384}), frozenset({1024, 32768})],
        [frozenset({65536, 131072}), frozenset({1024, 2048, 65536}), frozenset({262144})],
        [frozenset({524288}), frozenset({1024, 1048576}), frozenset({2048, 4096, 8192})]
    ]
    
    # Greedy frequency tracking
    hash_occurrences = {}
    
    # Nested loop to process categories and documents
    for category in archive_categories:
        temp_category_hashes = set()
        for document in category:
            temp_category_hashes.update(document)
        
        # Count occurrences using lambda
        count_hash = lambda h: sum(1 for doc in category if h in doc)
        
        for hash_val in temp_category_hashes:
            freq = count_hash(hash_val)
            hash_occurrences[hash_val] = hash_occurrences.get(hash_val, 0) + freq
    
    # Early termination condition with logical operations
    peak_frequency = 0
    for freq in hash_occurrences.values():
        # Ternary operator for updating peak
        peak_frequency = freq if freq > peak_frequency and not (freq % 2 == 0 and freq < 10) else peak_frequency
    
    return peak_frequency

# Execute analysis
peak_frequency = analyze_collection()
print(f"Result: {peak_frequency}")