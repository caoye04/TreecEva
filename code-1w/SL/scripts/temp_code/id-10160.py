import itertools

def analyze_sequence(data):
    # Irrelevant function: analyzes sequence but not used in final calculation
    if len(data) < 5:
        return False
    increasing = all(data[i] < data[i+1] for i in range(len(data)-1))
    oscillating = sum(1 for a, b in zip(data, data[1:]) if a != b) > len(data) // 2
    return increasing or oscillating

def preprocess_metrics(raw):
    # Distractor preprocessing: modifies data but not part of critical path
    cleaned = [x for x in raw if x > 0]
    smoothed = [sum(cleaned[i:i+3]) / 3 for i in range(len(cleaned)-2)]
    return [round(s * 1.05) for s in smoothed]

def calculate_baseline(ref, mode='fast'):
    # Dead code path — looks important but unused
    if mode == 'precise':
        return sum(ref) / len(ref) * 0.95
    else:
        return ref[0] * 0.8

def score_component(values, weight):
    # Core logic buried among distractions
    base = sum(values) // len(values)
    adjustment = 0
    for v in values:
        if v % 2 == 0 and v > 10:
            adjustment += 2
        elif v < 5:
            adjustment -= 1
    return base + adjustment * weight

def validate_integrity(trace_log):
    # Completely irrelevant validation routine
    if not trace_log:
        return False
    checksum = 0
    for entry in trace_log:
        checksum ^= entry
    return checksum % 7 == 0

def evaluate_performance(metrics, weights):
    # Critical function with embedded logic and red herrings
    temp_results = []
    decoy_accum = 0
    
    # Real computation mixed with fake ones
    for i, (m, w) in enumerate(zip(metrics, weights)):
        chunk = m[::2]  # slicing operation used meaningfully
        decoy_chunk = m[1::2]
        
        # Actual contribution to result
        score = score_component(chunk, w)
        temp_results.append(score)
        
        # Fake accumulation — distractor
        for d in decoy_chunk:
            decoy_accum += d * (i + 1)
    
    # Red herring: complex transformation with no impact
    cartesian_view = list(itertools.product([1, 2], temp_results[:2]))
    expansion_total = sum(a * b for a, b in cartesian_view)
    
    # Final logic step: real answer computed here
    raw_final = sum(temp_results[i] * 0.7 for i in range(len(temp_results)))
    penalty = 0
    if len(metrics) > 3:
        penalty += 5
    if sum(weights) > 10:
        penalty += 3
    
    final_score = int(raw_final - penalty)  # This is the actual target variable
    
    # Unused variables to mislead
    auxiliary_score = expansion_total // 4
    normalized_decoy = decoy_accum / (decoy_accum + 1) if decoy_accum else 0
    
    return final_score

# Main execution block
if __name__ == '__main__':
    # Input data setup
    metrics = [
        [12, 15, 8, 20, 7],
        [5, 6, 13, 4, 9],
        [10, 11, 6, 14],
        [7, 8, 3, 12]
    ]
    weights = [3, 2, 4, 3]
    
    # Irrelevant auxiliary data
    trace_data = [23, 45, 67, 12, 89, 34, 56]
    sequence_input = [1, 3, 2, 5, 4, 7, 6]
    baseline_reference = [100, 200, 150]
    
    # Trigger irrelevant functions (dead calls)
    _ = analyze_sequence(sequence_input)
    _ = calculate_baseline(baseline_reference, mode='fast')
    _ = validate_integrity(trace_data)
    
    # Preprocess — looks important but not used in final score
    processed_metrics = []
    for m in metrics:
        processed_metrics.append(preprocess_metrics(m))
    
    # Key statement: this determines the answer
    final_score = evaluate_performance(metrics, weights)
    
    # Output result as required
    print(f"Result: {final_score}")