def analyze_patterns(sequence):
    # Extract subsequences using slicing
    window_size = 3
    subsequences = [sequence[i:i+window_size] for i in range(len(sequence) - window_size + 1)]
    
    # Count frequency of each subsequence
    freq_map = {}
    for seq in subsequences:
        key = tuple(seq)
        freq_map[key] = freq_map.get(key, 0) + 1

    # Compute entropy-like measure (distraction)
    import math
    total = len(subsequences)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)

    # Return frequent patterns above threshold (actual relevance)
    threshold = 2
    frequent = {k: v for k, v in freq_map.items() if v > threshold}
    return frequent, entropy  # entropy not used later


def filter_candidates(raw_candidates, constraints_set):
    # Apply set operations to filter valid candidates
    valid_keys = set()
    for candidate in raw_candidates:
        key_tuple = tuple(sorted(candidate))
        if len(key_tuple) == 3 and sum(key_tuple) % 2 == 1:
            valid_keys.add(key_tuple)
    
    # Extra irrelevant filtering
    redundant_filter = [c for c in raw_candidates if min(c) > 0]
    size_check = len(redundant_filter) > 5

    # Use set difference as distraction
    universe = set(tuple(sorted(c)) for c in raw_candidates)
    diff = universe - valid_keys
    discarded_count = len(diff)

    return valid_keys


def calculate_final_score(data):
    base_sum = sum(sum(tup) for tup in data)
    adjustment_factor = len(data) * 0.95
    
    # Dummy state tracking (distractor)
    history = []
    temp_val = 0
    for item in data:
        temp_val += len(item)
        history.append(temp_val)
    
    # Actual computation
    score = base_sum * adjustment_factor
    return int(score)

# Main execution block
if __name__ == '__main__':
    # Simulated sensor readings (domain: signal processing)
    signal_readings = [1, 2, 3, 2, 3, 4, 3, 4, 5, 4, 5, 6]

    # Step 1: Pattern analysis
    patterns, info_entropy = analyze_patterns(signal_readings)
    
    # Misleading intermediate calculation
    avg_pattern_length = sum(len(k) for k in patterns.keys()) / max(len(patterns), 1)
    pattern_complexity = len(patterns) * avg_pattern_length

    # Step 2: Generate candidate triples from patterns
    raw_candidate_triples = []
    for pattern, count in patterns.items():
        if count >= 2:
            shifted = [x + 1 for x in pattern]  # artificial variation
            raw_candidate_triples.append(list(pattern))
            raw_candidate_triples.append(shifted)

    # Step 3: Filter candidates using set logic
    constraint_thresholds = {1, 2, 3, 4, 5}
    filtered_groups = filter_candidates(raw_candidate_triples, constraint_thresholds)

    # Step 4: Process into structured format
    processed_data = []
    for group in filtered_groups:
        if sum(group) > 6:  # additional logical filter
            processed_data.append(group)

    # Final scoring step
    final_score = calculate_final_score(processed_data)
    
    # Irrelevant aggregation
    total_elements = sum(len(t) for t in processed_data)
    flat_list = [x for t in processed_data for x in t]
    median_guess = sorted(flat_list)[len(flat_list)//2] if flat_list else 0

    print(f"Result: {final_score}")