def analyze_outliers(values, limit):
    """Identify outlier values above limit using set operations."""
    upper_bound = limit * 1.5
    lower_bound = limit * 0.5
    valid_range = set(range(int(lower_bound), int(upper_bound) + 1))
    data_points = set(values)
    outliers = data_points - valid_range
    return len(outliers)


def accumulate_metrics(records):
    """Accumulate weighted scores with lambda-based transformations."""
    weights = [0.8, 1.2, 0.9, 1.1]
    weighted_sum = 0.0
    for i, record in enumerate(records):
        transform = lambda x, w: round(x * w, 3)
        weighted_sum += transform(record, weights[i % len(weights)])
    
    # Distractor: unused accumulation
    square_accum = sum(r**2 for r in records if r > 50)
    avg = sum(records) / len(records) if records else 0
    
    return weighted_sum


def recursive_filter(items, depth=0):
    """Recursively filter items below median (simple recursion)."""
    if depth >= 2 or len(items) <= 1:
        return items
    
    mid = sum(items) / len(items)
    filtered = [x for x in items if x >= mid]
    
    # Distractor: irrelevant transformation
    inverted = [100 - x for x in items]
    inverted_sum = sum(inverted)
    
    return recursive_filter(filtered, depth + 1)


def calculate_final_score(raw_data, threshold):
    """Compute final score combining multiple reasoning paths."""
    # Step 1: Filter relevant entries
    filtered_data = [x for x in raw_data if x >= threshold // 2]
    
    # Step 2: Analyze outliers (set operation)
    outlier_count = analyze_outliers(filtered_data, threshold)
    
    # Step 3: Apply recursive filtering
    stable_subset = recursive_filter(filtered_data)
    
    # Step 4: Accumulate metrics using lambda
    base_score = accumulate_metrics(stable_subset)
    
    # Step 5: Apply penalty logic
    penalty_factor = 0.95 if outlier_count > 0 else 1.0
    adjusted_score = base_score * penalty_factor
n    
    # Step 6: Final adjustment with distractor variables
    temp_offset = sum([i*i for i in range(outlier_count)])  # Not used
    debug_trace = {'outliers': outlier_count, 'stable_len': len(stable_subset)}
    
    final_score = int(round(adjusted_score))
    return final_score

# Main execution
raw_input = [45, 70, 52, 81, 47, 90, 50, 60, 58]
threshold = 60
final_score = calculate_final_score(raw_input, threshold)
print(f"Target result: {final_score}")