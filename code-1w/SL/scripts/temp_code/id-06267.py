import itertools
from functools import reduce

# Simulated biomedical signal processing pipeline with decoy analytics

def generate_waveform_components(base_freq, harmonics):
    return [base_freq * (i + 1) for i in range(harmonics)]

def compute_coherence_index(signal_a, signal_b):
    # Irrelevant coherence metric (dead computation path)
    return sum(a * b for a, b in zip(signal_a, signal_b)) / 100.0

def analyze_spectral_entropy(frequencies, weights):
    # Distractor function - not used in final calculation
    entropy = 0.0
    for w in weights:
        if w > 0:
            entropy -= w * __import__('math').log(w + 0.1)
    return round(entropy, 3)

def extract_phase_shifts(components, phase_offset=0.5):
    # Unused signal analysis branch
    return [(c * phase_offset) % 1.0 for c in components]

def validate_signal_integrity(raw_sequence):
    # Red herring validation that looks important but isn't used
    checksum = sum(raw_sequence) % 17
    threshold = len(raw_sequence) * 0.7
    return checksum > threshold

# Core diagnostic logic
baseline_readings = [0.8, 1.2, 0.9, 1.5, 1.1]
reference_peaks = {1.0, 1.2, 1.4, 1.6}
decoherence_flags = set()

# Generate multiple irrelevant data streams
noise_floor = tuple((n * 0.01) for n in range(10))
amplitude_envelope = list(map(lambda x: x ** 0.5, baseline_readings))
filtered_baseline = [x for x in baseline_readings if x >= 1.0]

# Complex distractor: nested transformations with partial usage
transform_chain = [
    lambda x: x + 0.1,
    lambda x: x * 1.5,
    lambda x: abs(x - 0.2)
]

intermediate_results = []
for val in baseline_readings:
    temp = val
    for func in transform_chain[:2]:  # Only first two used; third is red herring
        temp = func(temp)
    intermediate_results.append(round(temp, 2))

# Real-time spike detection (partially relevant)
counted_spikes = 0
for reading in baseline_readings:
    if reading > 1.0:
        counted_spikes += 1

# Generate health signature using itertools (actual input source)
signal_windows = list(itertools.combinations(baseline_readings, 3))
window_averages = [sum(window) / 3 for window in signal_windows]
activation_peaks = [w for w in window_averages if w > 1.05]

health_signature = {
    'amplitude': max(baseline_readings),
    'stability': min(baseline_readings),
    'complexity': len(activation_peaks),
    'consistency': reduce(lambda x, y: x + y, [int(p) for p in activation_peaks if p < 2.0], 0)
}

# Decoy correlation matrix (heavy distraction)
correlation_matrix = [[0 for _ in range(5)] for _ in range(5)]
for i in range(5):
    for j in range(5):
        if i != j:
            correlation_matrix[i][j] = (i * j) % 4 + 0.5

# Unused advanced processing branches
spectral_data = generate_waveform_components(440, 8)
phase_shifts = extract_phase_shifts(spectral_data)
coherence_score = compute_coherence_index(spectral_data[:5], baseline_readings)

# Main processing function with critical logic embedded

def process_metrics(signature, readings):
    # Multi-step diagnostic inference
    level_1 = signature['amplitude'] * 100
    level_2 = signature['stability'] * 50
    
    # Key branching logic
    if signature['complexity'] > 2:
        level_2 += 25
    
    # Critical arithmetic chain
    raw_metric = level_1 - level_2
    adjustment_factor = 0
    
    # Conditional bit manipulation decoy
    if raw_metric > 70:
        adjustment_factor = (counted_spikes << 2)  # Uses outer scope variable
    else:
        adjustment_factor = counted_spikes >> 1
    
    # Integration with distractor data
    dummy_offset = sum(noise_floor) * 0.0  # Neutralized but looks active
    
    # Final composition
    aggregated = raw_metric + adjustment_factor + dummy_offset
    
    # Set operation filtering (actually used)
    above_reference = {r for r in readings if r > 1.0}
    reference_match = len(above_reference.intersection(reference_peaks))
    
    # Final adjustment
    aggregated -= reference_match * 5
    
    # This is the true answer path
    return int(aggregated)

# Execute core logic
final_diagnostic = process_metrics(health_signature, baseline_readings)

# Print result as required
print(f"Result: {final_diagnostic}")