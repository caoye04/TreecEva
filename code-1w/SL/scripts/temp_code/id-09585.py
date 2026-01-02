from itertools import combinations

def analyze_segments(data):
    segments = data.split(',')
    valid_parts = set()
    temp_scores = []
    
    for i, segment in enumerate(segments):
        cleaned = segment.strip().lower()
        if 'error' in cleaned:
            continue
        if len(cleaned) > 3:
            valid_parts.add(cleaned)
            temp_scores.append(len(cleaned) * (i + 1))
    
    # Irrelevant computation: tracking unused indices
    unused_indices = [j for j in range(len(segments)) if j >= len(temp_scores)]
    scaling_factor = sum(temp_scores) / (len(temp_scores) + 1) if temp_scores else 1.0
    
    return valid_parts, temp_scores, scaling_factor

def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        if v > 0:
            p = v / total
            entropy -= p * __import__('math').log(p)
    return round(entropy, 4)

def calculate_final_score(data_tuple):
    parts, scores, factor = data_tuple
    base = sum(scores)
    adjustment = 0
    
    # Real logic: count overlapping character sets
    char_sets = [set(p) for p in parts]
    overlap_count = 0
    for a, b in combinations(char_sets, 2):
        if a & b:  # shared characters
            overlap_count += 1
    
    # Distractor: complex but unused triple nested loop
    phantom_sum = 0
    for x in range(2):
        for y in range(2):
            for z in range(2):
                phantom_sum += (x * y * z) ** 2  # always 0
    
    if overlap_count > 2:
        adjustment = 10
    elif overlap_count == 2:
        adjustment = 5
    else:
        adjustment = 0
    
    # Final score calculation
    final_score = base + adjustment
    return int(final_score)

# Main execution
raw_input = "FragmentA, error_code_9, FragmentB, FragmentC, debug_mode"
data_result = analyze_segments(raw_input)
entropy_metric = compute_entropy(data_result[1])  # unused metric
final_score = calculate_final_score(data_result)
print(f"Target result: {final_score}")