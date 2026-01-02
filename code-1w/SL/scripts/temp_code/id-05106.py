import itertools

# System parameters (many are red herrings)
base_threshold = 17.3
redundancy_factor = 2.4
core_dampener = 0.85
legacy_offset = -4.2
sync_granularity = 128
timing_jitter = 0.0031
phase_lock = True

# Irrelevant signal processing constants
carrier_frequency = 960.7
data_bandwidth = 14.2
modulation_index = 1.8
fft_resolution = 1024

# Node simulation data with realistic naming
node_ids = ['NTR-204', 'NTR-318', 'NTR-112', 'NTR-405', 'NTR-522']
activation_states = [True, False, True, True, False]
signal_strengths = [87.3, 45.1, 92.7, 68.4, 33.9]
latency_buckets = [12, 23, 8, 17, 41]

# Distractor: unused transformation chain
def legacy_normalizer(val):
    return (val - legacy_offset) * core_dampener

def deprecated_encoder(x):
    return (x ** 1.05) % 256

# Decoy function that looks important but isn't used
def calculate_phase_shift(nodes, jitter, lock):
    if lock:
        return sum(hash(n) for n in nodes) * jitter
    else:
        return 0

# Real computation begins here — subtle and buried among noise
active_indices = [
    i for i, active in enumerate(activation_states) if active
]

filtered_strengths = [
    signal_strengths[i] for i in active_indices
]

# Simulate multi-dimensional load distribution using Cartesian product
load_combinations = list(itertools.product([2, 3], [4, 5]))
combination_sums = [a * b for a, b in load_combinations]  # [8, 10, 12, 15]

# Weighted transform using lambda abstraction
weight_function = lambda s, lat: (s ** 2) / (lat + 1) if lat > 0 else s
weighted_metrics = [
    weight_function(signal_strengths[i], latency_buckets[i])
    for i in range(len(signal_strengths))
]

# Aggregation pipeline with red herring intermediate steps
rolling_buffer = []
for val in combination_sums:
    rolling_buffer.append(val * 0.75)  # Distractor accumulation

# Key transformation logic — non-obvious due to surrounding noise
transform_chain = [
    filtered_strengths[0] + weighted_metrics[2],
    filtered_strengths[1] * 0.5,
    weighted_metrics[3] - base_threshold  # base_threshold is real but others aren't
]

intermediate_flux = sum(transform_chain) * core_dampener  # core_dampener is relevant

# Final aggregation function — looks like it does more than it does
def aggregate_transform(nodes):
    node_hash_vals = [hash(n) % 1000 for n in nodes]
    hash_sum = sum(node_hash_vals)
    # Only uses intermediate_flux and hash_sum; all other params are decoys
    return int(intermediate_flux + (hash_sum % 47))

# Execution point of interest
final_flux = aggregate_transform(network_nodes=node_ids)

# Print result as required
print(f"Result: {final_flux}")