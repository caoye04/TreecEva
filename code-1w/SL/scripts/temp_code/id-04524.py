def analyze_system_performance(input_data):
    # Initialize tracking variables
    cumulative_load = 0
    transient_peaks = []
    baseline_offset = 0.003
    adjustment_log = []

    for reading in input_data:
        if reading > 100:
            transient_peaks.append(reading * 0.05)
        cumulative_load += reading + baseline_offset

    avg_load = cumulative_load / len(input_data)
    peak_count = len(transient_peaks)

    # Distractor: Irrelevant smoothing operation
    smoothed_values = [x * 0.98 + baseline_offset for x in input_data if x > 50]
    if smoothed_values:
        smoothed_avg = sum(smoothed_values) / len(smoothed_values)
        adjustment_log.append(smoothed_avg)

    # Key computation begins
    convergence = sum(1 for x in input_data if 80 <= x <= 120)
    fluctuation_index = (max(input_data) - min(input_data)) / avg_load

    # Secondary distractor: unused conditional branch
    if fluctuation_index > 0.5:
        status_flag = "UNSTABLE"
        temp_correction = lambda x: x * 0.75
    else:
        status_flag = "STABLE"
        temp_correction = lambda x: x * 1.0

    # Stability factor involves multiple steps
    raw_stability = (convergence / len(input_data)) * 100
    decay_factor = 0.9 ** peak_count
    stability_factor = raw_stability * decay_factor

    # Auxiliary calculation with red herring variables
    diagnostic_codes = {i: f"D{i}" for i in range(peak_count)}
    metadata_checksum = sum(len(code) for code in diagnostic_codes.values())

    def calculate_rating(cvg, stab):
        base_rating = cvg * 1.5
        bonus = stab * 0.1 if stab > 75 else 0
        penalty = 10 if peak_count > 5 else 0
        return int(base_rating + bonus - penalty)

    final_score = calculate_rating(convergence, stability_factor)
    
    # Final distractor: dead code path
    if False:
        fallback_score = (avg_load // 10) - metadata_checksum
        final_score = max(final_score, fallback_score)

    print(f"Result: {final_score}")
    return final_score

# Input data with realistic sensor readings
data_stream = [95, 110, 88, 105, 97, 115, 85, 102, 99, 108, 93]
analyze_system_performance(data_stream)