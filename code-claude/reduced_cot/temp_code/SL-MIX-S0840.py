from collections import Counter, defaultdict

def apply_filter(signal, threshold=5):
    # Apply noise reduction filter
    noise_reduction = []
    for i in range(len(signal)):
        if i > 0 and i < len(signal) - 1:
            noise_reduction.append((signal[i-1] + signal[i] + signal[i+1]) / 3)
        else:
            noise_reduction.append(signal[i])
    
    # This is actually never used
    frequency_map = defaultdict(int)
    for amp in noise_reduction:
        frequency_map[round(amp)] += 1
    
    # Apply threshold filter
    return [x for x in noise_reduction if abs(x) > threshold]

def calculate_metrics(data):
    if not data:
        return 0, 0, 0
    
    min_val = min(data)
    max_val = max(data)
    avg_val = sum(data) / len(data)
    
    # These metrics aren't actually used in the main processing
    variance = sum((x - avg_val) ** 2 for x in data) / len(data)
    skewness = sum((x - avg_val) ** 3 for x in data) / (len(data) * variance ** 1.5) if variance > 0 else 0
    
    return min_val, max_val, avg_val

def analyze_peaks(signal):
    # Find peaks in signal (local maxima)
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            peaks.append(signal[i])
    
    # Count frequency of peak values
    peak_counter = Counter(round(p) for p in peaks)
    
    # This peak analysis isn't actually used for the result
    dominant_peak = peak_counter.most_common(1)[0][0] if peaks else 0
    return len(peaks), dominant_peak

def process_signal(signal, window_size):
    if not signal or window_size <= 0:
        return 0
    
    # Apply sliding window and calculate average energy
    energy_levels = []
    for i in range(0, len(signal) - window_size + 1):
        window = signal[i:i+window_size]
        
        # Distracting calculation that isn't used
        peak_count, dominant = analyze_peaks(window)
        
        # Calculate energy (sum of squares)
        energy = sum(x**2 for x in window)
        energy_levels.append(energy)
    
    # More distracting calculations
    min_energy, max_energy, avg_energy = calculate_metrics(energy_levels)
    
    # The key calculation
    signal_strength = 0
    if energy_levels:
        # Find the index of maximum energy
        max_idx = energy_levels.index(max(energy_levels))
        
        # Extract the window with maximum energy
        max_window = signal[max_idx:max_idx+window_size]
        
        # Calculate the signal strength as the product of the first
        # and last elements in the max energy window, divided by window size
        if len(max_window) > 0:
            signal_strength = (max_window[0] * max_window[-1]) / window_size
    
    return round(signal_strength, 2)

# Raw signal data (simulating sensor readings)
raw_signal = [3.2, 4.7, 8.1, 12.3, 15.6, 14.2, 9.8, 7.5, 6.3, 8.9, 10.4, 7.2, 4.1]

# Preprocessing steps
shifted_signal = raw_signal[2:] + raw_signal[:2]  # This shift isn't actually needed
inverted_signal = [-x for x in raw_signal]  # This inversion isn't used

# Threshold parameters
base_threshold = 4
scaling_factor = 1.2
effective_threshold = base_threshold * scaling_factor  # = 4.8

# Apply filter to original signal
filtered_signal = apply_filter(raw_signal, effective_threshold)

# Window size for processing
default_window = 3
optimal_window = 4  # Research shows this is better
window_size = optimal_window if len(filtered_signal) > 5 else default_window

# Process the signal
final_signal_strength = process_signal(filtered_signal, window_size)

print(f"Result: {final_signal_strength}")