def analyze_pattern(data, limit):
    # Irrelevant preprocessing (distractor)
    normalized = [x / max(data) for x in data if x > 0]
    filtered = [x for x in data if x % 2 == 1]
    
    # Red herring: unused transformation
    transformed = []
    for x in data:
        if x > 10:
            transformed.append(x ** 0.5 + 3)
        else:
            transformed.append(x * 2 - 1)

    # Real logic begins: count transitions above threshold
    above_threshold = [i for i, x in enumerate(data) if x > limit]
    gaps = [above_threshold[i+1] - above_threshold[i] for i in range(len(above_threshold)-1)] if len(above_threshold) > 1 else [0]
    
    # Misleading intermediate: average_gap looks important but isn't used in final result
    average_gap = sum(gaps) / len(gaps) if gaps else 0
    
    # Actual key logic: compute weighted pattern score using string-based digit analysis
    digit_frequencies = {}
    for x in data:
        for digit in str(x):
            if digit.isdigit():
                digit_frequencies[digit] = digit_frequencies.get(digit, 0) + 1
    
    # Use conditional expression to decide scoring mode
    scoring_mode = 'high' if len([v for v in digit_frequencies.values() if v > 2]) > 0 else 'low'
    
    # Compute combinatorics-inspired score: sum of min and max gap, multiplied by unique digit count
    unique_digits = len([d for d in digit_frequencies if digit_frequencies[d] >= 1])
    min_gap = min(gaps) if gaps else 0
    max_gap = max(gaps) if gaps else 0
    
    # Decoy function call that does nothing
    def log_analysis(x):
        return None  # Dead code path
    log_analysis(digit_frequencies)

    # Final computation
    base_score = min_gap + max_gap
    adjustment = len(filtered) - len(normalized)  # Irrelevant difference
    final_score = base_score * unique_digits + (10 if scoring_mode == 'high' else 0)

    # String method distraction: process metadata tag
    metadata_tag = "DGN-7821-X"
    if metadata_tag.startswith("DGN") and metadata_tag.endswith("X"):
        code_number = int(metadata_tag[4:7])  # 782
        final_score -= code_number % 97  # Minor red herring adjustment

    # Key result
    final_diagnostic = final_score + 5  # Final offset
    return final_diagnostic

# Simulated sensor signal data
signal_sequence = [12, 7, 15, 3, 21, 9, 18, 5, 24, 8, 14, 6, 19, 11]
threshold = 10

# Execute main logic
final_diagnostic = analyze_pattern(signal_sequence, threshold)
print(f"Result: {final_diagnostic}")