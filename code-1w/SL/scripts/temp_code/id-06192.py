def preprocess_items(raw_list):
    # Irrelevant preprocessing: transforms data in a way that's not used later
    temp_result = [x ** 2 for x in raw_list if x % 2 == 0]
    normalized = [round(val / (sum(temp_result) + 1e-8), 4) for val in temp_result]
    return sorted(normalized, reverse=True)


def validate_constraints(entries):
    # Dead-end validation function, never called in execution path
    if len(entries) < 5:
        return False
    return all(e >= 0 for e in entries)


def accumulate_metrics(values):
    # Distractor function: looks important but unused
    total = 0
    for v in values:
        if v > 30:
            total += v * 0.1
    return total


def filter_outliers(dataset, threshold=75):
    # Seemingly relevant filtering, but result not used in final computation
    filtered = {k: v for k, v in dataset.items() if v < threshold}
    extra_calc = sum(filtered.values()) / (len(filtered) + 1)
    adjustment = extra_calc * 0.05
    return adjustment  # Never actually used


def calculate_entropy(values):
    # Red herring: computes entropy but isn't part of final score logic
    from math import log2
    total = sum(values)
    probabilities = [(v / total) for v in values]
    entropy = -sum(p * log2(p) for p in probabilities if p > 0)
    return round(entropy, 4)


def calculate_final_score(data, weight_map):
    # Core logic embedded within noise
    
    # Step 1: Extract keys and transform
    keys = list(data.keys())
    key_weights = [weight_map.get(k, 1) for k in keys]
    
    # Step 2: Compute weighted sum (actual core)
    weighted_sum = 0
    for i, k in enumerate(keys):
        weighted_sum += data[k] * key_weights[i]
    
    # Step 3: Apply conditional bonus based on set properties
    key_set = set(keys)
    control_set = {'alpha', 'beta', 'gamma', 'delta'}
    overlap = key_set & control_set  # Intersection
    bonus_factor = len(overlap) * 0.2
    
    # Step 4: Adjust sum with bonus
    adjusted_sum = weighted_sum * (1 + bonus_factor)
    
    # Step 5: Secondary correction using symmetric difference
    diff_set = key_set ^ {'alpha', 'beta'}  # XOR
    correction = len(diff_set) * 0.05
    
    # Step 6: Apply correction
    corrected_score = adjusted_sum * (1 - correction)
    
    # Step 7: Floor to nearest integer if above threshold
    if corrected_score > 100:
        final = int(corrected_score)
    else:
        final = round(corrected_score, 2)
    
    # Step 8: Final override condition (looks like edge case, but always triggers)
    if 'omega' in key_set:
        final -= 17  # Critical adjustment
    
    return final

# Main execution block
if __name__ == '__main__':
    
    # Irrelevant data structures
    legacy_data = [12, 15, 22, 30, 31, 32]
    processed_legacy = preprocess_items(legacy_data)
    
    # Unused metric accumulation
    dummy_entries = [45, 60, 75, 90]
    dummy_total = accumulate_metrics(dummy_entries)
    
    # Real input data (obscured among distractors)
    data_set = {
        'alpha': 20,
        'beta': 35,
        'gamma': 25,
        'omega': 40
    }
    
    # Weight map: critical for calculation
    weights = {
        'alpha': 1.2,
        'beta': 0.8,
        'gamma': 1.5,
        'delta': 2.0,
        'omega': 1.0
    }
    
    # Irrelevant outlier filtering
    _ = filter_outliers(data_set, threshold=75)
    
    # Entropy computed but unused
    _ = calculate_entropy(list(data_set.values()))
    
    # Key execution point
    final_score = calculate_final_score(data_set, weights)
    
    # Output result
    print(f"Result: {final_score}")