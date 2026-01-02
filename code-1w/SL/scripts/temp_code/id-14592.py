import math

# Simulated sensor data processing with red herrings and complex flow
def analyze_noise_profile(samples):
    noise_floor = 0.0
    peak_noise = 0.0
    dummy_accum = 0.0
    for s in samples:
        if s < -0.5:
            noise_floor += abs(s)
        elif s > 0.8:
            peak_noise += s
        dummy_accum += math.sin(s)  # Irrelevant computation
    return noise_floor

# Decoy function – never called but looks important
def decrypt_sequence(seq):
    result = 0
    for i, val in enumerate(seq):
        result ^= (val * i) % 7
    return result

# Signal preprocessing with slicing and transformations
def extract_features(raw_data):
    n = len(raw_data)
    segment_a = raw_data[:n//3]
    segment_b = raw_data[n//3:2*n//3]
    segment_c = raw_data[2*n//3:]
    
    # Real feature extraction
    avg_a = sum(segment_a) / len(segment_a)
    avg_b = sum(segment_b) / len(segment_b)
    trend = avg_b - avg_a
    
    # Distractor variables
    magnitude_flux = 0
    for i in range(1, len(segment_c)):
        magnitude_flux += abs(segment_c[i] - segment_c[i-1])
    
    # This normalization is unused later
    normalized_c = [x / (max(segment_c) + 1e-9) for x in segment_c]
    
    return trend, segment_c

# Core transformation function
def apply_filter(buffer, factor=1.5):
    filtered = []
    for i in range(len(buffer)):
        temp_val = buffer[i] * factor
        if i > 0:
            temp_val -= buffer[i-1] * 0.1
        filtered.append(abs(temp_val) ** 0.5)
    return filtered

# Main signal processor
def process_transmission(slices):
    flat_signal = [item for sublist in slices for item in sublist]  # Flatten
    
    # Step 1: Extract trend and last segment
    trend_comp, critical_segment = extract_features(flat_signal)
    
    # Step 2: Apply filter to relevant part
    processed_segment = apply_filter(critical_segment, factor=1.2)
    
    # Step 3: Slice into overlapping windows (using slicing heavily)
    window_size = 3
    step = 1
    windows = [processed_segment[i:i+window_size] for i in range(0, len(processed_segment)-window_size+1, step)]
    
    # Step 4: Compute energy in each window
    energies = []
    for win in windows:
        energy = sum(x**2 for x in win)
        energies.append(energy)
    
    # Step 5: Find dominant frequency index (argmax)
    max_energy_idx = 0
    max_energy = energies[0]
    for i in range(1, len(energies)):
        if energies[i] > max_energy:
            max_energy = energies[i]
            max_energy_idx = i
    
    # Step 6: Apply phase shift based on index
    shifted_idx = (max_energy_idx + int(trend_comp * 10)) % len(energies)
    
    # Step 7: Retrieve value at shifted index
    anchor_value = energies[shifted_idx]
    
    # Step 8: Final transformation using bit manipulation (red herring included)
    temp_int = int(anchor_value * 100)
    masked = temp_int & 0xFF  # Keep lower 8 bits
    inverted = (~masked) & 0xFF
    final_signal = masked - inverted  # Effective: 2*masked - 255
    
    # DEAD CODE PATHS AND DISTRACTORS BELOW
    audit_log = []
    for i, e in enumerate(energies):
        if e > anchor_value * 0.9:
            flag = 'HIGH'
        else:
            flag = 'LOW'
        audit_log.append({'index': i, 'energy': e, 'flag': flag})  # Unused
    
    # Noise analysis on irrelevant data
    dummy_samples = [-0.7, 0.1, 0.9, -1.2, 0.3]
    _ = analyze_noise_profile(dummy_samples)  # Called but result ignored
    
    # Another decoy calculation
    magic_offset = 0
    for i in range(50):
        magic_offset += (i * i) % 5
    magic_offset = magic_offset % 13  # Unused
    
    # THIS IS THE FINAL ANSWER OUTPUT
    print(f"Result: {final_signal}")
    return final_signal

# Generate input structure: list of lists
base_pattern = [0.5, -0.3, 0.8, 1.1, -0.7, 0.2, 0.9, -1.0, 0.6]
signal_slices = [
    [x * 1.1 for x in base_pattern],
    [x * 0.9 for x in base_pattern[::-1]],
    [x * 1.05 for x in base_pattern[::2]]
]

# Execute
final_signal = process_transmission(signal_slices)