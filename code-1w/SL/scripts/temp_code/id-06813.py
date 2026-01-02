import math

# Simulated sensor array diagnostics with interference

def collect_readings():
    raw_signals = [127, 255, 192, 64, 224]
    offset = 3
    adjusted = [sig ^ 0x55 for sig in raw_signals]  # Apply XOR mask
    return adjusted + [sum(adjusted) % 256]  # Append checksum

# Irrelevant signal smoothing function (dead code path)
def smooth_signal(data, factor=0.3):
    smoothed = [data[0]]
    for i in range(1, len(data)):
        smoothed.append(smoothed[-1] * (1 - factor) + data[i] * factor)
    return smoothed

# Data transformation pipeline
def transform_sensor_data(raw_readings):
    scaled = [x * 1.25 for x in raw_readings]
    filtered = [y for y in scaled if y > 100]  # Only high-magnitude signals
    processed = list(map(lambda val: int(val) & 0xFF, filtered))  # Truncate to byte
    return processed

# Baseline calibration with decoy logic
def generate_baseline(n):
    base = []
    for i in range(n):
        temp = (i * 17) % 251
        if temp % 3 == 0:
            base.append(temp // 2)
        else:
            base.append(temp)
    return base[:n]

# Core metric processor (uses lambda and bitwise ops)
def compute_integrity_score(data):
    xor_fingerprint = 0
    for val in data:
        xor_fingerprint ^= (val * 3) & 0xFFFF
    return xor_fingerprint >> 4

# Secondary validation (unused but plausible)
def validate_coherence(data):
    if len(data) < 2:
        return False
    diffs = [abs(data[i+1] - data[i]) for i in range(len(data)-1)]
    avg_diff = sum(diffs) / len(diffs)
    return avg_diff < 150

# Main processing function
def process_metrics(data, baseline):
    # Accumulate weighted deviations
    deviation_sum = 0
    for i in range(min(len(data), len(baseline))):
        weight = 1 + (i % 3)
        deviation_sum += abs(data[i] - baseline[i]) * weight
    
    # Compute secondary indicators (distractors)
    peak_value = max(data) if data else 0
    entropy_proxy = 0
    for x in data:
        if x > 0:
            entropy_proxy += x * math.log(x, 2)
    
    # Critical diagnostic computation chain
    stage_one = deviation_sum * 2
    stage_two = stage_one ^ 0xBEEF
    stage_three = stage_two + sum(data[:3])
    intermediate = (stage_three & 0xFFFF) ^ (stage_three >> 16)
    
    # Final fusion using lambda-based reducer
    fuse = lambda a, b: (a << 1) ^ b
    final_hash = 0
    parts = [intermediate, len(data), peak_value]
    for part in parts:
        final_hash = fuse(final_hash, part)
    
    # Answer derivation
    result = (final_hash * 3) % 987654
    return result

# Irrelevant auxiliary routine (misleading coherence check)
def analyze_pattern(seq):
    if not seq:
        return None
    pattern_mask = 0
    for idx, val in enumerate(seq):
        pattern_mask |= (val << (idx % 8))
    return pattern_mask & 0xFFFF

# --- Execution Sequence ---
readings = collect_readings()  # Step 1: Collect raw sensor data
transformed_data = transform_sensor_data(readings)  # Step 2: Transform
baseline_ref = generate_baseline(len(transformed_data) + 5)  # Step 3: Baseline
baseline_ref = baseline_ref[2:]  # Align length

# Dead code paths (distractors)
signal_trace = smooth_signal(transformed_data)
coherence_flag = validate_coherence(signal_trace)
pattern_sig = analyze_pattern(transformed_data)

# Key statement
final_diagnostic = process_metrics(transformed_data, baseline_ref)

print(f"Result: {final_diagnostic}")