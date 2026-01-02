from collections import defaultdict
import math

# Irrelevant sensor array initialization (distractor)
sensor_grid = [[0 for _ in range(8)] for _ in range(8)]
baseline_readings = defaultdict(lambda: 0)
for i in range(8):
    baseline_readings[f'sensor_{i}'] = (i * 17 + 3) % 19

# Decoy function - never called but looks important
def compute_entropy(data):
    entropy = 0.0
    freq = {}
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    total = len(data)
    for count in freq.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

# Unused transformation matrix (red herring)
transform_matrix = [
    [1, 0, 0, 0],
    [0, math.cos(math.pi/4), -math.sin(math.pi/4), 0],
    [0, math.sin(math.pi/4), math.cos(math.pi/4), 0],
    [0, 0, 0, 1]
]

# Core system simulation with relevant logic buried in noise
quantum_registers = [
    {'state': 5, 'phase': 3.14159, 'flagged': False},
    {'state': 12, 'phase': 1.5708, 'flagged': True},
    {'state': 8, 'phase': 0.0, 'flagged': False}
]

# Misleading auxiliary calculations
temp_buffer = []
for reg in quantum_registers:
    temp_buffer.append((reg['state'] ** 2 + int(reg['phase'])) % 13)

# Another decoy - bit manipulation that isn't used later
bit_fingerprint = 0
for val in temp_buffer:
    bit_fingerprint ^= (val << 2) | (val >> 1)

# Real processing begins here - nested logic with distractors
status_codes = []
def process_register(reg):
    code = reg['state']
    if reg['flagged']:
        code *= 3
        # Dead branch - condition never met due to data
        if reg['phase'] > 10:
            code += 100  # unreachable
    else:
        if code > 10:
            code += 10
        else:
            code -= 2
    status_codes.append(code)
    return code

# Apply processing via lambda (required feature)
processor = lambda regs: [process_register(r) for r in regs]
processor(quantum_registers)

# Additional irrelevant aggregation
aggregated_metrics = {
    'max_code': max(status_codes),
    'sum_squares': sum(x * x for x in status_codes),
    'range': max(status_codes) - min(status_codes)
}

# Core diagnostic logic - depends on prior steps
intermediate_score = 0
for i, code in enumerate(status_codes):
    intermediate_score += code * (i + 1)

# Conditional override based on phase sum (only some registers matter)
phase_sum = sum(r['phase'] for r in quantum_registers if r['flagged'])
if phase_sum < 2.0:
    adjustment_factor = 2
else:
    adjustment_factor = 1  # this branch taken

adjusted_score = intermediate_score // adjustment_factor

# Final transformation using list comprehension (required feature)
log_contributions = [
    int(math.log(abs(adjusted_score) + 1)) for _ in range(3)
]
final_diagnostic = adjusted_score + sum(log_contributions)

# Output required result
print(f"Result: {final_diagnostic}")