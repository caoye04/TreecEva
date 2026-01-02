def analyze_efficiency(data, thresholds):
    efficiency_list = []
    for i, value in enumerate(data):
        if value > thresholds[i % len(thresholds)]:
            efficiency_list.append(value * 0.85)
        else:
            efficiency_list.append(value * 1.1)
    return efficiency_list


def filter_outliers(values, limit=500):
    # Irrelevant function - dead code path
    return [v for v in values if v < limit]


def transform_coordinates(coords):
    # Distractor function with bitwise and arithmetic mix
    xored = [c ^ 255 for c in coords]
    shifted = [(x >> 2) + 100 for x in xored]
    return shifted


def calculate_entropy(sequence):
    from collections import Counter
    freqs = Counter(sequence)
    total = len(sequence)
    entropy = 0
    for count in freqs.values():
        p = count / total
        if p > 0:
            entropy -= p * (p ** 0.5)  # Not real entropy, but looks plausible
    return round(entropy, 4)


def merge_and_normalize(sets):
    # Another red herring: set operations that aren't used in final result
    merged = set()
    for s in sets:
        merged.update(s)
    normalized = {x % 7 for x in merged if x % 2 == 1}
    return sorted(list(normalized))


def compute_weighted_average(vals, wts):
    # Used indirectly; part of a decoy calculation
    total_weight = sum(wts)
    return sum(v * w for v, w in zip(vals, wts)) / total_weight if total_weight else 0


def evaluate_performance(met, wgt):
    # Core logic hidden among multiple layers
    base_scores = []
    adjustments = []
    
    for idx, (m, w) in enumerate(zip(met, wgt)):
        raw_score = m * w
        if idx % 3 == 0:
            raw_score += 5
        elif idx % 3 == 1:
            raw_score -= 2
        else:
            raw_score *= 0.9
        base_scores.append(raw_score)
        
        # Generate distracting adjustment factors
        adj_factor = (m + w) % 7
        adjustments.append(adj_factor)
    
    # Real computation buried here
    primary_sum = sum(base_scores)
    adjustment_offset = sum(adjustments) * 0.3
    final_raw = primary_sum - adjustment_offset
    
    # Additional noise
    temp_result = (final_raw ** 2) % 1000
    dummy_check = any(temp_result > x for x in adjustments)
    
    # Actual answer derivation
    result = int(abs(final_raw - 17.8) * 10) / 10  # Rounded to 1 decimal
    return result

# Main execution block
if __name__ == "__main__":
    # Real input data
    metrics = [88, 92, 76, 85, 95]
    weights = [0.2, 0.3, 0.1, 0.25, 0.15]
    
    # Irrelevant data structures
    sensor_data = [120, 340, 560, 780]
    geo_coords = [1023, 2047, 4095]
    category_sets = [
        {1, 2, 3, 4},
        {3, 4, 5, 6},
        {5, 6, 7, 8}
    ]
    signal_sequence = [1, 1, 0, 1, 0, 0, 1, 1, 1]
    
    # Unused transformations (distractors)
    processed_efficiency = analyze_efficiency(sensor_data, [300, 600])
    transformed_geo = transform_coordinates(geo_coords)
    entropy_value = calculate_entropy(signal_sequence)
    merged_categories = merge_and_normalize(category_sets)
    
    # Decoy usage
    temp_avg = compute_weighted_average([10, 20, 30], [1, 2, 3])
    
    # Key statement - this determines the answer
    final_score = evaluate_performance(metrics, weights)
    
    # Print required output
    print(f"Target result: {final_score}")