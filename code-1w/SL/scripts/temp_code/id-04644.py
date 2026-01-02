import math

# Simulated sensor array data processing with diagnostic evaluation
def collect_readings():
    raw_samples = [i * 0.5 + (i % 7) for i in range(120)]
    offset = 3.14159
    scaled = [x * 1.05 + offset for x in raw_samples]
    return scaled

# Irrelevant helper: simulates temperature drift (not used in final calculation)
def calculate_drift(samples):
    avg = sum(samples) / len(samples)
    drift = [math.sin(x / 10) * 0.1 for x in samples]
    adjusted = [s + d for s, d in zip(samples, drift)]
    return adjusted

# Signal filtering using moving window (partially relevant)
def filter_noise(data):
    window_size = 5
    smoothed = []
    for i in range(len(data) - window_size + 1):
        window = data[i:i+window_size]
        median_val = sorted(window)[window_size // 2]
        smoothed.append(median_val)
    # Truncate to alignment boundary
    trimmed = smoothed[:len(smoothed) - (len(smoothed) % 4)]
    return trimmed

# Data transformation with bit manipulation masking (core relevance)
def transform_frame(sequence):
    # Map to integers via scaling
    ints = [int(abs(x) * 10) % 256 for x in sequence]
    masked = []
    for val in ints:
        # Apply XOR mask based on position
        key = (val ^ (val << 1)) & 255
        key = (key ^ (val >> 2)) & 255
        masked.append(key)
    # Extract every 3rd element as signature
    signature = masked[::3]
    return signature

# Checksum using modular arithmetic and bit counting (distractor)
def compute_checksum(values):
    total = 0
    for v in values:
        bits = bin(v).count('1')
        total = (total + bits * v) % 65536
    return total

# Main analysis function with conditional logic chain
def analyze_signal(buffer):
    size = len(buffer)
    if size < 16:
        return -999
    
    # Conditional branching based on divisibility
    mode_flag = (size % 4 == 0) + 2 * (size % 6 == 0) + 4 * (size % 8 == 0)
    accumulator = 0
    
    if mode_flag & 1:
        segment = buffer[:32]
        for i, val in enumerate(segment):
            if i % 3 == 0:
                accumulator += (val * i) % 100
    elif mode_flag & 2:
        segment = buffer[-24:]
        for i, val in enumerate(reversed(segment)):
            accumulator += (val + i) ** 2
    else:
        accumulator = sum(buffer) // 10
    
    # Additional transformation layer
    temp_result = (accumulator * 7) ^ 0xAAAA
    temp_result ^= (temp_result >> 16)
    
    # Final adjustment using mathematical identity
    final_value = abs(temp_result) % 100000
    return final_value

# Unused diagnostic path (dead code - red herring)
def legacy_diagnostic(data):
    if not data:
        return 0
    score = 0
    for x in data:
        if x > 100:
            score += 1
    return score * len(data)

# Secondary transformation chain (irrelevant)
def augment_sequence(seq):
    augmented = []
    for i, x in enumerate(seq):
        mod = (x + i * 2) % 255
n        augmented.append(mod)
    checksummed = compute_checksum(augmented)
    return augmented, checksummed

# Primary execution flow
if __name__ == "__main__":
    readings = collect_readings()  # 120 elements
    drifted = calculate_drift(readings)  # Computed but unused
    filtered = filter_noise(readings)  # Used
    processed_data = transform_frame(filtered)  # Input to final analysis
    extra_data, chk = augment_sequence(filtered)  # Dead end
    final_diagnostic = analyze_signal(processed_data)
    print(f"Result: {final_diagnostic}")