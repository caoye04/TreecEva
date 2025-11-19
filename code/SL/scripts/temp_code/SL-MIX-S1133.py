import statistics
from itertools import combinations, permutations

def analyze_linguistic_coherence():
    # Fragment word frequency data
    fragment_a_freq = [12, 18, 15, 22]
    fragment_b_freq = [10, 14, 19, 16, 20]
    fragment_c_freq = [13, 17, 11, 21, 23, 18]
    
    # Combine all frequencies for statistical analysis
    all_frequencies = fragment_a_freq + fragment_b_freq + fragment_c_freq
    
    # Calculate basic statistics
    mean_frequency = statistics.mean(all_frequencies)
    std_deviation = statistics.stdev(all_frequencies)
    
    # Determine unique words (using set for uniqueness)
    unique_word_count = len(set(all_frequencies))
    
    # Threshold for coherence check
    coherence_threshold = mean_frequency / unique_word_count if unique_word_count > 0 else 0
    
    # Total fragments count
    fragment_set = frozenset(['A', 'B', 'C'])
    fragment_count = len(fragment_set)
    
    # Coherence condition check
    is_statistically_coherent = (std_deviation < coherence_threshold) and (unique_word_count > 10)
    
    # Calculate coherence score based on condition
    coherence_score = (
        mean_frequency * len(list(permutations(fragment_set, 2)))
        if is_statistically_coherent
        else sum(all_frequencies) - len(list(combinations(fragment_set, 2)))
    )
    
    return coherence_score

# Execute analysis and print result
coherence_score = analyze_linguistic_coherence()
print(f"Result: {coherence_score}")