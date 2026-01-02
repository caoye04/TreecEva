import itertools

# Simulated sensor data processing pipeline for aerospace telemetry
raw_readings = [0x1a3, 0x2b4, 0x3c5, 0x4d6, 0x5e7]
offset_correction = 17

def collect_samples(data, threshold=0x300):
    # Irrelevant filtering based on hex threshold
    return [x for x in data if x > threshold]

def apply_mask(sequence, mask=0xFF):
    # Bitwise masking - partially relevant
    masked = [x & mask for x in sequence]
    scaling_factor = 2.5
    adjusted = [x * scaling_factor for x in masked]
    return adjusted

def generate_checksum(values):
    # Dead code path - never used
    chk = 0
    for v in values:
        chk = (chk + v) % 256
    return chk

def integrate_phase_amplitude(signal):
    # Complex transformation with red herring math
    real_part = [int(s) % 100 for s in signal]
    imag_part = [int(s) // 50 for s in signal]
    phasors = []
    for r, i in zip(real_part, imag_part):
        magnitude = (r**2 + i**2)**0.5
        phase = (r + i) % 8  # Simplified phase logic
        phasors.append(magnitude * (phase + 1))
    return phasors

def extract_frequency_bins(phasor_data):
    # Uses itertools - relevant but obscured by noise
    filtered = [p for p in phasor_data if p > 50]
    grouped = [list(group) for k, group in itertools.groupby(filtered, key=lambda x: x//10)]
    bin_sums = [sum(g) for g in grouped]
    
    # Distractor computation
    temp_accumulator = 0
    for i in range(len(bin_sums)):
        temp_accumulator += bin_sums[i] * (i + 1)
    normalization_offset = len(bin_sums) * 12
    return [b - normalization_offset for b in bin_sums]

def compute_entropy_metric(bins):
    # Redundant entropy-like calculation (distraction)
    total = sum(bins) + 1
    entropy = 0
    for b in bins:
        prob = b / total
        if prob > 0:
            entropy -= prob * prob  # Not real entropy, just mimicry
    return abs(entropy * 100)

def validate_frame_integrity(raw):
    # Unused validation function (decoy)
    checksum = 0
    for r in raw:
        checksum ^= r
    return checksum == 0x123

def decode_modulation_scheme(readings):
    # Main relevant transformation chain
    corrected = [r + offset_correction for r in readings]
    masked_signal = apply_mask(corrected)
    phased_data = integrate_phase_amplitude(masked_signal)
    frequency_bins = extract_frequency_bins(phased_data)
    
    # Critical distraction: multiple similar variables
    preliminary_diagnostic = sum(frequency_bins) % 1000
    intermediate_diagnostic = preliminary_diagnostic * 2
    auxiliary_diagnostic = intermediate_diagnostic + 33
    
    return frequency_bins

def analyze_signal(frames):
    # Final analysis with correct result derivation
    score = 0
    for f in frames:
        if f > 0:
            score += f * 0.7
        else:
            score -= f * 0.3
    
    # Misleading complex expression
    adjustment = len(frames) ** 2 * 0.1
    refined_score = score - adjustment
    
    # Final deterministic assignment
    final_diagnostic = int(refined_score + 0.5)
    
    # Dead branch - never executed
    if final_diagnostic < 0:
        fallback = 0
        for c in str(final_diagnostic):
            if c.isdigit():
                fallback += int(c)
        final_diagnostic = fallback
        
    return final_diagnostic

# Orchestration logic
acquired_data = collect_samples(raw_readings)
processed_frames = decode_modulation_scheme(acquired_data)
final_diagnostic = analyze_signal(processed_frames)

# Output result as required
print(f"Result: {final_diagnostic}")