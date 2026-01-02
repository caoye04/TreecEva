from collections import defaultdict, Counter
import math

# Simulated sensor data processing pipeline with red herrings
def fetch_raw_samples():
    return [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

def apply_noise_filter(data):
    filtered = []
    for x in data:
        if x % 2 == 0:
            filtered.append(x + 1)
        else:
            filtered.append(x)
    return filtered

def compute_legacy_checksum(arr):
    # Irrelevant legacy function — dead code path
    checksum = 0
    for i, val in enumerate(arr):
        checksum += val * (i + 1)
    return checksum % 1000

def generate_frequency_bands(signal):
    # Real but misleading intermediate transformation
    bands = defaultdict(int)
    for sample in signal:
        if sample < 3:
            bands['low'] += 1
        elif sample < 7:
            bands['medium'] += 1
        else:
            bands['high'] += 1
    return dict(bands)

def compress_data_stream(raw):
    # Actual relevant compression: run-length encoding
    compressed = []
    count = 1
    for i in range(1, len(raw)):
        if raw[i] == raw[i-1]:
            count += 1
        else:
            compressed.append((raw[i-1], count))
            count = 1
    compressed.append((raw[-1], count))
    return compressed

def evaluate_signal_quality(metrics):
    # Distractor function — never called
    quality = 0.0
    for k, v in metrics.items():
        quality += v * 0.33
    return round(quality, 2)

def build_threshold_profile(config):
    # Relevant configuration map
    profile = defaultdict(float)
    profile['alpha'] = 0.7
    profile['beta'] = 1.4
    profile['gamma'] = 2.1
    profile['delta'] = 0.5  # unused but plausible
    return profile

def analyze_peaks_only(data):
    # Decoy analysis — not used
    peaks = []
    for i in range(1, len(data)-1):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            peaks.append(data[i])
    return len(peaks)

def analyze_signal(compressed, thresholds):
    # Core logic with subtle dependencies
    total_weight = 0.0
    base_offset = thresholds['alpha'] * thresholds['beta']
    
    # Real computation begins here
    for value, count in compressed:
        if count >= 2:
            contribution = value * count
            if value >= 5:
                contribution *= thresholds['gamma']
            else:
                contribution *= base_offset
            total_weight += contribution
    
    # Secondary adjustment using set logic
    unique_values = {v for v, _ in compressed}
    overlap_set = {5, 6} & unique_values
    bonus = 0
    if len(overlap_set) > 0:
        bonus = sum(overlap_set) * 10
    
    # Tertiary filter based on frequency pattern (distractor usage)
    freq_counter = Counter([v for v, c in compressed])
    rare_contrib = 0
    for val, freq in freq_counter.items():
        if freq == 1 and val % 2 == 0:
            rare_contrib += val  # minor effect
    
    final_score = total_weight + bonus - rare_contrib
    return int(round(final_score))

# --- Execution Pipeline ---
raw_samples = fetch_raw_samples()
filtered_samples = apply_noise_filter(raw_samples)

# Dead assignment — irrelevant structure
checksum = compute_legacy_checksum(filtered_samples)
diagnostic_metrics = generate_frequency_bands(filtered_samples)

# Unused decoy call
# peak_count = analyze_peaks_only(filtered_samples)

compressed_data = compress_data_stream(filtered_samples)

# Build threshold map (relevant)
threshold_map = build_threshold_profile({'mode': 'strict'})

# Unused variable — distractor
signal_quality = 0.0  # never updated

# Key statement
final_diagnostic = analyze_signal(compressed_data, threshold_map)

print(f"Result: {final_diagnostic}")