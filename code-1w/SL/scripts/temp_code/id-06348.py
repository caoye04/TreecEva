def preprocess_signal(data):
    # Irrelevant preprocessing step (dead code path)
    filtered = [x for x in data if x > 0]
    normalized = [x / max(filtered) for x in filtered]
    return normalized

# Simulated telemetry stream from satellite subsystems
telemetry_stream = tuple([18, 23, 15, 42, 7, 31, 28, 19, 36])

# Misleading diagnostic flag (not used in final result)
critical_failure_flag = any(x < 10 for x in telemetry_stream)

# Historical baseline data (distractor)
historical_avg = sum(telemetry_stream[:5]) / 5

# Bitmask configuration for communication protocol (partially relevant)
protocol_mask = 0b1101
shift_offset = len(telemetry_stream) % 7  # Used later

# Decoy function that calculates unused metrics
def compute_resilience_index(seq):
    resilience = 0
    for i in range(len(seq)):
        if seq[i] % 2 == 0:
            resilience += (seq[i] >> 1) & 0b111
    return resilience  # Never called in main logic

# Secondary data structure with red herring values
auxiliary_buffer = [telemetry_stream[i] ^ 5 for i in range(0, len(telemetry_stream), 2)]

# Data slicing to extract working segment
working_segment = telemetry_stream[1:6]  # [23, 15, 42, 7, 31]

# Complex transformation chain
transformed = []
for val in working_segment:
    shifted = val << 1
    masked = shifted & protocol_mask
    transformed.append(shifted - masked)  # Effectively val*2 - (val*2 & mask)

# Intermediate aggregation (some values are distractions)
aggregated_diagnostics = [
    sum(transformed),
    max(transformed) - min(transformed),
    len([x for x in transformed if x > 30]),
    transformed[2]  # Key value embedded here
]

# Control flow with misleading condition
if len(aggregated_diagnostics) > 3 and shift_offset > 0:
    adjustment_factor = 3
    # Nested operation with slicing and tuple unpacking
    snapshot = tuple(aggregated_diagnostics[1:4])
    span, count, key_value = snapshot
    
    # Core calculation buried in noise
    raw_seed = key_value + (shift_offset * adjustment_factor)
    
    # Dead branch (never executed due to fixed data)
    if raw_seed < 0:
        raw_seed = abs(raw_seed) * 2

    # Actual answer derivation
    final_diagnostic = (raw_seed // 4) + (protocol_mask ^ 2)
else:
    final_diagnostic = -1

# Unused recursive function (decoy)
def analyze_health_recursively(log, idx=0):
    if idx >= len(log):
        return 0
    return (log[idx] & 1) + analyze_health_recursively(log, idx + 1)

# Critical execution point
final_diagnostic = analyze_shift_pattern(operational_log)

# Function containing the real logic (defined late to increase interference)
def analyze_shift_pattern(log):
    # Re-process log using bit shifts and masking
    processed = [((x << 2) & 0xFF) ^ 0xAA for x in log[::2]]
    selected = processed[1]  # Take second element after transformation
    offset = len(log) % 4
    return selected + offset*2

# Reassign final_diagnostic with correct computation
operational_log = list(telemetry_stream) + [44, 12, 8]
final_diagnostic = analyze_shift_pattern(operational_log)

print(f"Result: {final_diagnostic}")