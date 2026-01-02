import math

# Simulated sensor data preprocessing with red herrings
def acquire_signal(raw_samples):
    offset = 0.003
    gain = 1.05
    calibrated = [(x * gain + offset) for x in raw_samples]
    return [val for val in calibrated if val > 0.1]  # filtering noise

# Irrelevant transformation: spectral mirroring (unused path)
def mirror_spectrum(data):
    reversed_part = data[::-1]
    return [a + b for a, b in zip(data, reversed_part)]

# Data shifting function with misleading normalization (distractor)
def shift_phase(signal, phase=1):
    shifted = [signal[(i + phase) % len(signal)] for i in range(len(signal))]
    norm_factor = sum(shifted) / len(shifted)
    return [s / norm_factor for s in shifted]

# Core transformation: apply logarithmic compression and edge detection
def compress_logarithmic(vals):
    compressed = []
    for v in vals:
        if v > 0:
            compressed.append(math.log(v * 100 + 1))
        else:
            compressed.append(0)
    return compressed

# Edge detection via difference thresholding
def detect_edges(seq, delta_threshold=0.75):
    edges = []
    for i in range(1, len(seq)):
        if abs(seq[i] - seq[i-1]) > delta_threshold:
            edges.append(i)
    return edges

# Secondary analysis: computes irrelevant harmonic alignment score (decoy)
def compute_harmonic_score(edges):
    if len(edges) < 2:
        return 0
    diffs = [edges[i] - edges[i-1] for i in range(1, len(edges))]
    avg = sum(diffs) / len(diffs)
    variance = sum((d - avg) ** 2 for d in diffs) / len(diffs)
    return round(avg * (1 + variance), 4)

# Real processing chain — only this matters for final answer
def transform_sequence(init_seq):
    # Step 1: basic scaling
    scaled = [x * 1.8 for x in init_seq]
    
    # Step 2: filter outliers
    mean_val = sum(scaled) / len(scaled)
    filtered = [v for v in scaled if abs(v - mean_val) < 1.2]
    
    # Step 3: square and shift
    processed = [(v ** 2) - 0.5 for v in filtered]
    
    # Step 4: discretize into bins
    binned = [int(p * 2) for p in processed]
    
    # Step 5: remove duplicates while preserving order
    unique_binned = []
    seen = set()
    for item in binned:
        if item not in seen:
            seen.add(item)
            unique_binned.append(item)
    
    return unique_binned

# Misleading frequency analysis (dead code path)
def analyze_frequency(pattern):
    freq_map = {}
    for p in pattern:
        freq_map[p] = freq_map.get(p, 0) + 1
    sorted_freq = sorted(freq_map.items(), key=lambda x: -x[1])
    return sorted_freq[0][0] if sorted_freq else None

# Critical diagnostic function determining final result
def analyze_pattern(nums, limit):
    total = 0
    factor = 1
    for idx, num in enumerate(nums):
        if idx % 2 == 0:
            total += num * factor
        else:
            total -= num // (factor + 1)
        if total > limit:
            factor *= 2
    return abs(total)

# === MAIN EXECUTION WITH DISTRACTORS ===
if __name__ == '__main__':
    # Initial dataset
    base_readings = [0.45, 0.67, 0.23, 0.89, 0.55, 0.33, 0.78]

    # Distractor 1: Acquire signal (used but leads nowhere critical)
    calibrated_readings = acquire_signal(base_readings)
    
    # Distractor 2: Mirror spectrum (computed but unused)
    mirrored = mirror_spectrum(calibrated_readings)
    
    # Distractor 3: Phase shift (assigned but not used in main flow)
    phased = shift_phase(mirrored, phase=2)
    
    # Distractor 4: Harmonic analysis on fake edges
    fake_compressed = compress_logarithmic(phased)
    fake_edges = detect_edges(fake_compressed, 0.6)
    alignment_score = compute_harmonic_score(fake_edges)  # dead end
    
    # REAL DATA FLOW starts here
    transformed_data = transform_sequence(base_readings)  # This is critical
    
    # Additional red herring: frequency analysis (called but result ignored)
    dominant_value = analyze_frequency(transformed_data)
    
    # Key execution point
    threshold = 15
    final_diagnostic = analyze_pattern(transformed_data, threshold)
    
    # Output target result
    print(f"Result: {final_diagnostic}")