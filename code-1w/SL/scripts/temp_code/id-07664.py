def calculate_final_score(raw_data, limit):
    # Preprocess: filter and transform
    processed = [x ** 0.5 for x in raw_data if x > 0]
    temp_sum = sum(processed)
    
    # Irrelevant statistical distraction
    mean_val = temp_sum / len(processed) if processed else 0
    variance_proxy = sum((x - mean_val) ** 2 for x in processed) / len(processed) if processed else 0

    # String-based flag extraction (semi-relevant)
    status_str = "valid_high" if temp_sum > 100 else "valid_low"
    flag_code = status_str.split('_')[-1].upper()  # e.g., 'HIGH'

    # Core logic masked by distractions
    clipped = [min(x, limit) for x in processed]
    adjusted = [x * 1.1 if flag_code == 'HIGH' else x * 0.9 for x in clipped]
    
    # Red herring: unused transformation
    inverted_map = {i: round(1.0 / (x + 1), 4) for i, x in enumerate(raw_data)}

    # Conditional aggregation with slicing twist
    window = adjusted[::2] if len(adjusted) > 5 else adjusted[1:]  # every other or skip first
    aggregate = sum(window)

    # Final adjustment based on string property
    penalty_factor = 0.95 if 'H' in flag_code else 1.0
    score = aggregate * penalty_factor

    # Dead code: never used
    debug_snapshot = {"raw_len": len(raw_data), "post_filter": len(processed)}

    return int(round(score))

# Input setup
sensor_readings = [16, 25, 9, 64, 36, 49, -4, 81, 100]
threshold = 8.5

# Key execution point
final_score = calculate_final_score(sensor_readings, threshold)

print(f"Result: {final_score}")