import itertools

def analyze_noise_floor(signal_sequence):
    noise_floor = sum(x ** 2 for x in signal_sequence if x < 0) / len(signal_sequence)
    normalized_energy = [abs(x - noise_floor) for x in signal_sequence]
    return normalized_energy

def filter_transient_peaks(data_stream):
    filtered = []
    for i in range(1, len(data_stream) - 1):
        if data_stream[i] > data_stream[i-1] and data_stream[i] > data_stream[i+1]:
            filtered.append(data_stream[i])
    return filtered if filtered else [0]

def detect_equilibrium(amplitude_profile):
    total_power = sum(itertools.accumulate(amplitude_profile, lambda x, y: x + y * 0.9))
    phase_shift = 0
    for val in amplitude_profile:
        if val > 5:
            phase_shift += 1
    baseline = total_power / len(amplitude_profile)
    stability_metric = abs(baseline - phase_shift)
    equilibrium_score = int(baseline - stability_metric)
    
    # Distractor computations (not directly used)
    dummy_transform = ''.join([str(int(x)) for x in amplitude_profile[:5] if x.is_integer()]) if hasattr(amplitude_profile[0], 'is_integer') else '0'
    checksum = sum(len(dummy_transform) * x for x in range(len(amplitude_profile))) % 100 if dummy_transform != '0' else 0
    
    return equilibrium_score

def main():
    raw_input_signal = [-2, 3, 7, -1, 4, 9, 0, 5, 8, -3]
    
    # Step 1: Analyze noise floor and normalize
    processed_signals = analyze_noise_floor(raw_input_signal)
    
    # Step 2: Extract transient peaks (distraction - not used later)
    spike_magnitudes = filter_transient_peaks(raw_input_signal)
    average_spike = sum(spike_magnitudes) / len(spike_magnitudes) if spike_magnitudes else 0
    
    # Step 3: Detect equilibrium state
    equilibrium_score = detect_equilibrium(processed_signals)
    
    # Irrelevant post-processing
    final_diagnostics = {"count": len(raw_input_signal), "max_raw": max(raw_input_signal), "checksum": average_spike}
    
    print(f"Result: {equilibrium_score}")

if __name__ == "__main__":
    main()