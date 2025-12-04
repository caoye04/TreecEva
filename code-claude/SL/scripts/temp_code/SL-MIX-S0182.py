import itertools
from functools import reduce

def analyze_spectral_density(frequencies, amplitudes):
    # Analyze spectral density (not relevant to main calculation)
    density_map = {}
    for f, a in zip(frequencies, amplitudes):
        density_map[f] = a * a
    
    # This calculation is a distraction
    max_density = max(density_map.values()) if density_map else 0
    normalized = {f: d/max_density for f, d in density_map.items()}
    return sum(normalized.values()) / len(normalized) if normalized else 0

def filter_harmonics(signal_data, threshold=0.3):
    # Filter out harmonics below threshold (distraction)
    filtered = [(f, a) for f, a in signal_data if a > threshold]
    # This sorting isn't actually used
    sorted_data = sorted(filtered, key=lambda x: x[1], reverse=True)
    
    # The harmonics calculation is a distraction
    harmonics = set()
    for f, _ in filtered:
        harmonics.update([f*2, f*3, f/2])
    
    return filtered  # Note: returns filtered, not sorted_data

def calculate_resonance_factor(frequencies):
    # Calculate resonance factor (misleading)
    if not frequencies:
        return 0
    # This lambda function is overly complex for distraction
    resonance = lambda x, y: (x + y) / (abs(x - y) + 0.01)
    pairs = list(itertools.combinations(frequencies, 2))
    if not pairs:
        return sum(frequencies) / len(frequencies)
    
    # This calculation doesn't impact the final result
    factors = [resonance(a, b) for a, b in pairs]
    return sum(factors) / len(factors)

def calculate_optimal_frequency(signal_data):
    # Extract frequencies and amplitudes
    frequencies = [f for f, _ in signal_data]
    amplitudes = [a for _, a in signal_data]
    
    # Calculate the mean frequency (relevant)
    mean_freq = sum(frequencies) / len(frequencies) if frequencies else 0
    
    # Filter the data (distraction)
    filtered_data = filter_harmonics(signal_data)
    filtered_freqs = [f for f, _ in filtered_data]
    
    # Calculate spectral density (distraction)
    density = analyze_spectral_density(frequencies, amplitudes)
    
    # Calculate resonance (distraction)
    resonance = calculate_resonance_factor(filtered_freqs)
    
    # Create sets for distraction
    freq_set = set(frequencies)
    filtered_set = set(filtered_freqs)
    
    # Set operations (partially relevant)
    common_freqs = freq_set.intersection(filtered_set)
    unique_freqs = freq_set.symmetric_difference(filtered_set)
    
    # Calculate weighted frequencies (relevant)
    weighted_sum = 0
    total_weight = 0
    
    for f, a in signal_data:
        if f in common_freqs:
            # Higher weight for frequencies that survived filtering
            weight = a * 2
        else:
            weight = a * 0.5
        
        weighted_sum += f * weight
        total_weight += weight
    
    # The actual optimal frequency calculation
    if total_weight > 0:
        return weighted_sum / total_weight
    else:
        return mean_freq

# Main program
signal_data = [
    (20, 0.1),  # (frequency, amplitude)
    (45, 0.8),
    (60, 0.5),
    (75, 0.3),
    (90, 0.2),
    (120, 0.9),
    (150, 0.4)
]

# Calculate some misleading metrics
peak_amplitude = max(a for _, a in signal_data)
peak_frequency = next(f for f, a in signal_data if a == peak_amplitude)

# Calculate a misleading "dominant frequency"
dominant = reduce(lambda acc, item: acc + item[0] * item[1], signal_data, 0)
dominant /= sum(a for _, a in signal_data)

# This variable isn't used in the final calculation
frequency_range = max(f for f, _ in signal_data) - min(f for f, _ in signal_data)

# The key calculation we're interested in
optimal_frequency = calculate_optimal_frequency(signal_data)

# More distraction calculations after the key value is determined
average_amplitude = sum(a for _, a in signal_data) / len(signal_data)
normalized_range = frequency_range / peak_frequency

print(f"Result: {optimal_frequency}")