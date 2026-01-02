def analyze_sensor_data(raw_readings, thresholds):
    # Simulate preprocessing with distractions
    processed = [x * 1.05 for x in raw_readings if x > 0]
    adjusted = [round(x, 2) for x in processed]

    # Irrelevant transformation chain (dead path)
    inverted = [1 / x for x in adjusted if x != 0]
    normalized = [x / max(adjusted) for x in adjusted]
    capped = [min(x, 100) for x in normalized]

    # Decoy statistical calculations
    mean_val = sum(adjusted) / len(adjusted) if adjusted else 0
    variance_proxy = sum((x - mean_val) ** 2 for x in adjusted) / len(adjusted) if adjusted else 0
    outlier_threshold = mean_val + 2 * (variance_proxy ** 0.5)

    # Real logic hidden among noise
    clipped_readings = [x for x in raw_readings if x <= outlier_threshold]  # Filtering step
    scaled_readings = [x * 2 for x in clipped_readings]  # Actual scaling

    # String manipulation red herring (no effect on result)
    status_flags = ['OK' if x > 50 else 'LOW' for x in raw_readings]
    flag_summary = ''.join(status_flags).lower()
    analysis_code = flag_summary.title().replace('Ok', 'Pass')

    # Multiple assignments and tuple unpacking distraction
    a, b = 10, 20
    a, b = b, a  # Swap - irrelevant
    meta_info = (a * 2, b // 2, len(flag_summary))
    _, _, version = meta_info

    # Core computation embedded in list operations
    candidate_values = [x for x in scaled_readings if x > thresholds[0]]
    filtered_directions = [1 if x % 2 == 0 else -1 for x in raw_readings]
    modulated = [candidate_values[i] * filtered_directions[i % len(filtered_directions)] 
                 for i in range(len(candidate_values))]

    # Key slicing operation (relevant but masked by context)
    relevant_slice = modulated[::2] if len(modulated) > 5 else modulated[1::2]

    # Final filtering based on secondary threshold
    secondary_filtered = [x for x in relevant_slice if abs(x) < thresholds[1]]

    # Critical assignment - target of question
    relevant_values = [abs(x) for x in secondary_filtered if x != 0]
    filtered_sum = sum(relevant_values)

    # Unused but plausible-looking aggregations (distractors)
    product_of_positives = 1
    for x in relevant_values:
        if x > 10:
            product_of_positives *= x
    entropy_like_metric = sum(-x/filtered_sum * (x/filtered_sum).__log__ for x in relevant_values if x > 0) if filtered_sum != 0 else 0

    # Output the required result
    print(f"Result: {filtered_sum}")
    return filtered_sum

# Simulate execution with seeded input
import math
math.inf = float('inf')
input_readings = [45, -12, 67, 83, 29, 91, 55, 14, 77, 38]
external_thresholds = [50, 200]

# Trigger function call
result_value = analyze_sensor_data(input_readings, external_thresholds)