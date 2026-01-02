from collections import defaultdict, Counter
import math

# Simulated system telemetry data
timing_samples = [1.2, 0.8, 1.5, 2.3, 1.1, 0.9, 1.4, 2.0, 1.7, 1.3]
error_codes = [0, 1, 0, 2, 0, 0, 1, 0, 0, 2]
system_load = [0.45, 0.67, 0.89, 0.34, 0.78, 0.56, 0.91, 0.23, 0.65, 0.77]

# Irrelevant auxiliary mappings (distractor)
legacy_code_map = {i: f'LEGACY_{i}' for i in range(5)}
opcode_lookup = defaultdict(lambda: 'UNKNOWN')
for idx, op in enumerate(['INIT', 'READ', 'WRITE', 'EXEC', 'SYNC']):
    opcode_lookup[idx] = op

# Misleading preprocessing (dead path)
def validate_checksum(data):
    return sum(data) % 7 == 0  # Unused logic

# Decoy function with plausible but irrelevant computation
def compute_entropy(values):
    counts = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 3)

# Another red herring: complex transformation with no downstream use
def generate_wave_pattern(n):
    return [math.sin(2 * math.pi * i / n) for i in range(n)]
waves = generate_wave_pattern(10)

# Real processing begins here — nested and interwoven with noise
status_registry = []
for i, (t, e, load) in enumerate(zip(timing_samples, error_codes, system_load)):
    status = 'STABLE'
    if e != 0:
        if e == 1:
            status = 'WARNING'
        elif e == 2:
            status = 'CRITICAL'
    elif load > 0.85:
        status = 'OVERLOAD'
    elif t > 2.0:
        status = 'LATENCY'
    
    # Store structured log entry
    status_registry.append({'index': i, 'timing': t, 'status': status, 'load': load})

# Extract logs meeting diagnostic threshold
diagnostic_entries = [entry for entry in status_registry if entry['status'] in ('CRITICAL', 'LATENCY')]
timing_log = [round(entry['timing'] * 1000) for entry in diagnostic_entries]  # Convert to ms

# System-wide flags from multiple sources (some irrelevant)
flag_sources = [
    [True, False, True],
    [False, False, True],
    [True, True, False]
]
flattened_flags = [flag for sublist in flag_sources for flag in sublist]
system_flags = {
    'panic_trigger': any(flattened_flags),
    'degraded_mode': len([f for f in flattened_flags if not f]) > 3,
    'clock_synced': False,
    'legacy_active': False
}

# Secondary decoy analysis (never used)
config_trace = [(i, math.exp(-i*0.1)) for i in range(len(timing_samples))]
normalized_trace = [v for i, v in config_trace if v > 0.5]

# Core aggregation logic buried in abstraction
def aggregate_metrics(times, flags):
    if not times:
        return -1
    
    # Real calculation: weighted mean adjusted by flag state
    base_avg = sum(times) / len(times)
    variance = sum((t - base_avg) ** 2 for t in times) / len(times)
    std_dev = math.sqrt(variance)
    
    # Adjustment factor based on system flags
    adjustment = 1.0
    if flags['panic_trigger']:
        adjustment *= 1.2
    if flags['degraded_mode']:
        adjustment *= 0.9
    
    # Final diagnostic score: adjusted average plus stability penalty
    raw_score = base_avg * adjustment
    penalty = std_dev * 0.1
    
    # Red herring: unused conditional branch
    if flags['clock_synced']:
        raw_score += 100  # Never executed
    
    result = raw_score - penalty
    return int(round(result))

# Critical execution point
final_diagnostic = aggregate_metrics(timing_log, system_flags)
print(f"Result: {final_diagnostic}")