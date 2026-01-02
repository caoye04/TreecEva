import math

# System calibration constants (irrelevant to final result)
CALIBRATION_FACTOR = 0.987
REFERENCE_VOLTAGE = 3.3
MAX_ITERATIONS = 1000
EPSILON = 1e-6

# Signal processing parameters
def generate_phase_map(resolution):
    return [math.sin(i * 0.1) + math.cos(i * 0.05) for i in range(resolution)]

def integrate_diagnostics(history, threshold=0.5):
    cumulative = 0
    for val in history:
        if abs(val) > threshold:
            cumulative += val ** 2
    return cumulative

# Irrelevant helper function – dead code path
def deprecated_normalization(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    return [(x - mean_val) / (variance ** 0.5) for x in data]

# Core signal analysis with distractors
def transform_sequence(seq, key):
    # Bit manipulation red herring
    masked_key = key ^ 0b1101 & 0b11111  # irrelevant masking
    shifted = [((x << 2) ^ masked_key) % 256 for x in seq]  # distraction
    return shifted[::2]  # slicing - relevant later

# Frequency warping (unused in final path)
def warp_frequency_domain(signal, factor):
    return [s * math.log(abs(s) + 1) * factor for s in signal]

# Main diagnostic engine
def analyze_signal(buffer, shift):
    # Step 1: Apply transformation with slicing operation
    processed = transform_sequence(buffer, shift)
    
    # Distractor variables
    temp_analysis = [x * 1.5 for x in buffer if x % 2 == 0]
    baseline_rms = sum(x**2 for x in temp_analysis) ** 0.5 if temp_analysis else 0
    
    # Step 2: Set-based filtering - actual relevant logic
    unique_remainders = set(x % 7 for x in processed)  # set operation
    filtered_peaks = [x for x in processed if x % 7 in {1, 2, 4}]
    
    # Step 3: Accumulation through conditional logic
    accumulator = 0
    for idx, val in enumerate(filtered_peaks):
        if idx % 2 == 0:
            accumulator += val * 3
        else:
            accumulator -= val // 4
    
    # Step 4: Logical combination with bitwise interference
    control_flag = len(processed) > 5 and len(unique_remainders) < 6
    adjustment = (shift & 0b101) | 0b11  # bitwise OR/AND red herring
    
    # Step 5: Conditional override based on control logic
    if control_flag:
        intermediate = accumulator ^ 0xAA  # XOR obfuscation
    else:
        intermediate = accumulator + 5000
    
    # Step 6: Final adjustment using summation and combinatorics
    peak_count = len(filtered_peaks)
    combinatoric_factor = 1
    for i in range(1, min(peak_count, 4)):
        combinatoric_factor *= (peak_count - i + 1) // i
    
    # Step 7: Key calculation
    result = intermediate - combinatoric_factor * 13
    
    # Irrelevant logging output
    debug_log = f"Diag: {len(buffer)}, Peaks: {peak_count}, Adjust: {adjustment}"
    
    # Final diagnostic output
    final_result = int(result)  # this will be the answer
    return final_result

# Initialization with decoy data
pattern_buffer = [12, 7, 3, 8, 15, 21, 9, 4]
frequency_shift = 13

# Unused data structures as distractions
decoys = {
    'noise_profile': [0.1, 0.4, 0.8, 1.2],
    'phase_cache': generate_phase_map(50),
    'legacy_modes': ['A', 'B', 'C']
}

historical_traces = [
    [1, 1, 2], [3, 5, 8], [13, 21, 34]  # Fibonacci remnants
]

# Dead computation path - looks important but unused
aggregate_diagnostic = 0
for trace in historical_traces:
    aggregate_diagnostic += integrate_diagnostics(trace, threshold=1.0)

# Critical execution point
final_diagnostic = analyze_signal(pattern_buffer, frequency_shift)

# Output result as required
print(f"Target result: {final_diagnostic}")