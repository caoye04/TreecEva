def compute_adaptive_threshold(data_sequence, window_size=4):
    # Irrelevant preprocessing: reverse and pad
    padded_data = [0] * window_size + data_sequence[::-1]
    smoothed = []
    
    # Real smoothing logic (used)
    for i in range(len(data_sequence)):
        segment = data_sequence[i:i+window_size]
        if len(segment) < window_size:
            break
        avg = sum(segment) / window_size
        smoothed.append(avg)
    
    # Distractor: complex but unused frequency analysis
    freq_map = {}
    for x in data_sequence:
        freq_map[x] = freq_map.get(x, 0) + 1
    entropy = 0
    total = len(data_sequence)
    for count in freq_map.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Not real entropy, misleading
    
    # Dead code path: never called
    def analyze_pattern(seq):
        return [seq[i] - seq[i-1] for i in range(1, len(seq))] if len(seq) > 1 else []
    
    # Used transformation: apply exponential weighting
    weighted_values = []
    for i, val in enumerate(smoothed):
        weight = 0.9 ** i
        weighted_values.append(val * weight)
    
    # Red herring: irrelevant normalization
    max_val = max(weighted_values) if weighted_values else 1
    normalized_weights = [w / (max_val + 1e-8) for w in weighted_values]

    # Actual key computation path
    cumulative_shift = 0
    for v in data_sequence:
        if v % 2 == 0:
            cumulative_shift += v // 4
        else:
            cumulative_shift -= v % 3

    # Core logic: build final weights using slicing and conditional logic
    truncated_weights = normalized_weights[:len(normalized_weights)//2 or 1]
    extended_weights = truncated_weights + [truncated_weights[-1]] * 2
    adjustment = 1.5 if len(extended_weights) > 3 else 1.0
    
    # Conditional expression used
    final_weights = [w * adjustment if w > 0.7 else w * 0.9 for w in extended_weights]
    
    # Decoy output variables
    baseline_estimate = sum(final_weights) / len(final_weights)
    volatility_index = max(final_weights) - min(final_weights)
    
    # Key statement with slicing and arithmetic
    correction_factor = (cumulative_shift + 5) / 10.0
    threshold_balance = final_weights[-1] * correction_factor

    # Print required result
    print(f"Result: {threshold_balance}")
    return threshold_balance

# Input data
input_seq = [12, 7, 9, 14, 6, 11, 8]
result = compute_adaptive_threshold(input_seq)