import itertools

# System performance monitoring with irrelevant telemetry and complex preprocessing

def preprocess_signals(raw_data, threshold=0.75):
    filtered = [x for x in raw_data if abs(x) > threshold]
    normalized = [round(x / max(filtered), 3) for x in filtered]
    return sorted(normalized, reverse=True)


def generate_frequency_peaks(data_stream):
    peaks = []
    for i in range(1, len(data_stream) - 1):
        if data_stream[i] > data_stream[i-1] and data_stream[i] > data_stream[i+1]:
            peaks.append((i, round(data_stream[i], 3)))
    return peaks


def evaluate_coherence(segment):
    if len(segment) < 2:
        return 0.0
    diffs = [abs(segment[i] - segment[i+1]) for i in range(len(segment)-1)]
    return round(sum(diffs) / len(diffs), 4)


def calculate_bandwidth(segments):
    total = 0
    for seg in segments:
        total += sum(x * 10 for x in seg if x > 0.5)
    return int(total)

# Irrelevant diagnostic functions (dead code paths)

def log_diagnostics(info_map):
    timestamp = "2023-12-05T10:30:45Z"
    for key, val in info_map.items():
        print(f"[DIAG] {timestamp}: {key} -> {val}")
    return False  # Never used


def simulate_latency(nodes, load_factor=1.0):
    import random
    random.seed(42)
    return [random.uniform(0.1, load_factor * 2.0) for _ in nodes]

# Real input data disguised among synthetic noise
raw_telemetry = [
    0.12, -0.33, 0.81, 0.92, -0.05, 0.76, 0.88, -0.41, 0.63, 0.55,
    1.05, -0.22, 0.71, 0.67, 0.93, -0.51, 0.44, 0.39, 0.85, 0.77
]

# Step 1: Preprocess signal data (relevant)
signal_input = preprocess_signals(raw_telemetry, threshold=0.4)

# Step 2: Extract peak frequencies (partially relevant)
peaks = generate_frequency_peaks(signal_input)
peak_values = [p[1] for p in peaks]

# Step 3: Create overlapping segments using slicing and itertools (core logic)
segments = []
for i in range(len(signal_input) - 3):
    segments.append(signal_input[i:i+4])

# Misleading coherence filtering (distractor - appears important but unused)
coherence_scores = {idx: evaluate_coherence(seg) for idx, seg in enumerate(segments)}
decoy_ranking = sorted(coherence_scores.items(), key=lambda x: x[1])

# Hidden selection criterion: only segments containing values from peak list
valid_indices = []
for idx, seg in enumerate(segments):
    if any(round(val, 3) in peak_values for val in seg):
        valid_indices.append(idx)

optimal_segments = [segments[i] for i in valid_indices if i % 2 == 0]  # Additional filter

# Decoy statistics (irrelevant computations)
avg_peak_spacing = 0.0
if len(peaks) > 1:
    positions = [p[0] for p in peaks]
    avg_peak_spacing = sum(positions[i+1] - positions[i] for i in range(len(positions)-1)) / (len(positions) - 1)

# Unused set operations (red herring)
unique_signal_set = set(round(x, 2) for x in signal_input)
expected_reference_set = {0.48, 0.52, 0.61, 0.71, 0.82, 0.88, 0.92}
missing_refs = expected_reference_set - unique_signal_set

# Critical calculation point (answer depends on this)
final_bandwidth = calculate_bandwidth(optimal_segments)

# Another decoy: frequency correlation matrix (never used)
correlation_matrix = [[abs(a - b) for a in peak_values] for b in peak_values]

# Final output
print(f"Result: {final_bandwidth}")