import itertools

# Simulated biomedical signal processing pipeline with decoy analytics
def analyze_waveform(signal):
    if len(signal) < 5:
        return 0
    amplified = [x * 2.5 for x in signal]
    filtered = [y for y in amplified if y > 3]
    return len(filtered)

# Irrelevant auxiliary function (dead code path)
def compute_harmonic_chains(values):
    total = 0
    for i in range(1, len(values) + 1):
        total += 1 / i  # harmonic series accumulator
    return round(total, 4)

# Core transformation logic with distractors
def generate_phase_shift(pattern):
    shifted = []
    for i, val in enumerate(pattern):
        if i % 2 == 0:
            shifted.append(val + (i * 1.1))
        else:
            shifted.append(val - (i * 0.9))
    return shifted

# Decoy statistical analysis (misleading intermediate)
def evaluate_entropy(data):
    from math import log2
    freq_map = {}
    for item in data:
        freq_map[item] = freq_map.get(item, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq_map.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 3)

# Real processing chain buried under noise
def extract_diagnostic_key(sequence):
    base_offset = sum(sequence) // len(sequence)
    mod_sequence = [(x + base_offset) % 7 for x in sequence]
    grouped = {k: list(g) for k, g in itertools.groupby(sorted(mod_sequence))}
    score = 0
    for k, group in grouped.items():
        if k % 3 == 0 and len(group) >= 2:
            score += k * len(group)
    return score

# Primary metric processor (key function)
def process_metrics(signature, thresholds):
    temp_result = 0
    for i, val in enumerate(signature):
        if val in thresholds and i % 2 == 1:
            temp_result += thresholds[val] * (i + 1)
    return temp_result + extract_diagnostic_key(signature)

# === BEGIN: High interference setup ===

# Distractor variables (irrelevant data structures)
baseline_readings = [0.8, 1.2, 1.9, 2.1, 1.8, 0.9]
anomaly_catalog = {'A1': 0.5, 'B2': 1.3, 'C3': 0.7}
reference_grid = [[i + j*3 for i in range(4)] for j in range(3)]

# Fake diagnostic trace (red herring)
current_state = "STABLE"
if sum(baseline_readings) > 6:
    current_state = "MONITORING"

# Real input construction buried in noise
temporal_signal = [4, 7, 2, 9, 5]
health_signature = generate_phase_shift(temporal_signal)  # actual use

# Unused transformations (decoy processing)
spectral_analysis = [x**2 for x in baseline_readings if x > 1]
peak_indices = [i for i, x in enumerate(spectral_analysis) if x > 2]

# Misleading intermediate results
effective_amplitude = analyze_waveform([1, 2, 3])
structural_entropy = evaluate_entropy([1, 1, 2, 3, 3, 3])
harmonic_weight = compute_harmonic_chains([1, 2, 3, 4])

# Critical parameter map (used in final calculation)
threshold_map = {
    4: 3,
    5.1: 2,
    6.2: 5,
    8.3: 4,
    9.4: 1
}

# Spurious reassignments (distraction)
health_signature[0] = 4.0  # overwrites first element
health_signature.append(3.5)
health_signature = [round(x, 1) for x in health_signature]

# Key execution point — answer depends on this call
final_diagnostic = process_metrics(health_signature, threshold_map)

# Output requirement
print(f"Target result: {final_diagnostic}")