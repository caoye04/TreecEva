import itertools
import math

# Simulated biomedical signal processing system with red herrings
def analyze_waveform(signal):
    if not signal:
        return 0
    peak = max(signal)
    trough = min(signal)
    amplitude = (peak - trough) / 2
    # Irrelevant transformation (distractor)
    normalized = [x / (max(signal) + 1e-9) for x in signal]
    filtered = [x for x in signal if x > amplitude]
    return len(filtered)

# Unused decoy function (dead code path)
def compute_harmonic_profile(data):
    total = 0
    for i in range(len(data)):
        total += data[i] % (i + 1) if i % 2 == 0 else 0
    return total

# Core diagnostic engine
def generate_phase_vector(base):
    vector = []
    for i in range(8):
        angle = base + i * math.pi / 4
        vector.append(math.sin(angle) * math.cos(angle))
    return vector

# Misleading utility with partial relevance
def assess_rhythm_pattern(sequence):
    differences = [abs(a - b) for a, b in zip(sequence, sequence[1:])]
    avg_diff = sum(differences) / len(differences) if differences else 0
    # Distraction: complex logic that isn't used in final result
    threshold_map = {i: avg_diff * (1.5 ** i) for i in range(5)}
    anomalies = 0
    for d in differences:
        if d > threshold_map.get(3, 0):
            anomalies += 1
    return anomalies * 2  # Never actually used

# Key processing function
def process_metrics(signature, readings):
    # Extract components from signature (tuple unpacking)
    sig_type, sig_strength, sig_noise = signature
    
    # Destructuring assignment distraction
    reading_vals = [r[0] for r in readings]
    reading_ages = [r[1] for r in readings]
    
    # Real computation begins
    base_score = sig_strength * 100 - sig_noise * 5
    
    # Generate phase space (relevant)
    phase_space = generate_phase_vector(sig_strength * math.pi / 6)
    coherence = sum(abs(x) for x in phase_space if x > 0) / 4
    
    # Set operations - relevant grouping
    high_coherence = {i for i, x in enumerate(phase_space) if abs(x) > 0.4}
    low_coherence = {i for i, x in enumerate(phase_space) if abs(x) <= 0.2}
    overlap = high_coherence & {2, 3, 4, 5}  # Critical intersection
    
    # Bit manipulation red herring
    mask = 0
    for i in sorted(overlap):
        mask |= (1 << i)
    masked_value = mask & 0xFF
    
    # Actual determinant of answer
    age_factor = sum(a for a in reading_ages if a < 65) / (len(reading_ages) or 1)
    adjusted_base = base_score * (1 + coherence * 0.1)
    
    # Final calculation (answer depends on this)
    temp_result = adjusted_base + len(overlap) * 25
    
    # Multiple distractor variables
    entropy_score = -sum(x * math.log(abs(x) + 1e-9) for x in phase_space)
    rhythm_index = assess_rhythm_pattern(reading_vals)
    waveform_metric = analyze_waveform(reading_vals)
    derived_key = itertools.product([1, 2], ['a', 'b'])  # Unused iterator
    
    # Final adjustment using set difference (critical step)
    critical_offset = len(high_coherence - low_coherence)
    final_diagnostic = int(temp_result - age_factor + critical_offset * 2)
    
    return final_diagnostic

# Initialize inputs
health_signature = ('cardiac', 0.67, 12)
baseline_readings = [
    (0.82, 72), (0.31, 68), (0.91, 55), 
    (0.49, 78), (0.63, 63), (0.77, 59)
]

# Execute main logic
final_diagnostic = process_metrics(health_signature, baseline_readings)
print(f"Result: {final_diagnostic}")