import itertools

def simulate_growth(factor, cycles):
    # Irrelevant simulation function (dead code path)
    return sum((i ** factor) % 7 for i in range(cycles))

def filter_active_nodes(node_list, threshold=5):
    # Misleading filtering logic with decoy behavior
    return [n for n in node_list if (n * 3) % 11 > threshold]

def transform_sequence(seq):
    # Complex transformation with red herring operations
    shifted = [(x + 2) * 3 for x in seq]
    mapped = list(map(lambda y: (y ^ 5) & 15, shifted))
    filtered = [z for z in mapped if z != 12]
    return filtered[:len(filtered)//2] if len(filtered) > 3 else filtered

def accumulate_metrics(data_stream):
    # Real computation buried under distractions
    accumulator = 0
    scale = 1.75
    for val in data_stream:
        if val % 4 == 0:
            accumulator += val // 4
        elif val % 3 == 0:
            accumulator -= val // 5
    return round(accumulator * scale, 6)

def compute_entropy(signal):
    # Decoy scientific-looking computation
    total = 0.0
    for s in signal:
        if s > 0:
            total -= s * math.log(s + 1e-9)
    return total

def harvest_result(dataset):
    # Core logic hidden among multiple layers
    temp_grid = [[i + j for j in range(3)] for i in dataset]
    flat = list(itertools.chain.from_iterable(temp_grid))
    refined = [x for x in flat if x % 2 == 1]
    base_score = sum(refined)
    adjustment = len([x for x in flat if x > 6])
    return base_score - (adjustment * 2)

# --- Main execution block ---
if __name__ == "__main__":
    # Initialize various variables (many irrelevant)
    raw_input = [2, 3, 5, 7, 11]
    growth_pattern = [simulate_growth(f, 6) for f in raw_input]  # Dead computation
    
    # Distractor: complex-looking but unused data structures
    node_cluster = [x * 2 + 1 for x in range(8)]
    active_units = filter_active_nodes(node_cluster, threshold=6)  # Unused result
    
    # Real data processing begins here
    processed_data = transform_sequence(raw_input)
    
    # More red herrings
    entropy_signal = [0.1, 0.3, 0.5, 0.1]
    noise_level = compute_entropy(entropy_signal)  # Never used
    
    # Key accumulation step (partially relevant)
    interim_metric = accumulate_metrics(processed_data)
    
    # Critical statement containing the answer
    final_yield = harvest_result(processed_data)
    
    # Print required output
    print(f"Result: {final_yield}")