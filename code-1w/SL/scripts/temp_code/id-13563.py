import math

# System diagnostics simulation with signal processing and red herrings
def generate_noise(length):
    return [math.sin(i * 0.1) + math.cos(i * 0.3) for i in range(length)]

def extract_features(data):
    # Irrelevant feature extraction (dead-end function)
    return {f'feat_{i}': val ** 2 for i, val in enumerate(data[:5])}

def filter_anomalies(signal_list):
    # Real filtering logic buried among distractions
    threshold = sum(abs(x) for x in signal_list) / len(signal_list) * 1.5
    clean = [x for x in signal_list if abs(x) < threshold]
    return clean

def shift_cipher(values, key):
    # Bit manipulation red herring
    shifted = []
    for v in values:
        raw = int(abs(v) * 100) & 0xFF
        masked = (raw ^ key) << 1
        if masked > 255:
            masked >>= 1
        shifted.append(masked)
    return shifted

def compute_entropy(seq):
    # Distractor: looks important but unused in final result
    from collections import Counter
    counts = Counter(seq)
    total = len(seq)
    entropy = -sum((count / total) * math.log2(count / total) for count in counts.values())
    return round(entropy, 4)

def rolling_average(data, window=3):
    # Unused but plausible intermediate calculation
    averages = []
    for i in range(len(data) - window + 1):
        averages.append(sum(data[i:i+window]) / window)
    return averages

def build_lookup_table(keys):
    # Complex-looking but irrelevant dictionary transformation
    table = {}
    for k in keys:
        bin_str = bin(k)[2:].zfill(8)
        flipped = ''.join('1' if b == '0' else '0' for b in bin_str)
        table[k] = int(flipped, 2)
    return table

def detect_sequence_pattern(arr):
    # Core logic step 1: find alternating sign runs
    runs = []
    current_run = 0
    for i in range(1, len(arr)):
        if arr[i] * arr[i-1] < 0:  # sign change
            current_run += 1
        else:
            if current_run > 0:
                runs.append(current_run)
                current_run = 0
    if current_run > 0:
        runs.append(current_run)
    
    mode = max(set(runs), key=runs.count) if runs else 0
    return mode

def aggregate_metrics(signals):
    # Core logic step 2: statistical summary
    positive_count = len([x for x in signals if x > 0])
    negative_count = len([x for x in signals if x < 0])
    zero_crossings = sum(1 for i in range(1, len(signals)) if signals[i]*signals[i-1] < 0)
    total_energy = sum(x*x for x in signals)
    return {
        'pos': positive_count,
        'neg': negative_count,
        'cross': zero_crossings,
        'energy': total_energy
    }

def analyze_pattern(raw_signal, key):
    # === Critical execution point ===
    filtered = filter_anomalies(raw_signal)
    
    # Red herring: complex set operations with no impact
    raw_set = set(int(abs(x)*10) for x in raw_signal)
    noise_floor = set(range(10, 20))
    spectral_components = raw_set & noise_floor | {key}
    adjustment_factor = len(spectral_components) - len(raw_set.intersection(noise_floor))
    
    # Real work continues...
    metrics = aggregate_metrics(filtered)
    pattern_length = detect_sequence_pattern(filtered)
    
    # Key dictionary usage: cross-referencing
    config_map = {
        'gain': 2.1,
        'bias': -0.5,
        'scale': 1.75
    }
    
    # Core calculation chain
    base_score = metrics['energy'] * 0.01
    adjusted = (base_score + config_map['bias']) * config_map['scale']
    if pattern_length > 0:
        adjusted *= (1 + pattern_length * 0.1)
    
    # Final interference: decoy recursive call
    def decay_sequence(n, factor=0.9):
        if n <= 1:
            return n
        return factor * decay_sequence(n - 1, factor)
    
    # This looks impactful but only adds minor perturbation
    recursive_dampener = decay_sequence(5)
    adjusted *= recursive_dampener
    
    # Final adjustment using set-derived factor (only slight influence)
    adjustment_factor = max(1.0, adjustment_factor * 0.1)
    final_value = adjusted * adjustment_factor
    
    return int(round(final_value))

# Simulated sensor input (deterministic)
sensor_baseline = [0.1, -0.3, 0.2, -0.4, 0.35, -0.2, 0.15, -0.5, 0.4, -0.3]
noise_component = generate_noise(10)
collected_signals = [sensor_baseline[i] + noise_component[i] for i in range(10)]

# Decoy data structures
diagnostic_log = {
    'timestamp': 1234567890,
    'status': 'active',
    'readings': collected_signals.copy(),
    'checksum': sum(abs(x) for x in collected_signals)
}

# Unused but plausible transformation
transformed = shift_cipher(collected_signals, key=7)
feature_dump = extract_features(collected_signals)
lookup = build_lookup_table([7, 15, 31])

# Key system parameter (used in analysis)
system_key = len(lookup)  # evaluates to 3

# === EXECUTION POINT OF INTEREST ===
final_diagnostic = analyze_pattern(collected_signals, system_key)

# Output result as required
print(f"Target result: {final_diagnostic}")