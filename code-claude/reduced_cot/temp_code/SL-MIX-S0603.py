from collections import defaultdict, Counter
import math

def calculate_bandwidth(frequencies, base_width=10):
    # Calculate bandwidth based on frequency range
    if not frequencies:
        return 0
    spread = max(frequencies) - min(frequencies)
    return base_width + spread * 0.5

def analyze_noise_floor(signal_data):
    # Analyze noise characteristics - unused function
    noise_levels = [x & 0x0F for x in signal_data]
    return sum(noise_levels) / len(noise_levels) if noise_levels else 0

def filter_harmonics(frequencies):
    # Remove harmonic frequencies that are multiples of others
    result = []
    for freq in sorted(frequencies):
        is_harmonic = False
        for base in result:
            if freq > base and freq % base < 0.01:
                is_harmonic = True
                break
        if not is_harmonic:
            result.append(freq)
    return result

def calculate_signal_strength(frequencies):
    # Calculate signal strength based on frequency pattern
    if not frequencies:
        return 0
    
    # Count frequencies in different bands
    bands = defaultdict(int)
    for freq in frequencies:
        band = int(freq // 20)
        bands[band] += 1
    
    # Determine band with most frequencies
    dominant_band = max(bands.items(), key=lambda x: x[1])[0] if bands else 0
    
    # Calculate strength based on dominant band and frequency count
    base_strength = sum(frequencies) / len(frequencies)
    modifier = (dominant_band * 5) - (len(bands) * 3)
    
    return base_strength + modifier

# Signal processing simulation
raw_frequencies = [42, 58, 62, 84, 86, 120, 124, 126, 168, 210, 252]
time_slots = [i for i in range(15)]

# Map frequencies to time slots (unused operation)
frequency_map = {}
for i, freq in enumerate(raw_frequencies):
    time_index = i % len(time_slots)
    frequency_map[time_slots[time_index]] = freq

# Apply various filters
filtered_frequencies = [f for f in raw_frequencies if f > 50]

# Calculate bit patterns for each frequency (distraction)
bit_patterns = {}
for freq in raw_frequencies:
    pattern = freq & 0x3F  # Get lower 6 bits
    bit_patterns[freq] = pattern

# Analyze bit pattern distribution (unused)
bit_counts = Counter(bit_patterns.values())
most_common_bits = bit_counts.most_common(2)

# Calculate potential interference patterns (distraction)
interference_score = 0
for i, freq1 in enumerate(raw_frequencies[:-1]):
    for freq2 in raw_frequencies[i+1:]:
        if abs(freq1 - freq2) < 10:
            interference_score += 1

# Apply harmonic filtering
harmonic_free = filter_harmonics(filtered_frequencies)

# Revert to filtered frequencies for final calculation
filtered_frequencies = [f for f in filtered_frequencies if f % 2 == 0]

# Calculate bandwidth (unused result)
bandwidth = calculate_bandwidth(filtered_frequencies)

# Calculate signal-to-noise ratio (distraction)
snr_base = 10
for freq in filtered_frequencies:
    if freq > 100:
        snr_base += 2
    elif freq > 80:
        snr_base += 1.5
    else:
        snr_base += 0.5

# Calculate phase differences (unused)
phase_diffs = []
for i in range(len(filtered_frequencies) - 1):
    diff = (filtered_frequencies[i+1] - filtered_frequencies[i]) % 360
    phase_diffs.append(diff)

# Calculate final signal strength
final_signal_strength = calculate_signal_strength(filtered_frequencies)

# Apply interference adjustment (distraction - not actually used)
adjusted_strength = final_signal_strength - (interference_score * 0.5)

print(f"Result: {final_signal_strength}")