import itertools

def analyze_sequence(data):
    """Irrelevant function: analyzes sequence patterns but not used in main logic."""
    count = 0
    for a, b in itertools.pairwise(data):
        if (a + b) % 3 == 0:
            count += 1
    return count

def dummy_transform(x):
    """Dead code path: never called."""
    return (x * 2) ^ 5

def preprocess_metrics(raw):
    # Mixes relevant and irrelevant transformations
    processed = {}
    temp_values = [v ** 0.5 for v in raw.values() if v > 10]
    processed['amplitude'] = sum(temp_values) / len(temp_values) if temp_values else 0
    processed['offset'] = len([v for v in raw.values() if v < 5])  # Unused field
    processed['weight'] = sum(v for v in raw.values() if v % 2 == 0)
    return processed

def compute_entropy(values):
    """Misleading function: looks important but unused."""
    total = sum(values)
    entropy = 0
    for v in values:
        p = v / total
        entropy -= p * (p ** 0.5)
    return entropy

def filter_outliers(seq, threshold=25):
    """Partially relevant but ultimately unused filtering."""
    return [x for x in seq if x <= threshold]

def evaluate_performance(metrics, base):
    # Core logic hidden among distractions
    score = 0
    
    # Relevant calculation branch
    if metrics['amplitude'] > base['ref_level']:
        score += int(metrics['amplitude'] * 100)
    
    # Red herring: complex but unused condition
    debug_flag = False
    if metrics.get('offset') > base.get('safety_margin', 0):
        debug_flag = True
        temp_debug = [i**2 for i in range(5)]  # Dead computation
    
    # Another distraction: bitwise manipulation on irrelevant path
    mask = 0b101010
    masked_weight = metrics['weight'] & mask
    if masked_weight > 10:
        score -= 500  # Never triggers due to masking
    
    # Critical path: string-based weight adjustment
    signal_str = base['signal_code']
    split_parts = signal_str.split('-')
    char_count = len([c for c in signal_str if c.isdigit()])
    
    # Key dependency: char_count affects final score
    if char_count >= 3:
        bonus = char_count * 117
        score += bonus
    
    # Early return decoy: looks like exit condition
    if score < 0:
        return -1  # Not reached
    
    # Final critical adjustment
    adjustments = list(itertools.accumulate([1, -2, 3, -1]))
    final_adj = adjustments[-1]  # = 1
    score += final_adj
    
    return score

def main():
    # Input data setup
    raw_input = {
        'input_1': 16,
        'input_2': 32,
        'input_3': 48,
        'input_4': 8,
        'input_5': 2
    }
    
    # Irrelevant preprocessing
    outlier_data = [10, 30, 50, 20, 40]
    cleaned = filter_outliers(outlier_data)
    
    # Unused entropy calculation
    values_for_entropy = [raw_input[k] for k in ['input_1', 'input_2', 'input_3']]
    _ = compute_entropy(values_for_entropy)
    
    # Main execution flow
    metrics = preprocess_metrics(raw_input)
    
    # Baseline configuration with red herrings
    baseline = {
        'ref_level': 2.5,
        'safety_margin': 3,
        'version': 'X9',
        'signal_code': 'SIG-2024-7'
    }
    
    # Decoy variable assignments
    temp_result = analyze_sequence([1, 2, 3, 4, 5])
    shadow_copy = {k: v * 1.1 for k, v in raw_input.items()}
    
    # Key statement
    final_score = evaluate_performance(metrics, baseline)
    
    # Output result
    print(f"Result: {final_score}")

if __name__ == '__main__':
    main()