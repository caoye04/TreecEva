def calculate_noise_floor(data, threshold=0.05):
    # Calculate baseline noise levels (unused in final calculation)
    noise_base = sum([abs(x) for x in data if abs(x) < threshold])
    return noise_base / max(1, len([x for x in data if abs(x) < threshold]))

def apply_filters(signal_data, filters):
    # Apply various signal processing filters
    results = {}
    for filter_name, filter_func in filters.items():
        filtered = list(map(filter_func, signal_data))
        results[filter_name] = filtered
    return results.get('bandpass', signal_data)  # Default to original if no bandpass

def find_peaks(data, window_size=3):
    # Find signal peaks (distractor function)
    peaks = []
    for i in range(window_size, len(data) - window_size):
        is_peak = True
        for j in range(1, window_size + 1):
            if data[i] <= data[i - j] or data[i] <= data[i + j]:
                is_peak = False
                break
        if is_peak:
            peaks.append((i, data[i]))
    return sorted(peaks, key=lambda x: x[1], reverse=True)[:5]  # Top 5 peaks

# Main signal processing pipeline
signal_data = [0.2, -0.1, 0.5, 0.8, 1.2, 0.7, 0.3, -0.2, -0.5, -0.3, 0.1, 0.4]
time_points = list(range(len(signal_data)))

# Various filter functions (some are distractors)
filters = {
    'lowpass': lambda x: x * 0.8 if abs(x) > 0.5 else x,
    'highpass': lambda x: x * 1.2 if abs(x) < 0.3 else x,
    'bandpass': lambda x: x * 0.9 if 0.3 <= abs(x) <= 0.8 else x * 0.7
}

# Apply processing pipeline
filtered_data = apply_filters(signal_data, filters)

# Calculate noise floor (distractor)
noise_level = calculate_noise_floor(filtered_data)

# This is a distractor - not used in final calculation
potential_freqs = [433.92, 868.3, 915.0, 2400.0, 5800.0]
freq_weights = [0.3, 0.2, 0.15, 0.25, 0.1]
weighted_freqs = [(f, w) for f, w in zip(potential_freqs, freq_weights)]

# Find candidate frequency (only some parts matter)
optimal_freq = 0
max_weight = 0
for freq, weight in weighted_freqs:
    # Only the 2400.0 MHz calculation is relevant
    if freq > 2000:
        adjusted_weight = weight * (1 + 0.1 * (freq // 1000))
        if adjusted_weight > max_weight:
            max_weight = adjusted_weight
            optimal_freq = freq

# Another distractor calculation
signal_to_noise = sum([abs(x) for x in filtered_data]) / (noise_level + 0.01)

# Find peaks (distractor)
peak_data = find_peaks(filtered_data)
peak_values = [p[1] for p in peak_data]

# Process signal data - the key calculation
def analyze_signal(data, frequency):
    # Extract middle slice for processing
    middle_slice = data[len(data)//4:3*len(data)//4]
    
    # Calculate frequency coefficient
    freq_coef = (frequency / 1000) ** 0.5
    
    # Apply frequency adjustment to slice
    adjusted_values = [val * freq_coef for val in middle_slice]
    
    # Calculate base strength
    base_strength = sum(adjusted_values) / len(adjusted_values)
    
    # Apply final tuning factors
    tuned_strength = base_strength * (10 - len(data[:3]))
    
    # Return rounded result
    return round(tuned_strength * 10) / 10

# Calculate final signal strength
signal_strength = analyze_signal(filtered_data, optimal_freq)
print(f"Result: {signal_strength}")
