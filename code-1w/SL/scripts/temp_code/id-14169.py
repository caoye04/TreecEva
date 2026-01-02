from collections import defaultdict, Counter

# System health monitoring simulation with red herrings
def analyze_subsystem_metrics(raw_readings):
    normalized = []
    outlier_count = 0
    temp_cache = {}

    for idx, val in enumerate(raw_readings):
        if val < 0:
            outlier_count += 1
            continue
        
        shifted = val ^ 3  # Bit manipulation distraction
        if shifted % 2 == 0:
            normalized.append(shifted // 2)
        else:
            normalized.append(shifted * 3 + 1)  # Collatz-like distraction

    return normalized

# Irrelevant data transformation chain
def compute_legacy_checksum(data):
    checksum = 0
    for i, x in enumerate(data):
        checksum += (x ^ i) & 7
    return checksum * 2  # Dead-end computation

# Core diagnostic logic (buried among distractions)
def evaluate_system_integrity(sensor_log):
    stats = defaultdict(int)
    readings = [r['value'] for r in sensor_log if r['active']]

    processed = analyze_subsystem_metrics(readings)
    
    # Meaningful aggregation
    for p in processed:
        if p > 50:
            stats['critical'] += 1
        elif p > 25:
            stats['elevated'] += 1
        else:
            stats['normal'] += 1

    # Distractor: unused statistical analysis
    avg = sum(processed) / len(processed) if processed else 0
    variance = sum((x - avg) ** 2 for x in processed) / len(processed) if processed else 0

    # Another decoy function call
    legacy_flag = compute_legacy_checksum(processed)

    # Real signal extraction
    spike_events = [p for p in processed if p > 40]
    suppression_events = [p for p in processed if p < 10]
    
    base_index = len(spike_events) * 3 - len(suppression_events) * 2
    adjustment = 0
    
    # Conditional expression distraction
    adjustment = 5 if avg > 30 else -2
    
    # Key calculation buried here
    if stats['critical'] >= 3:
        adjustment += 7
    elif stats['elevated'] >= 5:
        adjustment += 4

    # Decoy data structure
    report_summary = {
        'outliers': 12,  # Fake stat
        'version': '2.1',
        'consistency': legacy_flag
    }
    
    # Actual path to answer
    aggregate_score = base_index + adjustment
    
    # More misdirection
    diagnostics = Counter(['STATUS_OK'] * 6 + ['WARN'] * 2)
    diagnostics['CRITICAL'] = stats['critical']
    
    # Red herring: complex but unused bitwise cascade
    mask = 0b1101
    for d in diagnostics.values():
        mask = (mask ^ d) & 0b1111
    
    # Correction factor depends on conditional logic and prior stats
    if stats['normal'] < 2:
        correction_factor = -3
    else:
        correction_factor = 2
    
    final_diagnostic = aggregate_score + correction_factor
    
    # Print required result
    print(f"Result: {final_diagnostic}")
    
    return final_diagnostic

# Simulated sensor input (deterministic)
sensor_data = [
    {'value': 12, 'active': True},
    {'value': 7, 'active': True},
    {'value': 45, 'active': True},
    {'value': 8, 'active': True},
    {'value': 60, 'active': True},
    {'value': 3, 'active': True},
    {'value': 92, 'active': True},
    {'value': 15, 'active': True},
    {'value': 52, 'active': True},
    {'value': 28, 'active': True},
    {'value': -5, 'active': True},  # outlier
    {'value': 77, 'active': True},
    {'value': 11, 'active': False},  # inactive
    {'value': 81, 'active': True}
]

# Execute main logic
evaluate_system_integrity(sensor_data)