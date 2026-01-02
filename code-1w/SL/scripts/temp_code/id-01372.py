from itertools import combinations
from math import log2

# Simulated biomedical sensor data processing pipeline
def analyze_rhythm(pattern, threshold=0.65):
    if len(pattern) < 3:
        return False
    rhythm_score = sum(1 for a, b in zip(pattern, pattern[1:]) if abs(a - b) < 0.3)
    return rhythm_score / (len(pattern) - 1) > threshold

# Irrelevant helper - distractor function
def calculate_resilience_index(stress_series):
    resilience = 0
    for i in range(len(stress_series)):
        if stress_series[i] > 0.7:
            resilience += log2(stress_series[i] + 1)
    return resilience  # Unused in main logic

# Auxiliary validation (partial use)
def validate_coherence(sequence):
    diffs = [abs(a - b) for a, b in zip(sequence, sequence[1:])]
    median_diff = sorted(diffs)[len(diffs)//2]
    return median_diff < 0.4

# Core transformation chain
def extract_phase_shift(readings):
    shifted = [(r * 1.87) % 1.0 for r in readings]
    filtered = [f for f in shifted if 0.2 < f < 0.8]
    return filtered[:len(filtered)//2] if len(filtered) > 4 else filtered

# Red herring: energy normalization (not used in final path)
def normalize_energy(signal):
    total_energy = sum(s**2 for s in signal)
    if total_energy == 0:
        return [0] * len(signal)
    return [s / total_energy**0.5 for s in signal]

# Key processing function with multiple concepts
def process_metrics(signature, baseline):
    # Step 1: Preprocess signature using bit manipulation simulation
    quantized = [int(s * 128) & 127 for s in signature]  # Scale and mask lower 7 bits
    
    # Step 2: Set operations on derived features
    unique_phases = set(round((q / 127.0), 3) for q in quantized)
    reference_phases = set(round(b, 3) for b in baseline)
    common_modes = unique_phases.intersection(reference_phases)
    
    # Step 3: Conditional data refinement
    if len(common_modes) >= 3:
        adjusted = [v * 1.618 for v in quantized if v % 2 == 1]  # Only odd values scaled
    else:
        adjusted = [v * 0.786 for v in quantized if v % 2 == 0]  # Even values alternative scale
    
    # Step 4: Multiple assignment and destructuring
    total, count, max_val = 0, 0, 0
    for val in adjusted:
        total += val
        count += 1
        if val > max_val:
            max_val = val
    
    # Step 5: Dictionary-based state tracking (used)
    stats = {
        'sum': total,
        'count': count,
        'peak': max_val,
        'ratio': total / count if count else 0
    }
    
    # Step 6: Logical cascade with comparisons and short-circuiting
    meets_strong = stats['ratio'] > 45.0 and stats['peak'] >= 90
    meets_weak = stats['ratio'] > 30.0 or (stats['count'] > 5 and len(common_modes) >= 2)
    
    # Step 7: Final conditional inference
    if meets_strong or (meets_weak and validate_coherence(signature)):
        candidate = int(stats['sum'] // 2)
    else:
        candidate = int(stats['sum'] // 3)
    
    # Step 8: Decoy modification (appears important but unused)
    temp_debug = [candidate ^ 255, candidate & 127, candidate | 64]
    
    # Final result
    return candidate

# --- Distractor Data Section ---
stress_tests = [
    [0.88, 0.76, 0.91, 0.83],
    [0.65, 0.72, 0.68],
    [0.95, 0.99, 0.87, 0.93, 0.90]
]
for test in stress_tests:
    idx = calculate_resilience_index(test)  # Dead code path

# --- Main Execution with Red Herrings ---
baseline_readings = [0.123, 0.456, 0.789, 0.234, 0.567]
signal_chain = [0.124, 0.455, 0.890, 0.233, 0.678, 0.345]

# Unused transformation - misleading intermediate
transformed = extract_phase_shift(signal_chain)
decoy_combinations = list(combinations(transformed, 3))  # Computation with no impact

# Generate health signature with subtle rounding dependencies
health_signature = []
for x in signal_chain:
    processed = (x ** 2 + 0.11) % 1.0
    if processed > 0.05:
        health_signature.append(round(processed, 3))

# Introduce decoy dictionary operation
snapshot = {
    'readings': len(health_signature),
    'version': '2.1a',
    'calibrated': False
}
snapshot['diagnostics'] = {k: v for k, v in stats.items()} if 'stats' in vars() else None  # Refers to undefined

# Critical execution point
final_diagnostic = process_metrics(health_signature, baseline_readings)

# Output result as required
print(f"Result: {final_diagnostic}")