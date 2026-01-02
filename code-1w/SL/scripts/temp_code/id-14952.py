import itertools

def analyze_pattern(sequence):
    # Irrelevant function - dead code path
    return [x ** 2 for x in sequence if x % 3 == 0]

def dummy_transform(values):
    # Distractor: unused transformation
    shifted = [(v << 2) ^ 7 for v in values]
    return [s for s in shifted if s > 10]

def compute_hash(key_vals):
    # Misleading intermediate result
    h = 0
    for k, v in key_vals.items():
        h += (len(k) + v) * 31
    return h % 1000

def filter_relevant(items, threshold=5):
    # Real but partially distracting logic
    filtered = []
    for i, item in enumerate(items):
        if i % 2 == 0 and item > threshold:
            filtered.append(item * 1.1)
    return filtered

def integrate_signals(signals):
    # Unused complex logic with bit manipulation red herring
    result = 0
    for s in signals:
        result ^= (s << 3) | (s >> 2)
    return result & 0xFFFF

def process_metrics(data, weights):
    # Core function containing actual answer computation
    
    # Step 1: Extract valid entries using conditional filtering
    valid_pairs = [(d, w) for d, w in zip(data, weights) if d > 0 and w > 0]
    
    # Step 2: Normalize weights using sum reduction
    total_weight = sum(w for _, w in valid_pairs)
    normalized = [(d, w / total_weight) for d, w in valid_pairs]
    
    # Step 3: Apply exponential scaling on data
    scaled_values = [d ** 1.5 for d, _ in normalized]
    
    # Step 4: Pair with index using enumerate for distraction
    indexed = list(enumerate(scaled_values))
    offset_correction = sum(i * 0.01 for i, _ in indexed)  # Minor correction
    
    # Step 5: Use itertools to group every two elements (some may be unused)
    grouped = list(itertools.zip_longest(scaled_values[::2], scaled_values[1::2]))
    
    # Step 6: Aggregate weighted contributions
    aggregate = 0.0
    for (val, (_, weight)), _ in zip(zip(scaled_values, normalized), range(len(normalized))):
        aggregate += val * weight
    
    # Step 7: Apply modular adjustment based on length
    adjustment_factor = len(valid_pairs) % 7
    
    # Step 8: Final score calculation
    final_score = aggregate * (1 + adjustment_factor * 0.05) - offset_correction
    
    # Step 9: Red herring - hash of something irrelevant
    dummy_dict = {f"key_{i}": int(sv) for i, sv in enumerate(scaled_values)}
    hash_value = compute_hash(dummy_dict)  # Not used in final result
    
    # Step 10: One more distraction with string operations
    labels = ['A', 'B', 'C', 'D']
    combined_label = ''.join([l + str(idx) for idx, l in enumerate(labels[:len(valid_pairs)])])
    
    # Step 11: Sorting unrelated array
    junk_array = [9, 4, 7, 1, 8]
    junk_array.sort(reverse=True)
    
    # Step 12: Return only the real answer
    return round(final_score, 6)

# Main execution block
if __name__ == "__main__":
    # Input data with meaningful and irrelevant parts
    raw_data = [3, -1, 4, 0, 5, 2]
    weights = [0.1, 0.4, 0.2, 0.6, 0.05, 0.05]
    
    # Unused signal processing
    signals = [12, 15, 10, 8]
    signal_integrated = integrate_signals(signals)
    
    # Filter relevant data (used)
    processed_data = filter_relevant(raw_data, threshold=2)
    
    # Dummy pattern analysis (dead end)
    patterns = analyze_pattern([6, 9, 12, 15])
    transformed = dummy_transform([4, 8, 12])
    
    # Critical assignment
    final_score = process_metrics(raw_data, weights)
    
    # Output result as required
    print(f"Result: {final_score}")