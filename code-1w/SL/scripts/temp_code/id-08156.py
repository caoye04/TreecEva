import math

# System calibration constants (irrelevant to final result)
CALIBRATION_OFFSET = 0.023
REFERENCE_VOLTAGE = 5.1
TEMP_CORRECTION_FACTOR = 1.007

# Signal processing parameters
def generate_harmonic_sequence(base_freq, count):
    """Generate harmonic frequency sequence (used in decoy path)"""
    return [base_freq * (i + 1) for i in range(count)]

# Irrelevant signal distortion simulation
def apply_distortion(signal_array, intensity=0.1):
    distorted = []
    for x in signal_array:
        if x > 0.5:
            distorted.append(x * (1 + intensity))
        else:
            distorted.append(x * (1 - intensity))
    return distorted

# Unused recursive filter (dead code path)
def recursive_damping(value, depth):
    if depth <= 0 or value < 0.01:
        return value
    return 0.7 * recursive_damping(value - 0.05, depth - 1)

# Core resonance analysis function
def compute_phasor(angle_radians):
    # Real component used in main logic
    real_part = math.cos(angle_radians)
    imag_part = math.sin(angle_radians)  # Computed but not used later
    return real_part

# Frequency grid transformation with distractor operations
def transform_grid(raw_frequencies):
    adjusted = []
    normalization_sum = 0.0
    
    for f in raw_frequencies:
        # Relevant transformation
        shifted = f - 0.5
        if shifted < 0:
            shifted = abs(shifted)  # Symmetric adjustment
        
        # Distractor: phase rotation not actually contributing
        angle = shifted * math.pi / 4
        phasor_component = compute_phasor(angle)
        dummy_rotation = complex(shifted * phasor_component, shifted * math.sin(angle))
        
        # Only the magnitude-like term is carried forward
        transformed_val = shifted * 1.5 + 0.2 * phasor_component  # phasor_component used once
        adjusted.append(transformed_val)
        
        # Accumulating irrelevant sum
        normalization_sum += transformed_val ** 2  # Never used later
    
    # Final scaling uses only adjusted values
    scale_factor = 1.0 / len(adjusted) if adjusted else 1.0
    return [x * scale_factor for x in adjusted]

# Main analysis function with misleading intermediate names
def analyze_resonance(grid):
    # Step 1: Transform input
    processed = transform_grid(grid)
    
    # Step 2: Compute energy envelope (only sum matters)
    energy_levels = [x ** 2 for x in processed]  # List comprehension (required feature)
    total_energy = sum(energy_levels)
    
    # Step 3: Apply spectral weighting with conditional suppression
    weighted_components = []
    suppression_threshold = 0.3 * total_energy
    cumulative_suppression = 0.0  # Distractor accumulator
    
    for e in energy_levels:
        if e > suppression_threshold:
            weighted = e * 0.85
        else:
            weighted = e * 1.15  # Minor boost for low-energy components
        weighted_components.append(weighted)
        
        # Red herring: track suppressed amount (never used)
        if e > weighted:
            cumulative_suppression += (e - weighted)
    
    # Step 4: Calculate final yield based on weighted sum and combinatorics
    n = len(weighted_components)
    if n < 2:
        combination_factor = 1
    else:
        # Simple combinatorics: number of unique pairs
        combination_factor = n * (n - 1) // 2  # C(n,2)
    
    base_yield = sum(weighted_components)
    adjustment_ratio = math.sqrt(combination_factor) if combination_factor > 0 else 1
    
    # Final nonlinear transformation
    final_exponent = math.log(adjustment_ratio + 1) if adjustment_ratio > 0 else 0
    spectral_yield = base_yield * (math.exp(final_exponent) / (1 + final_exponent))
    
    return spectral_yield

# Primary execution flow
if __name__ == "__main__":
    # Define core input (appears arbitrary but deterministic)
    frequency_grid = [0.1, 0.7, 1.3, 0.4, 2.1, 1.8]
    
    # Irrelevant preprocessing (distractor)
    normalized_grid = [f / max(frequency_grid) for f in frequency_grid]
    harmonics = generate_harmonic_sequence(0.3, 5)
    distorted_harmonics = apply_distortion(harmonics, 0.15)
    
    # Key computation — answer derived here
    spectral_yield = analyze_resonance(frequency_grid)
    
    # Print target result
    print(f"Target result: {spectral_yield}")