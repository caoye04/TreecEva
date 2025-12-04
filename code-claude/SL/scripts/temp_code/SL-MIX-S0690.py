def process_signal(data, threshold=0.5):
    # Process signal data with various filters
    filtered = [x * 0.8 for x in data if x > threshold]
    noise_reduction = sum(filtered) / len(filtered) if filtered else 0
    return noise_reduction, filtered

def analyze_interference(patterns):
    # Analyze interference patterns in signal
    strength = 0
    priority_queue = [(i, p % 10) for i, p in enumerate(patterns)]
    priority_queue.sort(key=lambda x: x[1], reverse=True)
    
    for idx, (pos, priority) in enumerate(priority_queue):
        if idx < 3:  # Only consider top 3 interference sources
            strength += priority * 1.5
        else:
            break
    
    return strength, priority_queue[:3]

def calculate_frequency_bands(signal_strength, base_frequency=100):
    # Calculate potential frequency bands
    bands = []
    distractor_val = 0
    
    for i in range(5):
        band = base_frequency * (i + 1) + signal_strength * 2
        bands.append(band)
        distractor_val += band % 10  # Misleading calculation
    
    # Distractor operations that don't affect the result
    noise_bands = {b + 20 for b in bands if b % 2 == 0}
    alternate_bands = bands[::2]
    
    return bands, noise_bands

def calculate_optimal_frequency(signal_data, interference_patterns):
    # Main function to calculate optimal transmission frequency
    signal_quality, filtered_data = process_signal(signal_data, 0.3)
    
    # Distractor: create a complex data structure that isn't used
    signal_metrics = {
        'amplitude': sum(filtered_data) / len(filtered_data) if filtered_data else 0,
        'variance': sum((x - signal_quality)**2 for x in filtered_data) / len(filtered_data) if filtered_data else 0,
        'peak': max(filtered_data) if filtered_data else 0
    }
    
    # Calculate interference strength
    interference_strength, top_sources = analyze_interference(interference_patterns)
    
    # More distractors: unused variables and calculations
    adjusted_quality = signal_quality * (1 - interference_strength/100)
    potential_channels = [i for i in range(1, 11) if i not in [s[0] % 10 for s in top_sources]]
    channel_weights = {ch: (ch * 3) % 10 + 1 for ch in potential_channels}
    
    # Calculate frequency bands
    frequency_bands, _ = calculate_frequency_bands(signal_quality * 10)
    
    # Determine optimal frequency - the actual calculation that matters
    band_index = int(interference_strength) % len(frequency_bands)
    base_freq = frequency_bands[band_index]
    
    # Distractor calculation
    if signal_quality > 5:
        optimal_adjustment = signal_quality * 0.8
    else:
        optimal_adjustment = interference_strength * 0.3
    
    # The key calculation that determines the answer
    optimal_frequency = base_freq - (interference_strength * 1.5)
    
    # More distraction
    alternative_freq = base_freq + signal_quality * 2
    backup_frequencies = [optimal_frequency * 0.9, alternative_freq * 1.1]
    
    return optimal_frequency

# Test data
signal_data = [0.2, 0.7, 0.9, 0.4, 0.6, 0.8, 0.3, 0.5]
interference_patterns = [12, 7, 25, 9, 14]

# Calculate and print the result
optimal_frequency = calculate_optimal_frequency(signal_data, interference_patterns)
print(f"Result: {optimal_frequency}")