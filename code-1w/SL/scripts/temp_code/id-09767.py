import itertools

# Simulated sensor fusion system for environmental monitoring
def preprocess_readings(raw_data):
    filtered = [x for x in raw_data if 10 <= x <= 100]
    normalized = [(x - 10) / 90 for x in filtered]
    return normalized

# Irrelevant helper - dead code path (decoy)
def legacy_calibrate(x):
    return (x * 3.14159) % 7

# Misleading transformation with no impact on final result
def spectral_transform(sequence):
    transformed = []
    for i in range(len(sequence)):
        val = sequence[i] * (2 ** (i % 4))
        if val > 50:
            val = val % 23
        transformed.append(val)
    return transformed[::-1]  # Reversed order

# Core diagnostic logic
def generate_diagnostics(data_stream):
    chunked = [data_stream[i:i+3] for i in range(0, len(data_stream), 3)]
    analysis = []
    for chunk in chunked:
        if len(chunk) == 3:
            metric = (chunk[0] + chunk[1]) * chunk[2]
            analysis.append(round(metric, 3))
    return analysis

# Red herring function - appears important but unused
def compute_entropy(values):
    total = sum(values)
    probs = [v / total for v in values]
    from math import log
    return -sum(p * log(p) for p in probs if p > 0)

# Decoy data structure
tuning_params = {
    'gain': 2.718,
    'threshold': 0.85,
    'window_size': 17,
    'damping': 0.92
}

# Unused intermediate calculations
baseline_offset = 14.3
reference_frame = [baseline_offset * (1.05 ** i) for i in range(8)]
correction_matrix = [[i * j for j in range(3)] for i in range(3)]

# Actual sensor input (simulated)
sensor_input = [15, 22, 8, 95, 43, 67, 102, 55, 12, 88, 34, 76, 9, 29]

# Preprocessing stage
sensor_array = preprocess_readings(sensor_input)

# Generate auxiliary log with diagnostic flags
diagnostic_flags = [int(x > 0.5) for x in sensor_array]
flag_pairs = list(itertools.combinations(diagnostic_flags, 2))
diagnostics_log = [pair[0] ^ pair[1] for pair in flag_pairs if sum(pair) > 0]

# Another distraction: complex string-based encoding (irrelevant)
status_message = "ERR_" + "_".join([str(int(b)) for b in diagnostic_flags[:4]])
encoded_shift = sum(ord(c) for c in status_message if c.isdigit())
pseudo_checksum = (encoded_shift * 11) % 19

# Real computation begins here — non-obvious due to distractions above
interim_results = []
for i, val in enumerate(sensor_array):
    if i % 2 == 0 and val > 0.3:
        adjusted = val * (i + 1)
        interim_results.append(adjusted)

# Secondary processing chain
expanded = []
for r in interim_results:
    expanded.extend([r, r * 0.5])

# Critical operation hidden among noise
trimmed = expanded[1:-1]  # slicing operation
smoothed = [sum(trimmed[i:i+3])/3 for i in range(len(trimmed)-2)]

# Final aggregation function
def aggregate_metrics(seq, log):
    base_score = sum(seq) * len(log)
    penalty = len([x for x in seq if x < 0.2]) * 1.5
    bonus = log.count(1) * 0.7
    return int(base_score - penalty + bonus)

# Key statement
final_diagnostic = aggregate_metrics(smoothed, diagnostics_log)

print(f"Result: {final_diagnostic}")