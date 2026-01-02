def analyze_signal(samples, threshold=0.75):
    normalized = [s / max(samples) for s in samples]
    filtered = [n for n in normalized if n > threshold]
    return len(filtered)


def transform_coordinates(coords):
    # Irrelevant coordinate transformation (decoy function)
    return [(c[0] * 2 + 1, c[1] * 2 - 1) for c in coords]


def compute_entropy(data):
    from math import log2
    total = sum(data)
    probabilities = [(d / total) for d in data if d > 0]
    entropy = -sum(p * log2(p) for p in probabilities)
    return round(entropy, 4)

# Unused signal analysis
raw_samples = [120, 150, 200, 180, 250, 300, 220, 210]
signal_peak = max(raw_samples)
noise_floor = sum(raw_samples) / len(raw_samples)

# Real processing begins here
sequence_data = 'AAGTCGCTTAAGACATCGGA'
base_frequencies = {base: sequence_data.count(base) for base in set(sequence_data)}
frequency_list = [base_frequencies[b] for b in sorted(base_frequencies)]

# Bit manipulation decoy
flag_register = 0b10101100
mask = 0b11110000
masked_out = flag_register & mask
shifted_flag = masked_out >> 4

# Enumerate and string method usage (required python features)
enumerated_ops = []
for i, base in enumerate(sequence_data):
    if base in 'GC':
        enumerated_ops.append((i, base.lower()))

grouped_pairs = [''.join(pair) for pair in zip(sequence_data[::2], sequence_data[1::2])]
transition_count = sum(1 for p in grouped_pairs if p[0] != p[1])

# Combinatorics distraction
def binomial_coeff(n, k):
    if k > n or k < 0:
        return 0
    result = 1
    for i in range(min(k, n - k)):
        result = result * (n - i) // (i + 1)
    return result

# Data structure transformations
readings = [18, 22, 19, 25, 24, 21, 20, 23]
windows = [readings[i:i+3] for i in range(len(readings)-2)]
avg_windows = [round(sum(w)/3, 2) for w in windows]

# Control flow with nesting (level 3)
diagnostics = []
for i, val in enumerate(avg_windows):
    status = None
    if val > 22:
        if i % 2 == 0:
            status = 'ELEVATED_EVEN'
        else:
            status = 'ELEVATED_ODD'
    elif val < 20:
        for j in range(2):  # Extra nesting level
            if i > 2:
                status = 'LOW_LATE'
                break
            else:
                status = 'LOW_EARLY'
                break
    else:
        status = 'NORMAL'
    diagnostics.append({'index': i, 'value': val, 'status': status})

# Tuple unpacking and multiple assignment
primary_metric, secondary_metric = transition_count, len(frequency_list)
meta_info = ('GENOMIC_SCAN', 2024, 'VALID')
scan_type, year, validity = meta_info

# Main processing chain (relevant path)
processing_chain = [
    len(sequence_data),
    len(grouped_pairs),
    primary_metric,
    secondary_metric,
    compute_entropy(frequency_list)
]

# Dead code path (misleading)
legacy_modes = ['A', 'B', 'C']
mode_index = 0
while mode_index < len(legacy_modes):
    temp_result = binomial_coeff(10, mode_index)
    mode_index += 1

# Final aggregation (key statement)
def aggregate_metrics(chain, diag):
    base_score = chain[0] * chain[2]
    adjustment = sum(d['value'] for d in diag if 'ELEVATED' in d['status'])
    penalty = len([d for d in diag if d['status'] == 'LOW_EARLY']) * 1.5
    final_score = base_score + adjustment - penalty
    return int(round(final_score))

final_diagnostic = aggregate_metrics(processing_chain, diagnostics)
print(f"Target result: {final_diagnostic}")