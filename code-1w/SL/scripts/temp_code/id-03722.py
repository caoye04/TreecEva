import math

# Simulated sensor array data processing with diagnostic evaluation

def collect_samples(duration_ms: int) -> list:
    samples = []
    for t in range(0, duration_ms, 10):
        # Irrelevant waveform - red herring
        noise = math.sin(t * 0.05) * math.cos(t * 0.02)
        signal = math.sin(t * 0.1 + noise) + 0.5 * math.sin(t * 0.3)
        samples.append(round(signal * 100) / 100)
    return samples[:50]  # Truncate to fixed size

# Decoy function - never called but looks important
def compute_coherence(data1, data2):
    mean1 = sum(data1) / len(data1)
    mean2 = sum(data2) / len(data2)
    cov = sum((data1[i] - mean1) * (data2[i] - mean2) for i in range(len(data1)))
    var1 = sum((x - mean1)**2 for x in data1)
    var2 = sum((y - mean2)**2 for y in data2)
    return cov / (math.sqrt(var1 * var2) + 1e-8)

# Auxiliary transformation - actually used but partially distracting
def normalize_signal(signal: list) -> list:
    max_val, min_val = max(signal), min(signal)
    if max_val == min_val:
        return [0.0 for _ in signal]
    return [(x - min_val) / (max_val - min_val) for x in signal]

# Bit manipulation decoy - looks critical but unused
def pack_sample(value: float) -> int:
    scaled = int((value + 2) * 1000)  # Assume offset encoding
    parity = bin(scaled).count('1') % 2
    return (scaled << 1) | parity

# String-based status encoder - irrelevant but plausible
def encode_status(code: int, time_tag: str) -> str:
    hex_code = hex(code)[2:].upper().zfill(4)
    reversed_tag = time_tag[::-1]
    return f"{hex_code}:{reversed_tag[:6]}"

# Real processing chain - core logic hidden among distractors
def detect_spike_clusters(seq: list, window_size: int) -> int:
    count = 0
    for i in range(len(seq) - window_size + 1):
        window = seq[i:i + window_size]
        avg = sum(window) / len(window)
        if all(x > avg * 1.8 for x in window):
            count += 1
    return count

# Recursive pattern analyzer - part of actual computation
def count_oscillations(data: list, index: int = 1, direction: int = 0) -> int:
    if index >= len(data):
        return 0
    current_dir = 1 if data[index] > data[index-1] else (-1 if data[index] < data[index-1] else 0)
    increment = 1 if direction != 0 and current_dir != 0 and current_dir != direction else 0
    return increment + count_oscillations(data, index + 1, current_dir)

# Main analysis function - only this matters for final result
def analyze_pattern(raw_sequence: list, threshold: float) -> float:
    # Step 1: Normalize relevant data
    processed = normalize_signal(raw_sequence)
    
    # Step 2: Extract features - one is relevant, others are distractions
    spike_clusters = detect_spike_clusters(processed, 3)
    oscillation_count = count_oscillations(processed)
    
    # Step 3: Compute entropy-like measure using slicing
    slice_a = processed[::2][:10]  # Even indices
    slice_b = processed[1::2][:10]  # Odd indices
    divergence = sum(abs(a - b) for a, b in zip(slice_a, slice_b))
    
    # Step 4: Apply threshold filtering on oscillations
    filtered_osc = oscillation_count if oscillation_count > 5 else 5
    
    # Step 5: Use string method as red herring
    status_flag = encode_status(0x7B2A, "2023-12-07T14:22:33")
    flag_value = int(status_flag.split(':')[0], 16)  # Extract hex part
    
    # Step 6: Actual key computation
    base_score = divergence * 100
    adjustment = (spike_clusters * 7) - (flag_value % 9)  # Small tweak
    final_score = base_score + adjustment
    
    # Step 7: Threshold-based classification
    if final_score > threshold * 1000:
        diagnostic = 864.23
    else:
        diagnostic = 432.17
    
    # Step 8: Final override based on recursive result
    if oscillation_count >= 12:
        diagnostic = 729.51  # Overwrites previous
    
    return round(diagnostic, 2)

# --- Execution Body ---

# Irrelevant initialization
sensor_id = "SNSR-7X"
deployment_zone = "Grid-9"
timestamp_log = [
    "2023-12-07 14:22:33",
    "2023-12-07 14:22:43",
    "2023-12-07 14:22:53"
]

# Generate raw data
raw_signal = collect_samples(500)

# Unused transformation path - dead code branch
if len(raw_signal) > 100:
    packed_data = [pack_sample(val) for val in raw_signal]
    packed_data.reverse()

# Normalize for real use
signal_sequence = normalize_signal(raw_signal)

# Dead loop - no effect
buffer = []
for item in timestamp_log:
    encoded = encode_status(0x1C84, item)
    buffer.append(encoded)

# Key statement
final_diagnostic = analyze_pattern(signal_sequence, threshold=0.65)

# Output result
print(f"Result: {final_diagnostic}")