import math

# Simulated system telemetry data processing with diagnostic validation
def process_telemetry(log_entries, threshold, mode='adaptive'):
    # Irrelevant transformation: time masking (unused in final result)
    masked_times = [entry['timestamp'] ^ 0xABCD for entry in log_entries if 'timestamp' in entry]
    
    # Data filtering based on severity (some entries are irrelevant)
    critical_logs = [e for e in log_entries if e.get('severity') > threshold]
    debug_logs = [e for e in log_entries if e.get('log_type') == 'DEBUG']  # Unused branch

    # Real computation path: extract diagnostic codes
    raw_codes = [log['diagnostics'] for log in critical_logs if 'diagnostics' in log]
    
    # Aggregation via lambda-based reduction
    sum_engine = lambda x, y: x + (y * 1.5)
    base_value = int(sum_engine(len(raw_codes), sum(raw_codes)) // 1.0)

    # Secondary path: offset calculation with red herring operations
    shift = 0
    for i in range(len(log_entries)):
        entry = log_entries[i]
        if 'flags' in entry:
            for flag in entry['flags']:
                shift ^= flag  # Bitwise mix, partially relevant
    shift &= 0xFF  # Bound to 8 bits

    # Distractor: complex unused cryptographic hash simulation
    def simulate_hash(data):
        acc = 0xCAFEBABE
        for d in data:
            acc = ((acc << 5) + acc) ^ d
        return acc & 0xFFFFFFFF
    
    # Unused recursive function (dead code path)
    def deep_validate(seq):
        if len(seq) <= 1:
            return seq[0] if seq else 0
        return seq[0] ^ deep_validate(seq[1:])

    # Control flow misdirection: conditional that always evaluates false in this context
    anomaly_score = 0
    if mode == 'strict' and len(debug_logs) > 100:
        anomaly_score = len([x for x in debug_logs if x['payload_size'] > 1024])

    # Real data used: trend analysis from diagnostic codes
    trend_data = [abs(code - 90) < 10 for code in raw_codes]  # Within normal operating range?
    baseline = len([c for c in raw_codes if c > 100])

    # Core logic hidden among distractions
    def aggregate_metrics(trends, base):
        count = sum(1 for t in trends if t)  # Count True values
        return count * 17 + base

    offset = shift ^ 0xAA  # Final offset derived from flag mixing

    def security_check(val):
        # Simple deterministic check with misleading name
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        return val if val in primes else (val * 2) % 23

    # Key execution point
    final_diagnostic = aggregate_metrics(trend_data, baseline) + security_check(offset)

    # Additional red herring: unused list comprehension with string parsing
    parsed_metadata = [str(entry.get('meta', ''))[::-1] for entry in log_entries if isinstance(entry.get('meta'), str)]
    filtered_metadata = [m for m in parsed_metadata if 'X' in m]  # Never used

    # Final output
    print(f"Result: {final_diagnostic}")

# Input data crafted to yield deterministic result
input_logs = [
    {'timestamp': 1001, 'severity': 6, 'diagnostics': 85, 'flags': [0x10, 0x20]},
    {'timestamp': 1002, 'severity': 8, 'diagnostics': 92, 'flags': [0x20, 0x40]},
    {'timestamp': 1003, 'severity': 5, 'diagnostics': 105},  # Below threshold
    {'timestamp': 1004, 'severity': 9, 'diagnostics': 88, 'flags': [0x10, 0x40]},
    {'timestamp': 1005, 'severity': 9, 'diagnostics': 112, 'flags': [0x80]},
    {'timestamp': 1006, 'severity': 7, 'diagnostics': 91, 'flags': [0x10]},
    {'log_type': 'DEBUG', 'payload_size': 2048, 'severity': 3}  # Not critical
]

process_telemetry(input_logs, threshold=6)