from collections import defaultdict

# Simulate sensor data stream with noise and valid readings
def process_sensor_stream(raw_data):
    filtered_data = []
    noise_floor = 0.1
    for val in raw_data:
        if abs(val) > noise_floor:
            filtered_data.append(abs(val))
    return filtered_data

# Analyze segment for peak detection and baseline drift
def process_segment(data_chunk):
    stats = defaultdict(float)
    cumulative = 0
    peak = float('-inf')
    baseline_shift = 0
    
    for i, reading in enumerate(data_chunk):
        cumulative += reading
        if reading > peak:
            peak = reading
            stats['peak_index'] = i  # Track index of highest peak
        
        # Simulated baseline correction (not used in final result)
        if i % 5 == 0:
            baseline_shift += 0.01 * reading
    
    stats['average'] = cumulative / len(data_chunk)
    stats['peak_value'] = peak
    stats['baseline_drift'] = baseline_shift
    return stats

# Main analysis pipeline
raw_signal = [
    0.05, -0.03, 0.45, 0.21, 0.18, 0.02, -0.07, 0.63, 0.55, 0.12,
    0.08, 0.33, 0.72, 0.69, 0.04, -0.01, 0.51, 0.88, 0.91, 0.77
]

processed_signal = process_sensor_stream(raw_signal)
segmented_batches = []
for i in range(0, len(processed_signal), 4):
    segment = processed_signal[i:i+4]
    if len(segment) >= 3:  # Only process substantial segments
        segmented_batches.append(segment)

final_analysis = []
summary_metrics = {}
redundant_calc = 0

for idx, segment_data in enumerate(segmented_batches):
    # Extraneous computation - simulates diagnostic trace
    if idx > 0:
        diff = segment_data[0] - segmented_batches[idx-1][-1]
        redundant_calc += abs(diff)
    
    # Key processing step
    final_analysis.append(process_segment(segment_data))
    
    # Additional distraction: build unused summary map
    summary_metrics[f'segment_{idx}'] = {
        'size': len(segment_data),
        'first_val': segment_data[0]
    }

# Secondary analysis on results (does not alter final target)
total_peaks = 0
counted_segments = 0
for entry in final_analysis:
    total_peaks += entry['peak_value']
    counted_segments += 1

# Final derived metric (never actually used)
avg_peak = total_peaks / counted_segments if counted_segments else 0

# Critical variable assignment based on last segment's peak
peak_capacity = final_analysis[-1]['peak_value']

# Irrelevant scaling operation (distraction)
normalized_capacity = peak_capacity * 0.95 ** 2

# Output target result
print(f"Result: {peak_capacity}")