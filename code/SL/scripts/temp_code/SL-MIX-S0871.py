import math
from functools import reduce

def process_audio_segment(amplitude_values):
    # Apply logarithmic transformation to each amplitude
    log_transformed = [math.log(abs(val)) if val != 0 else 0 for val in amplitude_values]
    
    # Reconstruct with exponential mapping
    reconstructed = [math.exp(val) for val in log_transformed]
    
    # Quality check conditions
    mean_amplitude = sum(reconstructed) / len(reconstructed)
    peak_value = max(reconstructed)
    stability_index = peak_value / (mean_amplitude + 1e-10)
    
    # Multiple boolean conditions for quality scoring
    is_stable = stability_index < 2.5
    has_sufficient_energy = mean_amplitude > 0.1
    no_distortion = all(val < 10 for val in reconstructed)
    
    # Calculate quality score using logical combinations
    base_score = 100
    if is_stable and has_sufficient_energy:
        base_score += 20
    if not no_distortion or not is_stable:
        base_score -= 30
    if has_sufficient_energy or is_stable:
        base_score += 10
    
    return base_score

# Test segments
audio_segments = [
    [0.5, 1.2, 0.8, 2.1],
    [0.01, 0.02, 0.015, 0.03],
    [1.5, 2.0, 1.8, 2.5, 3.0]  # Third segment
]

segment_quality_score = process_audio_segment(audio_segments[2])
print(f"Result: {segment_quality_score}")