def calculate_final_score(raw_data, limits):
    # Preprocessing: Normalize data using a lambda
    normalized = list(map(lambda x: x / max(raw_data), raw_data))

    # Track state with auxiliary variables (some are distractions)
    cumulative = 0
    peak_magnitude = 0
    adjustment_factor = 0.85
    temp_buffer = []
    ignored_outliers = []

    # Secondary computation: detect significant values
    for i, val in enumerate(normalized):
        if val > limits[1]:
            temp_buffer.append(val * adjustment_factor)
        elif val < limits[0]:
            ignored_outliers.append(val)  # collected but not used
        else:
            cumulative += val ** 2

    # Another loop to simulate signal smoothing (partially relevant)
    smoothed = []
    for i in range(1, len(temp_buffer) - 1):
        smoothed.append((temp_buffer[i-1] + temp_buffer[i] + temp_buffer[i+1]) / 3)

    # Distractor: complex but unused calculation
    noise_estimate = sum([abs(smoothed[i] - smoothed[i+1]) for i in range(len(smoothed)-1)]) if smoothed else 0.0
    spectral_power = noise_estimate * 1.5 if noise_estimate > 0.1 else 0.0

    # Core logic: combine cumulative baseline and smoothed contribution
    bonus_component = sum(smoothed) * 10 if smoothed else 0
    base_score = int(cumulative * 100)

    # Final aggregation
    final_score = base_score + bonus_component

    # Irrelevant post-processing
    diagnostic_report = {"entries": len(raw_data), "ignored": len(ignored_outliers)}
    return final_score

# Main execution context
if __name__ == '__main__':
    # Input setup
    data = [12, 45, 67, 23, 89, 34, 56, 91, 11, 6]
    thresholds = [0.15, 0.75]  # normalize and filter based on these

    # Key statement
    final_score = calculate_final_score(data, thresholds)
    
    # Print result as required
    print(f"Target result: {final_score}")