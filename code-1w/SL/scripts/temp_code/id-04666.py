import math

def analyze_signal_strength(signal_data, threshold=0.5):
    """Compute signal energy and filter strong components."""
    energy = sum([x ** 2 for x in signal_data])
    filtered = [x for x in signal_data if abs(x) > threshold]
    return energy, len(filtered)

def generate_frequency_components(base_freq, harmonics):
    """Generate harmonic frequency multiples."""
    return [base_freq * (i + 1) for i in range(harmonics)]

def calculate_interference_phase(freqs, alignment):
    """Calculate net phase shift from aligned frequency interference."""
    total_phase = 0.0
    phase_log = []
    
    for i, (freq, align) in enumerate(zip(freqs, alignment)):
        # Simulate phase contribution based on alignment index
        raw_phase = (freq * align * math.pi / 180) % (2 * math.pi)
        direction = 1 if i % 2 == 0 else -1
        adjusted_phase = direction * raw_phase
        total_phase += adjusted_phase
        phase_log.append(adjusted_phase)
    
    # Dummy accumulation to increase cognitive load
    cumulative_sum = 0
    temp_results = []
    for val in phase_log:
        cumulative_sum += abs(val) * 0.1
        temp_results.append(cumulative_sum)
    
    # Irrelevant secondary processing
    peak_deviation = max(phase_log) - min(phase_log) if phase_log else 0
    dummy_metric = len(temp_results) * cumulative_sum / (peak_deviation + 1e-5)
    
    # Final deterministic computation
    normalized_phase = total_phase % (2 * math.pi)
    scaled_output = int(normalized_phase * 1000)
    return scaled_output

# Main execution block
if __name__ == '__main__':
    # Signal parameters
    sample_window = [0.1, 0.4, 0.8, 0.9, -0.3, -0.7, 0.2]
    base_frequency = 12
    harmonic_count = 6

    # Extract features (some irrelevant)
    signal_energy, strong_components = analyze_signal_strength(sample_window, threshold=0.35)
    frequency_profile = generate_frequency_components(base_frequency, harmonic_count)
    
    # Alignment sequence derived from window indices above threshold
    alignment_mask = [i for i, x in enumerate(sample_window) if x > 0.25]
    extended_alignment = alignment_mask * 2  # Duplicate pattern
    alignment_sequence = extended_alignment[:len(frequency_profile)]
    
    # Fill missing alignment slots if any
    while len(alignment_sequence) < len(frequency_profile):
        alignment_sequence.append(len(alignment_sequence))
    
    # Introduce unused intermediate variables
    spectral_density = [math.sin(f * 0.1) for f in frequency_profile]
    coherence_score = sum(1 for s in spectral_density if s > 0.5)
    normalization_factor = math.sqrt(signal_energy + 1)
    
    # Key computational step with target variable
    net_phase_shift = calculate_interference_phase(frequency_profile, alignment_sequence)
    
    # Print result as required
    print(f"Result: {net_phase_shift}")