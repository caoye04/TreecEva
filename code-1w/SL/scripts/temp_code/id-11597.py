import math

# Irrelevant helper function (dead code path)
def unused_utility(x):
    return (x ** 2 + 3 * x + 1) % 7

# Misleading data transformation chain
def transform_input(raw):
    temp_a = [x * 1.5 for x in raw if x > 5]
    temp_b = [y for y in temp_a if y < 20]
    offset = sum(temp_b) / len(temp_b) if temp_b else 0
    return [z - offset for z in temp_a], offset

# Decoy metric calculation with misleading intermediate result
def decoy_analysis(data):
    count_valid = len([x for x in data if x >= 0])
    fake_metric = (count_valid * 1.75) ** 1.1
    # This function looks important but isn't used in final logic
    return fake_metric

# Conditional expression-based filtering and scoring
def filter_relevant(entries, threshold):
    return [e for e in entries if e > threshold] if threshold >= 0 else [abs(e) for e in entries]

# Core evaluation logic with nested conditions and modular arithmetic
def compute_weighted_index(values):
    base_sum = 0
    weight_sequence = [1, 3, 2, 1, 3, 2]  # repeating pattern
    
    for i, val in enumerate(values):
        # Apply modular arithmetic to simulate cyclical weighting
        effective_weight = weight_sequence[i % len(weight_sequence)]
        adjusted_val = (val * effective_weight) % 13
        base_sum += adjusted_val
    
    # Introduce conditional scaling based on set properties
    unique_count = len(set(values))
    scaling_factor = 2.5 if unique_count >= 4 else 1.8
    
    # Use conditional expression to decide correction term
    correction = 7 if base_sum % 5 == 0 else (-3 if base_sum > 30 else 0)
    
    return (base_sum * scaling_factor) + correction

# Character counting side computation (irrelevant)
def count_chars_in_repr(obj_list):
    total = 0
    for item in obj_list:
        total += len(repr(item))
    return total  # Never used

# Main performance evaluator combining multiple concepts
def evaluate_performance(metrics):
    # Step 1: Filter relevant metrics using dynamic threshold
    threshold = 6.0 if len(metrics) > 5 else 4.5
    filtered = filter_relevant(metrics, threshold)
    
    # Step 2: Transform via irrelevant function that returns unused offset
    processed_data, _ = transform_input(filtered)
    
    # Step 3: Extract key values using set operations to remove duplicates
    clean_values = list(set([int(x) for x in processed_data if x.is_integer()]))
    
    # Step 4: Compute primary index using weighted algorithm
    raw_index = compute_weighted_index(clean_values)
    
    # Step 5: Apply conditional bonus based on modulo condition
    bonus = 12 if len(clean_values) % 4 == 0 and raw_index > 20 else 0
    
    # Step 6: Final adjustment using trigonometric red herring (cosine of constant)
    # This looks sophisticated but contributes nothing due to fixed input
    phantom_boost = math.cos(math.pi / 3) * 0  # Always zero
    
    # Step 7: Assemble final score through layered logic
    preliminary = raw_index + bonus + phantom_boost
    
    # Step 8: Apply final clamp and rounding (answer emerges here)
    final_score = round(preliminary, 2) if preliminary > 0 else 0
    
    return final_score

# --- Execution Block ---

# Simulated input data (real signal)
data_stream = [4, 7, 8, 12, 3, 9, 11]

# Irrelevant preprocessing (distractor)
sorted_snapshot = sorted(data_stream, reverse=True)
duplicate_check = len(data_stream) != len(set(data_stream))

# Unused statistical measures (red herrings)
mean_value = sum(data_stream) / len(data_stream)
variance_proxy = sum((x - mean_value) ** 2 for x in data_stream)

# Key data structure used in actual logic
metric_data = [x * 1.1 for x in data_stream]  # Feeds into evaluate_performance

# Call to critical function containing answer
final_score = evaluate_performance(metric_data)

# Output required result
print(f"Result: {final_score}")