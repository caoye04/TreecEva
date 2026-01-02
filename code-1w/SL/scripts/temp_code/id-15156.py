import itertools

# Simulated system telemetry data
technical_metrics = [87, 92, 76, 88, 95, 84, 91]
operational_flags = [True, False, True, True, False, True, True]
context_weights = [0.8, 1.2, 0.9, 1.1, 0.7, 1.3, 1.0]

# Irrelevant baseline calibration (distractor)
calibration_offset = sum([x * 0.05 for x in technical_metrics]) / len(technical_metrics)
adjusted_baseline = 85 + calibration_offset

# Misleading secondary processing path (dead code path)
def deprecated_analysis(data):
    return [d * 1.05 if d < 90 else d * 0.98 for d in data]

legacy_results = deprecated_analysis(technical_metrics)  # Unused

# Auxiliary transformation using enumerate and zip (partially relevant)
normalized_metrics = []
for i, (metric, flag) in enumerate(zip(technical_metrics, operational_flags)):
    if flag:
        adjusted = metric * context_weights[i]
    else:
        adjusted = metric * 0.85  # Penalty for inactive flag
    normalized_metrics.append(round(adjusted, 2))

# Spurious list comprehension with no effect (red herring)
_ = [x for x in range(len(normalized_metrics)) if normalized_metrics[x] > 90]

# Bit manipulation decoy (irrelevant to final result)
signal_signature = 0
for val in technical_metrics:
    signal_signature ^= int(val) << 1
    signal_signature &= 0xFFFF

# Dummy dictionary for configuration (mostly irrelevant)
system_profile = {
    'version': '2.7.1',
    'mode': 'production',
    'threshold': 88.5,
    'debug_level': 3,
    'checksum': signal_signature
}

# Real computation begins here — hidden among noise
consistency = sum(normalized_metrics) / len(normalized_metrics)

# Efficiency computed via itertools.chain (valid use)
flat_context = list(itertools.chain([1.0], context_weights[:3], [0.95]))
efficiency = consistency * (sum(flat_context) / len(flat_context))

# Resilience based on conditional counting (logical operation)
resilience = 0
for val, orig in zip(normalized_metrics, technical_metrics):
    if val >= 85 and orig >= 80:
        resilience += 1
resilience = resilience * 10.5  # Scale factor

# Decoy function that's defined but not used (distractor)
def calculate_robustness(seq):
    return max(seq) - min(seq)

intermediate_diagnostics = {
    'peak': max(normalized_metrics),
    'floor': min(normalized_metrics),
    'spread': calculate_robustness(normalized_metrics)  # Unused
}

# Core processing function (uses dictionary operations)
def process_metrics(a, b, c):
    factors = {'alpha': a, 'beta': b, 'gamma': c}
    scaling = {'alpha': 0.3, 'beta': 0.4, 'gamma': 0.3}
    
    # Redundant dictionary comprehension (distraction)
    _ = {k: v * 1.1 for k, v in factors.items() if k != 'beta'}
    
    # Actual weighted sum
    result = 0
    for key in factors:
        result += factors[key] * scaling[key]
    
    # Extra rounding step to obscure logic
    return round(result, 2)

# Key statement
final_score = process_metrics(consistency, efficiency, resilience)

# Output the target result
print(f"Target result: {final_score}")