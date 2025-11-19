import math

def process_audio_signal():
    # Generate impulse response: exponentially decaying sinusoid
    def impulse_response(n, alpha=0.1, freq=0.3):
        return math.exp(-alpha * n) * math.cos(2 * math.pi * freq * n)
    
    # Convolution operation
    def convolve(signal, kernel):
        result = [0.0] * (len(signal) + len(kernel) - 1)
        for i in range(len(signal)):
            for j in range(len(kernel)):
                result[i + j] += signal[i] * kernel[j]
        return result
    
    # Input signal: alternating sequence with noise-like pattern
    input_samples = [((-1)**i) * (i % 7 + 1) for i in range(12)]
    
    # Generate 8-point impulse response
    h = [impulse_response(n) for n in range(8)]
    
    # Perform convolution
    filtered_output = convolve(input_samples, h)
    
    # Compute energy in specified window (samples 5 through 15)
    signal_energy = 0.0
    for idx in range(5, min(16, len(filtered_output))):
        sample_value = filtered_output[idx]
        signal_energy += sample_value * sample_value
    
    return signal_energy

# Engineer's verification function using lambda for adaptive thresholding
verify_threshold = lambda energy, ref=1.25: energy > ref

# Process the signal and apply verification
computed_energy = process_audio_signal()
is_valid = verify_threshold(computed_energy)

# Apply correction factor if needed
if not is_valid:
    correction_factor = 1.0 + sum([1/(i+1) for i in range(5)])
    computed_energy *= correction_factor

print(f"Result: {round(computed_energy, 6)}")