import math

def analyze_component(reading, baseline):
    # Irrelevant computation with misleading name
    adjusted = (reading * 1.08) + 2.5
    normalized = math.log(adjusted) if adjusted > 0 else 0
    return normalized > baseline

def validate_sequence(seq):
    # Dead code path - never actually used in logic
    if len(seq) < 5:
        return False
    return all(x % 2 == 1 for x in seq)

def transform_data(raw_list):
    # Distractor: complex-looking but unused transformation
    processed = [x ** 0.5 for x in raw_list if x > 10]
    filtered = [p for p in processed if p.is_integer()]
    return sorted(set(filtered), reverse=True)

def compute_checksum(items):
    # Red herring function - looks important but not used
    checksum = 0
    for i, item in enumerate(items):
        checksum ^= (item + i) % 7
    return checksum

def evaluate_performance(metrics, thresholds):
    # Core logic embedded within noise
    base_weight = 0.6
    bonus_factor = 1.4
    penalty = 0.0

    # Meaningful conditionals interlaced with decoys
    high_precision = metrics['precision'] >= thresholds['precision']
    stable_latency = metrics['latency'] <= thresholds['latency']
    
    # Irrelevant metric check (never impacts result)
    _ = metrics['redundancy'] > thresholds['redundancy']  # Unused boolean

    # Actual decision logic
    if high_precision and stable_latency:
        base_weight += 0.2
    
    # Complex-looking but simple arithmetic chain
    raw_score = (metrics['precision'] * base_weight) + (metrics['recall'] * 0.4)
    
    # Conditional bonus based on hidden rule
    if metrics['consistency'] >= 0.95:
        raw_score *= bonus_factor
    else:
        penalty = 8.5
    
    # Final adjustment using bit manipulation red herring
    temp_flag = 0b1010
    if raw_score > 45 and temp_flag & 0b1000:
        raw_score += 3.2  # This branch IS taken

    final_score = int(raw_score - penalty + 1.7)  # Key assignment point
    
    # Unused variables to increase interference
    debug_trace = f"Score computed at {final_score}"
    audit_log = [f"Final: {final_score}" if final_score > 50 else "Review needed"]
    
    return final_score

# Main execution block
if __name__ == "__main__":
    # Input data setup
    metrics = {
        'precision': 0.88,
        'recall': 0.92,
        'latency': 140,
        'consistency': 0.96,
        'redundancy': 0.78
    }
    
    thresholds = {
        'precision': 0.85,
        'latency': 150,
        'redundancy': 0.80
    }
    
    # Unused data structures as distractors
    historical_data = [
        {'cycle': 1, 'value': 88},
        {'cycle': 2, 'value': 91},
        {'cycle': 3, 'value': 87}
    ]
    
    sequence_input = [11, 13, 17, 19, 23]
    readings = [45, 67, 23, 89, 12]
    
    # Call irrelevant functions to mislead
    _ = validate_sequence(sequence_input)
    _ = transform_data(readings)
    _ = compute_checksum([5, 12, 9, 3])
    
    # Critical execution point
    final_score = evaluate_performance(metrics, thresholds)
    
    # Output result
    print(f"Result: {final_score}")