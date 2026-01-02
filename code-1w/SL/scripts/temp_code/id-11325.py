def analyze_waveform(samples, window_size):
    total_energy = 0
    peak_amplitude = 0
    energy_threshold = 150
    
    for i in range(0, len(samples) - window_size + 1):
        signal_segment = samples[i:i + window_size]
        segment_energy = sum(x ** 2 for x in signal_segment)
        total_energy += segment_energy
        
        if segment_energy > energy_threshold:
            peak_amplitude = max(signal_segment)
    
    normalization_factor = 1.0 / len(samples)
    average_energy = total_energy * normalization_factor
    
    return peak_amplitude

# Simulated sensor data from a vibration monitor
data_stream = [2, -7, 12, 8, -3, 15, -11, 6, 4, -9, 13]
result = analyze_waveform(data_stream, window_size=3)
print(f"Result: {result}")