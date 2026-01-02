import math

# Simulated sensor frame preprocessing with red herrings
def preprocess_frame(frame_data, threshold=0.75):
    amplified = [x * 1.8 for x in frame_data if x > threshold]
    normalized = [val / (max(amplified) + 1e-5) for val in amplified]
    return normalized

# Misleading noise filter (unused in final path)
def denoise_signal(signal, method='moving_avg'):
    if method == 'moving_avg':
        return [sum(signal[i:i+3]) / 3 for i in range(len(signal)-2)]
    elif method == 'median':
        return sorted(signal)[len(signal)//2]
    return signal

# Core transformation: frequency extraction via zero-crossing approximation
def extract_frequency_envelope(signal_chunk):
    if len(signal_chunk) < 2:
        return 0.0
    zero_crossings = 0
    for i in range(1, len(signal_chunk)):
        if signal_chunk[i-1] < 0 <= signal_chunk[i]:
            zero_crossings += 1
    return round(zero_crossings * (1000 / len(signal_chunk)), 4)

# Secondary analysis: entropy approximation (distractor)
def estimate_entropy(data):
    from collections import Counter
    counts = Counter([round(x, 2) for x in data])
    total = sum(counts.values())
    return -sum((freq/total) * math.log2(freq/total) for freq in counts.values())

# Signal combiner with conditional logic and zip usage
def fuse_signals(primary, secondary):
    if len(primary) != len(secondary):
        pad_len = abs(len(primary) - len(secondary))
        if len(primary) < len(secondary):
            primary += [0] * pad_len
        else:
            secondary += [0] * pad_len
    
    fused = []
    for p, s in zip(primary, secondary):
        fused.append(p * 0.7 + s * 0.3)
    return fused

# Frame processor using enumerate and conditional modification
def process_frames_sequential(frames):
    results = []
    for idx, frame in enumerate(frames):
        if idx % 3 == 0:
            transformed = [math.sin(x * 0.1) for x in frame]
        elif idx % 3 == 1:
            transformed = [math.cos(x * 0.1) for x in frame]
        else:
            transformed = [abs(math.tanh(x * 0.05)) for x in frame]
        results.append([val for val in transformed if val > 0.1])
    return results

# Recursive harmonic detector (actual used component)
def detect_harmonic_depth(signal, level=0, max_levels=5):
    magnitude = sum(abs(x) for x in signal) / (len(signal) + 1e-5)
    if level >= max_levels or magnitude < 0.2:
        return level
    boosted = [x * 1.2 for x in signal]
    return detect_harmonic_depth(boosted[::2], level + 1, max_levels)

# Main analyzer that integrates multiple concepts
def analyze_signal(processed_frames):
    # Flatten frames with index tracking
    flat_signal = []
    for i, frame in enumerate(processed_frames):
        for j, val in enumerate(frame):
            if (i + j) % 2 == 0:  # Conditional inclusion
                flat_signal.append(val * (1 + 0.1 * i))

    # Distractor: unused statistical block
    mean_val = sum(flat_signal) / len(flat_signal) if flat_signal else 0
    variance = sum((x - mean_val)**2 for x in flat_signal) / (len(flat_signal) + 1e-5)
    peak_to_peak = max(flat_signal) - min(flat_signal) if flat_signal else 0

    # Key frequency analysis
    freq_signature = extract_frequency_envelope(flat_signal)
    
    # Conditional branching based on frequency band
    if freq_signature < 15.0:
        base_score = 883
    elif freq_signature < 30.0:
        base_score = 1427
    else:
        base_score = 964

    # Recursive depth analysis
    recursive_diagnosis = detect_harmonic_depth(flat_signal[:50] if len(flat_signal) > 50 else flat_signal)
    
    # Bit manipulation mask based on diagnosis
    mask = (base_score << 2) ^ (recursive_diagnosis << 3)
    masked_result = mask & 0xFFFF  # Clamp to 16-bit

    # Final computation with distractor variables
    stability_factor = len(processed_frames) / (recursive_diagnosis + 1)
    entropy_distractor = estimate_entropy(flat_signal)  # Computed but unused
    final_diagnostic = (masked_result + int(stability_factor * 100)) % 10000

    return final_diagnostic

# Unused diagnostic function (dead code path)
def legacy_diagnostic(sequence):
    return sum((i * val) for i, val in enumerate(sequence)) % 5000

# Simulation input data
raw_frames = [
    [1.2, 0.8, -0.3, 0.9, 1.5],
    [0.7, -1.1, 0.4, 0.2],
    [1.3, 0.9, -0.8, 1.0, 0.6, 0.1],
    [-0.2, 0.5, 0.7, 1.4],
    [0.9, -0.6, 0.3]
]

# Preprocessing chain
filtered_frames = [preprocess_frame(frame) for frame in raw_frames]
processed_frames = process_frames_sequential(filtered_frames)

# Signal fusion (creates decoy data)
decoy_primary = [0.5, 0.7, 0.6, 0.8]
decoy_secondary = [0.3, 0.9, 0.4]
fused_test = fuse_signals(decoy_primary, decoy_secondary)

# Critical execution point
final_diagnostic = analyze_signal(processed_frames)
print(f"Result: {final_diagnostic}")