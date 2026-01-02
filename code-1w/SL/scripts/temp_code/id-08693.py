from itertools import combinations, cycle

# Simulate bioinformatics-inspired pattern analysis with noise filtering
def count_motif_occurrences(sequence, motif):
    count = 0
    for i in range(len(sequence) - len(motif) + 1):
        if sequence[i:i+len(motif)] == motif:
            count += 1
    return count

def compute_entropy(values):
    # Irrelevant helper function (dead code path)
    from math import log2
    total = sum(values)
    if total == 0: return 0
    entropy = 0
    for v in values:
        p = v / total
        if p > 0:
            entropy -= p * log2(p)
    return entropy

def filter_noisy_signals(signal_list, threshold=0.5):
    # Distractor function that isn't used in final computation
    return [x for x in signal_list if abs(x) > threshold]

def analyze_pattern(freq_map, control_seq):
    base_score = 0
    adjustment = 0
    
    # Real logic: analyze repeating patterns using itertools
    seq_cycle = list(cycle(control_seq))[:12]  # Extend control sequence
    triplet_windows = [seq_cycle[i:i+3] for i in range(10)]
    
    valid_triplets = 0
    for window in triplet_windows:
        if len(set(window)) == 2:  # exactly two unique elements
            valid_triplets += 1
    
    # Intermediate distractor variables
    temp_analysis = [count_motif_occurrences(control_seq, c*2) for c in 'XYZ']  # always 0, irrelevant chars
    noise_buffer = sum(temp_analysis) * 10
    
    # Core calculation
    for key in freq_map:
        if key in control_seq:
            base_score += freq_map[key] * 3
        else:
            adjustment -= 1
    
    # Use combination to simulate complex interaction
    keys = list(freq_map.keys())
    pair_interactions = 0
    for pair in combinations(keys, 2):
        if abs(ord(pair[0]) - ord(pair[1])) < 3:
            pair_interactions += 1
    
    # Final score influenced by valid_triplets and pair_interactions
    equilibrium_score = base_score + valid_triplets * 2 + pair_interactions - adjustment
    
    # Red herring operation (no effect)
    dummy_cycle = cycle([1, 2])
    for _ in range(5):
        next(dummy_cycle)
    
    return equilibrium_score

# Main execution
frequency_map = {'A': 4, 'C': 2, 'T': 5, 'G': 1}
control_sequence = "ACGTAC"

# Triggering computation
intermediate_noise = [i**2 for i in range(6) if i % 2 == 0]  # unused list
scaling_factor = 1.0  # never used

result_aux = compute_entropy(list(frequency_map.values()))  # dead-end call

# Key statement
equilibrium_score = analyze_pattern(frequency_map, control_sequence)

print(f"Result: {equilibrium_score}")