import math

def analyze_harmonic_distortion(samples, threshold):
    """Irrelevant function analyzing signal distortion (dead code path)."""
    harmonics = [abs(math.sin(x)) for x in samples if x > threshold]
    return sum(harmonics) / len(harmonics) if harmonics else 0.0

def generate_synthetic_pulse(duration, resolution):
    """Generates a synthetic signal pulse (unused distractor)."""
    return [math.cos(i * duration / resolution) for i in range(resolution)]

def shift_phase_components(buffer, shift):
    """Applies phase shifting to buffer elements (distractor operation)."""
    shifted = []
    for val in buffer:
        shifted.append(val * math.cos(shift) + math.sin(shift))
    return shifted

def calculate_entropy(data_stream):
    """Calculates information entropy of data stream (misleading intermediate)."""
    from collections import Counter
    counts = Counter(data_stream)
    total = len(data_stream)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)

def compute_refinement_score(sequence, factor):
    """Computes adaptive refinement score based on filtered sequence dynamics."""
    # Step 1: Filter values above dynamic threshold
    dynamic_limit = factor * 1.75
    filtered_sequence = [x for x in sequence if x % 3 == 1 and x > dynamic_limit]
    
    # Step 2: Apply exponential scaling
    scaled_values = [math.exp(val / 10) for val in filtered_sequence]
    
    # Step 3: Compute moving average of adjacent pairs
    averaged_pairs = []
    for i in range(len(scaled_values) - 1):
        avg = (scaled_values[i] + scaled_values[i+1]) / 2
        averaged_pairs.append(avg)
    
    # Step 4: Apply logarithmic compression
    compressed = [math.log(x) if x > 1 else 0 for x in averaged_pairs]
    
    # Step 5: Aggregate using weighted sum with index bias
    weighted_sum = 0.0
    for idx, val in enumerate(compressed):
        weighted_sum += val * (idx + 1) * 0.5
    
    # Step 6: Normalize by length and apply floor
    if len(compressed) == 0:
        base_score = 0
    else:
        base_score = int(weighted_sum / len(compressed))
    
    # Step 7: Augment with modular checksum of original sequence
    checksum = sum([x % 7 for x in sequence]) % 5
    final_score = base_score + checksum
    
    return final_score

# Main execution context
if __name__ == "__main__":
    # Initialize sensor data buffer (real input source)
    signal_buffer = [12, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52]
    
    # Calibration parameters from external system (some are decoys)
    calibration_factor = 8
    normalization_constant = 3.14159
    baseline_offset = -1.5
    temporal_damping = 0.85
    
    # Irrelevant preprocessing steps (distractors)
    normalized_signal = [x / normalization_constant for x in signal_buffer]
    dampened = [x * temporal_damping for x in normalized_signal]
    phase_shifted = shift_phase_components(dampened, math.pi / 4)
    
    # Entropy analysis (red herring)
    discrete_stream = [int(abs(x * 10)) % 100 for x in phase_shifted]
    signal_entropy = calculate_entropy(discrete_stream)
    
    # Generate unused synthetic data (dead path)
    synthetic_pulse = generate_synthetic_pulse(2.5, 50)
    harmonic_profile = analyze_harmonic_distortion(synthetic_pulse, 0.3)
    
    # Key computation: determine filtration threshold
    filtration_threshold = compute_refinement_score(signal_buffer, calibration_factor)
    
    # Output target result
    print(f"Result: {filtration_threshold}")