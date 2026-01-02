def analyze_workload():
    # Simulate time-series server load data (in requests per minute)
    raw_load_data = [120, 135, 140, 180, 175, 200, 210, 190, 220, 250, 240, 230, 260, 280]

    # Irrelevant preprocessing: normalize to percentage (not used in final logic)
    max_theoretical = 500
    normalized_load = [round((x / max_theoretical) * 100, 2) for x in raw_load_data]

    # Distractor: calculate average of first half (unused)
    first_half_avg = sum(raw_load_data[:len(raw_load_data)//2]) / len(raw_load_data)//2

    # Actual processing: apply sliding window to detect usage bursts
    window_size = 3
    usage_peaks = []
    temp_sum_tracker = 0  # Semi-relevant: used in loop but not final result

    for i in range(len(raw_load_data) - window_size + 1):
        window = raw_load_data[i:i + window_size]
        avg_load = sum(window) / window_size
        temp_sum_tracker += sum(window)
        
        # Only consider windows where middle element exceeds threshold
        if window[1] > 170:
            usage_peaks.append(avg_load)

    # Distractor: reverse and slice (creates confusion about intent)
    usage_peaks_reversed = usage_peaks[::-1]
    trimmed_peaks = usage_peaks_reversed[1:-1]  # remove first and last of reversed

    # Key computation: focus on recent high-usage pattern
    recent_peak_index = len(raw_load_data) - window_size
    usage_window = raw_load_data[recent_peak_index - 1:recent_peak_index + 2]

    # Critical statement
    peak_capacity = max(usage_window)

    # Additional red herring calculation
    projected_growth = peak_capacity * 1.15
    safety_margin = projected_growth * 0.1

    # Output the target result
    print(f"Target result: {peak_capacity}")

analyze_workload()