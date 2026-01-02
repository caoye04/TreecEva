from itertools import compress, cycle

def main():
    # Simulate sensor readings over time (real data)
    raw_readings = [23.4, 25.1, 24.8, 26.7, 22.9, 27.3, 28.1, 25.6]
    
    # Thresholds for performance bands
    thresholds = {'low': 24.0, 'optimal': 26.0, 'high': 27.5}
    
    # Irrelevant auxiliary data - distractor
    calibration_offsets = [0.1, -0.2, 0.05, 0.15, -0.1, 0.0, 0.2, -0.15]
    adjusted_offsets = [x * 1.05 for x in calibration_offsets]  # Unused path

    # Apply offset correction (simulated preprocessing)
    corrected_readings = [raw_readings[i] + calibration_offsets[i] for i in range(len(raw_readings))]
    
    # Identify stable periods (within optimal band)
    is_stable = [(thresholds['low'] <= x <= thresholds['optimal']) for x in corrected_readings]
    
    # Extract only stable segments using itertools
    processed_data = list(compress(corrected_readings, is_stable))
    
    # Secondary filtering: ignore spikes above high threshold (additional logic)
    filtered_spikes = [x for x in processed_data if x <= thresholds['high']]

    # Misleading intermediate calculation - not used in final result
    avg_deviation = sum(abs(x - 25.0) for x in raw_readings) / len(raw_readings)
    normalized_weights = [round(1 / (1 + abs(w - 25)), 3) for w in raw_readings]  # Dead code

    # Key computation: efficiency score based on proximity to ideal (25.5)
    ideal_temp = 25.5
    efficiency_score = calculate_efficiency(filtered_spikes, thresholds)
    
    # Extraneous post-processing (no effect on answer)
    smoothing_factor = 0.85
    trend_adjusted = [smoothing_factor * x + (1 - smoothing_factor) * ideal_temp for x in filtered_spikes]
    final_prediction = sum(trend_adjusted) / len(trend_adjusted) if trend_adjusted else 0  # Unused

    print(f"Result: {efficiency_score}")


def calculate_efficiency(data, config):
    if not data:
        return 0.0
    
    ideal = 25.5
    deviations = [abs(x - ideal) for x in data]
    
    # Use conditional expression to handle edge cases
    penalty = 10 if any(d > 2.0 for d in deviations) else 5
    
    # Efficiency decreases with deviation
    base_score = 100 - (sum(deviations) / len(deviations)) * 8
    
    # Apply penalty based on outlier presence
    adjusted_score = base_score - penalty if len(data) < 5 else base_score
    
    # Additional distraction: cycle usage with no impact
    pattern_cycle = cycle([1, -1])
    dummy_shift = [next(pattern_cycle) * d for d in deviations[:4]]  # Not used
    
    return round(adjusted_score, 4)

if __name__ == "__main__":
    main()