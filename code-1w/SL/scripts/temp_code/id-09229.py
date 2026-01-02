def preprocess_data(raw):
    # Irrelevant preprocessing steps (distractors)
    cleaned = [x for x in raw if isinstance(x, int) and x > 0]
    normalized = [x / max(cleaned) for x in cleaned] if cleaned else [0]
    stats = {'sum': sum(normalized), 'count': len(normalized)}
    
    # Dead code path - never executed due to logic
    if len(normalized) > 100:
        return [round(x, 3) for x in normalized]
    else:
        pass  # Placeholder distraction

    # Actual relevant transformation
    transformed = []
    for i, val in enumerate(normalized):
        if i % 2 == 0:
            transformed.append(val * 2)
        else:
            transformed.append(val ** 2)
    return transformed


def compute_entropy(values):
    # Decoy function: looks important but unused in final calculation
    import math
    total = sum(values)
    if total == 0:
        return 0.0
    probs = [v / total for v in values]
    entropy = -sum(p * math.log2(p) for p in probs if p > 0)
    return round(entropy, 6)


def bitwise_diagnostic(arr):
    # Misleading bit manipulation - distracts from main logic
    result = 0
    for x in arr:
        result ^= int(x * 100) & 0xFF
    return result


def calculate_final_score(dataset, config):
    # Core logic embedded with distractions
    
    # Irrelevant intermediate variables
    temp_buffer = []
    for item in dataset:
        temp_buffer.append(item * 1.5 + 2)  # Not used later

    # Key processing begins
    base_scores = [x * config.get(f'weight_{i}', 1) for i, x in enumerate(dataset)]
    
    # Accumulation with early termination red herring
    running_total = 0
    for idx, score in enumerate(base_scores):
        adjustment = 0
        if idx == 2:
            adjustment = -5  # Specific correction
        elif idx == 4:
            break  # Early break that seems impactful but isn't triggered

        running_total += score + adjustment
    
    # Secondary adjustment using zip and enumerate (required features)
    multipliers = [1.1, 0.9, 1.0, 1.2]
    for i, (val, mult) in enumerate(zip(base_scores[:4], multipliers)):
        if i % 2 == 1:
            running_total += val * (mult - 1)

    # Final nonlinear transformation
    final_score = int(running_total ** 1.1)

    # Dead assignment - looks like it matters
    final_score += len(config) - len(str(running_total))

    return final_score

# Main execution block
if __name__ == '__main__':
    # Input data with hidden structure
    raw_input = [10, 20, 30, 40, 50, 'ignore', None, 60]
    weights = {'weight_0': 2, 'weight_1': 1, 'weight_2': 3, 'weight_3': 0.5, 'extra': 99}

    # Irrelevant data structures
    log_entries = [{'step': 'init', 'value': 100}, {'step': 'fail', 'value': 0}]
    metadata_cache = {k: v for k, v in zip(['a','b','c'], [1,2,3])}  # Unused

    # Real pipeline
    processed = preprocess_data(raw_input)
    
    # Diagnostic calls that don't affect outcome (red herrings)
    _ = compute_entropy(processed)
    _ = bitwise_diagnostic(processed)
    
    # Critical statement
    final_score = calculate_final_score(processed, weights)
    
    # Output result as required
    print(f"Result: {final_score}")