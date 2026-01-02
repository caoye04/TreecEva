from collections import defaultdict, Counter

def analyze_sequence_data(sequence):
    frequency_map = defaultdict(int)
    for item in sequence:
        frequency_map[item] += 1

    # Misleading computation: unused later
    rare_elements = [k for k, v in frequency_map.items() if v < 2]
    total_skips = sum(1 for x in rare_elements if x % 2 == 0)

    # Relevant transformation
    normalized = [x % 7 for x in sequence]
    mod_freq = Counter(normalized)

    return mod_freq

def validate_bounds(data, threshold=5):
    above_threshold = 0
    for val in data.values():
        if val > threshold:
            above_threshold += 1
    # Dead code path (never used)
    if above_threshold > 10:
        return False
    return True

def compute_aggregate_score(items):
    base_score = 0
    adjustment_factor = 0.0

    for i, (idx, val) in enumerate(zip(range(len(items)), items)):
        if i % 3 == 0:
            base_score += val * 2
        elif i % 3 == 1:
            base_score -= val
        else:
            base_score += (val + i) // 2

    temp_result = base_score * 1.5  # Intermediate distraction
    adjustment_factor = abs((base_score % 4) - 1.5)

    return int(temp_result - adjustment_factor)

def calculate_performance_rating():
    raw_data = [12, 7, 3, 8, 14, 6, 9, 11, 4, 5, 13, 2, 10]
    
    # Step 1: Analyze modulo distribution
    mod_analysis = analyze_sequence_data(raw_data)
    
    # Step 2: Validate structural constraint (always passes)
    is_valid = validate_bounds(mod_analysis, threshold=5)
    
    # Step 3: Extract values for scoring
    extracted_values = [v for k, v in sorted(mod_analysis.items()) if k in [0, 1, 2, 4, 6]]
    
    # Step 4: Compute primary score
    primary = compute_aggregate_score(extracted_values)
    
    # Step 5: Apply conditional multiplier based on set properties
    unique_mods = set(mod_analysis.keys())
    expected_set = set(range(7))
    missing_count = len(expected_set - unique_mods)
    
    # Step 6: Secondary adjustment using modular arithmetic
    secondary_adjust = (primary + 3) % 17
    if missing_count == 0:
        secondary_adjust *= 2
    else:
        secondary_adjust += 5
    
    # Step 7: Final integration with string-based key derivation (distractor)
    status_key = ''.join([str(x) for x in sorted(unique_mods)[:3]])
    key_numeric = sum(int(d) for d in status_key) if status_key.isdigit() else 0
    
    # Final score calculation
    final_score = primary + secondary_adjust - key_numeric
    
    # Output required result
    print(f"Result: {final_score}")
    return final_score

# Execute function
calculate_performance_rating()