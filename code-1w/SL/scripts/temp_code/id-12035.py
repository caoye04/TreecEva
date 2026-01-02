from collections import defaultdict, Counter
from itertools import cycle, islice

# Simulated sensor data aggregation for a spacecraft subsystem
def collect_telemetry(packets, channel_mask):
    raw_streams = defaultdict(list)
    error_flags = []
    temp_buffer = []

    for pkt in packets:
        node_id = pkt & 0xF
        if node_id & channel_mask:
            raw_streams[node_id].append((pkt >> 4) % 256)
        else:
            error_flags.append(node_id)

    # Irrelevant transformation - distractor
    for k in raw_streams:
        raw_streams[k] = [x for x in raw_streams[k] if x > 10]

    # Decoy function call with side effect that isn't used
    def analyze_entropy(data):
        counts = Counter(data)
        return sum(v * v for v in counts.values())

    entropy_map = {k: analyze_entropy(v) for k, v in raw_streams.items()}

    # Actual relevant processing begins here
    flattened = []
    for stream in raw_streams.values():
        flattened.extend(stream[:len(stream)//2 + 1])  # Take only first half + 1

    return flattened

# Signal conditioning and noise filtering
def apply_window(signal, window_type='hann'):
    n = len(signal)
    if n == 0:
        return [0]
    
    # Unused window types - red herring
    if window_type == 'hann':
        window = [0.5 - 0.5 * (i / (n-1))**2 for i in range(n)]
    elif window_type == 'hamming':
        window = [0.54 - 0.46 * (i / (n-1)) for i in range(n)]
    else:
        window = [1] * n

    # Apply windowing (only hann is actually triggered)
    weighted = [s * w for s, w in zip(signal, window)]
    
    # Distractor: unused statistical moment calculation
    mean_val = sum(weighted) / len(weighted)
    variance = sum((x - mean_val)**2 for x in weighted) / len(weighted)
    skewness = sum(((x - mean_val)/variance)**3 for x in weighted) / len(weighted) if variance > 0 else 0

    return weighted  # Only this matters

# Core diagnostic logic
def generate_baseline(length, seed=1337):
    # Pseudo-random but deterministic sequence using bit manipulation
    state = seed
    result = []
    for _ in range(length):
        state = ((state << 5) + state) ^ 0x23456789
        state = state & 0xFFFFFFFF
        result.append((state >> 16) & 0xFF)
    return result

# Misleading auxiliary function - looks important but unused
def compute_checksum(data):
    chk = 0
    mult_cycle = cycle([1, 3, 7])
    for i, val in enumerate(data):
        chk += val * next(mult_cycle)
    return chk % 65536

# Main processing pipeline
def process_metrics(signature, reference):
    # Step 1: Align lengths
    min_len = min(len(signature), len(reference))
    sig_trim = signature[:min_len]
    ref_trim = reference[:min_len]

    # Step 2: Compute element-wise difference
    diff_vector = [abs(a - b) for a, b in zip(sig_trim, ref_trim)]

    # Step 3: Filter outliers (values more than 2 std devs away)
    mean_diff = sum(diff_vector) / len(diff_vector)
    sq_diffs = [(d - mean_diff)**2 for d in diff_vector]
    std_dev = (sum(sq_diffs) / len(sq_diffs)) ** 0.5
    threshold = 2 * std_dev
    filtered_deltas = [d for d in diff_vector if d <= threshold]

    # Step 4: Detect persistent deviation patterns
    sustained_errors = 0
    for i in range(1, len(filtered_deltas)):
        if filtered_deltas[i] > 1.5 and filtered_deltas[i] == filtered_deltas[i-1]:
            sustained_errors += 1

    # Step 5: Apply weighting based on position (recent errors matter more)
    weights = [0.9 ** i for i in range(len(filtered_deltas))][::-1]
    weighted_sum = sum(d * w for d, w in zip(filtered_deltas, weights))

    # Step 6: Normalize and cap
    norm_factor = sum(weights)
    if norm_factor > 0:
        final_score = weighted_sum / norm_factor
    else:
        final_score = 0.0

    # Step 7: Discretize into diagnostic level
    if final_score < 5.0:
        level = 1
    elif final_score < 15.0:
        level = 2
    elif final_score < 30.0:
        level = 3
    else:
        level = 4

    # Step 8: Combine with pattern count to produce final output
    # This is where the real answer is formed
    final_diagnostic = (level * 1000) + sustained_errors

    # Dead code path - misleading
    debug_info = {}
    if final_diagnostic > 3000:
        debug_info['status'] = 'CRITICAL'
        debug_info['retry_count'] = 3
    else:
        debug_info['status'] = 'STABLE'
        debug_info['retry_count'] = 0  # Never used

    return final_diagnostic

# --- Execution Flow ---
if __name__ == '__main__':
    # Simulated telemetry packets (hex values represent encoded sensor readings)
    telemetry_packets = [
        0x1A3, 0x2B7, 0x1C1, 0x3D5, 0x1E9, 0x2F3, 0x1A7, 0x3B9,
        0x2C3, 0x1D7, 0x3E1, 0x1F5, 0x2A9, 0x3B3, 0x1C7, 0x2D9
    ]
    
    # Extract raw signal
    raw_signal = collect_telemetry(telemetry_packets, channel_mask=0x1)
    
    # Apply noise reduction
    cleaned_signal = apply_window(raw_signal, window_type='hann')
    
    # Generate fixed baseline for comparison
    baseline_readings = generate_baseline(len(cleaned_signal) + 5, seed=1337)[:len(cleaned_signal)]
    
    # Create health signature (add systematic offset to simulate degradation)
    health_signature = [x + 8 for x in cleaned_signal]
    
    # Introduce subtle bias in first few elements - affects mean and thus final score
    for i in range(min(3, len(health_signature))):
        health_signature[i] += 5

    # Critical statement: compute final diagnostic code
    final_diagnostic = process_metrics(health_signature, baseline_readings)
    
    # Output result as required
    print(f"Target result: {final_diagnostic}")
