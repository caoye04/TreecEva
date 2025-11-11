import itertools

def process_signals(frequencies):
    # Step 1: Transform frequencies using a lambda-based mapping
    transformed = list(map(lambda x: x**2 if x % 2 == 0 else x**3, frequencies))
    
    # Step 2: Group transformed values into sets based on magnitude ranges
    low_freq = {x for x in transformed if x < 100}
    high_freq = {x for x in transformed if x >= 100}
    
    # Step 3: Compute intersection and union of frequency sets
    common_freq = low_freq & high_freq
    all_freq = low_freq | high_freq
    
    # Step 4: Apply a ternary scoring rule
    base_score = len(common_freq) * 10 if len(common_freq) > 0 else len(all_freq) * 5
    
    # Step 5: Adjust score using a string-based encoding of the largest element
    max_element = max(all_freq) if all_freq else 0
    encoded_max = ''.join(filter(str.isdigit, str(max_element)))
    adjusted_score = base_score + int(encoded_max) if encoded_max else base_score
    
    # Step 6: Use itertools to compute pairwise differences and sum them
    sorted_values = sorted(all_freq)
    differences = [abs(b - a) for a, b in itertools.combinations(sorted_values, 2)]
    diff_sum = sum(differences)
    
    # Final coherence score computation
    coherence_score = adjusted_score + (diff_sum // 100)
    return coherence_score

# Observed signal frequencies
frequencies = [2, 3, 5, 8, 12]
coherence_score = process_signals(frequencies)
print(f"Result: {coherence_score}")