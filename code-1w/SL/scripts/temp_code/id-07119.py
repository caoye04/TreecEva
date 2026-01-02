def analyze_signal_integrity(raw_samples, threshold=0.75):
    sample_size = len(raw_samples)
    amplitude_peaks = [x for x in raw_samples if x > threshold]
    peak_count = len(amplitude_peaks)
    
    # Irrelevant signal smoothing (distractor)
    smoothed = []
    for i in range(len(raw_samples)):
        window = raw_samples[max(0, i-2):min(i+3, len(raw_samples))]
        smoothed.append(sum(window) / len(window))
    
    # Misleading normalization path (dead logic)
    normalized = [x / max(raw_samples) for x in raw_samples if max(raw_samples) != 0]
    if len(normalized) > 10:
        normalized = normalized[:10]

    # Actual relevant metric: count of samples above dynamic threshold
    dynamic_ref = sum(raw_samples) / sample_size if sample_size else 0
    high_energy_regions = 0
    for val in raw_samples:
        if val > dynamic_ref * 1.1:
            high_energy_regions += 1

    return high_energy_regions


def evaluate_noise_profile(noise_sequence):
    # Bit manipulation red herring
    binary_fingerprint = 0
    for num in noise_sequence:
        binary_fingerprint ^= int(num * 100) & 0xFF
    
    # Character counting decoy (never used)
    digit_frequency = {}
    for char in ''.join([str(int(x*10)) for x in noise_sequence]):
        digit_frequency[char] = digit_frequency.get(char, 0) + 1

    # Real computation: modular periodicity check
    period_count = 0
    for i in range(1, min(8, len(noise_sequence))):
        if all(abs(noise_sequence[j] - noise_sequence[j-i]) < 0.05 for j in range(i, len(noise_sequence), i)):
            period_count += 1

    return period_count

# Distractor function with no impact
def compute_spectral_entropy(signal):
    import math
    power_spectrum = [x**2 for x in signal]
    total_power = sum(power_spectrum)
    if total_power == 0:
        return 0.0
    entropy = -sum((p / total_power) * math.log(p / total_power + 1e-9) for p in power_spectrum)
    return entropy

# Unused recursive structure (red herring)
def recursive_window_sum(data, depth=0):
    if depth >= 3 or len(data) < 2:
        return sum(data)
    return data[0] + recursive_window_sum(data[1:], depth + 1)

# Main processing chain
baseline_signals = [0.4, 0.6, 0.8, 0.3, 0.7, 0.9, 0.5, 0.2]
interference_pattern = [0.1, 0.7, 0.6, 0.8, 0.2, 0.6, 0.4, 0.9]

# Composite transformation with zip and enumerate (relevant)
combined_weights = []
for i, (a, b) in enumerate(zip(baseline_signals, interference_pattern)):
    weight = a * 0.6 + b * 0.4
    adjustment = 0.1 if i % 3 == 0 else 0.05
    combined_weights.append(weight + adjustment)

# Dead code path: conditional expression not used
status_flag = 'stable' if len(combined_weights) > 5 else 'caution'
diagnostic_log = {f'step_{i}': 'ok' for i in range(len(combined_weights))}

# Decoy dictionary operations
validation_map = {
    'tolerance': 0.05,
    'thresholds': [0.3, 0.5, 0.7],
    'modes': {'safe', 'active', 'debug'},
    'checksum': sum(1 for x in combined_weights if x > 0.5)
}

# Irrelevant case conversion chain
mode_labels = ['SafeMode', 'ActiveMode', 'DebugMode']
mapped_modes = {label.lower().replace('mode', ''): idx for idx, label in enumerate(mode_labels)}

# Real processing begins here (hidden among distractors)
processing_chain = []
for w in combined_weights:
    if w > 0.6:
        processing_chain.append(w * 1.2)
    elif w > 0.4:
        processing_chain.append(w * 0.8)
    else:
        processing_chain.append(w * 1.5)

# Critical multi-step aggregation (target)
def aggregate_metrics(chain, validations):
    base_score = 0
    # Step 1: Sum of scaled values above threshold
    for val in chain:
        if val > 0.7:
            base_score += val * 100
    
    # Step 2: Subtract penalty based on modular distribution
    mod_penalty = 0
    for i, val in enumerate(chain):
        if i % 4 == 0:
            mod_penalty += int(val * 10) % 3
    
    # Step 3: Add bonus for consecutive high values
    bonus = 0
    consecutive_high = 0
    for val in chain:
        if val > 0.75:
            consecutive_high += 1
        else:
            if consecutive_high >= 2:
                bonus += 25
            consecutive_high = 0
    if consecutive_high >= 2:
        bonus += 25
    
    # Step 4: Apply bitwise adjustment (minor effect)
    final_bits = int(base_score) & int(bonus * 2)
    final_bits ^= int(mod_penalty * 50)
    
    # Final diagnostic calculation
    raw_diagnostic = base_score - (mod_penalty * 15) + bonus
    final_diagnostic = abs(raw_diagnostic + final_bits * 0.1)
    
    # Red herring: this print is irrelevant
    debug_state = 'normal' if final_diagnostic < 100 else 'alert'
    return int(final_diagnostic)

# Execution point of interest
final_diagnostic = aggregate_metrics(processing_chain, validation_map)
Result: {final_diagnostic}