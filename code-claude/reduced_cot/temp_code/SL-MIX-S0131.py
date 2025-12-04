import itertools
from collections import Counter, defaultdict

def analyze_spectrum(data, window_size=3):
    # Analyze spectral properties (distractor)
    spectral_map = defaultdict(int)
    for i in range(len(data) - window_size + 1):
        window = tuple(data[i:i+window_size])
        spectral_map[window] += 1
    
    # Find dominant patterns
    potential_patterns = [k for k, v in spectral_map.items() if v > 1]
    if not potential_patterns:
        return 0
    return len(potential_patterns)

def filter_noise(signal_data, threshold=10):
    # Apply noise filtering (distractor)
    filtered = []
    for val in signal_data:
        if abs(val) > threshold:
            filtered.append(val - (val % threshold))
        else:
            filtered.append(val)
    return filtered

def calculate_harmonic_series(base, count=5):
    # Generate harmonic series (distractor)
    harmonics = [base * (i + 1) for i in range(count)]
    return set(harmonics)

def normalized_signal(raw_data, sampling_rate):
    # Key processing function
    # First, calculate signal metrics
    signal_count = len(raw_data)
    dominant_freq = 0
    
    # Preprocessing - truncate to relevant section
    if signal_count > 10:
        raw_data = raw_data[3:13]  # Only positions 3-12 matter
    
    # Calculate frequency components
    freq_counter = Counter(raw_data)
    most_common = freq_counter.most_common(2)
    
    # Harmonic analysis (distractor)
    harmonics = calculate_harmonic_series(sampling_rate / 8, 3)
    harmonic_power = sum(h % 10 for h in harmonics)  # Unused value
    
    # Calculate dominant frequency
    if most_common:
        dominant_value, count = most_common[0]
        secondary_value = 0
        if len(most_common) > 1:
            secondary_value = most_common[1][0]
        
        # Apply sampling rate correction
        correction_factor = (sampling_rate & 0xF) / 8  # Bitwise AND with 0xF (15)
        
        # Calculate intermediate values
        intermediate_a = dominant_value * correction_factor
        intermediate_b = secondary_value * (correction_factor / 2)
        
        # Misleading calculation path (distractor)
        if dominant_value > secondary_value and count > 2:
            potential_freq = (dominant_value + secondary_value) / 2
            noise_factor = analyze_spectrum(raw_data)
            adjusted_freq = potential_freq + noise_factor
        else:
            adjusted_freq = dominant_value - secondary_value
        
        # The actual calculation that matters
        dominant_freq = intermediate_a - intermediate_b
    
    # Apply final corrections
    noise_filtered = filter_noise(raw_data)  # Unused distractor
    
    # Final frequency calculation
    cycles = itertools.cycle([1, -1, 0.5, -0.5])
    cycle_sum = sum(next(cycles) for _ in range(5))  # Sum of first 5 elements = 0
    
    # Combine bit operations with mathematical operations
    bit_factor = (sampling_rate >> 2) & 7  # Right shift by 2 then AND with 7
    final_adjustment = cycle_sum + bit_factor
    
    # Return the final result
    return dominant_freq + final_adjustment

# Main processing
raw_data = [5, 8, 3, 7, 7, 7, 4, 7, 7, 9, 2, 5, 8, 3, 1]
sampling_rate = 32

# Additional misleading calculations
max_amplitude = max(raw_data)  # 9
min_amplitude = min(raw_data)  # 1
dynamic_range = max_amplitude - min_amplitude  # 8
signal_power = sum(x**2 for x in raw_data) / len(raw_data)  # Not used

# Special processing for edge cases
if sampling_rate < 16:
    adjusted_rate = sampling_rate * 2
else:
    adjusted_rate = sampling_rate
    
# More distractors
harmonic_set = calculate_harmonic_series(adjusted_rate / 4)
filtered_signal = filter_noise(raw_data, 5)
noise_profile = analyze_spectrum(filtered_signal)

# The key calculation we're interested in
final_frequency = normalized_signal(raw_data, sampling_rate)
print(f"Result: {final_frequency}")