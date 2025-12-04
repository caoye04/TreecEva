def process_signal(raw_data, threshold=50, noise_factor=0.3, amplify=True):
    # Initialize processing variables
    processed = []
    noise_samples = [x * noise_factor for x in range(5, 15)]
    
    # Apply initial filtering
    filtered_data = [x for x in raw_data if x > threshold]
    
    # Process signal with various techniques (some not used)
    for i, value in enumerate(filtered_data):
        # Amplification logic
        if amplify and value > 0:
            amplified = value * 2.5
        else:
            amplified = value
            
        # Apply pseudo-noise reduction (not actually used)
        noise_reduced = amplified - noise_samples[i % len(noise_samples)]
        
        # Track potential peaks for later analysis
        if i > 0 and i < len(filtered_data) - 1:
            if filtered_data[i-1] < value > filtered_data[i+1]:
                processed.append(value * 1.2)  # Peak enhancement
            else:
                processed.append(value)
        else:
            processed.append(value)
    
    return processed

# Signal processing pipeline
def analyze_frequency_components(signal_data):
    # Frequency domain analysis simulation
    frequency_bins = {}
    for i, amplitude in enumerate(signal_data):
        bin_index = i % 5
        if bin_index in frequency_bins:
            frequency_bins[bin_index] += amplitude
        else:
            frequency_bins[bin_index] = amplitude
    
    # Find dominant frequency (distractor calculation)
    max_bin = max(frequency_bins.items(), key=lambda x: x[1])
    return max_bin[0], frequency_bins

# Main execution
raw_signal = [23, 45, 67, 82, 91, 76, 65, 45, 30, 12]
enhanced_signal = [x + 10 for x in raw_signal]  # Not used in final calculation

# Apply band-pass filter (simulated)
band_filtered = [x for x in raw_signal if 30 <= x <= 85]

# Process signal with various parameters
processed_signal = process_signal(raw_signal, threshold=25, noise_factor=0.2)
filtered_signal = [x for i, x in enumerate(processed_signal) if i % 2 == 0]

# Analyze signal components
dominant_freq, freq_distribution = analyze_frequency_components(processed_signal)

# Calculate signal metrics
signal_mean = sum(processed_signal) / len(processed_signal) if processed_signal else 0
signal_range = max(processed_signal) - min(processed_signal) if processed_signal else 0

# Find maximum value index
max_value = max(processed_signal) if processed_signal else 0
max_index = processed_signal.index(max_value) if max_value in processed_signal else -1

# Calculate quality metrics (distractors)
snr = signal_mean / (signal_range * 0.1) if signal_range else 0
quality_factor = (max_value / signal_mean) if signal_mean else 0

# Set default values
default_value = 42
emergency_signal = 999

# Determine optimal signal based on analysis
if signal_range > 100:
    candidate_signal = max_value * 0.8
else:
    candidate_signal = signal_mean * 1.5

# Apply final signal selection logic
optimal_signal = filtered_signal[max_index] if max_index < len(filtered_signal) else default_value

# Output results
print(f"Processed signal: {processed_signal}")
print(f"Filtered signal: {filtered_signal}")
print(f"Signal metrics - Mean: {signal_mean}, Range: {signal_range}")
print(f"Maximum value: {max_value} at index {max_index}")
print(f"Result: {optimal_signal}")