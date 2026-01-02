def analyze_pattern(seq):
    if len(seq) < 3:
        return 0
    count = 0
    for i in range(1, len(seq)-1):
        if seq[i-1] < seq[i] > seq[i+1]:
            count += 1
    return count

# Irrelevant helper function (decoy)
def calculate_entropy(data):
    import math
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    entropy = 0
    total = len(data)
    for f in freq.values():
        p = f / total
        entropy -= p * math.log2(p)
    return round(entropy, 6)

# Unused transformation (dead code path)
def transform_signal(x):
    return (x << 2) ^ 0xFF

# Core logic disguised among distractions
def evaluate_thresholds(values, limit=100):
    valid = [v for v in values if v % 2 == 1 and v < limit]
    return sum(valid) if len(valid) > 3 else len(valid)

# Complex processing with distractors
def filter_and_map(records):
    result = []
    for idx, record in enumerate(records):
        if idx % 2 == 0:
            transformed = (record * 3) + 5
            if transformed % 7 == 0:
                result.append(transformed)
    return result

# Misleading aggregation (looks important but unused)
def aggregate_metrics(data_list):
    stats = {}
    for i, d in enumerate(data_list):
        stats[f'metric_{i}'] = {
            'raw': d,
            'square': d**2,
            'inverse': round(1/d, 4) if d != 0 else 0
        }
    return stats

# Real computation buried in noise
def process_entry(item):
    a, b, c = item
    temp = (a + b) * c
    if temp > 50:
        return temp // 2
    return temp

def process_results(dataset):
    # Distractor variables
    baseline = 42
    threshold_mask = [1, 0, 1, 1, 0]
    dummy_lookup = {f'key_{i}': i*3 for i in range(10)}

    # Real logic begins
    extracted = [process_entry(row) for row in dataset]
    
    # Apply filter based on pattern analysis (real use)
    pattern_seq = [1, 3, 2, 5, 4, 6, 3]
    spike_count = analyze_pattern(pattern_seq)
    
    # Conditional expression with zip and enumerate (required features)
    adjusted = [
        val + idx if flag else val
        for idx, (val, flag) in enumerate(zip(extracted, threshold_mask * (len(extracted)//5 + 1)))
    ]
    
    # Dictionary operation: mapping indices
    index_map = {i: v for i, v in enumerate(adjusted)}
    
    # More irrelevant computation (distractor)
    outlier_check = set()
    for k, v in index_map.items():
        if v % 11 == 0:
            outlier_check.add(k)
    
    # Actual final calculation
    subset = [v for k, v in index_map.items() if k % 2 == 1]
    base_score = sum(subset)
    bonus = evaluate_thresholds(subset, limit=200)
    
    # Final composition
    final_score = base_score + bonus - spike_count
    
    # Only this print matters
    print(f"Result: {final_score}")
    return final_score

# Main execution block
if __name__ == "__main__":
    # Input data
    assessment_data = [
        (4, 5, 3),
        (2, 8, 4),
        (7, 1, 6),
        (3, 3, 7),
        (6, 2, 5)
    ]
    
    # Dead code calls (red herrings)
    _ = calculate_entropy([1,2,2,3,3,3])
    _ = aggregate_metrics([10,20,30])
    
    # Key statement
    final_score = process_results(assessment_data)