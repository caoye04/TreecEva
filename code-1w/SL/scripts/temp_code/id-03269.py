import itertools

def analyze_stability(sequence, limit):
    # Precompute transformed segments using slicing and filtering
    shifted = sequence[1:] + [0]
    differences = [abs(a - b) for a, b in zip(sequence, shifted)]
    
    # Irrelevant computation: simulate decay (not used in final result)
    decay_mask = [0.95 ** i for i in range(len(sequence))]
    dampened = [sequence[i] * decay_mask[i] for i in range(len(sequence))]
    avg_dampened = sum(dampened) / len(dampened)

    # Core logic: find stable subsequences using itertools
    cumulative_fluctuation = 0
    stable_segments = 0
    for length in range(2, len(sequence) + 1):
        for subset in itertools.combinations(sequence, length):
            if sum(subset) > limit * 2:
                continue
            sorted_sub = sorted(subset)
            if len(sorted_sub) > 1:
                # Use slice to check internal consistency
                mid_section = sorted_sub[1:-1]
                if not mid_section or max(mid_section) - min(mid_section) < limit:
                    stable_segments += 1

    # Secondary path: linear search for first major drop (distractor)
    spike_index = -1
    for i in range(len(differences)):
        if differences[i] > limit * 1.5:
            spike_index = i
            break

    # Actual determining factor: count low-fluctuation windows
    window_size = 3
    valid_windows = 0
    for i in range(len(differences) - window_size + 1):
        window = differences[i:i + window_size]
        if sum(window) < limit and all(w < limit / 1.2 for w in window):
            valid_windows += 1

    # Final score based on combinatorial stability and window analysis
    equilibrium_score = stable_segments * 3 - valid_windows
    return equilibrium_score

# Main execution
energy_sequence = [8, 6, 7, 5, 3, 9, 4]
threshold = 4

# Misleading pre-analysis with no impact
baseline_avg = sum(energy_sequence) // len(energy_sequence)
adjusted_seq = [x - baseline_avg for x in energy_sequence]
filtered = [x for x in adjusted_seq if x > 0]
proxy_metric = len(filtered) * 2

# Key statement
equilibrium_score = analyze_stability(energy_sequence, threshold)

# Output result
print(f"Result: {equilibrium_score}")