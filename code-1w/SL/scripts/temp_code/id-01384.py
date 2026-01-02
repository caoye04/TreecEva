def analyze_text_patterns(input_str):
    # Irrelevant text analysis with distracting computations
    char_count = len(input_str)
    upper_case_count = sum(1 for c in input_str if c.isupper())
    lower_case_count = sum(1 for c in input_str if c.islower())
    digit_count = sum(1 for c in input_str if c.isdigit())
    
    # Distractor: unused transformation
    reversed_cleaned = input_str.strip().replace(' ', '_')[::-1].lower()
    
    # Semi-relevant metric
    alpha_ratio = (upper_case_count + lower_case_count) / max(char_count, 1)
    
    return alpha_ratio


def compute_data_metrics(data_list):
    # Accumulate various stats, some irrelevant
    total = sum(data_list)
    squared_sum = sum(x ** 2 for x in data_list)
    average = total / len(data_list) if data_list else 0
    variance_proxy = (squared_sum / len(data_list)) - (average ** 2) if data_list else 0
    
    # Dead computation path (not used later)
    normalized_vals = [round((x - average) / (variance_proxy ** 0.5 + 1e-8), 3) for x in data_list]
    
    # Return only relevant aggregated values
    return total, average


def evaluate_condition_set(flag_str, threshold):
    # String-based condition evaluation with red herring logic
    flag_parts = flag_str.lower().split('|')
    activation_score = 0
    
    for part in flag_parts:
        trimmed = part.strip()
        if 'critical' in trimmed:
            activation_score += 10
        elif 'enabled' in trimmed:
            activation_score += 5
        elif 'debug' in trimmed:
            # Misleading branch — looks important but not impactful
            temp_debug_val = len(trimmed) % 7
            activation_score += temp_debug_val * 0.1  # negligible effect
    
    meets_threshold = activation_score >= threshold
    return activation_score if meets_threshold else 0


def calculate_performance_rating():
    # Core input data
    raw_data_stream = "Error|CRITICAL|retry=3|timeout=15|DEBUG_MODE"
    sensor_readings = [12, 15, 14, 18, 16, 20, 13]
    config_flags = "normal|critical|enabled|verify"  # Used in evaluation
    
    # Step 1: Analyze text pattern (returns ratio, not directly used)
    text_consistency = analyze_text_patterns(raw_data_stream)
    
    # Step 2: Compute metrics from sensor data
    data_total, data_avg = compute_data_metrics(sensor_readings)
    
    # Step 3: Evaluate configuration flags
    activation_level = evaluate_condition_set(config_flags, threshold=12)
    
    # Step 4: Generate intermediate scores with distractions
    base_score = data_avg * 2.5
    adjustment_factor = 1.0
    
    if activation_level > 0:
        adjustment_factor += 0.3
        
        # Nested conditional with distractor variables
        if data_avg > 15:
            peak_correction = min(sensor_readings) / max(sensor_readings)
            adjusted_peak = (max(sensor_readings) - min(sensor_readings)) * peak_correction
            base_score += adjusted_peak

        # Unused bonus logic
        bonus_weights = [base_score * 0.1 for _ in range(3) if activation_level > 15]
    
    # Step 5: Apply final transformations
    preliminary_score = base_score * adjustment_factor
    
    # Step 6: Final normalization using string property (key dependency)
    token_count = len(raw_data_stream.split('='))  # splits: ['Error|CRITICAL|retry', '3|timeout', '15|DEBUG_MODE'] -> 3
    final_score = int(preliminary_score + (activation_level * token_count))
    
    # Output target result
    print(f"Result: {final_score}")
    return final_score

# Execute and capture result
calculate_performance_rating()