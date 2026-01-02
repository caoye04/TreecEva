import math

# Simulated sensor data processing with diagnostic analysis
def preprocess_signal(raw_samples):
    cleaned = []
    noise_floor = 0.05
    gain_compensation = 1.07
    clip_threshold = 987.6

    for sample in raw_samples:
        if abs(sample) < noise_floor:
            adjusted = 0.0
        else:
            adjusted = sample * gain_compensation
            
        if adjusted > clip_threshold:
            adjusted = clip_threshold
        elif adjusted < -clip_threshold:
            adjusted = -clip_threshold
            
        cleaned.append(round(adjusted, 4))

    return cleaned


def detect_spikes(data_sequence, sensitivity=0.8):
    spike_indices = []
    baseline = sum(data_sequence) / len(data_sequence)
    deviation = sensitivity * (sum(abs(x - baseline) for x in data_sequence) / len(data_sequence))

    for i in range(1, len(data_sequence) - 1):
        if abs(data_sequence[i]) > abs(baseline) + deviation:
            if data_sequence[i] > data_sequence[i-1] and data_sequence[i] > data_sequence[i+1]:
                spike_indices.append(i)

    # Irrelevant transformation
    decoy_map = {i: (i*17)%13 for i in range(len(data_sequence))}
    normalized_score = len(spike_indices) / (len(data_sequence) + 1)
    return spike_indices, normalized_score


def compute_harmonic_envelope(signal_chunk):
    envelope = 0.0
    for x in signal_chunk:
        if x != 0:
            envelope += abs(math.sin(x) * math.cos(x/2))
    return round(envelope, 5) if envelope > 0.1 else 0.0


def filter_artifacts(data_stream, method='median'):
    window_size = 3
    filtered = data_stream[:]
    padding_value = data_stream[0]

    # Add irrelevant buffer
    buffer_zone = [padding_value]*5
    temp_offset = sum(buffer_zone) / len(buffer_zone)

    for i in range(len(data_stream)):
        start = max(0, i - window_size//2)
        end = min(len(data_stream), i + window_size//2 + 1)
        window_slice = data_stream[start:end]

        if method == 'median':
            sorted_window = sorted(window_slice)
            median_val = sorted_window[len(sorted_window)//2]
            filtered[i] = median_val
        elif method == 'mean':
            filtered[i] = sum(window_slice) / len(window_slice)

    # Dead code path - never executed due to default argument
    if method == 'fft':
        fourier_magnitude = [abs(math.sin(j*0.1)) for j in range(len(data_stream))]
        return fourier_magnitude

    return filtered


def analyze_signal(processed_data, significance_threshold):
    # Key metric computation
    amplitude_sum = sum(abs(x) for x in processed_data)
    zero_crossings = 0
    for i in range(1, len(processed_data)):
        if (processed_data[i-1] < 0 <= processed_data[i]) or (processed_data[i-1] >= 0 > processed_data[i]):
            zero_crossings += 1

    avg_magnitude = amplitude_sum / len(processed_data)
    peak_to_peak = max(processed_data) - min(processed_data)

    # Complex conditional logic with slicing
    mid_segment = processed_data[len(processed_data)//4 : 3*len(processed_data)//4]
    core_energy = sum(x**2 for x in mid_segment)

    # Set operation to identify unique magnitude bands
    magnitude_levels = {round(abs(x), 1) for x in processed_data}
    band_count = len(magnitude_levels)

    # Diagnostic score calculation
    stability_factor = 1.0 if band_count < 50 else 0.85
    rhythm_index = zero_crossings / len(processed_data)

    # Primary decision logic
    if core_energy > significance_threshold * 2:
        confidence = 0.9
    elif avg_magnitude > significance_threshold:
        confidence = 0.7
    else:
        confidence = 0.3

    # Final diagnostic score
    diagnostic_score = (avg_magnitude * 0.3 + 
                       peak_to_peak * 0.2 + 
                       rhythm_index * 0.15 + 
                       stability_factor * 0.35) * confidence

    # Decoy computations
    decoy_entropy = -sum((len(str(x))/10)*math.log2(len(str(x))/10) for x in processed_data if x != 0)
    ghost_metric = sum(1 for x in processed_data if x in {0.5, 1.5, 2.5})

    return round(diagnostic_score * 1000, 0)

# Main execution flow
if __name__ == "__main__":
    # Simulated input - realistic sensor readings
    raw_sensor_data = [
        0.12, -0.34, 0.56, 1.23, -2.34, 3.45, -4.56, 5.67, 6.78, -7.89,
        8.91, -9.12, 10.23, -11.34, 12.45, 13.56, -14.67, 15.78, 16.89, 17.91,
        -18.12, 19.23, 20.34, -21.45, 22.56, 23.67, -24.78, 25.89, 26.91, 27.12
    ]

    # Irrelevant calibration sequence
    calibration_matrix = [[i*j % 7 for j in range(5)] for i in range(6)]
    calibration_sum = sum(sum(row) for row in calibration_matrix)
    adjustment_factor = math.sqrt(calibration_sum) if calibration_sum > 0 else 1.0

    # Signal processing pipeline
    cleaned_signal = preprocess_signal(raw_sensor_data)
    spike_locations, relevance_score = detect_spikes(cleaned_signal, sensitivity=0.75)
    
    # Apply filtering
    filtered_data = filter_artifacts(cleaned_signal, method='median')
    
    # Compute auxiliary metrics (distractors)
    envelope_strength = compute_harmonic_envelope(filtered_data)
    data_range = max(filtered_data) - min(filtered_data)
    outlier_ratio = len([x for x in filtered_data if abs(x) > 10.0]) / len(filtered_data)
    
    # Threshold determined from domain knowledge
    threshold = 8.5
    
    # Critical statement
    final_diagnostic = analyze_signal(filtered_data, threshold)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")