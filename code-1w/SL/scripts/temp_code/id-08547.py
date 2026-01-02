def analyze_sequence(data):
    # Irrelevant transformation: bit manipulation red herring
    masked_values = [x ^ 255 for x in data[:10]]
    shifted_sum = sum((x >> 3) for x in masked_values) // 2

    # Distractor: unused recursive function
    def recurse(n):
        if n <= 1:
            return 1
        return n * recurse(n - 2)

    # Meaningful but obscured computation
    base_stats = {"mean": sum(data) / len(data), "count": len(data)}
    
    # Red herring: complex but unused set operations
    unique_pairs = set((data[i], data[j]) for i in range(3) for j in range(i+1, 5))
    pair_sums = {a + b for a, b in unique_pairs}
    
    # Actual relevant logic buried here
    thresholds = [base_stats["mean"] * 0.9, base_stats["mean"] * 1.1]
    valid_range = [x for x in data if thresholds[0] < x < thresholds[1]]
    
    # Decoy list processing
    processed = []
    for val in data:
        if val > 50:
            processed.append(val * 0.85)
        else:
            processed.append(val * 1.1)
    
    # Core logic disguised among distractions
    outlier_count = len([x for x in data if x < 10 or x > 90])
    adjustment_factor = 1 - (outlier_count / len(data) * 0.15)
    
    # Another decoy: tuple unpacking with no effect
    info_tuple = (shifted_sum, len(pair_sums), recurse(6))
    temp_a, temp_b, temp_c = info_tuple

    # Real accumulation path
    cumulative = 0
    for i, val in enumerate(valid_range):
        cumulative += val * (0.95 ** i)  # Exponential decay weighting

    # Secondary correction based on set size
    metric_set = set(round(x * adjustment_factor) for x in valid_range)
    
    # Final computation depends only on this function
    def evaluate_performance(s):
        total = sum(s)
        penalty = len(s.intersection({0, 1})) * 5  # small penalty for edge values
        return int(total - penalty)

    final_score = evaluate_performance(metric_set)
    
    # Dead code paths and unused variables to mislead
    debug_log = f'Shifted: {shifted_sum}, Recurse: {recurse(6)}, Pairs: {len(pair_sums)}'
    unused_array = [[i+j for j in range(4)] for i in range(4)]
    
    # Print required output
    print(f"Result: {final_score}")

# Input data with hidden structure
input_data = [12, 45, 67, 89, 23, 55, 76, 81, 94, 33, 47, 58, 73, 82, 39]
analyze_sequence(input_data)