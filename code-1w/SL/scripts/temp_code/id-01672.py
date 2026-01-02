from collections import defaultdict, Counter
import math

# Simulated sensor array data for a spacecraft subsystem
telemetry_packets = [
    [1.2, 0.9, 1.5, 2.3, 1.1],
    [0.8, 1.0, 1.6, 2.1, 0.9],
    [1.3, 1.1, 1.4, 2.5, 1.2],
    [0.7, 0.8, 1.7, 1.9, 0.85]
]

# Irrelevant auxiliary mapping (distractor)
status_codes = {'OK': 200, 'WARN': 300, 'FAULT': 500, 'CRIT': 600}
code_lookup = defaultdict(lambda: 'UNKNOWN')
for k, v in status_codes.items():
    code_lookup[v] = k

# Misleading transformation chain (dead path)
def legacy_calibrate(data):
    adjusted = []
    for row in data:
        adjusted.append([x * 0.98 + 0.1 for x in row])
    return adjusted  # Never used

# Unused recursive smoother (red herring)
def smooth_recursive(seq, factor=0.3, depth=0):
    if depth >= 3 or len(seq) < 2:
        return seq
    smoothed = [seq[0]]
    for i in range(1, len(seq)):
        smoothed.append(factor * seq[i] + (1 - factor) * smoothed[i-1])
    return smooth_recursive(smoothed, factor, depth + 1)

# Core processing functions
threshold_map = defaultdict(float)
def generate_signature(packets):
    signature = []
    variances = []
    for i, pkt in enumerate(packets):
        avg = sum(pkt) / len(pkt)
        var = sum((x - avg)**2 for x in pkt) / len(pkt)
        variances.append(var)
        if i % 2 == 0:
            signature.append(avg * 1.1)
        else:
            signature.append(avg * 0.95)
    
    # Store intermediate stats (some irrelevant)
    threshold_map['mean_variance'] = sum(variances) / len(variances)
    threshold_map['peak'] = max(variances)
    threshold 
    return [round(x, 3) for x in signature]

baseline_readings = [1.05, 0.92, 1.18, 0.89]

# Complex conditional mapping with decoy logic
def map_diagnostics(vals):
    result = []
    for v in vals:
        if v > 1.2:
            result.append(3)
        elif v > 1.0:
            result.append(2)
        elif v > 0.85:
            result.append(1)
        else:
            result.append(0)
    # Extra logic that seems important but isn't connected
    freq_count = Counter(result)
    dominant = freq_count.most_common(1)[0][0] if freq_count else 0
    return result

# Bit manipulation decoy (irrelevant)
def obfuscate_key(sequence):
    key = 0
    for val in sequence:
        shifted = int(val * 100) << 2
        key ^= shifted
    return key >> 1

obfuscate_key(baseline_readings)  # Called but result unused

# Main metric processor with multiple concerns
def process_metrics(sig, base):
    # Initialize multiple accumulators (some misleading)
    diff_sum = 0.0
    weight_factor = 1.0
    adjustment_log = []
    parity_tracker = defaultdict(int)
    
    for i, (s, b) in enumerate(zip(sig, base)):
        diff = abs(s - b)
        diff_sum += diff
        
        # Seemingly important conditional weight adjustment
        if diff > 0.2:
            weight_factor *= 0.9
            adjustment_log.append(f'Step {i}: Reduced')
        elif diff < 0.05:
            weight_factor *= 1.05
            adjustment_log.append(f'Step {i}: Boosted')
        
        # Bitwise tracking of pattern (appears significant)
        bin_diff = int(diff * 100)
        parity_tracker['xor'] ^= bin_diff
        parity_tracker['or'] |= bin_diff
    
    # Secondary calculation with plausible but unused result
    avg_diff = diff_sum / len(sig)
    severity_score = int(avg_diff * 100)
    
    # Critical distraction: complex-looking but irrelevant transform
    transformed = []
    for x in sig:
        temp = math.sin(x) * math.cos(x)
        normalized = (temp + 1) / 2
        transformed.append(round(normalized * 100))
    
    # Actual answer derivation (non-obvious due to noise)
    diagnostic_code = 0
    for val in parity_tracker.values():
        diagnostic_code += val % 7
    
    # Final computation buried in distractions
    final_diagnostic = int((avg_diff * 1000) + diagnostic_code)
    
    # Additional red herring: case conversion on string version
    str_code = str(final_diagnostic)
    swapped = str_code.swapcase()  # Looks meaningful but unused
    
    return final_diagnostic

# Generate primary signal
health_signature = generate_signature(telemetry_packets)

# Execute main logic
final_diagnostic = process_metrics(health_signature, baseline_readings)

print(f"Result: {final_diagnostic}")