def analyze_pattern(sequence):
    counts = {c: sequence.count(c) for c in set(sequence)}
    total_pairs = sum(1 for i in range(len(sequence)-1) if sequence[i] == sequence[i+1])
    entropy = 0
    for count in counts.values():
        p = count / len(sequence)
        entropy -= p * __import__('math').log2(p) if p > 0 else 0
    return total_pairs, entropy


def validate_checksum(items):
    checksum = 0
    for i, item in enumerate(items):
        if i % 2 == 0:
            checksum += item * 3
        else:
            checksum += item * 2
    return checksum % 11


def calculate_final_score(data, thresholds):
    # Step 1: Filter relevant entries based on threshold
    filtered_data = [x for x in data if x > thresholds['min_val']]
    
    # Step 2: Compute rolling differences (distractions included)
    diffs = []
    for i in range(1, len(filtered_data)):
        diffs.append(filtered_data[i] - filtered_data[i-1])
    
    # Step 3: Count positive transitions (relevant)
    pos_transitions = sum(1 for d in diffs if d > 0)
    
    # Step 4: Apply transformation using zip and enumerate (core logic)
    transformed = []
    for idx, (a, b) in enumerate(zip(filtered_data, filtered_data[1:])):
        if idx % 2 == 0:
            transformed.append(a * 2 + b)
        else:
            transformed.append(a - b // 2)
    
    # Step 5: Aggregate with conditional scaling (key step)
    base_score = sum(transformed)
    adjustment_factor = len(filtered_data) / (len(data) + 1)
    
    # Irrelevant computations (distractors)
    temp_stats = {}
    temp_stats['max_diff'] = max(diffs) if diffs else 0
    temp_stats['pattern_analysis'] = analyze_pattern(''.join(map(str, [d % 10 for d in data[:5]])))
    temp_stats['checksum'] = validate_checksum([int(d ** 0.5) for d in data if d > 0])
    
    # Final computation chain
    intermediate = base_score * adjustment_factor
    if intermediate > thresholds['high_bound']:
        intermediate -= thresholds['penalty']
    elif intermediate < thresholds['low_bound']:
        intermediate += thresholds['bonus']
    
    # Final decision logic
    final_score = int(intermediate // 1)  # Ensure integer
    
    # Dead code path (red herring)
    if False:
        fallback = 0
        for k in temp_stats:
            fallback += hash(k) % 100
        final_score = fallback
    
    return final_score

# Input setup
raw_data = [12, 15, 10, 23, 18, 25, 30, 5, 40]
config = {
    'min_val': 14,
    'high_bound': 100,
    'low_bound': 30,
    'penalty': 8,
    'bonus': 5
}

# Execution
result = calculate_final_score(raw_data, config)
final_score = result
print(f"Target result: {final_score}")