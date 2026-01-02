import itertools

# Simulate multi-sensor signal processing with noise filtering and pattern detection
def preprocess_signal(raw_data, threshold=0.1):
    filtered = []
    cumulative_noise = 0
    for val in raw_data:
        if abs(val) > threshold:
            filtered.append(val * 0.95)
        else:
            cumulative_noise += val * 0.1  # Irrelevant accumulation
    return filtered


def generate_combinations(signals):
    # Generate all pairwise magnitude combinations (distractor: not directly used)
    pairs = list(itertools.combinations(signals, 2))
    magnitudes = [abs(a) + abs(b) for a, b in pairs]
    avg_magnitude = sum(magnitudes) / len(magnitudes) if magnitudes else 0
    return avg_magnitude


def analyze_phase(signal):
    positive_count = 0
    negative_count = 0
    zero_crossings = 0
    prev = signal[0]

    for val in signal:
        if val > 0:
            positive_count += 1
        elif val < 0:
            negative_count += 1
        
        if (prev < 0 and val >= 0) or (prev > 0 and val <= 0):
            zero_crossings += 1
        prev = val

    balance_ratio = (
        min(positive_count, negative_count) / max(positive_count, negative_count)
        if max(positive_count, negative_count) > 0 else 0
    )
    
    # Dead code path - never executed due to logic above
    if len(signal) == 0:
        balance_ratio = 0
        
    return balance_ratio, zero_crossings


def detect_equilibrium(signal_list):
    if not signal_list:
        return 0
        
    total_weight = 0
    adjustment_factor = 0.0
    equilibrium_candidates = []
    
    for sig in signal_list:
        ratio, crossings = analyze_phase(sig)
        weighted_score = ratio * (1 + 0.1 * crossings)
        
        # Use combination analysis as minor correction (semi-relevant)
        comb_mag = generate_combinations(sig)
        adjustment_factor += comb_mag * 0.05  # Minor influence
        
        equilibrium_candidates.append(weighted_score)
    
    # Final equilibrium score based on average stability
    base_equilibrium = sum(equilibrium_candidates) / len(equilibrium_candidates)
    final_score = base_equilibrium + adjustment_factor
    
    # Distractor variables below
    temp_normalization = sum([len(s) for s in signal_list]) * 0.001
    debug_state = {'processed': len(signal_list), 'adjusted': adjustment_factor}
    
    return int(round(final_score * 100))  # Discretized score


# Main execution block
raw_sensor_data = [
    [-0.2, 0.3, -0.15, 0.4, -0.35, 0.1],
    [0.5, -0.6, 0.2, -0.1, 0.05, -0.05],
    [-0.4, 0.3, -0.3, 0.25, -0.2, 0.15]
]

# Preprocess each sensor's data
processed_signals = []
noise_log = []
for data in raw_sensor_data:
    clean = preprocess_signal(data)
    processed_signals.append(clean)
    
    # Distractor: track something irrelevant
    noise_level = sum([abs(x) for x in data]) - sum([abs(x) for x in clean])
    noise_log.append(noise_level)

# Additional unused helper (dead code)
def validate_coherence(signals):
    return all(len(s) > 0 for s in signals)

# Key computation step
equilibrium_score = detect_equilibrium(processed_signals)

# Print result as required
print(f"Target result: {equilibrium_score}")