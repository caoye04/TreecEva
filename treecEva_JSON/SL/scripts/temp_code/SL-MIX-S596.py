from collections import defaultdict
import math

class FrequencyBin:
    def __init__(self, frequency, amplitude=0):
        self.frequency = frequency
        self.amplitude = amplitude
        self.active = False
    
    def activate(self, threshold):
        self.active = self.amplitude > threshold
        return self.active

def harmonic_search(bins, fundamental):
    harmonics = []
    for bin in bins:
        ratio = bin.frequency / fundamental
        if abs(round(ratio) - ratio) < 0.01 and round(ratio) > 1:
            harmonics.append(bin)
    return harmonics

def process_signal_spectrum(frequency_data, amplitude_data):
    bins = [FrequencyBin(freq, amp) for freq, amp in zip(frequency_data, amplitude_data)]
    threshold = sum(amplitude_data) / len(amplitude_data)
    
    # Activate bins above threshold
    active_count = 0
    for bin in bins:
        if bin.activate(threshold * 0.8):
            active_count += 1
    
    # Find fundamental frequency (lowest active bin)
    fundamental_freq = min([bin.frequency for bin in bins if bin.active], default=0)
    
    # Search for harmonics
    harmonic_bins = harmonic_search(bins, fundamental_freq) if fundamental_freq else []
    
    # Apply harmonic weighting
    weighted_harmonics = 0
    for h_bin in harmonic_bins:
        harmonic_order = round(h_bin.frequency / fundamental_freq)
        h_bin.amplitude *= math.log(harmonic_order + 1)
        if h_bin.amplitude > threshold:
            weighted_harmonics += 1
    
    # Final count calculation using bit operations
    final_bin_count = (active_count & ~len(harmonic_bins)) | (weighted_harmonics ^ 3)
    return final_bin_count

# Signal data
frequencies = [100, 200, 300, 400, 500, 600, 800, 1000]
amplitudes = [0.5, 1.2, 0.8, 2.1, 0.3, 1.5, 0.9, 1.8]

result = process_signal_spectrum(frequencies, amplitudes)
print(f"Result: {result}")