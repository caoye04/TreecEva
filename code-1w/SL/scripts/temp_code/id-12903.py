import math

# Simulated network telemetry data
timestamps = [1623456780 + i*60 for i in range(100)]
base_frequency = 2.4
doppler_shift = 0.07

# Irrelevant astronomical constants (distractor)
gravitational_constant = 6.67430e-11
light_speed_ratio = 1 / 137
planck_length = 1.616255e-35

# System node configuration
node_ids = [f'N{str(i).zfill(3)}' for i in range(1, 16)]
node_weights = {nid: (int(nid[1:]) % 7) + 1 for nid in node_ids}

# Signal processing chain
raw_signals = []
for t in timestamps:
    phase = base_frequency * t + math.sin(t * doppler_shift)
    signal = math.cos(phase) * math.exp(-((t % 3600) / 1800)**2)
    raw_signals.append(round(signal * 1000) / 1000)

# Decoy function: processes irrelevant astrophysical approximation
def calculate_redshift_factor(z):
    return light_speed_ratio * (1 + z)**2  # Unused later

# Real processing: extract peaks from signal
peak_magnitudes = []
for i in range(1, len(raw_signals) - 1):
    if raw_signals[i] > raw_signals[i-1] and raw_signals[i] > raw_signals[i+1]:
        peak_magnitudes.append(raw_signals[i])

# Distractor: unused peak smoothing with lambda (dead abstraction)
smooth_peak = lambda x: sum(x[i-1:i+2]) / 3 if len(x) >= 3 else x[0]

# Network node clustering based on weight classes
weight_classes = set(node_weights.values())
heavy_nodes = {k for k, v in node_weights.items() if v > 5}
medium_nodes = {k for k, v in node_weights.items() if 3 <= v <= 5}
light_nodes = {k for k, v in node_weights.items() if v < 3}

# Simulated packet loss patterns (partially relevant)
packet_loss_rate = {}
for nid in node_ids:
    base_loss = 0.01
    if nid in heavy_nodes:
        base_loss *= 1.5
    elif nid in light_nodes:
        base_loss *= 0.7
    packet_loss_rate[nid] = round(base_loss + (int(nid[1:]) % 10) * 0.001, 4)

# Data structure transformation: slice critical segment
signal_slice = raw_signals[25:75]  # Middle portion for analysis
slice_avg = sum(signal_slice) / len(signal_slice)
slice_variance = sum((x - slice_avg)**2 for x in signal_slice) / len(signal_slice)
slice_stddev = math.sqrt(slice_variance)

# False diagnostic path (red herring)
critical_threshold = planck_length * 1e30  # Absurdly small, never triggered
device_stability = 'STABLE'
if slice_stddev < critical_threshold:
    device_stability = 'UNSTABLE'

# Real metric computation
def compute_coherence_index(peaks, window_size=5):
    if len(peaks) < window_size:
        return 0.0
    windows = [peaks[i:i+window_size] for i in range(0, len(peaks), window_size)]
    coherences = []
    for w in windows:
        if len(w) == window_size:
            mean_w = sum(w) / len(w)
            var_w = sum((x - mean_w)**2 for x in w) / len(w)
            norm_var = var_w / (mean_w**2 + 1e-8)
            coherences.append(1 / (1 + norm_var))
    return round(sum(coherences) / len(coherences), 6) if coherences else 0.0

coherence_score = compute_coherence_index(peak_magnitudes)

# System load simulation
system_load = [round(0.3 + (i % 15) * 0.05, 3) for i in range(len(node_ids))]

# Core aggregation logic with distractors
irrelevant_combinations = set()
for h in heavy_nodes:
    for m in medium_nodes:
        irrelevant_combinations.add((h, m))

# Key function: combines multiple concepts
def aggregate_metrics(nodes, load_profile):
    # Nested logic with multiple steps
    weighted_load = 0.0
    active_count = 0
    
    # Map node ID to load using index-based offset (not direct correlation)
    node_load_map = {}
    for idx, nid in enumerate(nodes):
        shifted_idx = (idx + 7) % len(load_profile)  # Non-trivial indexing
        node_load_map[nid] = load_profile[shifted_idx] * node_weights[nid]
        
    # Filter nodes by dynamic condition
    for nid in nodes:
        w = node_weights[nid]
        l = node_load_map[nid]
        if w >= 4 and l > 0.45:  # Selective activation
            weighted_load += l * w
            active_count += 1
    
    # Incorporate coherence from signal analysis (cross-domain dependency)
    global coherence_score
    if active_count > 0:
        base_metric = weighted_load / active_count
        # Inject external computational result
        adjusted_metric = base_metric * (1 + coherence_score)
        final_value = int(round(adjusted_metric * 10000))
    else:
        final_value = 999
        
    # Dead code branch (never reached due to logic above)
    if len(irrelevant_combinations) > 100:
        fallback = math.gamma(final_value)  # Unused
        return fallback
        
    return final_value

# Execution point of interest
final_diagnostic = aggregate_metrics(network_nodes=node_ids, system_load=system_load)

# Print target result
print(f"Result: {final_diagnostic}")