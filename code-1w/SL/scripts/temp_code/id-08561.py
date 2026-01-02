import math

# Simulated user interaction data for a cognitive task platform
def generate_user_data():
    raw_inputs = [3.2, 4.1, 2.8, 5.0, 3.6, 4.4, 2.9]
    response_times = [1.2, 0.9, 1.5, 0.7, 1.1, 0.8, 1.3]
    accuracy_flags = [True, True, False, True, True, False, True]
    
    # Irrelevant transformation (distractor)
    transformed = [math.log(x) * 1.5 for x in response_times]
    offset = sum(transformed) / len(transformed)

    user_data = []
    for i in range(len(raw_inputs)):
        entry = {
            'input_val': raw_inputs[i],
            'rt': response_times[i],
            'acc': accuracy_flags[i],
            'weighted_rt': response_times[i] * 1.5 if accuracy_flags[i] else response_times[i] * 2.0,
            'priority': int(4 + math.sin(i))  # Constant across all, irrelevant
        }
        user_data.append(entry)
    
    # Dead code path (never executed)
    if False:
        user_data.clear()
        for _ in range(3):
            user_data.append({'input_val': 0, 'rt': 0, 'acc': False})
    
    return user_data

# System calibration weights (simulated)
def get_system_weights():
    base_weights = {'w1': 0.4, 'w2': 0.35, 'w3': 0.25}
    adjustment_factor = 1.05
    
    # Red herring: unused weight set
    deprecated_weights = {'w1': 0.5, 'w2': 0.3, 'w3': 0.2}
    temp_cache = {k: v * adjustment_factor for k, v in base_weights.items()}
    
    # Complex but irrelevant computation
    checksum = 0
    for w in temp_cache.values():
        checksum += int(w * 100) % 7
    checksum = (checksum * 1.03) % 1.0
    
    # Actual returned weights (used later)
    final_weights = {k: v * adjustment_factor for k, v in base_weights.items()}
    return final_weights

# Auxiliary function: computes efficiency score
def compute_efficiency(entries):
    total_time = sum(e['rt'] for e in entries)
    valid_count = sum(1 for e in entries if e['acc'])
    if valid_count == 0:
        return 0.0
    avg_time_per_valid = total_time / valid_count
    efficiency = (valid_count / len(entries)) * (5.0 / avg_time_per_valid)
    return round(efficiency, 4)

# Auxiliary: calculates input consistency using set operations
def calculate_consistency(entries):
    rounded_values = {round(e['input_val']) for e in entries}
    all_values = {round(e['input_val'], 1) for e in entries}
    
    # Set difference to find precision variation (only some are integers)
    precise_drift = all_values - rounded_values
    
    # Measure dispersion
    min_val = min(rounded_values)
    max_val = max(rounded_values)
    range_penalty = max_val - min_val
    
    # Consistency score: higher if less drift and smaller range
    if len(precise_drift) > 2:
        return 0.6 - (range_penalty * 0.1)
    else:
        return 0.8 - (range_penalty * 0.05)

# Core aggregation logic
def aggregate_performance(user_data, weights):
    # Step 1: Compute base metrics
    raw_scores = [e['input_val'] for e in user_data]
    base_average = sum(raw_scores) / len(raw_scores)
    
    # Step 2: Apply dynamic clamping based on median
    sorted_vals = sorted(raw_scores)
    mid = len(sorted_vals) // 2
    median_val = sorted_vals[mid] if len(sorted_vals) % 2 else (sorted_vals[mid-1] + sorted_vals[mid]) / 2
    
    clamped = []
    for v in raw_scores:
        if v < median_val - 1.0:
            clamped.append(median_val - 1.0)
        elif v > median_val + 1.0:
            clamped.append(median_val + 1.0)
        else:
            clamped.append(v)
    
    # Step 3: Weighted components
    comp_a = base_average * weights['w1']
    comp_b = compute_efficiency(user_data) * weights['w2']
    comp_c = calculate_consistency(user_data) * weights['w3']
    
    # Step 4: Conditional boost for high accuracy streaks
    acc_streak = 0
    max_streak = 0
    for e in user_data:
        if e['acc']:
            acc_streak += 1
            if acc_streak > max_streak:
                max_streak = acc_streak
        else:
            acc_streak = 0
    
    streak_bonus = 0.1 if max_streak >= 3 else 0.0
    
    # Step 5: Aggregate with bonus
    preliminary_score = comp_a + comp_b + comp_c + streak_bonus
    
    # Step 6: Final adjustment using modular arithmetic (simulate calibration cycle)
    cycle_offset = len(user_data) % 4
    if cycle_offset == 0:
        final_adjustment = 0.95
    elif cycle_offset == 1:
        final_adjustment = 1.02
    elif cycle_offset == 2:
        final_adjustment = 0.98
    else:
        final_adjustment = 1.0
    
    # Step 7: Apply final adjustment
    adjusted_score = preliminary_score * final_adjustment
    
    # Step 8: Floor to two decimals (deterministic)
    final_score = math.floor(adjusted_score * 100) / 100
    
    # Irrelevant side calculation (distractor)
    phantom_score = 0
    for i, e in enumerate(user_data):
        phantom_score += (e['input_val'] * (i+1)) % (e['rt'] * 10)
    phantom_score = math.sqrt(phantom_score) if phantom_score > 0 else 0
    
    return final_score

# Main execution flow
if __name__ == "__main__":
    # Generate real data
    user_data = generate_user_data()
    
    # Retrieve system weights
    system_weights = get_system_weights()
    
    # Compute final performance score
    final_score = aggregate_performance(user_data, system_weights)
    
    # Output result
    print(f"Result: {final_score}")