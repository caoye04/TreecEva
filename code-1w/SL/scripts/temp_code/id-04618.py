import math

def analyze_signal(samples, threshold=100):
    # Irrelevant signal processing function (dead code path)
    filtered = [x for x in samples if abs(x) > threshold]
    return [math.sin(x / 10) for x in filtered]


def shift_register(state, rotation):
    # Bit manipulation red herring
    shifted = (state << 3) | (state >> (rotation - 3))
    masked = shifted & 0xFFFF
    return masked ^ 0xAAAA


def compute_entropy(data):
    # Unused entropy calculation (distractor)
    total = sum(data)
    probabilities = [v / total for v in data if v > 0]
    return -sum(p * math.log2(p) for p in probabilities)


def validate_sequence(seq):
    # Misleading validation with side effects
    checksum = 0
    for i, val in enumerate(seq):
        if i % 5 == 0:
            checksum += val % 7
        elif i % 5 == 2:
            checksum -= (val >> 2)
    return checksum == 0


def aggregate_metrics(log_entries, flags):
    base_score = 0
    penalty = 0

    # Real logic begins: extract timing anomalies
    anomalies = [entry['delay'] for entry in log_entries if entry['delay'] > 50]

    # Compute base score using list comprehension and filtering
    valid_entries = [e for e in log_entries if e['status'] != 'failed']
    if len(valid_entries) > 0:
        avg_normal = sum(e['delay'] for e in valid_entries) / len(valid_entries)
        base_score = int(avg_normal * 1.5)

    # Apply penalties based on fault flags using bitwise analysis
    active_faults = 0
    for flag in flags:
        if (flag & 0x0F) > 0:  # Check lower nibble
            active_faults += 1

    # Red herring: complex bit shifting that doesn't affect final result
    decoy_state = 0x1234
    for _ in range(3):
        decoy_state = shift_register(decoy_state, 16)

    # Real penalty logic
    critical_flags = [f for f in flags if f in {0x101, 0x102, 0x104}]
    penalty = len(critical_flags) * 12

    # Diagnostic override check (never triggers - dead logic path)
    overrides = {k: v for k, v in globals().items() if 'OVERRIDE' in k}
    if 'DIAG_OVERRIDE' in overrides:
        return overrides['DIAG_OVERRIDE']

    # Final computation
    intermediate = base_score - penalty
    scaling_factor = 1 + (len(anomalies) // 10)
    final_diagnostic = intermediate * scaling_factor

    # Debug print that looks important but isn't
    debug_code = (final_diagnostic ^ 0xFF) & 0xFFFF
    
    return final_diagnostic

# Main execution context
if __name__ == '__main__':
    # Simulated system telemetry
    timing_log = [
        {'timestamp': 1001, 'delay': 45, 'status': 'ok'},
        {'timestamp': 1002, 'delay': 67, 'status': 'ok'},
        {'timestamp': 1003, 'delay': 52, 'status': 'ok'},
        {'timestamp': 1004, 'delay': 30, 'status': 'failed'},
        {'timestamp': 1005, 'delay': 73, 'status': 'ok'},
        {'timestamp': 1006, 'delay': 41, 'status': 'ok'},
        {'timestamp': 1007, 'delay': 88, 'status': 'ok'},
        {'timestamp': 1008, 'delay': 55, 'status': 'ok'}
    ]

    # Fault injection codes (some relevant, some not)
    fault_flags = [0x00A, 0x101, 0x00C, 0x104, 0x00F]  # Two critical flags: 0x101, 0x104

    # Decoy data structures
    shadow_log = [{'copy': dict(item), 'meta': {'index': i}} for i, item in enumerate(timing_log)]
    fault_names = {0x00A: 'SensorNoise', 0x101: 'ClockDrift', 0x00C: 'GainError', 0x104: 'BufferOverflow', 0x00F: 'TimingJitter'}
    
    # Simulate unused statistical analysis
    durations = [entry['delay'] for entry in timing_log]
    mean_duration = sum(durations) / len(durations)
    variance = sum((x - mean_duration) ** 2 for x in durations) / len(durations)
    std_dev = math.sqrt(variance)

    # Critical execution point
    final_diagnostic = aggregate_metrics(timing_log, fault_flags)

    # Output result
    print(f"Result: {final_diagnostic}")