import math

def analyze_signal_integrity(signal_chain):
    # Irrelevant signal metrics (distractor computations)
    avg_amplitude = sum(abs(s) for s in signal_chain) / len(signal_chain)
    peak_to_peak = max(signal_chain) - min(signal_chain)
    rms_value = math.sqrt(sum(s**2 for s in signal_chain) / len(signal_chain))

    # Real computation: extract phase components (in radians)
    phases = [math.atan2(s, 1.0) for s in signal_chain]

    # Weighting factors based on frequency bin (some are red herrings)
    base_weights = [0.1 * i for i in range(1, len(signal_chain) + 1)]
    adjustment_factors = [math.cos(p * 0.5) for p in phases]
    weights = [w * af for w, af in zip(base_weights, adjustment_factors)]

    # Misleading normalization (not used in final calculation)
    normalized_weights = [w / sum(weights) for w in weights] if sum(weights) != 0 else weights

    # Noise threshold filtering (dead code path - condition never triggers due to data)
    filtered_pairs = []
    for i, (p, w) in enumerate(zip(phases, weights)):
        noise_floor = 0.05 * abs(math.sin(p))
        if w > noise_floor:  # Always true for this data
            filtered_pairs.append((p, w))

    # Actual key logic: calculate weighted phase interference
    def calculate_interference(phase_list, weight_list):
        total_weighted = sum(p * w for p, w in zip(phase_list, weight_list))
        total_weight = sum(weight_list)
        return total_weighted / total_weight if total_weight != 0 else 0.0

    net_phase_shift = calculate_interference(phases, weights)

    # Distractor: unused state tracking
    state_log = []
    for idx, val in enumerate(signal_chain):
        state_log.append({'index': idx, 'processed': False})

    return net_phase_shift

# Input signal sequence (fixed test vector)
signal_input = [0.5, -1.2, 0.8, -0.3, 1.7, -0.9]

# Execute main analysis
result = analyze_signal_integrity(signal_input)

# Critical variable assignment point
net_phase_shift = result

# Output target result
print(f"Target result: {net_phase_shift}")