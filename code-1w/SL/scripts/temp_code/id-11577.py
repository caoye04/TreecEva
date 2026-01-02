import math
from collections import defaultdict, Counter

# Simulate a signal processing pipeline with multiple transformations and red herrings

def generate_frequency_map(data):
    # Distractor function: calculates frequencies but not used in final result
    freq_map = defaultdict(int)
    for x in data:
        freq_map[x] += 1
    return freq_map

def decrypt_segment(segment, shift):
    # Decoy decryption logic that looks relevant but is unused
    return [(x - shift) % 256 for x in segment]

def apply_hamming_weight(seq):
    # Calculates bit population count - used in intermediate distraction
    return [bin(x).count('1') for x in seq]

def compute_checksum(data):
    # Seemingly important but unused checksum (red herring)
    return sum(data) % 1024

def transform_basis(sequence, matrix):
    # Applies linear transformation using matrix (actual core logic)
    result = []
    for i in range(len(sequence)):
        val = 0
        for j in range(len(matrix)):
            val += matrix[j] * sequence[(i + j) % len(sequence)]
        result.append(int(val))
    return result

def filter_outliers(data, threshold=3.5):
    # Distractor: sophisticated filtering not actually affecting main path
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    return [x for x in data if abs(x - mean_val) <= threshold * std_dev]

def accumulate_with_damping(seq, damping=0.9):
    # Complex-looking transformation with decay - irrelevant to final answer
    acc = 0
    result = []
    for x in seq:
        acc = acc * damping + x
        result.append(acc)
    return result

def extract_peaks(signal):
    # Finds local maxima - looks useful but unused
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i-1] < signal[i] > signal[i+1]:
            peaks.append(signal[i])
    return peaks

def process_transmission(seq, key):
    # Core function - only this contributes to final answer
    
    # Irrelevant preprocessing steps (distractors)
    temp_analysis = {'length': len(seq), 'max': max(seq), 'min': min(seq)}
    normalized = [x / (max(seq) + 1e-6) for x in seq]  # Not actually used
    
    # Real computation buried among distractions
    transformed = transform_basis(seq, key)
    
    # More red herrings
    magnitude = math.sqrt(sum(x**2 for x in transformed))
    phase_shifted = [x * math.cos(math.pi / 4) for x in transformed]  # Unused
    
    # Actual critical step
    aggregated = sum(transformed[::2]) - sum(transformed[1::2])  # Alternating sum
    
    # Additional misleading post-processing
    if magnitude > 100:
        adjusted = aggregated * 0.95
    else:
        adjusted = aggregated * 1.05  # This branch taken
    
    # Final manipulation
    final_value = int(round(adjusted + 50))
    
    # Dead code path
    if False:
        fallback = sum(apply_hamming_weight(seq))
        final_value = fallback
        
    return final_value

# Main execution block
if __name__ == '__main__':
    # Input signal sequence
    signal_sequence = [12, 7, 31, 18, 25, 42, 13, 8, 29, 21]
    
    # Key matrix for transformation
    key_matrix = [3, -2, 1, -1]
    
    # Various irrelevant variables (distractors)
    sample_rate = 44100
    bit_depth = 16
    frame_size = 1024
    buffer_window = [0] * 50
    
    # Seemingly important analysis
    freq_distribution = generate_frequency_map(signal_sequence)
    hamming_weights = apply_hamming_weight(signal_sequence)
    redundant_checksum = compute_checksum(signal_sequence)
    
    # Apply complex but irrelevant filters
    cleaned_signal = filter_outliers(signal_sequence)
    damped_accumulation = accumulate_with_damping(signal_sequence)
    detected_peaks = extract_peaks(signal_sequence)
    
    # Critical assignment
    final_signal = process_transmission(signal_sequence, key_matrix)
    
    # Print result as required
    print(f"Target result: {final_signal}")