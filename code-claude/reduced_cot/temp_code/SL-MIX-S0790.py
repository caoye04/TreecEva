# Signal Processing Analysis

def calculate_noise_profile(readings):
    # Generate noise profile (not used in main calculation)
    profile = {}
    for i, reading in enumerate(readings):
        profile[f'sensor_{i}'] = reading ** 2 - reading
    return profile

# Initialize sensor readings
sensor_data = [12, 8, 15, 10, 7, 9, 14]
background_noise = 3

# Process sensor readings
filtered_readings = [max(0, reading - background_noise) for reading in sensor_data]

# Calculate signal metrics
signal_strength = sum(filtered_readings) // len(filtered_readings)

# Additional parameters (some are distractions)
frequency_bands = {'low': 0.2, 'mid': 0.5, 'high': 0.3}
max_amplitude = max(filtered_readings) * 2
min_amplitude = min(filtered_readings) / 2

# Distraction calculations
decibel_levels = {}
for i, reading in enumerate(filtered_readings):
    if reading > 0:
        decibel_levels[f'channel_{i}'] = 10 * (reading / max(filtered_readings))
    else:
        decibel_levels[f'channel_{i}'] = 0

# More distraction metrics
avg_decibel = sum(decibel_levels.values()) / len(decibel_levels)
signal_to_noise = max_amplitude / (background_noise if background_noise > 0 else 1)

# Intermediate processing (some relevant, some not)
amplification_modes = ['low', 'medium', 'high']
selected_mode = amplification_modes[1]  # medium mode

amplification_factors = {'low': 1.5, 'medium': 2.5, 'high': 4.0}
amplification_factor = int(amplification_factors[selected_mode])

# More distractions - unused processing paths
if selected_mode == 'high':
    noise_ceiling = 20
    signal_threshold = signal_strength * 0.8
elif selected_mode == 'low':
    noise_ceiling = 5
    signal_threshold = signal_strength * 1.2
else:
    noise_ceiling = 10
    signal_threshold = signal_strength * 1.0

# Distraction - additional calculations that aren't used
for band, weight in frequency_bands.items():
    if band == 'high':
        high_boost = weight * signal_strength
    elif band == 'low':
        low_cut = weight * background_noise

# Key processing steps
noise_reduction = 2
sensor_efficiency = 0.75

# This is the key statement
effective_signal = (signal_strength * amplification_factor) // noise_reduction

# More distractions - unused processing
detection_threshold = effective_signal * sensor_efficiency
if detection_threshold > signal_threshold:
    detection_status = 'confirmed'
else:
    detection_status = 'pending'
    
# Slicing operations (distraction)
sorted_readings = sorted(filtered_readings)
middle_readings = sorted_readings[1:-1]
median_reading = sorted_readings[len(sorted_readings) // 2]

# Final output - this is what we're looking for
print(f"Result: {effective_signal}")