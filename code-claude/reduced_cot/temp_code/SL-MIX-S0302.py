def calculate_spectrum_intensity(wavelengths, amplitudes):
    # Calculate weighted spectrum intensity - distractor function
    intensity = 0
    for w, a in zip(wavelengths, amplitudes):
        if w > 700:  # Infrared region
            intensity += a * 0.7
        elif w < 400:  # Ultraviolet region
            intensity += a * 1.2
        else:  # Visible spectrum
            intensity += a * 1.0
    return intensity

def analyze_noise_pattern(signal_data):
    # Analyze noise in the signal - another distractor
    noise_levels = set([round(x % 10, 2) for x in signal_data])
    return sum(noise_levels) / len(noise_levels) if noise_levels else 0

def calculate_priority(wavelengths):
    # This is the critical function that calculates our target value
    base_factor = 100
    threshold = 550
    
    # Count wavelengths above and below threshold
    above_count = len([w for w in wavelengths if w > threshold])
    below_count = len(wavelengths) - above_count
    
    # Initialize variables for calculation
    adjustment = 0
    weight_factor = 2.5
    
    # Red herring calculations that don't affect the result
    potential_values = {450: 1.5, 500: 2.0, 600: 2.5, 650: 3.0}
    for val, multiplier in potential_values.items():
        if val in wavelengths:
            adjustment += multiplier  # This adjustment is never used
    
    # The actual calculation that matters
    if above_count > below_count:
        return base_factor + (above_count - below_count) * weight_factor
    else:
        return base_factor - (below_count - above_count)

# Main processing code
raw_wavelengths = [420, 532, 580, 632, 780, 455, 620, 590, 510, 700, 650]
raw_amplitudes = [0.8, 1.2, 0.9, 1.5, 0.6, 1.0, 1.1, 0.7, 0.85, 1.3, 1.4]

# Preprocessing - appears important but actually irrelevant
processed_wavelengths = sorted(raw_wavelengths)
processed_amplitudes = [a * 2 for a in raw_amplitudes]

# Filtering operation - this is relevant
threshold_min = 500
threshold_max = 700
filtered_wavelengths = [w for w in raw_wavelengths if threshold_min <= w <= threshold_max]

# More distractor calculations
spectrum_intensity = calculate_spectrum_intensity(raw_wavelengths, raw_amplitudes)
noise_level = analyze_noise_pattern(raw_wavelengths)
wavelength_range = max(raw_wavelengths) - min(raw_wavelengths)

# Misleading calculations
wavelength_groups = {}
for i, w in enumerate(raw_wavelengths):
    group = w // 100
    if group not in wavelength_groups:
        wavelength_groups[group] = []
    wavelength_groups[group].append(i)

# Another distractor variable
adjustment_factor = noise_level * 10 if noise_level > 1 else 5

# The critical calculation we're asking about
priority_factor = calculate_priority(filtered_wavelengths)

# Final computations - more distractors
final_result = (spectrum_intensity / 10) + priority_factor if spectrum_intensity > 0 else priority_factor
optimized_value = wavelength_range / 100 * adjustment_factor

# Output the result
print(f"Result: {priority_factor}")