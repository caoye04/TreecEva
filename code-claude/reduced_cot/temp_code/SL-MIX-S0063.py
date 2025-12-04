from collections import Counter
import math

def process_signal_amplitude(raw_data):
    """Process signal amplitude data with filtering."""
    noise_threshold = 15
    filtered_data = []
    for value in raw_data:
        if abs(value) > noise_threshold:
            # Apply logarithmic scaling to high amplitude signals
            scaled = math.log(abs(value)) * (1 if value > 0 else -1)
            filtered_data.append(scaled)
        else:
            filtered_data.append(value / 2)  # Reduce noise
    
    # Calculate statistics that won't be used
    max_amplitude = max([abs(x) for x in filtered_data])
    min_amplitude = min([abs(x) for x in filtered_data])
    avg_amplitude = sum([abs(x) for x in filtered_data]) / len(filtered_data)
    
    return filtered_data

def identify_harmonic_patterns(data):
    """Identify harmonic patterns in the data."""
    # Convert values to discrete frequency bins
    bins = [int(abs(val * 10)) % 16 for val in data]
    
    # Count occurrences of each bin
    bin_counts = Counter(bins)
    
    # Find dominant patterns (this is a distraction)
    dominant = bin_counts.most_common(3)
    
    # Calculate harmonic ratio (misleading calculation)
    harmonic_ratio = sum(count for bin, count in dominant) / len(data)
    
    # Return the bin values, not the counts (the important part)
    return [bin for bin in bins if bin % 3 == 0]

def calculate_target_frequency(signal_data):
    """Calculate the target frequency from signal data."""
    # Process amplitude (mostly distraction)
    processed_data = process_signal_amplitude(signal_data)
    
    # This branch is never taken due to length check
    if len(processed_data) < 5:
        return sum(processed_data) * 2
    
    # Extract harmonic patterns (contains the relevant logic)
    harmonic_bins = identify_harmonic_patterns(processed_data)
    
    # Misleading calculation path
    potential_frequencies = [bin * 1.5 for bin in harmonic_bins]
    max_potential = max(potential_frequencies) if potential_frequencies else 0
    min_potential = min(potential_frequencies) if potential_frequencies else 0
    
    # Calculate interference factors (distraction)
    interference_xor = 0
    for i in range(len(harmonic_bins) - 1):
        if i < len(harmonic_bins) - 1:
            interference_xor ^= (harmonic_bins[i] & harmonic_bins[i + 1])
    
    # The actual calculation that matters
    base_frequency = len(harmonic_bins)
    frequency_factor = sum(1 for bin in harmonic_bins if bin > 5)
    
    # More distraction calculations
    modulation_index = (max_potential - min_potential) / (max_potential + min_potential + 1)
    carrier_frequency = base_frequency * (1 + modulation_index)
    
    # The key calculation
    target_frequency = base_frequency * 2 + frequency_factor * 3
    
    # Dead code path - never executed due to condition always being false
    if sum(harmonic_bins) < 0:
        target_frequency = interference_xor * 4
    
    return target_frequency

# Main execution
signal_data = [23, 14, 7, 42, -31, 19, -25, 16, 8, -5]
carrier_wave = [abs(x) % 10 for x in signal_data]  # Distraction
modulation = [x >> 2 for x in carrier_wave]        # More distraction

# Misleading intermediate calculation
intermediate_result = sum(carrier_wave) * 2 - sum(modulation)

# The key statement that computes the answer
target_frequency = calculate_target_frequency(signal_data)

# Distraction operations after the key calculation
filtered_result = target_frequency
if intermediate_result > 100:
    filtered_result = target_frequency * 0.8

print(f"Target result: {target_frequency}")