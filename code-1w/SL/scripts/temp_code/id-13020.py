from collections import defaultdict, Counter
import math

# Simulated sensor data processing with diagnostic evaluation
def analyze_readings(raw_samples):
    sample_stats = defaultdict(float)
    outliers = []
    normalizer = 1.0
    temp_cache = []

    for reading in raw_samples:
        if reading < -100 or reading > 100:
            outliers.append(reading)
            continue

        sample_stats['sum'] += reading
        sample_stats['count'] += 1
        temp_cache.append(reading ** 0.5 if reading >= 0 else 0)

    if sample_stats['count'] == 0:
        sample_stats['mean'] = 0
    else:
        sample_stats['mean'] = sample_stats['sum'] / sample_stats['count']

    variance_accum = 0
    for reading in raw_samples:
        if -100 <= reading <= 100:
            variance_accum += (reading - sample_stats['mean']) ** 2

    sample_stats['variance'] = variance_accum / sample_stats['count'] if sample_stats['count'] > 0 else 0
    sample_stats['std_dev'] = math.sqrt(sample_stats['variance'])

    # Irrelevant transformation chain (distractor)
    transformed = list(map(lambda x: (x * 1.5) % 7, temp_cache))
    freq_dist = Counter(transformed)
    entropy_proxy = 0
    total = sum(freq_dist.values())
    for v in freq_dist.values():
        if v > 0 and total > 0:
            p = v / total
            entropy_proxy -= p * math.log(p)

    # Dead code path - never used (red herring)
    def deprecated_filter(x):
        return x > 2.7

    sample_stats['entropy_approx'] = entropy_proxy
    return sample_stats

# Secondary processing with bit manipulation decoy
def encrypt_key(base_value):
    masked = base_value ^ 0b110101
    shifted = (masked << 3) & 0b11111111
    return shifted ^ 0b10101010

# Unused recursive function (dead code, distraction)
def recursive_checksum(n):
    if n <= 1:
        return 1
    return (recursive_checksum(n - 1) + recursive_checksum(n - 2)) % 100

# Core logic buried among distractions
def compute_bounded_score(values, limit):
    score = 0
    for v in values:
        if v > limit:
            score += int(v // 10)
        elif v < -limit:
            score -= 1
    return abs(score)

# Main data pipeline with cross-references
data_stream = [23, -45, 67, 89, -12, 105, -200, 55, 77, 91]

# Step 1: Basic filtering and summary
valid_data = [x for x in data_stream if abs(x) <= 100]
size_factor = len(valid_data) * 2 if len(valid_data) % 2 == 0 else len(valid_data) * 3

# Step 2: Statistical analysis (relevant)
metrics = analyze_readings(data_stream)

# Step 3: Generate fake encryption trail (irrelevant)
key_seed = int(metrics['mean'])
cipher_tag = encrypt_key(key_seed)

# Step 4: Build composite structure with dictionary operations
aggregated = {
    'base': metrics,
    'flags': {f"F{i}": i * cipher_tag for i in range(3)},
    'aux_data': [compute_bounded_score(valid_data, t) for t in [5, 10, 15]]
}

# Step 5: Derive summary with min/max/average mix (some relevant)
data_summary = [
    aggregated['base']['mean'],
    aggregated['base']['std_dev'],
    min(valid_data),
    max(valid_data),
    len(aggregated['aux_data'])
]

# Step 6: Activation logic with modular arithmetic red herring
mod_trigger = (cipher_tag + len(valid_data)) % 13
activation_threshold = 4 if mod_trigger > 6 else 6

# Step 7: Final processing buried in lambda and dict ops (KEY STATEMENT)
process_metrics = lambda d, t: {
    'diagnosis': sum(math.ceil(x) for x in d if x > t),
    'backup': sum(1 for x in d if x < 0),
    'version': encrypt_key(8)  # unused field
}['diagnosis']

final_diagnostic = process_metrics(data_summary, activation_threshold)
print(f"Result: {final_diagnostic}")