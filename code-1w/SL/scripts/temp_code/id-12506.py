import itertools

# System health monitoring with diagnostic metrics
base_signals = [12, 8, 15, 3, 9, 7]
event_log = [(1, 'startup'), (2, 'ping'), (3, 'sync'), (4, 'idle')]

# Irrelevant transformation - red herring
shadow_buffer = [x ** 2 + y for x, y in enumerate([4, 2, 1, 8, 5])]

# Core data: signal harmonics and phase weights
timing_phases = [0.5, 1.2, 0.8, 1.6]
amplitude_weights = [2, 1, 3, 2]

# Misleading diagnostic chain
legacy_flags = {k: v == 'ping' for k, v in event_log}
status_integrity = sum(legacy_flags.values()) > 2  # Always False

# Real computation begins
weighted_harmonics = []
for i, signal in enumerate(base_signals):
    harmonic = signal * ((i + 1) % 4 + 1)
    weighted_harmonics.append(harmonic)

# Generate combinatorial pairs for cross-validation
pairwise_consistency = 0
for pair in itertools.combinations(weighted_harmonics[:4], 2):
    if pair[0] > pair[1]:  # Directional check
        pairwise_consistency += 1

# Decoy structure - unused but plausible
recovery_sequence = list(itertools.accumulate([3, -1, 4, -2], lambda acc, x: acc + x if acc > 5 else acc))

# Threshold map construction (relevant)
threshold_map = {}
for i, phase in enumerate(timing_phases):
    threshold_map[f'level_{i}'] = int(phase * amplitude_weights[i] * 10)

# Construct health signature using filtered harmonics
filtered_harmonics = [h for h in weighted_harmonics if h % 2 == 0]
compression_factor = len(filtered_harmonics) // 2
health_signature = [
    sum(filtered_harmonics[:compression_factor]),
    sum(filtered_harmonics[compression_factor:])
]

# Dummy checksum - looks important but unused
checksum = sum(shadow_buffer) ^ sum(recovery_sequence)

# Auxiliary bit manipulation - partial relevance
bit_context = 0
for val in health_signature:
    bit_context ^= (val << 1) | (val >> 2)

# Actual processing function
def process_metrics(signature, thresholds):
    # Intermediate decoy variables
    temp_cache = [t * 0.1 for t in thresholds.values()]
    audit_trace = [x + bit_context for x in signature]  # Looks critical

    # Real logic: compare signature against dynamic baseline
    baseline = sum(thresholds.values()) / len(thresholds)
    adjustment = (signature[0] - signature[1]) // 4
    
    # Conditional override simulation (not triggered)
    if status_integrity and all(x > 100 for x in audit_trace):
        return int(baseline)  # Dead path
    
    # Primary diagnostic formula
    metric_a = signature[0] * 2 - signature[1]
    metric_b = abs(metric_a) + adjustment
    
    # Final adjustment based on threshold bands
    band_total = 0
    for key in sorted(thresholds.keys()):
        if thresholds[key] >= 16:
            band_total += 1
    
    # Critical result calculation
    final_score = metric_b + (band_total * 100)
    
    # Red herring return alternative
    # if len(temp_cache) == len(thresholds): return int(sum(temp_cache))
    
    return final_score

# Execute main logic
final_diagnostic = process_metrics(health_signature, threshold_map)

# Output result as required
print(f"Target result: {final_diagnostic}")