import itertools

# Simulated sensor data processing with red herrings and complex transformations
def collect_readings():
    raw_readings = [i for i in range(100, 200, 3)]
    offset_adjustment = sum([x % 7 for x in raw_readings if x % 13 == 0])
    filtered_readings = [x for x in raw_readings if x % 2 == 0]
    return filtered_readings

# Irrelevant auxiliary function - dead code path
def deprecated_normalization(data):
    if not data:
        return []
    mean_val = sum(data) / len(data)
    return [round(x - mean_val, 2) for x in data]

# Unused transformation chain
def transform_amplitude(signal):
    phase_shift = list(itertools.accumulate([1] * len(signal), lambda a, b: (a + b) % 5))
    modulated = [s * p for s, p in zip(signal, phase_shift)]n    return modulated

# Core logic disguised among distractions
def generate_reference_map(values):
    # Real usage begins here
    base_seq = [v % 41 for v in values]
    shift_key = sum(base_seq[::3]) % 25
    shifted = [(v + shift_key) % 100 for v in base_seq]
    return dict(zip(values, shifted))

# Misleading statistical summary (not used in final result)
def compute_ignored_metrics(data):
    stats = {}
    stats['max'] = max(data)
    stats['min'] = min(data)
    stats['range'] = stats['max'] - stats['min']
    stats['median_guess'] = data[len(data)//2]
    entropy_proxy = sum([abs(data[i] - data[i-1]) for i in range(1, len(data))])
    stats['entropy'] = round(entropy_proxy / len(data), 3)
    return stats  # Never used

# Real processing starts
processed_data = collect_readings()

# Distractor: unused filtering
outlier_mask = [x for x in processed_data if (x // 10) % 2 != 0]
complement_set = [x for x in processed_data if x not in outlier_mask]

# Real mapping generation
reference_grid = generate_reference_map(processed_data)

# Fake clustering attempt
cluster_ids = []
current_cluster = 0
for i, val in enumerate(processed_data):
    if i > 0 and (val - processed_data[i-1]) > 10:
        current_cluster += 1
    cluster_ids.append(current_cluster)

# Decoy structure
analysis_frame = {
    'readings': processed_data,
    'clusters': cluster_ids,
    'grid': reference_grid,
    'version': '2.1-alpha',
    'timestamp': 1678886400
}

# Hidden key computation using lambda and itertools
pairwise_deltas = [processed_data[i+1] - processed_data[i] for i in range(len(processed_data)-1)]
running_product = list(itertools.accumulate(pairwise_deltas, lambda x, y: (x * y) % 97 + 1))
smoothed_signal = list(map(lambda x: (x ** 2) % 83, running_product))

# Final analysis with critical dependency on prior steps
def analyze_sequence(seq):
    mapped_values = [reference_grid[v] for v in seq]
    base_score = sum(mapped_values) % 1000
    
    # Secondary correction using signal chain
    correction_factor = smoothed_signal[len(smoothed_signal)//2] if smoothed_signal else 0
    adjustment = (correction_factor * 7) % 89
    
    # Final diagnostic computation
    final_score = base_score + adjustment
    
    # Red herring: unused conditional branch
    if final_score > 500:
        backup_ref = sum(running_product[-5:]) % 200
        final_score -= backup_ref // 3  # Not triggered due to actual value
        
    return final_score

# Execution point of interest
final_diagnostic = analyze_sequence(processed_data)
print(f"Target result: {final_diagnostic}")