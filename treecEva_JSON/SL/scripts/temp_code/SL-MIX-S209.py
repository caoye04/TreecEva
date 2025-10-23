import heapq
import itertools

def process_spectral_data():
    # Initialize spectral peaks with their frequencies and amplitudes
    spectral_peaks = [(120, 8), (95, 15), (210, 6), (78, 12), (165, 9)]
    
    # Create max heap using negative values
    max_heap = [(-amp, freq) for freq, amp in spectral_peaks]
    heapq.heapify(max_heap)
    
    # Apply phase correction using XOR with mask 0x0F
    corrected_frequencies = []
    while max_heap:
        neg_amp, freq = heapq.heappop(max_heap)
        corrected_freq = freq ^ 0x0F
        corrected_frequencies.append(corrected_freq)
    
    # Apply bit-shift scaling: left shift by 2, then right shift by 1
    scaled_frequencies = []
    for freq in corrected_frequencies:
        scaled_freq = (freq << 2) >> 1
        scaled_frequencies.append(scaled_freq)
    
    # Combine with another sequence using itertools
    base_sequence = [10, 20, 30]
    combined_values = []
    for a, b in itertools.product(scaled_frequencies[:3], base_sequence):
        combined_values.append(a | b)  # Bitwise OR operation
    
    # Find maximum value from combined results
    primary_frequency_component = max(combined_values)
    
    return primary_frequency_component

# Execute processing pipeline
primary_frequency_component = process_spectral_data()
print(f"Result: {primary_frequency_component}")