from collections import defaultdict, Counter
import math

def analyze_signal_integrity(raw_samples, threshold=0.75):
    # Irrelevant preprocessing: normalize and filter noise (partially unused)
    normalized = [x / max(raw_samples) for x in raw_samples]
    filtered = [x for x in normalized if x > 0.1]
    spikes = [i for i, x in enumerate(normalized) if x > threshold]
    return spikes

def generate_timing_profile(sequence):
    # Generates timing intervals between pulses (red herring function)
    intervals = []
    last = 0
    for i, val in enumerate(sequence):
        if val == 1:
            intervals.append(i - last)
            last = i
    avg_interval = sum(intervals) / len(intervals) if intervals else 0
    return {'intervals': intervals, 'average': avg_interval}

def compute_entropy(data):
    # Unused entropy calculation (decoy)
    counts = Counter(data)
    total = len(data)
    return -sum((count/total) * math.log2(count/total) for count in counts.values())

def extract_diagnostic_codes(log_entries):
    # Extract codes but also create distractions
    codes = []
    metadata = defaultdict(int)
    for entry in log_entries:
        parts = entry.split('|')
        if len(parts) > 2:
            code = parts[1].strip()
            level = parts[0]
            metadata['entries'] += 1
            if code.startswith('D'):  # Only D-codes are relevant
                codes.append(int(code[1:]))
            metadata[level] += 1  # Red herring accumulation
    # Dead code path: never used
    if metadata.get('CRITICAL', 0) > 5:
        codes.append(999)
    return codes

def validate_sequence_consistency(seq):
    # Complex validation with misleading side calculations
    stack = []
    errors = 0
    for i, ch in enumerate(seq):
        if ch == '(':
            stack.append(i)
        elif ch == ')':
            if not stack:
                errors += 1
            else:
                stack.pop()
    # Return diagnostic ratio (unused in final result)
    correction_factor = errors / len(seq) if seq else 0
    parity_check = sum(1 for c in seq if c in 'AEIOU') % 7
    return correction_factor  # Misleading return

def aggregate_metrics(timing_log, diagnostics):
    base_score = sum(diagnostics) * 1.5
    penalty = 0
    
    # Real logic starts here
    for key, value in timing_log.items():
        if 'delay' in key and value > 10:
            penalty += value * 0.1
    
    # Critical distractor: complex-looking but irrelevant bit manipulation
    accumulator = 0
    for d in diagnostics:
        temp = (d << 2) ^ 0xABC
        temp = temp & (temp - 1)  # Clear lowest set bit
        accumulator += temp % 10
    
    # Actual key computation hidden among noise
    primary_signals = [x for x in diagnostics if x % 4 == 0]
    secondary_signals = [x for x in diagnostics if x % 3 == 0 and x % 4 != 0]
    
    # Real contribution to answer
    signal_value = sum(primary_signals) * 2 + sum(secondary_signals)
    
    # Fake complex adjustment (never affects outcome)
    dummy_adjustment = 0
    for i, val in enumerate(timing_log.values()):
        if i % 3 == 0:
            dummy_adjustment += math.sin(val) ** 2 + math.cos(val) ** 2  # Always 1
    
    # Final result combines real and fake elements, but fake ones cancel out
    result = base_score - penalty + signal_value
    return int(result)

# Main execution block
if __name__ == '__main__':
    # Simulated input data
    sensor_readings = [102, 205, 307, 409, 512, 614, 716, 819, 921, 1023]
    event_sequence = [0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1]
    system_log = [
        'INFO|D104|Stable',
        'WARN|D208|Fluctuation',
        'DEBUG|D104|Recheck',
        'ERROR|D416|CriticalDrop',
        'INFO|D312|Nominal',
        'WARN|D208|Repeated'
    ]
    timing_intervals = {
        'startup_delay': 15,
        'response_time': 8,
        'retry_backoff': 12,
        'sync_offset': 5
    }
    config_pattern = 'A(B(C)B(A))'
    
    # Trigger various functions - some results unused
    spike_positions = analyze_signal_integrity(sensor_readings)
    profile = generate_timing_profile(event_sequence)
    diagnostic_codes = extract_diagnostic_codes(system_log)
    consistency_metric = validate_sequence_consistency(config_pattern)
    entropy_value = compute_entropy([1, 2, 2, 3, 3, 3])  # Dead end
    
    # Key execution point
    final_diagnostic = aggregate_metrics(timing_intervals, diagnostic_codes)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")