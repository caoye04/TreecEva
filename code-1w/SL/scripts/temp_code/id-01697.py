import itertools

# Simulated sensor data processing with noise filtering and pattern analysis
def collect_samples():
    raw = [127, 63, 191, 31, 223, 15, 239, 7]
    filtered = []
    for x in raw:
        if x & 128:  # Only high-energy pulses
            filtered.append(x ^ 255)  # Invert bits for normalization
    return filtered

# Irrelevant helper - decoy function dealing with temperature (not used)
def compute_thermal_drift(samples):
    total = 0
    for s in samples:
        total += (s >> 4) * 0.3
    return round(total / len(samples), 2)

# Signal transformation: extract bit patterns and group by similarity
def transform_signal(data):
    patterns = []
    for d in data:
        ones = bin(d).count('1')
        shifted = (d << 1) & 255
        combined = d ^ shifted
        patterns.append({'value': d, 'popcount': ones, 'combined': combined})
    return patterns

# Frequency analysis on transformed signal blocks
def detect_frequencies(patterns):
    freq_map = {}
    for p in patterns:
        pc = p['popcount']
        freq_map[pc] = freq_map.get(pc, 0) + 1
    return freq_map

# Unused path: spectral decomposition (red herring)
def decompose_spectrum(freqs):
    result = 1
    for k, v in freqs.items():
        result *= (k + v) % 7
    return result

# Core logic: generate entropy-like metric from distribution
def calculate_entropy(dist):
    total = sum(dist.values())
    entropy = 0.0
    for count in dist.values():
        prob = count / total
        if prob > 0:
            entropy -= prob * __import__('math').log2(prob)
    return round(entropy, 6)

# Secondary transformation using itertools to generate rolling pairs
def create_pair_metrics(data_list):
    rolling = []
    for a, b in itertools.pairwise(data_list):
        rolling.append((a['combined'] & b['combined']) % 17)
    return rolling

# Threshold engine - evaluates multiple criteria across dimensions
def evaluate_thresholds(metrics, entropy_val):
    thresh = {}
    thresh['level_a'] = sum(1 for m in metrics if m > 5) > 2
    thresh['level_b'] = entropy_val > 2.1
    thresh['level_c'] = len(metrics) % 2 == 0
    thresh['level_d'] = metrics[-1] in [0, 1, 2] if metrics else False
    return thresh

# Misleading diagnostic - looks important but unused in final path
def legacy_diagnostic(patts, thres):
    score = 0
    for p in patts:
        if p['popcount'] >= 3:
            score += p['value'] % 5
    if thres.get('level_a'):
        score *= 2
    return score + 11

# Final analysis combining pattern structure and threshold logic
def analyze_pattern(transformed, thresholds):
    valid_count = 0
    for item in transformed:
        # Check if popcount matches frequent categories
        pc = item['popcount']
        if pc in [3, 4, 5]:
            valid_count += (item['value'] & 0xF)
    multiplier = 1
    if thresholds['level_b'] and not thresholds['level_d']:
        multiplier = 3
    elif thresholds['level_a']:
        multiplier = 2
    return valid_count * multiplier

# --- Main Execution ---
raw_sensor_data = collect_samples()

# Dead code path - assigned but never used
temperature_baseline = compute_thermal_drift(raw_sensor_data)
decoy_signal = [x * 0.95 for x in raw_sensor_data if x < 100]

transformed_data = transform_signal(raw_sensor_data)
frequency_distribution = detect_frequencies(transformed_data)

# Another unused transformation
pair_metrics = create_pair_metrics(transformed_data)
spectral_signature = decompose_spectrum(frequency_distribution)

entropy_diagnostic = calculate_entropy(frequency_distribution)

# Evaluate threshold conditions
critical_thresholds = evaluate_thresholds(pair_metrics, entropy_diagnostic)

# Legacy system call - computed but irrelevant
old_system_flag = legacy_diagnostic(transformed_data, critical_thresholds)

# Key computation step
final_diagnostic = analyze_pattern(transformed_data, critical_thresholds)

# Output the required result
print(f"Result: {final_diagnostic}")