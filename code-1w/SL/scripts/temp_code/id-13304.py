def analyze_signal(samples, config):
    filtered = [x for x in samples if abs(x) > config['noise_floor']]
    squared_energy = sum([x * x for x in filtered])
    peak_amplitude = max(filtered, default=0)
    normalized_power = squared_energy / (len(filtered) + 1e-8)

    # Irrelevant transformation chain (distractor)
    temp_cache = set()
    for val in samples:
        temp_cache.add(val % 7)
    derived_keys = {k: k * k + 2 for k in temp_cache if k % 3 == 1}
    unused_aggregate = sum(derived_keys.values()) * 0.5

    # Dead code path (misleading intermediate)
    def deprecated_calibrate(x):
        return (x + 32768) % 65536

    # Actual relevant logic buried in noise
    envelope = [abs(x) for x in samples]
    avg_envelope = sum(envelope) / len(envelope)
    zero_crossings = sum(1 for i in range(1, len(envelope)) if (envelope[i] > avg_envelope) != (envelope[i-1] > avg_envelope))

    stats_blob = {
        'energy': squared_energy,
        'zc': zero_crossings,
        'peak': peak_amplitude,
        'power': normalized_power
    }

    return stats_blob


def compute_entropy(data_list):
    from math import log2
    freq_map = {}
    for item in data_list:
        freq_map[item] = freq_map.get(item, 0) + 1
    total = len(data_list)
    entropy = -sum((count / total) * log2(count / total) for count in freq_map.values())
    return entropy if total > 0 else 0.0

# Unused diagnostic function (red herring)
def evaluate_coherence(signal_pair):
    a, b = signal_pair
    coherence_score = 0
    for i in range(min(len(a), len(b))):
        coherence_score += 1 if abs(a[i] - b[i]) < 0.1 else 0
    return coherence_score / min(len(a), len(b))

# Main processing pipeline
raw_samples = [i * (-1)**i * (i % 13) for i in range(1, 128) if i % 5 != 0]
config_settings = {
    'noise_floor': 5,
    'sample_rate': 44100,
    'window_size': 1024
}

# Step 1: Signal analysis
analysis_result = analyze_signal(raw_samples, config_settings)

# Step 2: Generate auxiliary metrics (some irrelevant)
character_profile = [chr(abs(x) % 26 + 97) for x in raw_samples]
duplicate_chars = len(character_profile) - len(set(character_profile))
char_entropy = compute_entropy(character_profile)

# Step 3: Build buffer with multiple layers of processing
aggregate_buffer = []
for i, sample in enumerate(raw_samples):
    if i % 7 == 0:
        transformed = sample ^ (i & 15)
        aggregate_buffer.append(transformed * (transformed > 0))

# Step 4: Create threshold map with decoy entries
threshold_map = {
    'low': 10,
    'mid': 25,
    'high': 60,
    'legacy_mode': False,
    'calibration_offset': -17  # unused
}

# Step 5: Conditional metric processing
if analysis_result['power'] > 150 and analysis_result['zc'] < 40:
    adjustment_factor = 1.75
else:
    adjustment_factor = 0.85

intermediate_score = (analysis_result['energy'] * 0.01) + (analysis_result['zc'] * 2)

# Step 6: Masked computation with list comprehension
mask_sequence = [i for i in range(len(aggregate_buffer)) if i % 3 == 2]
applied_mask = [aggregate_buffer[i] for i in mask_sequence if i < len(aggregate_buffer)]
masked_sum = sum(applied_mask)

# Step 7: Final processing function
def process_metrics(metrics_dict, thresholds):
    base_value = metrics_dict['energy'] // 100
    zc_factor = metrics_dict['zc'] % 11
    peak_level = metrics_dict['peak']

    # Real calculation hidden among distractions
    candidate_1 = base_value + zc_factor
    candidate_2 = (peak_level // 5) + len(applied_mask)

    # Distractor: unused conditional override
    if thresholds['legacy_mode']:
        result = candidate_1 * 3
    else:
        result = candidate_1 + candidate_2

    # Final adjustment using character entropy (irrelevant but plausible)
    final_adjust = int(char_entropy * 10)  # always 3 in this case
    result -= final_adjust

    return result

# Execute critical statement
final_diagnostic = process_metrics(analysis_result, threshold_map)
print(f"Target result: {final_diagnostic}")