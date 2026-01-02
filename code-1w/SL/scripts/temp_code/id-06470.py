import itertools

# Simulated sensor telemetry and fault detection system
def collect_telemetry(base_signal, noise_level):
    raw_samples = [base_signal + ((i * 0.1) % 0.5) for i in range(12)]
    noisy_samples = [x + noise_level * (-1)**i for i, x in enumerate(raw_samples)]
    filtered = [round(x, 3) for x in noisy_samples if abs(x - base_signal) < 0.6]
    return filtered[:8]

def detect_anomalies(samples):
    anomalies = []
    for i in range(1, len(samples)):
        if abs(samples[i] - samples[i-1]) > 0.2:
            anomalies.append(i)
    return anomalies if anomalies else [0]

def compute_entropy(signal):
    # Irrelevant entropy calculation (distractor)
    from math import log2
    counts = {x: signal.count(x) for x in set(signal)}
    total = len(signal)
    entropy = sum(-(c/total) * log2(c/total) for c in counts.values())
    return round(entropy, 4)

def validate_checksum(data):
    # Unused validation function (dead code path)
    checksum = sum(data) * 7 % 13
    return checksum == 5

def generate_combinations(values):
    # Distractor: generates combinations but not used in main logic
    combs = []
    for r in range(2, 4):
        combs.extend(list(itertools.combinations(values, r)))
    return combs

def decode_bit_pattern(flag_list):
    # Decodes list of flags into bit mask (used in fault analysis)
    pattern = 0
    for i, flag in enumerate(flag_list):
        if flag > 0:
            pattern |= (1 << i)
    return pattern & 0xFF

def analyze_system_state(telemetry, faults):
    # Core logic: computes diagnostic score based on signal stability and fault flags
    avg = sum(telemetry) / len(telemetry)
    deviations = [abs(x - avg) for x in telemetry]
    stability_score = 100 * (1 - sum(deviations) / (len(deviations) * 0.5))
    
    # Secondary processing: uses bit pattern from faults
    bitmask = decode_bit_pattern(faults)
    severity = bin(bitmask).count('1')
    
    # Tertiary adjustment: uses itertools to cycle through correction factors
    correction_cycle = itertools.cycle([0.98, 1.02, 0.99])
    adjustment = 1.0
    for _ in range(len(telemetry)):
        adjustment *= next(correction_cycle)
    
    intermediate_result = stability_score * adjustment  # Red herring: looks important
    
    # Final computation
    baseline = 85.0
    risk_factor = severity * 2.5
    final_diagnostic = int(baseline + (intermediate_result - baseline) / 2 - risk_factor)
    
    return final_diagnostic

# Main execution flow
base_input = 0.35
noise = 0.12

telemetry_buffer = collect_telemetry(base_input, noise)
anomaly_list = detect_anomalies(telemetry_buffer)
entropy_metric = compute_entropy(telemetry_buffer)  # Computed but unused

# Generate irrelevant combinatorial data
if len(telemetry_buffer) > 5:
    combinatorial_set = generate_combinations([int(x*100) for x in telemetry_buffer])

# Fault simulation
fault_flags = [0, 1, 0, 0, 1, 1, 0, 2]
fault_flags.extend([0]*8)  # Padding - misleading length

# Checksum test (never called)
cs_valid = False

# Critical execution point
final_diagnostic = analyze_system_state(telemetry_buffer, fault_flags)

print(f"Result: {final_diagnostic}")