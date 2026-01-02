import math

# Simulated sensor data processing with embedded diagnostics
def collect_readings():
    raw_stream = [18, 22, 14, 30, 26, 10, 34, 20, 28, 16]
    offset = 5
    adjusted = [x + offset for x in raw_stream]  # Misleading adjustment (not used in final path)
    return raw_stream

# Irrelevant helper: spectral weight calculation (dead code)
def compute_spectral_weight(seq):
    total = 0
    for i, val in enumerate(seq):
        total += val * (i % 4 + 1) ** 1.5
    return round(total, 3)

# Signal conditioner with slicing and distractor paths
def filter_noise(data):
    window_size = 3
    smoothed = []
    for i in range(len(data) - window_size + 1):
        segment = data[i:i+window_size]
        avg = sum(segment) // len(segment)
        smoothed.append(avg)
    return smoothed[::2]  # Return every other element — actual usage

# Decoy function: appears important but unused
def validate_coherence(signal):
    if len(signal) == 0:
        return False
    score = 0
    for a, b in zip(signal, signal[1:]):
        score += abs(a - b)
    return score < 50

# Real processing step: amplitude normalization
def normalize_amplitudes(fragments):
    normalized = []
    base_ref = fragments[0] if fragments else 1
    for val in fragments:
        ratio = val / (base_ref + 1e-8)
        normalized.append(int(ratio * 10))
    return normalized

# Data segmentation using enumerate and slicing distractions
def segment_data(stream):
    chunks = []
    for idx, val in enumerate(stream):
        if idx % 3 == 0:
            chunk = stream[idx:idx+4]
            if len(chunk) >= 3:
                chunks.append(chunk)
    # Chunks are overbuilt; only first one matters later
    return chunks

# Core analysis: derives diagnostic from processed segments
def analyze_signal(segments):
    if not segments:
        return -1
    
    # Only the first segment is actually used
    primary = segments[0]
    
    # Compute diagnostic using mixed arithmetic and modular steps
    product = 1
    for x in primary:
        product = (product * x) % 97  # Modular arithmetic to avoid overflow
    
    sum_sq = sum(x ** 2 for x in primary)
    mean_val = sum(primary) / len(primary)
    fluctuation = sum(abs(a - b) for a, b in zip(primary, primary[1:]))
    
    # Actual formula: combines product mod, fluctuation, and length
    magic_offset = 1234
    intermediate = (product + fluctuation * len(primary))
    final_score = magic_offset + intermediate - int(mean_val)
    
    # Red herring: unrelated transformation tree below
    transform_tree = []
    temp = final_score
    while temp > 100:
        temp //= 3
        transform_tree.append(temp * 2)  # Dead computation branch
    
    # Final result derived purely from earlier logic
    return final_score

# Unused complexity: recursive hierarchy builder (distractor)
def build_hierarchy(arr):
    if len(arr) <= 1:
        return arr[0] if arr else 0
    mid = len(arr) // 2
    left = build_hierarchy(arr[:mid])
    right = build_hierarchy(arr[mid:])
    return left * 2 + right

# Main execution flow
if __name__ == "__main__":
    readings = collect_readings()  # Original: [18, 22, 14, 30, 26, 10, 34, 20, 28, 16]
    filtered = filter_noise(readings)  # Results: [21, 22, 23, 21, 26] → then [21, 23, 26]
    normalized = normalize_amplitudes(filtered)  # Normalizes relative to 21 → [10, 10, 12]
    segments = segment_data(normalized)  # Builds overlapping chunks; returns multiple
    
    # Critical statement
    final_diagnostic = analyze_signal(processed_segments=segments)
    
    # Print required output
    print(f"Result: {final_diagnostic}")