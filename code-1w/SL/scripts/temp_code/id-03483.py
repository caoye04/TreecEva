def process_inventory(items, thresholds):
    counts = {k: 0 for k in thresholds}
    surplus_flags = []
    temp_accumulator = 0

    for idx, (name, value) in enumerate(items):
        temp_accumulator += idx * 0.1  # Distractor: not used later
        if value > thresholds.get('high', 100):
            counts['high'] += 1
            surplus_flags.append(True)
        elif value > thresholds.get('medium', 50):
            counts['medium'] += 1
            surplus_flags.append(False)
        else:
            counts['low'] += 1

    filtered_keys = [k for k, v in counts.items() if v > 0]
    return counts, filtered_keys, surplus_flags


def normalize_weights(raw_weights, mode='linear'):
    total = sum(raw_weights)
    if total == 0:
        return raw_weights
    normalized = [w / total for w in raw_weights]
    
    # Simulate dead code branch (never taken due to input)
    if mode == 'exponential':
        normalized = [w ** 2 for w in normalized]
        s = sum(normalized)
        normalized = [w / s for w in normalized]

    return normalized


def calculate_ranking(elements, importance):
    ranking = 0
    element_dict = {i: val for i, val in enumerate(elements)}
    reverse_lookup = {v: k for k, v in element_dict.items()}  # Unused but plausible

    sorted_vals = sorted(elements, reverse=True)
    position_ranks = {val: rank for rank, val in enumerate(sorted_vals)}

    for val in elements:
        index = reverse_lookup[val]
        bonus = 1 if val > 75 else 0  # Small boost for high values
        ranking += position_ranks[val] * importance[index] + bonus

    return ranking

# Main execution
if __name__ == '__main__':
    inventory = [
        ('gear', 120),
        ('sprocket', 65),
        ('cog', 45),
        ('piston', 90),
        ('spring', 30)
    ]

    limits = {'high': 100, 'medium': 50, 'low': 0}
    weights = [0.1, 0.3, 0.1, 0.4, 0.1]

    # Step 1: Process inventory with distractor outputs
    item_counts, valid_categories, flags = process_inventory(inventory, limits)
    
    # Irrelevant sorting (simulates data prep that isn't used)
    sorted_categories = sorted(valid_categories, key=lambda x: len(x))

    # Step 2: Normalize weights (necessary for calculation)
    normalized_importance = normalize_weights(weights)

    # Extract relevant values for ranking
    values_only = [val for _, val in inventory]

    # Introduce red herring computation
    avg_value = sum(values_only) / len(values_only)
    adjusted_avg = avg_value * 0.95 if avg_value > 70 else avg_value * 1.05

    # Track unused stats
    outlier_count = sum(1 for v in values_only if v < 40 or v > 110)

    # Core logic: calculate final score based on weighted ranking and position
    final_score = calculate_ranking(values_only, normalized_importance)

    # Additional distraction: simulate logging
    debug_info = []
    for i, v in enumerate(values_only):
        debug_info.append(f"Item{i}: {v}, weight={normalized_importance[i]:.3f}")

    print(f"Result: {final_score}")