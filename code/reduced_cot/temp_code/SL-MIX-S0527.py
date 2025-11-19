def compute_archival_metric(tag_collection):
    even_length_tags = frozenset(tag for tag in tag_collection if len(tag) % 2 == 0)
    odd_length_tags = frozenset(tag for tag in tag_collection if len(tag) % 2 != 0)
    
    # Quality check: tags must be disjoint by length parity
    if even_length_tags & odd_length_tags:
        return 0
    
    # Context manager simulates database transaction for metric calculation
    class MetricContext:
        def __enter__(self):
            return self
        def __exit__(self, exc_type, exc_val, exc_tb):
            pass
        def calculate_combinations(self, s1, s2):
            # Lambda to count valid pairings
            count_pairs = lambda x, y: sum(1 for a in x for b in y if a[0] == b[-1])
            return count_pairs(s1, s2)
    
    with MetricContext() as ctx:
        combination_count = ctx.calculate_combinations(even_length_tags, odd_length_tags)
        # Archival score combines set sizes and valid combinations
        archival_score = len(even_length_tags) * len(odd_length_tags) + combination_count
        
    return archival_score

document_tags = {'history', 'WWII', 'archive', '1945', 'memoir', 'digital', 'scan'}
archival_score = compute_archival_metric(document_tags)
print(f"Result: {archival_score}")