def analyze_signal_integrity(raw_readings):
    filtered_readings = [x for x in raw_readings if 0 <= x <= 100]
    baseline = sum(filtered_readings) / len(filtered_readings) if filtered_readings else 0
    
    # Misleading normalization branch (not used)
    normalized_offsets = []
    for val in filtered_readings:
        offset = (val - baseline) / (baseline + 1e-5)
        normalized_offsets.append(round(offset, 3))
    
    # Actual processing path
    squared_devs = [(x - baseline)**2 for x in filtered_readings]
    rms_deviation = (sum(squared_devs) / len(squared_devs))**0.5 if squared_devs else 0
    
    return rms_deviation


def calculate_peak_stability(signal_segments):
    segment_variability = []
    
    for i, segment in enumerate(signal_segments):
        if len(segment) < 3:
            continue
            
        # Real computation: assess central tendency stability
        mid_slice = segment[1:-1]  # Use slicing to exclude edge noise
        if not mid_slice:
            continue
            
        mean_center = sum(mid_slice) / len(mid_slice)
        variance = sum((x - mean_center)**2 for x in mid_slice) / len(mid_slice)
        stability_score = 100 / (1 + variance)  # Inverse relationship
        
        # Distractor: unused peak tracking
        peaks = [mid_slice[j] for j in range(1, len(mid_slice)-1) if mid_slice[j] > mid_slice[j-1] and mid_slice[j] > mid_slice[j+1]]
        avg_peak_height = sum(peaks) / len(peaks) if peaks else 0
        
        segment_variability.append(stability_score)
    
    final_stability = sum(segment_variability) / len(segment_variability) if segment_variability else 0
    return round(final_stability, 4)

# Simulated data input
readings = [85, 90, 92, 87, 88, 96, 101, 89, -5, 91, 86]
segment_data = [
    [10, 12, 15, 14, 13],
    [20, 18, 25, 22, 19],
    [30, 33, 31, 30, 34, 32]
]

# Irrelevant preprocessing step (distractor)
decimated = readings[::2]
smoothed = [sum(readings[i:i+3])/3 for i in range(len(readings)-2)]

# Core analysis chain
signal_noise_ratio = analyze_signal_integrity(readings)
peak_stability_index = calculate_peak_stability(segment_data)

# Final output
print(f"Target result: {peak_stability_index}")