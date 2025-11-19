from collections import deque

def transform_coeff(value):
    return value * 2 if value % 3 == 0 else value + 1

def calculate_power(spectrum):
    power = 0
    for freq in spectrum:
        power += freq ** 2 if freq > 0 else -freq
    return power

# Initialize signal processing components
signal_buffer = deque(maxlen=5)
frequency_spectrum = []
window_weights = [0.1, 0.2, 0.4, 0.2, 0.1]
processed_signal_strength = 0

# Process incoming signal data
raw_samples = [15, -6, 9, 0, 12, -3, 18, 21, -9, 24]
for sample in raw_samples:
    signal_buffer.append(sample)
    
    # Apply nested loop processing when buffer is full
    if len(signal_buffer) == signal_buffer.maxlen:
        temp_spectrum = []
        for i in range(len(signal_buffer)):
            weighted_val = signal_buffer[i] * window_weights[i]
            transformed_val = transform_coeff(int(weighted_val))
            temp_spectrum.append(transformed_val)
        
        # Calculate power with conditional logic
        chunk_power = calculate_power(temp_spectrum)
        processed_signal_strength += chunk_power if chunk_power > 10 else 0

# Final adjustment using ternary operator
processed_signal_strength = processed_signal_strength if processed_signal_strength > 100 else processed_signal_strength * 2
print(f"Result: {processed_signal_strength}")