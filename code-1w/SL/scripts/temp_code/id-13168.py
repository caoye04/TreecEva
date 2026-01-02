import itertools

# System health monitoring simulation with red herrings
def collect_telemetry():
    return [23.5, 24.1, 19.8, 22.0, 25.3, 26.7, 21.4, 20.9]

def compute_entropy(data):
    total = sum(data)
    entropy = 0
    for x in data:
        if x > 0:
            entropy -= (x / total) * __import__('math').log(x / total)
    return round(entropy, 4)

def generate_frequencies(n):
    # Irrelevant frequency generator (dead abstraction)
    return [i * 1.5 for i in range(n) if i % 3 != 0]

def analyze_pattern(seq):
    # Distractor: unused pattern analyzer
    windows = [seq[i:i+3] for i in range(len(seq)-2)]
    scores = []
    for w in windows:
        scores.append((w[2] - w[0]) / w[1] if w[1] != 0 else 0)
    return [s for s in scores if s > 0.5]

def filter_outliers readings(readings, limit=27.0):
    # Misleading function name, actually not used for main logic
    return [r for r in readings if r < limit]

# Core diagnostic processing
telemetry_data = collect_telemetry()
baseline_shift = sum([x - 20 for x in telemetry_data])  # Accumulate deviation

# Simulated diagnostic codes from subsystems
diagnostics = {
    'power': [1, 0, 1, 1],
    'thermal': [1, 1, 0, 1],
    'network': [0, 1, 1, 1],
    'storage': [1, 1, 1, 0]
}

# Thresholds with decoy entries
thresholds = {
    'critical': 0.75,
    'warning': 0.5,
    'info': 0.25,
    'debug': 0.1,  # Unused level
    'trace': 0.05  # Dead entry
}

# Irrelevant data transformation
expanded_diagnostics = {}
for k, v in diagnostics.items():
    expanded_diagnostics[k] = list(itertools.accumulate(v))

# Secondary computation - looks important but isn't part of final result
entropy_score = compute_entropy(telemetry_data)
spectral_freq = generate_frequencies(10)

# Real processing begins here — hidden in the middle of noise
active_nodes = 0
for k, v in diagnostics.items():
    if sum(v) >= 3:
        active_nodes += 1

# Key transformation: map diagnostics to weighted status
weight_map = {}
for key, values in diagnostics.items():
    # Only systems with consistent second reading contribute
    if values[1] == 1:
        weight_map[key] = sum(values) * 0.25

# Construct feature vector using slicing and accumulation
trend_slice = telemetry_data[2:6]  # Middle segment
accumulated_trend = list(itertools.accumulate(trend_slice))

# Decoy control flow
if len(accumulated_trend) > 5:
    adjustment = 0.0
else:
    adjustment = 0.15  # Never applied due to length

# Critical intermediate calculation
raw_stability = baseline_shift * 0.1

# Inject irrelevant set operation
unique_values = set(round(x, 1) for x in telemetry_data)

# Main metric aggregation
metric_components = []
for system, weight in weight_map.items():
    # Apply threshold logic
    if weight >= thresholds['warning']:
        metric_components.append(weight * 100)

# Add fixed offset from unused pattern analysis
pattern_noise = analyze_pattern([1, 2, 3, 5, 8, 13])  # Fibonacci-like
offset_penalty = len(pattern_noise) * 2  # Looks like penalty, unused

# Final computation chain
aggregated_metric = sum(metric_components) + raw_stability

# Hidden conditional based on active node count
if active_nodes > 2:
    aggregated_metric *= 1.1

# The real answer derivation — well concealed
final_diagnostic = int(round(aggregated_metric + 5.25))

# Red herring output
print(f"Entropy: {entropy_score}")
print(f"Active Frequencies: {spectral_freq[:3]}")

# Required output
print(f"Result: {final_diagnostic}")