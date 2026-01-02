def calculate_system_efficiency():
    components = ['valve', 'pump', 'sensor', 'actuator', 'regulator']
    base_ratings = [85, 92, 78, 88, 90]
    stress_factors = [1.05, 0.98, 1.12, 1.01, 0.97]
    maintenance_offsets = [5, -3, 10, 0, -2]

    # Irrelevant auxiliary data
    legacy_modes = {'auto': 1, 'manual': 0, 'hybrid': 2}
    calibration_cache = {i: i**2 for i in range(6)}

    efficiency_log = []
    total_efficiency = 0
    peak_found = False

    # Secondary distractor variables
    temp_buffer = [0] * len(components)
    debug_trace = []

    for idx, (name, rating) in enumerate(zip(components, base_ratings)):
        stress = stress_factors[idx]
        offset = maintenance_offsets[idx]

        # Primary efficiency calculation
        adjusted_rating = (rating + offset) * stress

        # Distractor: complex but unused logic
        lambda_transform = lambda x, s: x * s if x > 80 else x + s
        transformed = lambda_transform(rating, stress)
        temp_buffer[idx] = transformed ** 0.5  # Not used later

        # Real accumulation
        if adjusted_rating > 95 and not peak_found:
            efficiency_log.append(adjusted_rating * 0.9)
            peak_found = True
            break
        elif adjusted_rating >= 85:
            efficiency_log.append(adjusted_rating * 1.05)
        else:
            efficiency_log.append(adjusted_rating)

        # Distractor: dead code path with early return
        if name == 'sensor' and rating < 80:
            debug_trace.append('Critical: Low sensor rating')
            return -1  # Never reached due to data

        # Accumulate total (only up to break or full loop)
        total_efficiency += adjusted_rating

    else:
        # Default fallback
        total_efficiency = sum(temp_buffer)

    # Final adjustment unrelated to main logic
    outlier_filter = list(filter(lambda x: x > 70, efficiency_log))
    smoothing_factor = len(outlier_filter) / len(efficiency_log) if efficiency_log else 1

    total_efficiency *= smoothing_factor
    total_efficiency = round(total_efficiency, 4)

    print(f"Result: {total_efficiency}")

    return total_efficiency

result = calculate_system_efficiency()