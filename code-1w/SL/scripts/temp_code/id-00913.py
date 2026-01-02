def analyze_text_patterns(input_str):
    # Irrelevant text analysis function (dead code path)
    vowels = 'aeiou'
    vowel_count = sum(1 for c in input_str.lower() if c in vowels)
    word_list = input_str.split()
    reversed_words = [word[::-1] for word in word_list]
    return len(reversed_words)


def legacy_calculate_average(items):
    # Outdated averaging logic with bit manipulation red herring
    total = 0
    for item in items:
        total += item << 1  # Left shift as distraction
    shifted_len = len(items) if len(items) > 0 else 1
    return (total >> 1) / shifted_len  # Cancel out shifts, misleading


def transform_metrics(raw):
    # Real transformation used in computation
    filtered = [x for x in raw if x > 0]
    squared = [x ** 2 for x in filtered]
    clipped = [min(x, 100) for x in squared]
    return clipped


def compute_entropy(values):
    # Distractor: computes entropy but not used in final result
    from math import log2
    total = sum(values)
    if total == 0:
        return 0
    probabilities = [v / total for v in values if v > 0]
    entropy = -sum(p * log2(p) for p in probabilities)
    return round(entropy, 4)


def evaluate_performance(data):
    # Core logic embedded within distractions
    processed = transform_metrics(data)
    
    # Decoy variables and operations
    temp_result = sum(processed) * 0.5
    adjustment_factor = len(processed) % 7
    dummy_cache = {i: processed[i] for i in range(len(processed))}
    
    # Actual key computation chain
    base_score = sum(processed)  # Step 1: sum transformed values
    penalty = 0
    for i in range(1, len(processed)):
        if processed[i] < processed[i-1]:
            penalty += 1  # Step 2-8: count decreasing transitions
    multiplier = 1 + (len(processed) // 5)  # Step 9: scale by group size
    intermediate = base_score - (penalty * 3)  # Step 10
    final_score = intermediate * multiplier  # Step 11
    
    # More distractions below
    outlier_flags = [x for x in processed if x == 100]
    compression_ratio = len(processed) / (len(outlier_flags) + 1)
    metadata_summary = {
        'size': len(processed),
        'max_val': max(processed),
        'checksum': sum([x ^ 7 for x in processed])
    }
    
    return int(final_score)

# Main execution with decoy calls
raw_metrics = [3, -1, 4, 2, 5, -3, 4, 1]
metric_data = [x + 1 for x in raw_metrics if x != -1]  # Filter and shift data

# Dead function calls with no effect
_ = analyze_text_patterns("Performance evaluation log")
_ = legacy_calculate_average([2, 4, 6])

# Key statement
final_score = evaluate_performance(metric_data)

# Print result as required
print(f"Result: {final_score}")