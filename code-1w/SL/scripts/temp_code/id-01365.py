import math

# Network simulation with complex preprocessing and distractors
def generate_checksum(data):
    return sum(d % 7 for d in data) * 3

def deprecated_routing(nodes):
    # Dead function - never called
    return [n ^ 5 for n in nodes if n % 2 == 0]

def analyze_packet_frequencies(packets):
    freq_map = {}
    for p in packets:
        freq_map[p] = freq_map.get(p, 0) + 1
    sorted_keys = sorted(freq_map.keys())
    return [freq_map[k] for k in sorted_keys]

# Distractor: irrelevant audio processing analogy
def calculate_harmonics(frequency):
    harmonics = []
    for i in range(1, 5):
        harmonics.append(round(frequency * i / math.pi, 2))
    return harmonics

# Core logic disguised among red herrings
latency_weights = [0.8, 1.2, 0.9, 1.1]
dummy_stats = {'max': 999, 'min': -444, 'temp': 12345}

# Simulated packet chunks (some used, some not)
raw_chunks = [128, 256, 192, 320, 384]
filtered_chunks = [c for c in raw_chunks if c > 150]
scaled_chunks = [int(c * 1.5) for c in filtered_chunks]

# Unused transformation path (distractor)
encoded_stream = list(map(lambda x: (x << 2) ^ 0xFF, scaled_chunks))

# Real data path begins here
compression_mask = set([256, 384, 512])
active_chunks = [c // 2 for c in raw_chunks if c in compression_mask]

# Latency profile with misleading but valid calculations
base_latency = 42
latency_profile = [base_latency * w for w in latency_weights]
latency_correction = sum(l * 0.1 for l in latency_profile if l > 45)
adjusted_latency = [l - latency_correction for l in latency_profile]

# Key function containing relevant logic and distractions
def optimize_transmission(data_parts, lag_profile):
    # Irrelevant pre-checks
    if len(data_parts) < 2:
        return -1
    
    # Distractor: unused combinatorics
    from functools import reduce
    combination_factor = reduce(lambda a, b: a * b % 100, data_parts, 1) if data_parts else 0
    
    # Real accumulation logic hidden in middle
    total_volume = sum(data_parts)
    efficiency_ratio = len(data_parts) / 4.0
    
    # Apply weighted latency penalty
    penalty = 0
    for i, lag in enumerate(lag_profile):
        if i % 2 == 0:
            penalty += lag * 0.05
        else:
            penalty += lag * 0.03
    
    # Final bandwidth calculation (depends only on total_volume and penalty)
    initial_bw = total_volume * 10
    adjusted_bw = int(initial_bw - (initial_bw * penalty / 100))
    
    # Dead code branch (never reached due to return)
    if adjusted_bw < 0:
        return abs(adjusted_bw) * 2
        extended = [adjusted_bw + i for i in range(5)]
        return sum(extended)
    
    return adjusted_bw

# Auxiliary function that looks important but isn't used
def validate_transmission_integrity(signal):
    signal_str = ''.join(str(s) for s in signal)
    checksum = sum(ord(c) for c in signal_str if c.isdigit())
    return checksum % 17 == 0

# Execution flow
chunk_sets = {
    'A': raw_chunks,
    'B': filtered_chunks,
    'C': active_chunks
}

# Critical statement
final_bandwidth = optimize_transmission(chunk_sets['C'], latency_profile)

# Print result as required
print(f"Result: {final_bandwidth}")