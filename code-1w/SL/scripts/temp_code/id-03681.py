def analyze_data_stream(raw_input):
    # Irrelevant transformation: character frequency map (dead path)
    char_freq = {}
    for c in ''.join(map(str, raw_input)):
        char_freq[c] = char_freq.get(c, 0) + 1

    # Misleading intermediate: normalized scores (not used in final result)
    max_val = max(raw_input)
    normalized_scores = [round((x / max_val) * 100, 2) for x in raw_input]

    # Distractor: bitwise obfuscation (unused)
    obfuscated = [x ^ 255 for x in raw_input if x % 7 == 0]
    temp_result = sum(obfuscated) % 1000 if obfuscated else 42

    # Core logic begins: filter valid entries based on multiple criteria
    threshold = int(sum(raw_input) / len(raw_input))  # Mean-based threshold
    indexed_data = list(enumerate(raw_input))
    
    # Extract elements where index is even AND value passes modular test
    candidate_entries = [val for idx, val in indexed_data if idx % 2 == 0 and val % 3 != 0]

    # Further filter using zip with shifted version (modular phase alignment)
    shifted = candidate_entries[-1:] + candidate_entries[:-1]
    paired_diffs = [abs(a - b) for a, b in zip(candidate_entries, shifted)]
    
    # Only keep original candidates where paired difference > 10
    survival_mask = [diff > 10 for diff in paired_diffs]
    pre_filtered = [entry for entry, keep in zip(candidate_entries, survival_mask) if keep]

    # Final validation: must be expressible as sum of two earlier elements in raw_input
    def is_reconstructable(n):
        seen = set()
        for val in raw_input:
            if (n - val) in seen:
                return True
            seen.add(val)
        return False

    valid_entries = [x for x in pre_filtered if is_reconstructable(x)]

    # Key assignment point
    filtered_sum = sum(valid_entries)
    
    # Red herring: string transformation chain (irrelevant)
    labels = ['item_{}'.format(i) for i in range(len(valid_entries))]
    label_caps = list(map(str.upper, filter(lambda s: len(s) > 5, labels)))
    encoded_tag = ''.join([s[4] for s in label_caps]) if label_caps else 'X'
    tag_value = sum([ord(c) for c in encoded_tag])  # Unused

    # Output the target variable
    print(f"Result: {filtered_sum}")

# Execute with realistic dataset
data_stream = [12, 15, 18, 21, 14, 27, 30, 33, 11, 42, 45, 48, 13, 55]
analyze_data_stream(data_stream)