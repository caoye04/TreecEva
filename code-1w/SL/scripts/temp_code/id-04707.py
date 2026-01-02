import math

# Simulated sensor network diagnostic system
def collect_diagnostics():
    raw_readings = [145, 128, 203, 99, 176, 152, 111, 189, 134, 167]
    calibration_offset = 17
    gain_factor = 1.08
    temp_buffer = [0] * 5  # Unused buffer - red herring

    # Irrelevant temperature simulation (distractor)
    ambient_temps = [22.1, 23.5, 21.8, 24.0, 22.7]
    avg_temp = sum(ambient_temps) / len(ambient_temps)
    temp_impact = avg_temp * 0.3

    # Actual signal processing begins
    processed_data = []
    for val in raw_readings:
        corrected = (val + calibration_offset) * gain_factor
        if corrected > 150:
            processed_data.append(int(corrected))

    # Dead code path - never executed due to logic above
    if len(temp_buffer) > 10:
        fallback_mode = True
        processed_data = [x * 2 for x in raw_readings]

    # Set up threshold logic
    base_threshold = 165
    dynamic_adjustment = len(processed_data) * 2.3
    threshold_set = {int(base_threshold + i * dynamic_adjustment / 4) for i in range(4)}

    # Redundant set operation (distractor)
    decoy_set = {x % 50 for x in raw_readings}
    decoy_analysis = len(decoy_set.intersection({12, 25, 37}))

    # Unused recursive function - misleading complexity
    def explore_combinations(values, index=0, current=[]):
        if index == len(values):
            return [current[:]]
        result = []
        result.extend(explore_combinations(values, index + 1, current))
        result.extend(explore_combinations(values, index + 1, current + [values[index]]))
        return result

    # Linear search with conditional filtering
    critical_count = 0
    for reading in processed_data:
        if reading > 170:
            critical_count += 1

    # Auxiliary calculation (irrelevant to final result)
    mean_reading = sum(processed_data) / len(processed_data)
    variance = sum((x - mean_reading) ** 2 for x in processed_data) / len(processed_data)
    stability_score = math.exp(-variance / 1000)  # Unused metric

    # Core analysis function (closure)
    def analyze_readings(data, thresholds):
        count_above = 0
        max_value = float('-inf')
        min_value = float('inf')

        for item in data:
            if item > max_value:
                max_value = item
            if item < min_value:
                min_value = item

        span = max_value - min_value

        # Determine how many thresholds are exceeded
        exceeded = 0
        for t in thresholds:
            if span > t:
                exceeded += 1

        # Final computation chain
        adjustment = 0
        if exceeded == 0:
            adjustment = -50
        elif exceeded == 1:
            adjustment = -20
        elif exceeded == 2:
            adjustment = 15
        elif exceeded >= 3:
            adjustment = 40

        # Key result built from multi-step reasoning
        base_result = len(data) * 100 + exceeded * 10
        final_score = base_result + adjustment

        # Secondary validation path (dead end)
        if span < 50:
            secondary_path = True
            final_score = int(math.sqrt(final_score))  # Never reached

        return final_score

    # Execute main analysis
    final_diagnostic = analyze_readings(processed_data, threshold_set)
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    
    return final_diagnostic

# Entry point
result = collect_diagnostics()