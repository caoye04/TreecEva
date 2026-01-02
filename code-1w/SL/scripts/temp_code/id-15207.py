from itertools import combinations

def analyze_sequence(seq):
    total_peaks = 0
    temp_buffer = []
    for i, val in enumerate(seq):
        if i > 0 and i < len(seq) - 1:
            if seq[i-1] < val > seq[i+1]:
                total_peaks += 1
                temp_buffer.append(val)
    return sum(temp_buffer) if temp_buffer else 0

def validate_pattern(pattern):
    count = 0
    for a, b in zip(pattern, pattern[1:]):
        if abs(a - b) == 1:
            count += 1
    return count % 7  

def process_metrics(data, thresholds):
    baseline = 0
    adjustment_factor = 0.0
    peak_values = []
    
    for key, values in data.items():
        if len(values) >= 3:
            baseline += analyze_sequence(values)
            
    for t in thresholds:
        adjustment_factor += t ** 2
        
    adjustment_factor = adjustment_factor / len(thresholds) if thresholds else 1
    
    # Irrelevant string processing (distractor)
    status_labels = ["valid", "checked", "approved"]
    label_summary = ''.join([s.upper() for s in status_labels])
    
    # Dead code path (distractor)
    if len(label_summary) < 5:
        baseline -= 999

    # Semi-relevant combination logic
    valid_pairs = 0
    all_vals = [v for sublist in data.values() for v in sublist]
    for pair in combinations(all_vals, 2):
        if abs(pair[0] - pair[1]) in thresholds:
            valid_pairs += 1

    # Key metric computation
    final_score = int(baseline + validate_pattern(all_vals) - valid_pairs % 13)
    
    # Extra unused variables (interference)
    dummy_tracker = {i: x*2 for i, x in enumerate(all_vals)}
    temp_result = [x for x in map(lambda y: y//2, filter(lambda z: z>5, all_vals))]
    
    return final_score

# Input construction
data = {
    'series_a': [2, 5, 3, 8, 6],
    'series_b': [1, 4, 2, 7, 5, 9, 4],
    'series_c': [3, 3, 5]
}
thresholds = [1, 2, 4]

final_score = process_metrics(data, thresholds)
print(f"Result: {final_score}")