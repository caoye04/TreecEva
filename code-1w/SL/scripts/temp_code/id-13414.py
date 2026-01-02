import itertools

# Simulated sensor data processing system for industrial diagnostics
def collect_signals(channels, duration):
    return [[(i * j + 17) % 97 for j in range(duration)] for i in channels]

# Irrelevant transformation: frequency domain analysis (dead path)
def compute_fft(signal_chunk):
    return [sum(signal_chunk[:k]) * (k % 5) for k in range(1, len(signal_chunk)+1)]

# Misleading intermediate: generates plausible but unused values
def generate_diagnostics(trace, threshold=42):
    count = 0
    for x in trace:
        if x > threshold and x % 3 == 1:
            count += (x ^ 15) & 7
    return count * 1.5  # Never used in final calculation

# Core data alignment function (used)
def align_segments(segment_a, segment_b):
    return [a ^ b for a, b in zip(segment_a, segment_b)]

# Noise reduction via moving average (partially relevant)
def smooth_signal(signal_data, window=3):
    smoothed = []
    for i in range(len(signal_data)):
        start = max(0, i - window + 1)
        smoothed.append(sum(signal_data[start:i+1]) / (i - start + 1))
    return smoothed

# Secondary helper: extracts pattern signature (used)
def extract_signature(data_stream):
    if not data_stream:
        return [0]
    sig = [data_stream[0]]
    for val in data_stream[1:]:
        sig.append((sig[-1] + val) % 101)
    return sig[:len(data_stream)//2 + 1]

# Composite health metric calculator (used)
def evaluate_health_score(readings):
    total = 0
    for i, val in enumerate(readings):
        if i % 4 == 0:
            total += val * 2
        elif i % 3 == 0:
            total -= val // 3
        else:
            total += (val % 7) ^ 5
    return total

# Main processing pipeline (used)
def process_metrics(signature, base):
    # Step 1: reconstruct phase buffer
    phase_buffer = [s ^ (b % 23) for s, b in zip(signature, base)]
    
    # Step 2: apply cyclic redundancy adjustment
    adjusted = [(phase_buffer[i] + phase_buffer[(i+1)%len(phase_buffer)]) % 89 
                for i in range(len(phase_buffer))]
    
    # Step 3: reduce via weighted sum with bit manipulation
    weight_sum = 0
    for idx, val in enumerate(adjusted):
        shift = idx % 6
        weight_sum += (val << 1) ^ (val >> shift) if shift else val
    
    # Step 4: normalize using modular inverse approximation
    normalized = (weight_sum * 17) % 9973
    
    # Step 5: combine with entropy proxy from base
    entropy_proxy = sum(b & (b ^ (b >> 1)) for b in base[:10]) % 1000
    intermediate = (normalized + entropy_proxy) % 5000
    
    # Step 6: finalize through conditional modulation
    if intermediate % 3 == 0:
        final = intermediate * 3 + 1
    elif intermediate % 2 == 0:
        final = intermediate * 2 - 5
    else:
        final = intermediate + 13
    
    # Red herring: call irrelevant diagnostic function
    dummy_result = generate_diagnostics(base, threshold=35)  # No effect
    
    # Red herring: perform useless itertools operation
    _ = list(itertools.accumulate([1, -1]*50, lambda x, y: x*y))  # Distractor
    _ = list(itertools.combinations([2,3,5], 2))  # Unused
    
    return final

# --- Simulation Setup ---
channel_list = [3, 7, 11, 13]
duration_seconds = 12

# Collect raw signals (used)
collected_data = collect_signals(channel_list, duration_seconds)

# Extract primary channel trace (used)
primary_trace = collected_data[0]

# Smooth the signal (used later)
smoothed_primary = smooth_signal(primary_trace, window=4)

# Generate fake alternate paths
alt_traces = [compute_fft(chunk) for chunk in collected_data]  # Dead end
proxy_metrics = [evaluate_health_score(t) for t in alt_traces]  # Unused

# Build baseline reference from secondary transformations
baseline_readings = []
for i in range(4):
    segment = [collected_data[j][i] for j in range(4)]
    aligned = align_segments(segment, segment[::-1])
    baseline_readings.extend(aligned)

# Extract operational signature from smoothed data (used)
health_signature = extract_signature(smoothed_primary)

# Introduce more distractions
phantom_key = sum(1 for x in primary_trace if x > 40 and x % 4 == 2)  # Unused
shadow_buffer = [x | 15 for x in smoothed_primary if x < 50]  # Not used

# Critical computation step
final_diagnostic = process_metrics(health_signature, baseline_readings)

# Print result as required
print(f"Target result: {final_diagnostic}")