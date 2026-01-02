import itertools

def analyze_sequence(data):
    """Irrelevant analysis function - distractor"""
    return sum(x ** 2 for x in data if x > 0) / len(data) if data else 0

def normalize_vector(v):
    """Another red herring - not used in main logic"""
    magnitude = sum(x**2 for x in v) ** 0.5
    return [x / magnitude for x in v] if magnitude else v

def validate_input(text):
    """String validation distractor using string methods"""
    cleaned = text.strip().lower()
    if not cleaned.isalpha():
        return False
    return cleaned.startswith('a') or cleaned.endswith('z')

def transform_key_values(mapping):
    """Complex-looking but unused transformation"""
    result = {}
    for k, v in mapping.items():
        if isinstance(k, str) and k.isdigit():
            result[int(k)] = v * 2
        elif isinstance(v, int):
            result[k + '_mod'] = v + len(k)
    return result

def compute_entropy(values):
    """Dead-end computation with bit manipulation red herring"""
    total = 0
    for v in values:
        bits = bin(v).count('1')
        if bits % 3 == 0:
            total ^= v
        else:
            total += v & 0xFF
    return total >> 2

def filter_candidates(applicants, threshold=50):
    """Distractor involving conditional branches and loops"""
    selected = []
    for app in applicants:
        score = app.get('score', 0)
        if score >= threshold:
            penalty = 10 if app.get('late', False) else 0
            adjusted = score - penalty
            if adjusted >= threshold - 15:
                selected.append({**app, 'adj': adjusted})
    return selected

def evaluate_performance(metrics, base):
    # Core logic hidden among distractions
    adjustments = []
    
    # Real logic begins - depends on specific conditions
    for key, val in metrics.items():
        if 'efficiency' in key:
            adjustments.append(val * 1.1)
        elif 'latency' in key:
            adjustments.append(max(0, 100 - val))
        elif 'throughput' in key:
            adjustments.append(val // 2)
    
    # Actual answer derived here through composite calculation
    raw_total = sum(adjustments)
    
    # Conditional branch that does affect outcome
    if len(adjustments) >= 3:
        multiplier = 1.25
    else:
        multiplier = 0.9
    
    # Final computation chain
    temp_result = raw_total * multiplier
    
    # Integer division and rounding behavior is critical
    baseline_offset = int(round(base * 0.75))
    final_score = int(temp_result - baseline_offset)
    
    # Irrelevant print to mislead traceability
    debug_info = f"Final adjustments: {adjustments}, Raw: {raw_total}"
    
    return final_score

# Main execution block
if __name__ == '__main__':
    # Real input data
    performance_metrics = {
        'efficiency_v1': 45,
        'latency_ms': 68,
        'throughput_eps': 120,
        'reliability_pct': 99
    }
    
    baseline_ref = 88
    
    # Unused variables - dead code paths
    candidate_pool = [
        {'name': 'Alice', 'score': 78, 'late': True},
        {'name': 'Bob', 'score': 65, 'late': False}
    ]
    
    config_settings = {'max_iters': 100, 'tolerance': 1e-5}
    feature_flags = [True, False, True]
    
    # String method distractors
    labels = ['Status_A', 'Status_B', 'Status_C']
    valid_labels = [lbl for lbl in labels if lbl.endswith('A') or 'B' in lbl]
    
    # Complex but irrelevant itertools usage
    combinations = list(itertools.combinations([1, 2, 3, 4], 3))
    combo_sums = [sum(c) for c in combinations]
    
    # Bit manipulation decoy
    flags = 0b101010
    toggled = flags ^ 0b111111
    
    # Key execution point
    final_score = evaluate_performance(performance_metrics, baseline_ref)
    
    # Print required output
    print(f"Result: {final_score}")