import math

# Simulated sensor array data processing with diagnostic validation
def main():
    raw_readings = [3.2, 1.7, 4.8, 2.4, 9.1, 0.6, 5.5, 7.3, 6.0]
    calibration_offset = 0.3
    sensitivity_factor = 1.8
    baseline_ref = 2.0
    temp_cache = []
    cumulative_shift = 0.0
    adjusted_values = []
    
    # Irrelevant temperature simulation (distractor)
    for i in range(5):
        temp = (i * 1.5) + 20.0
        temp_cache.append(temp)
    
    # Apply sensitivity and offset (red herring - not used later)
    for val in raw_readings:
        shifted = (val * sensitivity_factor) + calibration_offset
        cumulative_shift += shifted
        adjusted_values.append(shifted)
    
    # Core signal filtering logic
    normalized = [x - baseline_ref for x in raw_readings]  # Center around baseline
    abs_normalized = [abs(x) for x in normalized]
    sorted_norm = sorted(abs_normalized, reverse=True)
    top_four_magnitude = sorted_norm[:4]
    avg_top_four = sum(top_four_magnitude) / 4
    
    # Threshold function using lambda (required feature)
    threshold_func = lambda x: x > (avg_top_four * 0.65)
    
    # Misleading secondary filter path (dead code branch)
    secondary_mask = []
    if len(raw_readings) > 10:
        for x in raw_readings:
            secondary_mask.append(x > 5.0)
    else:
        # This block runs but result unused
        dummy_calc = 0
        for x in raw_readings:
            dummy_calc += math.sqrt(x) * 0.1

    # Actual filtering based on magnitude deviation
    deviation_flags = [threshold_func(abs(x - baseline_ref)) for x in raw_readings]
    filtered_data = [raw_readings[i] for i in range(len(raw_readings)) if deviation_flags[i]]
    
    # Decoy statistical analysis (irrelevant computations)
    mean_raw = sum(raw_readings) / len(raw_readings)
    variance = sum((x - mean_raw) ** 2 for x in raw_readings) / len(raw_readings)
    stdev = math.sqrt(variance)
    outlier_boundary = mean_raw + 2 * stdev
    
    # Unused string-based flag encoding (distractor with string method)
    flag_codes = ['A', 'B', 'C']
    encoded_flags = ''.join([f'{code.lower()}_flag,' for code in flag_codes]).strip(',')
    parsed_labels = encoded_flags.replace('_flag', '').split(',')
    
    # Critical diagnostic processor
    def process_readings(data, threshold_fn):
        if not data:
            return 0.0
        
        # Transform via lambda mapping
        processed = list(map(lambda z: z ** 1.5, data))
        total_energy = sum(processed)
        count_weight = len(data) * 10
        
        # Additional irrelevant recursion (decoy)
        def recursive_dampen(n):
            if n <= 1:
                return n
            return recursive_dampen(n - 1) * 0.95
        
        dummy_damped = recursive_dampen(5)  # Computed but not used
        
        # Final computation
        stability_index = total_energy / (count_weight + 1)
        adjustment_curve = math.log(stability_index + 1)
        return round(stability_index * adjustment_curve, 6)

    final_diagnostic = process_readings(filtered_data, threshold_func)
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()