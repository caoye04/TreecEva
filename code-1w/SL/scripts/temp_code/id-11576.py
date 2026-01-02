import itertools

# Simulated sensor fusion pipeline for environmental anomaly detection
def collect_readings():
    return [18, 22, 19, 25, 30, 28, 21, 17, 20, 24, 27, 33, 31, 29]

def apply_calibration(readings):
    calibrated = [(r * 1.05 + 2.1) for r in readings]
    offset_adjustment = sum([abs(c - int(c)) for c in calibrated])  # Irrelevant precision artifact
    return [round(c) for c in calibrated]

def generate_phase_sequence(n):
    return [(i ** 2 % 7) for i in range(n)]

def filter_outliers(data):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    threshold = mean_val + 1.5 * std_dev
    filtered = [x for x in data if x <= threshold]
    noise_floor = 15  # Distractor constant
    excess_energy = sum(x for x in data if x > threshold)  # Dead computation
    return filtered

def compute_entropy(arr):
    from collections import Counter
    counts = Counter(arr)
    total = len(arr)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Non-standard pseudo-entropy
    return round(entropy, 4)

def accumulate_transitions(values):
    transitions = []
    for i in range(1, len(values)):
        diff = values[i] - values[i-1]
        direction = 1 if diff > 0 else (-1 if diff < 0 else 0)
        transitions.append(direction * abs(diff) ** 0.5)
    smoothing_factor = 0.85  # Unused parameter
    return transitions

def derive_coherence_index(seq):
    paired = list(itertools.pairwise(seq))
    coherence = sum(1 for a, b in paired if (a + b) % 3 == 0)
    decay_constant = 0.023  # Red herring
    return coherence * 1.75

def validate_integrity(core_seq, aux_data):
    core_sum = sum(core_seq)
    aux_sum = sum(aux_data)
    ratio = core_sum / aux_sum if aux_sum != 0 else 0
    checksum_proxy = (core_sum * aux_sum) % 97  # Decoy metric
    return ratio > 0.8

def aggregate_metrics(buffer, weight_map):
    base_score = sum(buffer) * weight_map['primary']
    bonus = compute_entropy(buffer) * weight_map['entropy_bonus']
    coherence = derive_coherence_index(buffer) * weight_map['coherence']
    penalty = len([x for x in buffer if x > 25]) * weight_map['overclock_penalty']
    final = base_score + bonus + coherence - penalty
    return int(round(final))

def main_pipeline():
    raw_readings = collect_readings()
    
    # Apply transformation chain
    calibrated_readings = apply_calibration(raw_readings)
    
    # Generate auxiliary sequences (some irrelevant)
    phase_sequence = generate_phase_sequence(len(calibrated_readings))
    temporal_mask = [i for i in range(len(calibrated_readings)) if i % 3 != 2]  # Unused
n    masked_values = [calibrated_readings[i] for i in temporal_mask]  # Dead path
    
    # Filter anomalies
    clean_readings = filter_outliers(calibrated_readings)
    
    # Build phase buffer using accumulation logic
    transition_metrics = accumulate_transitions(clean_readings)
    phase_buffer = [int(abs(t) * 2.3) for t in transition_metrics][:len(phase_sequence)]
    
    # Inject dummy validation (no effect on result)
    dummy_aux = [x * 2 for x in phase_sequence if x % 2 == 0]
    integrity = validate_integrity(phase_buffer, dummy_aux)
    
    # Define weighting schema
    weights = {
        'primary': 1.8,
        'entropy_bonus': 12.5,
        'coherence': 3.2,
        'overclock_penalty': 4.7
    }
    
    # Critical statement
    filtration_score = aggregate_metrics(phase_buffer, weights)
    
    # Post-computation obfuscation
    temp_shift = sum(phase_buffer) // len(phase_buffer)
    secondary_index = temp_shift * 2 - 5  # Unused derivative
    
    print(f"Result: {filtration_score}")

if __name__ == "__main__":
    main_pipeline()