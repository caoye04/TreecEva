def preprocess_signal(data, threshold=0.5):
    """Irrelevant signal preprocessing function (dead code path)"""
    filtered = [x for x in data if abs(x) > threshold]
    normalized = [x / max(filtered) for x in filtered]
    return normalized


def compute_entropy(seq):
    """Unused entropy computation (distractor)"""
    from math import log
    freq = {}
    for item in seq:
        freq[item] = freq.get(item, 0) + 1
    total = len(seq)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p, 2)
    return entropy


def validate_checksum(chunk):
    """Misleading validation function that appears important but isn't used in critical path"""
    checksum = 0
    for b in chunk:
        checksum ^= b
    return checksum == 0


# Simulated quantum register states (bit vectors)
quantum_registers = [
    [1, 0, 1, 1],
    [0, 1, 1, 0],
    [1, 1, 0, 0],
    [1, 1, 1, 1],
    [0, 0, 1, 1]
]

# Irrelevant system telemetry (red herring variables)
telemetry_data = {
    'voltage': [3.2, 3.3, 3.1, 3.4],
    'temperature': [25.1, 26.7, 24.9, 27.3],
    'timestamp': 1712345678,
    'mode': 'diagnostic'
}

# Unused transformation matrix (distractor)
transform_matrix = [
    [0.707, -0.707],
    [0.707, 0.707]
]

# Auxiliary state map with decoy logic
state_map = {i: bin(i).count('1') for i in range(16)}
parity_flags = [sum(reg) % 2 for reg in quantum_registers]

# Dummy diagnostic chain (unused)
current_diagnostics = []
for i, reg in enumerate(quantum_registers):
    if sum(reg) > 2:
        current_diagnostics.append((i, 'HIGH_ACTIVITY'))
    else:
        current_diagnostics.append((i, 'LOW_ACTIVITY'))

# Real processing begins here — non-obvious due to distractions above


mask_patterns = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 0, 0]
]

overlap_scores = []
for reg, mask in zip(quantum_registers, mask_patterns):
    overlap = sum(r & m for r, m in zip(reg, mask))
    overlap_scores.append(overlap)

# Conditional expression used idiomatically
adjusted_scores = [score if score >= 2 else (score + 1) for score in overlap_scores]

# Set operations: track unique configurations
register_tuples = [tuple(reg) for reg in quantum_registers]
unique_configurations = set(register_tuples)
duplicate_count = len(quantum_registers) - len(unique_configurations)

# Key intermediate variable (appears secondary but feeds into final result)
system_stability = len(unique_configurations) + (3 if duplicate_count == 0 else -1)

# Composite weight calculation using linear search through adjusted scores
max_score_index = 0
for i in range(1, len(adjusted_scores)):
    if adjusted_scores[i] > adjusted_scores[max_score_index]:
        max_score_index = i

# Weight derived from index and stability
weight_factor = (max_score_index + 1) * system_stability

# Final aggregation using integer division and rounding
raw_aggregate = sum(adjusted_scores) * weight_factor
scaled_result = raw_aggregate // 4  # Integer division

# Final diagnostic computed via multiple reasoning steps
final_diagnostic = round(scaled_result / 2.75, 4) if system_stability > 3 else scaled_result * 2

# Ensure output format compliance
print(f"Target result: {final_diagnostic}")