import math

# System calibration constants (irrelevant to final result)
CALIBRATION_OFFSET = 0.00314
BASELINE_DRIFT = [0.02, -0.01, 0.03]
REFERENCE_FREQ = 440.0

# Sensor input simulation (mixed relevant and irrelevant data)
sensor_a_reads = [128, 64, 32, 16, 8]
sensor_b_reads = [1, 3, 5, 7, 9, 11]
sensor_c_reads = [256, 128, 64, 32]  # Unused sensor path
temporal_weights = [0.1, 0.2, 0.4, 0.2, 0.1]

# Signal processing parameters
THRESHOLD_CEILING = 200
NORMALIZATION_FACTOR = 127.5
shift_magnitude = 3

# Decoy function - appears important but unused
def legacy_calibrate(x):
    return (x * 1.05 + 0.7) % 1.0

def generate_phase_shift(n, depth=2):
    # Complex-looking but deterministic phase generator
    if depth <= 0:
        return 1
    result = 0
    for i in range(n % 5):
        result += (i ^ (n + 2)) % 7
    return (result + generate_phase_shift(n // 3, depth - 1)) % 8

def mask_and_rotate(value, shift):
    # Apply bit manipulation: mask lower bits and rotate
    masked = value & 0b1111111  # Keep lower 7 bits
    rotated = ((masked << shift) | (masked >> (7 - shift))) & 0b1111111
    return rotated

def compute_harmonic_set(fundamental, count):
    # Generate harmonic frequencies (distractor computation)
    harmonics = []
    for i in range(1, count + 1):
        harmonics.append(fundamental * i + CALIBRATION_OFFSET)
    return harmonics

def derive_key_weights(inputs):
    # Derive weights using modular arithmetic and set operations
    squares = {x * x for x in inputs}  # Set comprehension - relevant
    evens = {x for x in inputs if x % 2 == 0}
    diffs = squares - evens  # Set difference operation
    base_weight = sum(diffs) % 100
    
    # Additional weight refinement (mix of relevant and irrelevant)
    adjustment = 0
    for val in inputs:
        if val > 50:
            adjustment += (val // 10) % 3
    
    return base_weight + adjustment

def build_composite_signal(levels, weights):
    # Combine signal levels with weights
    signal = 0
    for i, level in enumerate(levels):
        weight_index = i % len(weights)
        signal_component = (level ^ weights[weight_index]) & 0b111111
        signal += signal_component * (i + 1)
    return signal

def analyze_signal(pattern, criteria):
    # Core analysis with red herrings
    stage_one = pattern ^ 0b10101010  # Bitwise XOR
    stage_two = (stage_one >> 2) & 0b00111111  # Right shift and mask
    
    # Modular arithmetic chain
    mod_chain = stage_two
    mod_chain = (mod_chain * 3) % 89
    mod_chain = (mod_chain + 17) % 101
    mod_chain = (mod_chain * 2) % 97
    
    # Conditional mutation (only one branch is taken)
    if mod_chain > 50:
        mod_chain = (mod_chain // 2) + 25
    else:
        # This branch is actually taken
        mod_chain = (mod_chain * 2) + 13  # Final path
    
    # Final transformation with distractor variables
    reference_set = {13, 26, 39, 52, 65, 78, 91}
candidate_values = {mod_chain, mod_chain+13, mod_chain+26}
overlap = reference_set & candidate_values  # Intersection

    if overlap:
        mod_chain += min(overlap)
    else:
        mod_chain += 7  # Dead code - never reached

    return int(mod_chain)

# Main execution flow
if __name__ == '__main__':
    # Irrelevant audio calibration setup
    concert_A = REFERENCE_FREQ
    tuning_ratio = math.pow(2, 1/12)
    chromatic_scale = [concert_A * math.pow(tuning_ratio, i) for i in range(12)]

    # Real signal construction
    processed_weights = derive_key_weights(sensor_a_reads)
    
    # Simulate pattern generation with bit manipulation
    temp_patterns = []
    for val in sensor_b_reads:
        shifted = mask_and_rotate(val, shift_magnitude)
        phased = shifted ^ generate_phase_shift(val)
        temp_patterns.append(phased)
    
    # Build composite pattern (core input)
    composite_pattern = build_composite_signal(temp_patterns, [processed_weights % 256])
    
    # Create threshold structure (partly irrelevant)
    thresholds = {
        'upper': THRESHOLD_CEILING,
        'normalization': NORMALIZATION_FACTOR,
        'derived': processed_weights
    }
    
    # Apply harmonic analysis (unused)
    dummy_harmonics = compute_harmonic_set(440, 5)
    
    # Critical statement - target of query
    final_diagnostic = analyze_signal(composite_pattern, thresholds)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")