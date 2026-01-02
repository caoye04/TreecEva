from collections import defaultdict, Counter
import math

# Simulated sensor data processing with red herrings and complex routing

def preprocess_segment(segment):
    """Irrelevant preprocessing: applies unused transformation."""
    return [x * 1.05 for x in segment]

def dummy_filter(sequence):
    """Dead function: never called but looks important."""
    return [math.sqrt(y) for y in sequence if y > 0]

def accumulate_energy(signal):
    # Real but misleading intermediate: energy sum distracts from actual logic
    return sum(x ** 2 for x in signal)

def extract_peaks(data, limit=5):
    # Distractor: finds peaks but used only to populate irrelevant metric
    peaks = []
    for i in range(1, len(data) - 1):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            peaks.append(data[i])
    return peaks[:limit]

def build_frequency_map(pattern):
    # Relevant: counts digit frequencies in flattened pattern
    flat = [d for row in pattern for d in row]
    return Counter(flat)

def compute_entropy(values):
    # Looks important but unused; decoy scientific measure
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log2(p) for p in probs)

def validate_coherence(seq):
    # Unused validation that seems critical
    return all(seq[i] <= seq[i+1] for i in range(len(seq)-1))

def analyze_signal(buffer, thresholds):
    # Core logic hidden among distractions
    frequency_profile = build_frequency_map(buffer)
    
    # Decoy analysis
    peak_values = extract_peaks([sum(row) for row in buffer])
    energy_signature = accumulate_energy([sum(row) for row in buffer])
    entropy_metric = 0.0
    if len(peak_values) > 0:
        entropy_metric = compute_entropy(peak_values)
    
    # Critical path: find most frequent digit
    most_common_digit = frequency_profile.most_common(1)[0][0]
    
    # Threshold comparison using map that contains red herring keys
    base_threshold = thresholds.get('reference', 7)
    adjustment = thresholds.get('delta', 0)
    scale_factor = thresholds.get('nonlinear_scale', 1)  # unused distraction
    
    # Actual decision logic (obscured)
    if most_common_digit >= base_threshold + adjustment:
        diagnostic_code = 307
    else:
        diagnostic_code = 184
    
    # Inject meaningless transformations to obscure flow
    diagnostic_code = diagnostic_code ^ 12  # XOR obfuscation
    diagnostic_code = int(diagnostic_code * 1.0)  # no-op type consistency
    
    # Final computation
    final_value = diagnostic_code + len([v for v in frequency_profile.values() if v > 2])
    
    return final_value

# Irrelevant global variables
SYSTEM_TOLERANCE = 0.023
CALIBRATION_SEQUENCE = [0.1, 0.4, 0.7]
MAX_ITERATIONS = 15

# Input data with meaningful structure
pattern_buffer = [
    [3, 7, 7, 2],
    [7, 1, 9, 7],
    [4, 7, 3, 7],
    [7, 7, 0, 5]
]

# Threshold map with red herring keys
threshold_map = {
    'reference': 6,
    'delta': 1,
    'nonlinear_scale': 2.5,
    'safe_margin': 0.95,
    'version': 3
}

# Unused signal transform (dead code path)
transformed_patterns = []
for segment in pattern_buffer:
    processed = preprocess_segment(segment)
    transformed_patterns.append(processed)

# Energy analysis on raw and transformed (distraction)
signal_energy_raw = accumulate_energy([item for row in pattern_buffer for item in row])
signal_energy_proc = accumulate_energy([item for row in transformed_patterns for item in row])

# Fake coherence check
coherence_flag = validate_coherence([len(row) for row in pattern_buffer])

# Main execution point — where real answer is computed
final_diagnostic = analyze_signal(pattern_buffer, threshold_map)

# Output result as required
print(f"Target result: {final_diagnostic}")