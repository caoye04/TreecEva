from collections import defaultdict, Counter
import math

# Simulated sensor array data for a distributed health monitoring system
def generate_telemetry():
    return [62, 45, 78, 33, 91, 44, 67, 29, 88, 53]

# Irrelevant helper: computes geometric mean (not used in final path)
def geometric_mean(data):
    product = 1
    for x in data:
        product *= x
    return product ** (1 / len(data))

# Distraction function: analyzes outliers but returns unused result
def analyze_outliers(signal):
    avg = sum(signal) / len(signal)
    deviations = [abs(x - avg) for x in signal]
    threshold = avg * 0.5
    outliers = [x for x in signal if abs(x - avg) > threshold]
    outlier_map = defaultdict(int)
    for val in outliers:
        outlier_map[val] += 1
    return dict(outlier_map)  # Never used

# Core transformation: applies wavelet-like decomposition (simplified)
def decompose_signal(readings):
    transformed = []
    for i in range(len(readings) - 1):
        diff = readings[i+1] - readings[i]
        smoothed = (readings[i] + readings[i+1]) // 2
        transformed.append((diff * smoothed) % 19)
    return transformed

# Auxiliary checksum: Fletcher-style accumulation (distractor)
def fletcher_checksum(data):
    sum1, sum2 = 0, 0
    for val in data:
        sum1 = (sum1 + val) % 255
        sum2 = (sum2 + sum1) % 255
    return (sum2 << 8) | sum1

# Main metric processor: combines multiple analysis strands
def process_metrics(signature, baseline):
    # Step 1: unpack signature tuple
    level, flags, mode = signature
    
    # Step 2: apply bit manipulation on mode (relevant)
    mode_adjusted = (mode ^ 0b1010) & 0b1111
    
    # Step 3: filter baseline using list comprehension (relevant)
    filtered = [x for x in baseline if x % 2 == 1]  # Keep odds
    
    # Step 4: compute weighted contribution
    weight = 0
    for i, val in enumerate(filtered):
        if i % 3 == 0:
            weight += val // 4
    
    # Step 5: transform baseline
    processed = decompose_signal(baseline)
    
    # Step 6: count frequency clusters (using Counter - relevant)
    freq = Counter(processed)
    cluster_score = sum(v for k, v in freq.items() if k < 7)
    
    # Step 7: compute phase shift from flags (bitwise logic)
    phase_shift = 0
    if flags & 0b100:
        phase_shift += 3
    if flags & 0b010 and not (flags & 0b001):
        phase_shift += 2
    
    # Step 8: combine into diagnostic (this is the real answer)
    intermediate = (level * 7) + cluster_score - weight
    final_diagnostic = intermediate + phase_shift
    
    # === DISTRACTION BLOCK BELOW ===
    # Dead code path: never executed due to fixed condition
    if len(baseline) < 5:
        alt_path = [math.log(x) for x in baseline]
        temp_hash = fletcher_checksum([int(x) for x in alt_path])
        final_diagnostic = temp_hash  # unreachable
    
    # Unused variables to mislead
    dummy_1 = geometric_mean(baseline)
    dummy_2 = analyze_outliers(baseline)
    dummy_3 = fletcher_checksum([x * 2 for x in baseline])
    
    # Red herring assignment
    final_diagnostic_temp = (level + mode_adjusted) * 1000  # looks important
    
    return final_diagnostic  # Only this matters

# Setup: realistic initialization of system state
baseline_readings = generate_telemetry()
health_signature = (13, 0b110, 12)  # level=13, flags=6, mode=12

# Execution point of interest
final_diagnostic = process_metrics(health_signature, baseline_readings)
print(f"Target result: {final_diagnostic}")