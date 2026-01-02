def analyze_signal(samples, threshold=0.75):
    filtered = [s for s in samples if abs(s) > threshold]
    magnitude_sum = sum(abs(s) for s in filtered)
    peak_count = len([s for s in filtered if s > 0])
    return magnitude_sum / (peak_count + 1e-8)


def generate_reference(size):
    ref = []
    for i in range(size):
        if i % 3 == 0:
            ref.append(i * 0.1)
        elif i % 5 == 0:
            ref.append(-i * 0.05)
        else:
            ref.append(0.0)
    return ref

# Irrelevant transformation chain (distractor)
def transform_data(data):
    temp = [x * 1.5 for x in data]
    temp = [t + 0.1 for t in temp]
    result = []
    for val in temp:
        if val > 1.0:
            result.append(val ** 0.5)
        elif val < -1.0:
            result.append(val ** 2)
        else:
            result.append(val)
    return result

def compute_entropy(seq):
    from math import log
    freq = {}
    for item in seq:
        freq[item] = freq.get(item, 0) + 1
    total = len(seq)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p) if p > 0 else 0
    return entropy

# Core logic with decoys
def validate_calibration(signal, bounds):
    low, high = bounds
    valid_points = [x for x in signal if low <= x <= high]
    ratio = len(valid_points) / len(signal) if signal else 0
    return ratio > 0.6

# Unused function — dead code path (red herring)
def deprecated_calibrate(x):
    return (x + 0.5) ** 2 - 1

# Main processing pipeline
def process_metrics(sequence, flags):
    # Step 1: Extract oscillation pattern
    oscillations = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
    
    # Step 2: Compute weighted phase shift (relevant)
    weights = [abs(o) for o in oscillations]
    phase_shift = sum(o * w for o, w in zip(oscillations, weights))
    
    # Step 3: Apply conditional correction based on flag state (key branching)
    if flags['mode'] == 'AGGRESSIVE' and flags['active']:
        phase_shift *= 1.75
    elif flags['mode'] == 'PASSIVE':
        phase_shift *= 0.4
    else:
        phase_shift *= 1.1
    
    # Step 4: Modulate with cyclic checksum (modular arithmetic)
    checksum = 0
    for idx, val in enumerate(sequence):
        checksum = (checksum + int(val * 10) * (idx + 1)) % 97
    modulated = phase_shift + (checksum * 0.01)
    
    # Step 5: Apply non-linear gain (trigonometric distractor but not used directly)
    _unused_gain = 1 + abs(0.5 * (1 - 0.5 * (1 + __import__('math').cos(phase_shift))))
    
    # Step 6: Final adjustment using list comprehension filter (critical)
    significant = [v for v in sequence if abs(v) > 0.2]
    adjustment_factor = len(significant) * 0.05
    
    # Step 7: Combine into diagnostic score
    raw_diagnostic = modulated + adjustment_factor
    
    # Step 8: Normalize against theoretical max (derived constant)
    theoretical_max = 150.0  # Based on domain constraints
    final_diagnostic = int(raw_diagnostic * 1000) % int(theoretical_max)
    
    # Decoy print statements and unused vars
    _debug_aux = [x for x in sequence if x < 0]
    _temp_cache = {'version': 'legacy', 'status': False}
    
    return final_diagnostic

# Global irrelevant constants (distractors)
MAX_BUFFER_SIZE = 1024
DEFAULT_TIMEOUT = 30
CALIBRATION_OFFSET = -0.012

# Generate real input
calibration_sequence = generate_reference(42)

# Introduce misleading preprocessing (not affecting final result)
decoy_sequence = transform_data(calibration_sequence)
entropy_value = compute_entropy([int(x*10) for x in calibration_sequence if abs(x) > 0.01])

# Flags control actual behavior
diagnostics = {
    'mode': 'AGGRESSIVE',
    'active': True,
    'version': '2.1',
    'timestamp': 1712345678
}

# Execute key statement
final_diagnostic = process_metrics(calibration_sequence, diagnostics)

# Print result as required
print(f"Target result: {final_diagnostic}")