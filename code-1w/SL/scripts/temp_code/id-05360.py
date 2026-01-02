def calculate_final_score(raw_data):
    # Preprocessing: filter and transform data
    filtered = [x for x in raw_data if x > 0]
    squared = list(map(lambda x: x ** 2, filtered))
    shifted = [x >> 1 for x in squared]  # Bitwise shift as distraction

    # Irrelevant statistical computations (distractors)
    mean_val = sum(squared) / len(squared) if squared else 0
    max_val = max(squared) if squared else 0
    outlier_count = len([x for x in squared if x > 2 * mean_val])

    # Core logic: conditional scoring based on thresholds
    threshold = 100
    high_scores = [1 for x in squared if x >= threshold]
    low_scores = [0.5 for x in squared if x < threshold and x % 2 == 0]

    # Accumulate score using conditional expressions
    base_score = sum(high_scores) * 3 + sum(low_scores) * 2
    bonus = 5 if len(high_scores) > 2 else (2 if len(high_scores) == 2 else 0)
    penalty = 3 if any(x < 10 for x in filtered) else 0

    # Dummy state tracking (not used)
    history = []
    for val in filtered:
        status = 'valid' if val % 2 == 0 else 'odd'
        history.append(status)  # Dead code path

    # Final computation with nested conditionals
    adjustment = (lambda sc: sc * 1.1 if sc > 10 else sc * 0.9)(base_score)
    final_score = adjustment + bonus - penalty

    # Additional red herring variables
    normalized = [x / final_score for x in squared if final_score != 0]  # Depends on final_score
    entropy_proxy = -sum(x * __import__('math').log(x) for x in normalized if x > 0) if normalized else 0

    return int(final_score)

# Input data
data = [3, 4, 5, 6, 7]

# Execute and print result
final_score = calculate_final_score(data)
print(f"Target result: {final_score}")