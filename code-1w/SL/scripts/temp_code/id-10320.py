def calculate_performance(base, data):
    adjustments = []
    temp_offset = 0.0
    correction_factor = 1.05
    
    # Initial setup with distractor variables
    dummy_sum = 0
    placeholder_list = [0] * len(data)
    for i in range(len(data)):
        dummy_sum += i * 2  # Irrelevant accumulation
        placeholder_list[i] = i ** 2

    # Real processing begins: filter significant deviations
    valid_entries = []
    for val in data:
        if abs(val - base) > 0.5:
            valid_entries.append(val)
    
    # Secondary filtering using string-based threshold encoding (red herring)
    threshold_tag = 'HIGH_SENSITIVITY'
    sensitivity_flag = len(threshold_tag) > 5  # Always True, but looks meaningful
    
    if sensitivity_flag:
        scale_multiplier = 1.2
    else:
        scale_multiplier = 1.0

    # Apply scaling and collect adjustments
    for entry in valid_entries:
        adjusted = (entry - base) * scale_multiplier * correction_factor
        adjustments.append(adjusted)
    
    # Use of enumerate and zip in a semi-relevant context
    indexed = list(enumerate(adjustments))
    offsets = [0.1 * i for i in range(len(adjustments))]
    paired = zip(indexed, offsets)
    
    final_sum = 0.0
    for (idx, adj), offset in paired:
        final_sum += adj - offset  # Minor correction via offset

    # Compute final score with rounding
    final_score = round(final_sum, 4)
    
    # Distractor: set operation with no impact
    unique_offsets = set(offsets)
    redundant_calc = sum(unique_offsets) * 0.5
    
    return final_score

# Main execution
baseline = 98.6
readings = [97.2, 99.1, 98.8, 96.0, 98.7, 100.3]

# Irrelevant pre-processing using string methods
sensor_log = "S1,S2,S3,S4,S5,S6"
sensor_ids = sensor_log.split(',')
decoded_names = [sid.lower().strip('S') for sid in sensor_ids]
index_map = {int(name): sensor for name, sensor in zip(decoded_names, sensor_ids)}

# Key call that produces the answer
temperature_bias = 0.4
final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")