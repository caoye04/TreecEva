def analyze_sequence(data, config):
    # Irrelevant transformation chain
    temp_a = [x ** 2 for x in data if x % 2 == 0]
    temp_b = [x for x in data if x > config.get('limit', 10)]
    shadow_score = sum(temp_a) // (len(temp_b) or 1)

    # Distractor: complex but unused calculation
    def decoy_entropy(seq):
        import math
        counts = {}
        for item in seq:
            counts[item] = counts.get(item, 0) + 1
        entropy = 0
        total = len(seq)
        for count in counts.values():
            p = count / total
            entropy -= p * math.log2(p) if p > 0 else 0
        return round(entropy, 3)
    _ = decoy_entropy(data)

    # Actual relevant logic buried here
    base_metric = sum(x for x in data if x < 50) * config.get('multiplier', 1)
    adjustment = len([x for x in data if x in config.get('flags', [])]) * 10
    return base_metric + adjustment


def validate_checksum(sequence):
    # Unused validation function (dead code path)
    checksum = 0
    for i, val in enumerate(sequence):
        checksum ^= (val + i) & 0xFF
    return checksum == 0xAA

# Misleading preprocessing block
dummy_logs = [
    {'time': 1, 'level': 'ERROR', 'code': 500},
    {'time': 2, 'level': 'WARN', 'code': 404}
]
error_weights = {'CRITICAL': 10, 'ERROR': 5, 'WARN': 2}
accumulated_risk = sum(error_weights.get(log['level'], 0) for log in dummy_logs)

# Real input data hidden among noise
log_entries = [25, 12, 45, 8, 33, 58, 16, 9]
system_thresholds = {
    'limit': 40,
    'multiplier': 3,
    'flags': [12, 16],
    'mode': 'diagnostic'
}

# Secondary distractor: tuple unpacking with zip and enumerate (meets language feature requirement)
indices = list(range(len(log_entries)))
data_pairs = list(zip(indices, log_entries))
processed_layers = []
for i, (idx, val) in enumerate(data_pairs):
    if i % 3 == 0:
        processed_layers.append(val * 2)
    elif val < 20:
        processed_layers.append(val + 5)
    else:
        processed_layers.append(val // 2)

# Unused combinatorics red herring
from math import comb
combination_sum = sum(comb(len(log_entries), r) for r in range(1, 4)) if len(log_entries) >= 3 else 0

# Core computation disguised as one among many
primary_diagnostics = analyze_sequence(log_entries, system_thresholds)

# Final processing step with key variable
final_diagnostic = primary_diagnostics

# Decoy assignment to mislead tracking
final_diagnostic *= 1  # No-op

# Output required result
print(f"Result: {final_diagnostic}")