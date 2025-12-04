import itertools
from math import sin, cos, pi

def calculate_harmonic_frequency(signals):
    # Extract only the relevant portion of signals
    valid_signals = signals[2:5]
    
    # Calculate the base frequency
    base = sum(valid_signals) % 17
    
    # Distractor calculation
    noise_factor = 0
    for i, j in itertools.product(range(3), range(3)):
        noise_factor += (i * j) if i != j else 0
    
    # Main calculation
    if base > 10:
        return base * 3 - 7
    else:
        return base * 2 + 5

# Generate signal data
signal_data = []
for i in range(10):
    # Complex signal generation with trigonometric functions
    wave_component = int(10 * sin(i * pi / 4) + 5 * cos(i * pi / 3))
    distortion = i % 3
    signal_data.append(wave_component + distortion)

# Process signal data
processed_data = []
for idx, value in enumerate(signal_data):
    if idx % 2 == 0:  # Even indices
        processed_data.append(value * 2)
    else:  # Odd indices
        processed_data.append(value // 2)

# Apply filters
filter_coefficients = [0.5, 1.5, 2.0, 1.5, 0.5]
filtered_signals = []

# First filter - moving average (distractor)
for i in range(len(processed_data) - 2):
    avg = sum(processed_data[i:i+3]) / 3
    filtered_signals.append(int(avg))

# Second filter - apply coefficients (relevant)
filtered_signals = []
for i in range(len(processed_data) - len(filter_coefficients) + 1):
    weighted_sum = 0
    for j in range(len(filter_coefficients)):
        weighted_sum += processed_data[i+j] * filter_coefficients[j]
    filtered_signals.append(int(weighted_sum))

# Analyze frequency components (distractor)
frequency_bins = [0] * 5
for signal in filtered_signals:
    bin_idx = min(abs(signal) % 5, 4)
    frequency_bins[bin_idx] += 1

# Calculate potential resonance frequencies (distractor)
resonance_candidates = []
for idx, count in enumerate(frequency_bins):
    if count > 1:
        resonance_candidates.append(idx * 10 + count)

# Apply harmonic analysis to find target frequency
target_frequency = calculate_harmonic_frequency(filtered_signals)

# Additional misleading calculations
false_target = 0
if len(resonance_candidates) > 0:
    false_target = sum(resonance_candidates) // len(resonance_candidates)
    if false_target > target_frequency:
        # This branch is never taken due to the data
        target_frequency = false_target - 12

# Apply final correction based on noise profile (distractor)
noise_profile = [signal % 3 for signal in filtered_signals]
if sum(noise_profile) > 10:
    # This branch is never taken due to the data
    target_frequency += 5

print(f"Result: {target_frequency}")