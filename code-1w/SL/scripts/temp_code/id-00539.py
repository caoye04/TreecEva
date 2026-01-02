def analyze_signal(samples, threshold=0.7):
    filtered = [s for s in samples if abs(s) > threshold]
    squared_energy = sum(x * x for x in filtered)
    phase_shift = len(filtered) % 4
    return squared_energy + phase_shift * 0.25


def compress_data(data_stream):
    compressed = []
    for i in range(0, len(data_stream), 2):
        chunk = data_stream[i:i+2]
        if len(chunk) == 2:
            compressed.append(chunk[0] * 2 + chunk[1])
    return compressed


def evaluate_stability(readings):
    baseline = sum(readings) / len(readings)
    variance = sum((x - baseline) ** 2 for x in readings) / len(readings)
    stability_score = 1 / (1 + variance)
    return stability_score > 0.5

# Irrelevant helper (distractor)
def utility_checksum(seq):
    return sum(seq) % 17

# Unused function (dead code path)
def legacy_transform(x):
    return (x << 2) ^ 0xAFFE

# Simulated sensor inputs (real data)
sensor_samples = [0.1, 0.8, -0.9, 0.3, 0.75, -1.2, 0.05, 0.6]
data_payload = [1, 0, 1, 1]

# Misleading intermediate processing (red herring)
temp_analysis = [
    analyze_signal(sensor_samples, t) 
    for t in [0.5, 0.6, 0.7]
]

# Decoy variables with plausible but unused values
decoy_flag = evaluate_stability([0.5, 0.55, 0.48, 0.51])
decoy_buffer = compress_data(data_payload)

# Core processing chain (relevant)
processing_chain = [
    analyze_signal(sensor_samples, 0.65),
    analyze_signal([x * 1.1 for x in sensor_samples], 0.7),
    analyze_signal([x * 0.9 for x in sensor_samples], 0.6)
]

# Diagnostic flags (some irrelevant)
diagnostics = {
    'sensor_integrity': True,
    'cache_aligned': False,
    'legacy_mode': False,  # unused field
    'checksum_valid': True,
    'sample_count': len(sensor_samples)
}

# Secondary distraction: complex but unused calculation
aggregated_noise = sum(
    abs(sample) ** 1.5 for sample in sensor_samples 
    if abs(sample) < 0.5
) / len(sensor_samples)

# Unused bitwise transformation (distractor)
transformed_mask = 0
for val in data_payload:
    transformed_mask ^= (val << 3) & 0xF

# Critical function combining multiple concepts
def aggregate_metrics(metrics, meta):
    base = sum(metrics)
    modifier = 1.0
    if meta['sensor_integrity'] and meta['checksum_valid']:
        modifier += 0.1
    if meta['cache_aligned']:
        modifier *= 0.9
    # Inject conditional expression (required python feature)
    adjustment = 10 if len(metrics) >= 3 else 5
    return int(base * modifier) + adjustment

# Key execution point
final_diagnostic = aggregate_metrics(processing_chain, diagnostics)

# Output result as required
print(f"Result: {final_diagnostic}")