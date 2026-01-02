def process_segment(data, threshold):
    """Irrelevant preprocessing function (dead code path)"""
    return [x for x in data if x > threshold]


def validate_sequence(seq):
    """Misleading validation function that is never called"""
    return all(a <= b for a, b in zip(seq, seq[1:]))

# Irrelevant sensor calibration constants (distractors)
calibration_a = 0.8721
offset_factor = -0.341
temp_buffer = [0] * 15

# Core data used in actual computation
extraction_chain = [
    (3, 7), (11, 5), (2, 9), (13, 4), (6, 8)
]

# Decoy data structure with misleading labels
performance_metrics = {
    'peak_load': 987,
    'uptime_ratio': 0.992,
    'error_count': 4,
    'last_updated': '2023-12-01'
}

# Actual metrics used in computation (subtly named to blend in)
metrics_log = [2, 3, 5, 7, 11]

# Unused recursive red herring
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Simulated hardware flags (irrelevant)
hw_status = {flag: True for flag in ['f0', 'f1', 'f2']}
hw_status['f1'] = False  # Distractor mutation

# Complex but irrelevant bit manipulation chain
event_flag = 0b101010
mask = 0b111
shifted = (event_flag << 3) & 0b1111000
twisted = shifted ^ 0b100100

# Real logic begins — data transformation pipeline
def decode_segments(chain):
    result = []
    for idx, (a, b) in enumerate(chain):
        if idx % 2 == 0:
            # Even index: modular exponentiation
            val = pow(a, b, 17)
        else:
            # Odd index: bitwise blend
            val = (a & b) ^ (a >> 1)
        result.append(val)
    return result

# Secondary transformation with list comprehension and zip
def apply_filters(decoded, filters):
    filtered = [
        d * f for d, f in zip(decoded, filters)
        if (d + f) % 3 != 0  # Conditional filter (some elements dropped)
    ]
    return filtered

# Accumulation with conditional overrides
def integrate_with_context(processed, base_log):
    total = sum(base_log)
    adjustment = 0
    for i, val in enumerate(processed):
        if i == 0 and val > 10:
            adjustment += 5
        elif val % 4 == 0:
            adjustment -= 2
        else:
            adjustment += (val % 5)
    return total + adjustment

# Final aggregation — this is where the answer comes from
def harvest_results(chain, log):
    decoded = decode_segments(chain)
    filtered = apply_filters(decoded, log)
    integrated = integrate_with_context(filtered, log)
    
    # Key calculation step
    final = integrated * 2 - sum(decoded[:3])
    
    # Dead code branch (never executed)
    if False:
        backup = sum(temp_buffer) + calibration_a
        final = int(backup)
        
    return final

# Execution flow
segment_data = [1, 4, 2, 8, 5]
processed_segment = process_segment(segment_data, 3)  # Unused result

# Critical execution point
final_yield = harvest_results(extraction_chain, metrics_log)

print(f"Result: {final_yield}")