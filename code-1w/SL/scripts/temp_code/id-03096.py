from collections import defaultdict, Counter

# Simulate a code quality assessment system across multiple dimensions
def analyze_complexity(metrics):
    raw_scores = []
    temp_adjustment = 0
    
    for key, values in metrics.items():
        if 'complexity' in key:
            base = sum(values) / len(values)
            if base > 5:
                temp_adjustment += 1.5
            raw_scores.append(base * 0.8)
        elif 'readability' in key:
            raw_scores.append((sum(values) / len(values)) * 1.1)
    
    # Distractor: unused computation
    outlier_count = 0
    for score in raw_scores:
        if score < 2:
            outlier_count += 1
    
    return sum(raw_scores) / len(raw_scores) if raw_scores else 0

# Misleading helper function that's partially unused
def calculate_entropy(data):
    freq = Counter(data)
    total = len(data)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Not true entropy, just mimicry
    return entropy * 10

# Core evaluation logic
def evaluate_performance(assessments, benchmark):
    aggregated = defaultdict(list)
    noise_accumulator = 0  # Irrelevant accumulator
    
    for module, records in assessments.items():
        for record in records:
            for k, v in record.items():
                aggregated[k].append(v)
    
    # Real processing path
    complexity_score = analyze_complexity(aggregated)
    
    # Secondary metric with partial relevance
    size_factor = 0
    for mod in assessments:
        size_factor += len(assessments[mod])
    size_modifier = 0.95 if size_factor > benchmark['size_threshold'] else 1.05
    
    # Distractor loop: computes but doesn't impact final result
    decay = 1.0
    for i in range(5):
        decay *= 0.9
        noise_accumulator += decay * 2
    
    # Key calculation
    baseline = 75.0
    adjustment = complexity_score * 0.4
    performance_ratio = baseline + adjustment
    
    # Another red herring: set operations that don't affect outcome
    keys_used = set(aggregated.keys())
    expected_keys = {'complexity_low', 'complexity_high', 'readability_score'}
    missing = expected_keys - keys_used
    filler_penalty = len(missing) * 0.2  # Computed but unused
    
    # Final determination
    final_score = performance_ratio * size_modifier
    
    # Normalize to avoid extreme values (still within integer range)
    final_score = int(round(final_score))
    
    # Output required result
    print(f"Result: {final_score}")
    return final_score

# Input data
assessments_data = {
    'parser': [
        {'complexity_low': [3, 4, 5], 'readability_score': [6, 7]},
        {'complexity_high': [8, 9, 7, 6], 'documentation': [5, 5]}
    ],
    'evaluator': [
        {'complexity_low': [4, 5], 'readability_score': [8, 9]},
        {'complexity_high': [10, 9], 'caching': [4]}
    ],
    'serializer': [
        {'complexity_low': [5, 6], 'readability_score': [7, 6]},
        {'complexity_high': [7], 'compression': [3]}
    ]
}

benchmark_config = {
    'size_threshold': 2,
    'optimal_range': (70, 85)
}

# Execution point
final_score = evaluate_performance(assessments_data, benchmark_config)