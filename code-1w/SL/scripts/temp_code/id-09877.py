def preprocess_entry(entry):
    # Irrelevant transformation: character counting
    char_count = sum(1 for c in entry['name'] if c.isalpha())
    normalized = char_count / len(entry['name']) if entry['name'] else 0
    
    # Distractor: unused computation
    magic_factor = (entry['value'] ^ 255) & 127
    temp_offset = magic_factor % 7
    
    return entry['value'] * 1.1  # Actual relevant scaling


def validate_dataset(dataset):
    # Misleading validation that doesn't affect result
    issues = []
    for i, item in enumerate(dataset):
        if item['value'] < 0:
            issues.append(f"Negative at {i}")
        if len(item['name']) > 10:
            issues.append(f"Long name at {i}")
    return len(issues) > 0  # Unused return


def transform_sequence(seq):
    # Dead code path — never called
    return [x ** 0.5 for x in seq if x > 0]


def bitwise_integrity_check(value):
    # Decoy function: looks important but unused
    checksum = 0
    for _ in range(8):
        checksum ^= value & 255
        value >>= 8
    return checksum


def calculate_entropy(values):
    # Red herring: computes something plausible but irrelevant
    from math import log2
    total = sum(values)
    if total == 0:
        return 0.0
    probs = [v / total for v in values if v > 0]
    return -sum(p * log2(p) for p in probs)


def calculate_final_score(raw_data, importance_weights):
    # Core logic buried among distractions
    processed = []
    for idx, record in enumerate(raw_data):
        proc_val = preprocess_entry(record)
        weight = importance_weights[idx % len(importance_weights)]
        adjusted = proc_val * weight
        processed.append(adjusted)
    
    # Real key step: XOR fold with index shift
    accumulator = 0
    for i, val in enumerate(processed):
        truncated = int(round(val))
        accumulator ^= (truncated + i)  # Index-dependent XOR
    
    # Secondary transformation: sum of even-indexed only
    even_sum = sum(processed[i] for i in range(0, len(processed), 2))
    
    # Final score is a combination
    final_score = accumulator + int(even_sum) // 10
    
    # Irrelevant tuple unpacking distraction
    stats = ('max', max(processed)), ('min', min(processed)), ('len', len(processed))
    tag, peak, *_ = [item for t in stats for item in (t if isinstance(t, tuple) else [t])]
    
    return final_score

# Main execution
if __name__ == '__main__':
    # Input data with meaningful names
    raw_dataset = [
        {'name': 'alpha', 'value': 42},
        {'name': 'beta', 'value': 38},
        {'name': 'gamma', 'value': 56},
        {'name': 'delta', 'value': 41},
        {'name': 'epsilon', 'value': 63}
    ]
    
    # Weights used in actual computation
    feature_weights = [0.9, 1.3, 1.1]
    
    # Distractor variables
    baseline_metrics = [d['value'] for d in raw_dataset]
    sorted_names = sorted([d['name'] for d in raw_dataset], key=len)
    name_length_map = dict(zip(sorted_names, [len(n) for n in sorted_names]))
    
    # Unused set operations (red herring)
    unique_chars = set()
    for entry in raw_dataset:
        unique_chars.update(set(entry['name']))
    charset_size = len(unique_chars)
    
    # Critical call buried in noise
    is_invalid = validate_dataset(raw_dataset)
    entropy = calculate_entropy(baseline_metrics)
    
    # Key statement
    final_score = calculate_final_score(raw_dataset, feature_weights)
    
    # Print required output
    print(f"Target result: {final_score}")