from math import gcd
from statistics import mean, variance

def process_signal_waveform(raw_signal):
    # Apply a mask and shift operations
    masked_signal = [(s & 0xFF) >> 2 for s in raw_signal]
    
    # Filter out values below threshold
    threshold = int(mean(masked_signal))
    filtered_signal = [s for s in masked_signal if s > threshold]
    
    # Compute statistical measures
    if len(filtered_signal) == 0:
        return 0, 0
    signal_mean = int(mean(filtered_signal))
    signal_variance = int(variance(filtered_signal))
    
    # Bitwise checksum computation
    checksum = 0
    for val in filtered_signal:
        checksum ^= (val << 1) & 0xFF
    
    # Apply final transformation using GCD
    final_gcd = gcd(signal_mean, signal_variance) if signal_variance != 0 else 1
    checksum = (checksum >> 1) | (final_gcd << 4)
    
    return checksum

# Simulated audio signal data
audio_samples = [120, 200, 150, 180, 90, 240, 160, 130, 170, 110]
checksum = process_signal_waveform(audio_samples)
print(f"Result: {checksum}")