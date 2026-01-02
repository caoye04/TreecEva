def analyze_redundancy(items):
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return len(duplicates)


def compute_entropy(values):
    from math import log2
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        if v > 0:
            p = v / total
            entropy -= p * log2(p)
    return round(entropy, 4)


def filter_noisy_data(records, min_freq=2):
    freq = {}
    for r in records:
        freq[r] = freq.get(r, 0) + 1
    return {k for k, v in freq.items() if v >= min_freq}


def optimize_distribution(inventory_sets, threshold):
    # Core logic disguised among distractions
    aggregated = set()
    temp_union = set()
    
    for inv in inventory_sets:
        temp_union |= set(inv)
        if len(set(inv)) > threshold:
            aggregated.update([x for x in inv if x % 3 == 1])
        else:
            aggregated.update([x for x in inv if x % 4 == 2])
    
    # Irrelevant entropy calculation (distraction)
    counts = [len(s) for s in inventory_sets]
    _ = compute_entropy(counts)
    
    # Misleading redundancy analysis
    all_items = [item for sublist in inventory_sets for item in sublist]
    _ = analyze_redundancy(all_items)
    
    # Actual key computation
    valid_candidates = set()
    for x in aggregated:
        if x > 0 and (x ** 0.5).is_integer():
            valid_candidates.add(x)
    
    # Simulate capacity based on filtered perfect squares
    base_cap = sum(valid_candidates)
    adjustment_factor = len(temp_union) % 9
    final_capacity = base_cap - adjustment_factor
    
    # Dead code path (never executed unless threshold negative)
    if threshold < 0:
        fallback = filter_noisy_data(all_items)
        final_capacity = len(fallback)
    
    return final_capacity

# Input data
inventory_sets = [
    [16, 25, 10, 16, 30],
    [18, 22, 49, 50],
    [8, 12, 36, 44],
    [64, 70, 81, 21]
]
threshold = 3

# Execute main logic
temp_union_var = set().union(*inventory_sets)
dummy_analysis = analyze_redundancy([item for sublist in inventory_sets for item in sublist])

final_capacity = optimize_distribution(inventory_sets, threshold)
print(f"Result: {final_capacity}")