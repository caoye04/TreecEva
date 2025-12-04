import math
import itertools
from collections import deque

def calculate_noise_floor(samples):
    # Noise floor calculation - distractor function
    return sum(abs(x) for x in samples) / max(1, len(samples))

def apply_spectral_mask(signal, mask_pattern):
    # Another distractor function that doesn't affect the result
    return [s * m for s, m in zip(signal, itertools.cycle(mask_pattern))]

def calculate_signal_power(signal, harmonic):
    # This is the key function that determines the result
    if not signal:
        return 0
    
    # Initial power calculation
    base_power = sum(x**2 for x in signal) / len(signal)
    
    # Apply harmonic adjustment
    adjusted_power = base_power * (harmonic % 5 + 1)
    
    # Convert to decibels and round to 2 decimal places
    if adjusted_power > 0:
        return round(10 * math.log10(adjusted_power), 2)
    else:
        return -99.99

# Signal processing simulation
def process_signal_data():
    # Raw signal data - looks important but most values aren't used
    raw_signal = [2.5, 3.1, -1.7, 4.2, -0.8, 3.3, 1.9, -2.2, 3.7, -1.5]
    
    # Various processing parameters - most are distractors
    sample_rate = 44100  # Hz
    nyquist = sample_rate / 2
    filter_cutoff = 0.25 * nyquist
    window_size = 1024
    overlap = 512
    fft_size = 2048
    
    # Noise characteristics - distractors
    noise_floor = calculate_noise_floor(raw_signal)
    signal_to_noise = 10 * math.log10(sum(x**2 for x in raw_signal) / (noise_floor**2 + 1e-10))
    
    # Phase information - distractor
    phase_shift = math.pi / 4
    phase_corrected = [x * math.cos(phase_shift) for x in raw_signal]
    
    # Apply various "filters" - mostly distractors
    spectral_mask = [0.8, 0.9, 1.0, 0.9, 0.8]
    masked_signal = apply_spectral_mask(raw_signal, spectral_mask)
    
    # These variables look important but are misleading
    primary_band = [x for i, x in enumerate(raw_signal) if i % 2 == 0]
    secondary_band = [x for i, x in enumerate(raw_signal) if i % 2 == 1]
    
    # Signal power calculations - more distractions
    primary_power = sum(x**2 for x in primary_band) / len(primary_band) if primary_band else 0
    secondary_power = sum(x**2 for x in secondary_band) / len(secondary_band) if secondary_band else 0
    
    # The actual signal we'll use - the key part that matters
    filtered_signal = [3.0, 4.0, 5.0]
    
    # Harmonic calculations - looks complex but most is distraction
    harmonic_series = [1, 2, 3, 4, 5]
    harmonic_weights = [1.0, 0.5, 0.33, 0.25, 0.2]
    weighted_harmonics = sum(h * w for h, w in zip(harmonic_series, harmonic_weights))
    
    # This is the key value that affects the result
    harmonic_factor = 2
    
    # Calculate various "signal strengths" - mostly distractors
    strength_linear = sum(abs(x) for x in filtered_signal) / len(filtered_signal)
    strength_square = sum(x**2 for x in filtered_signal) / len(filtered_signal)
    strength_log = 10 * math.log10(strength_square) if strength_square > 0 else -99.99
    
    # This conditional looks important but doesn't execute
    if signal_to_noise < 10:
        harmonic_factor = 4
        print("Low SNR detected, adjusting harmonic factor")
    
    # This loop looks important but doesn't affect the result
    signal_queue = deque(maxlen=5)
    for i in range(min(5, len(raw_signal))):
        signal_queue.append(raw_signal[i])
        if len(signal_queue) >= 3:
            avg = sum(signal_queue) / len(signal_queue)
            if avg > strength_linear:
                harmonic_factor = harmonic_factor * 0.9
    
    # The key calculation that determines the final result
    final_signal_strength = calculate_signal_power(filtered_signal, harmonic_factor)
    
    # More distractor calculations after the key result
    normalized_strength = final_signal_strength / (1 + math.log(1 + abs(final_signal_strength)))
    quantized_strength = round(normalized_strength * 10) / 10
    
    return final_signal_strength

# Execute the signal processing
result = process_signal_data()
print(f"Result: {result}")