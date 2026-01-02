import math

def analyze_phase_shift(frequency, amplitude, phase):
    # Irrelevant signal processing function (dead code path)
    return (amplitude * math.sin(2 * math.pi * frequency + phase)) ** 2

def compute_entropy(data):
    # Misleading entropy calculation on shuffled data (distractor)
    total = 0
    for x in data:
        if x > 0:
            total -= x * math.log(x)
    return round(total, 4)

def evaluate_resilience(profile):
    # Unused structural analysis with complex but irrelevant logic
    resilience_score = 0
    for i in range(len(profile)):
        if profile[i] % 7 == 0:
            resilience_score += 3
        elif profile[i] % 3 == 0:
            resilience_score += 2
    return resilience_score

def extract_critical_segments(signal, window_size=5):
    # Slicing operation used in decoy path
    segments = []
    for i in range(0, len(signal) - window_size + 1):
        segment = signal[i:i+window_size]
        if sum(segment) > 15:
            segments.append(segment)
    return segments

def calculate_strain_response(stress_sequence, config):
    # Core relevant logic begins
    threshold = config['base'] * (1 + config['margin'])
    decay_factor = config['decay']
    cumulative_stress = 0
    transient_buffer = []

    for idx, stress in enumerate(stress_sequence):
        adjusted_stress = stress * (0.95 ** idx)  # Exponential decay

        if adjusted_stress < threshold:
            cumulative_stress += adjusted_stress * decay_factor
        else:
            cumulative_stress += max(0, adjusted_stress - threshold)

        # Bitwise manipulation as red herring
        masked = int(adjusted_stress) & 0xFF
        if masked % 5 == 0:
            transient_buffer.append(masked)

        # Early break based on misleading condition
        if len(transient_buffer) > 4:
            break

    # Real answer depends only on full traversal without early exit
    if len(transient_buffer) <= 4:
        processed = [x for x in stress_sequence[::2] if x > 8]  # Slicing and filtering
        avg_peak = sum(processed) / len(processed) if processed else 0
        peak_correction = abs(math.sin(avg_peak / 10))
        final_yield_value = math.floor((cumulative_stress + avg_peak) * peak_correction)
    else:
        final_yield_value = -999  # Decoy result

    return final_yield_value

# Main execution block
if __name__ == "__main__":
    # Input setup
    stress_levels = [12, 7, 15, 6, 21, 9, 13, 5]
    threshold_config = {
        'base': 8.5,
        'margin': 0.15,
        'decay': 1.2
    }

    # Distractor variables and computations
    entropy_data = [0.1, 0.3, 0.6, 0.2, 0.8]
    shannon_entropy = compute_entropy(entropy_data)
    phase_result = analyze_phase_shift(50, 1.5, 0.7)
    material_profile = [21, 14, 7, 28, 35]
    robustness_index = evaluate_resilience(material_profile)
    filtered_windows = extract_critical_segments(stress_levels)

    # Key computation
    final_yield = calculate_strain_response(stress_sequence=stress_levels, threshold_config=threshold_config)

    # Output
    print(f"Result: {final_yield}")