import math

# Simulated sensor array diagnostics with noise filtering and health scoring

def collect_sensor_data():
    raw_readings = [127, 255, 192, 64, 31, 88, 144, 201]
    noise_floor = 32
    adjusted = [x for x in raw_readings if x > noise_floor]
    return adjusted

# Irrelevant auxiliary function - decoy for signal smoothing
def smooth_signal(data, passes=2):
    temp = data.copy()
    for _ in range(passes):
        for i in range(1, len(temp) - 1):
            temp[i] = (temp[i-1] + temp[i] + temp[i+1]) // 3
    return temp  # Never used in critical path

# Misleading intermediate transformation
transform_matrix = lambda xs: [x ^ 0xAA for x in xs]  # Bitwise red herring

# Critical filtering based on entropy threshold
def is_high_entropy(val):
    binary = bin(val)[2:]
    ones = binary.count('1')
    zeros = binary.count('0')
    total = len(binary)
    if total == 0:
        return False
    entropy = -sum(p * math.log2(p) for p in [ones/total, zeros/total] if p > 0)
    return entropy > 0.9

# Decoy statistical analysis (unused)
def compute_skewness(data):
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean)**2 for x in data) / n
    std_dev = variance ** 0.5
    if std_dev == 0:
        return 0.0
    skew = sum(((x - mean) / std_dev)**3 for x in data) / n
    return skew

# Core processing chain
raw_data = collect_sensor_data()

# Distractor: transform using XOR (not actually needed)
masked_data = transform_matrix(raw_data)

# Real filter: select only high-entropy values
filtered_data = [x for x in raw_data if is_high_entropy(x)]

# Fake clustering attempt (dead code path)
def cluster_values(arr, k=3):
    if len(arr) == 0:
        return []
    centroids = arr[:k]
    for _ in range(10):
        groups = [[] for _ in range(k)]
        for val in arr:
            idx = min(range(k), key=lambda i: abs(centroids[i] - val))
            groups[idx].append(val)
    return groups  # Unused

# Health diagnostic engine
health_map = {127: 0.8, 192: 0.85, 144: 0.75, 201: 0.92}

# Primary processing function
def process_readings(readings):
    base_score = 0.0
    contribution = 0
    
    # Complex conditional weighting
    for val in readings:
        bit_length = val.bit_length()
        popcount = bin(val).count('1')
        parity = popcount % 2
        
        # Only certain patterns contribute
        if bit_length >= 7 and parity == 1:
            if val in health_map:
                base_score += health_map[val]
            else:
                base_score += 0.5
            contribution += 1
        
        # Early termination red herring (never triggered due to data)
        if val == 255:
            return -1.0  # Dead path
    
    # Secondary adjustment via set operations
    unique_bits = set(bin(v)[2:] for v in readings)
    pattern_rarity = len(unique_bits) / (1 << 8)  # Artificial rarity score
    
    # Final computation
    adjustment_factor = 1.0 + (pattern_rarity * 0.2)
    final_score = base_score * adjustment_factor
    
    # Normalize by contributions but ensure minimum
    if contribution == 0:
        final_score = 0.1
    
    return int(final_score * 1000)  # Scale to integer

# Execute main logic
intermediate_checksum = sum(transform_matrix([127, 192]))  # Distractor variable

# Key execution point
final_diagnostic = process_readings(filtered_data)

# Additional irrelevant post-processing
snapshot = {"readings": filtered_data, "diagnostic": final_diagnostic}
snapshot["hash"] = sum(ord(c) for c in str(snapshot)) % 1000  # Noise

# Output result
print(f"Result: {final_diagnostic}")