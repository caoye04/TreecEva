import math

# Simulate signal processing with noise filtering and frequency analysis
def analyze_frequency_profile(input_wave):
    base_amplitude = 8.4
    harmonic_series = [input_wave[i] * (i + 1) for i in range(len(input_wave))]
    
    # Apply windowing function to reduce spectral leakage (irrelevant for final result)
    hanning_window = [0.5 - 0.5 * math.cos(2 * math.pi * n / (len(input_wave) - 1)) for n in range(len(input_wave))]
    weighted_samples = [harmonic_series[i] * hanning_window[i] for i in range(len(harmonic_series))]
    
    # Distractor: Power spectrum estimation (not used in final calculation)
    power_spectrum = sum(x ** 2 for x in weighted_samples)
    avg_power = power_spectrum / len(weighted_samples) if weighted_samples else 0

    # Key computational chain begins here
    frequency_bins = []
    for val in harmonic_series:
        if val > 10:
            transformed = math.log(val, 2)
            if transformed > 3:
                frequency_bins.append(transformed)
    
    # Accumulate significant frequency contributions
    frequency_sum = sum(frequency_bins)
    
    # Correction based on system damping factor (semi-relevant)
    damping_log_table = {i: math.log(i+1, math.e) for i in range(1, 6)}
    raw_damping = sum(damping_log_table.values())
    normalized_damping = raw_damping / 5
    
    # Irrelevant smoothing filter
    smoothing_kernel = list(map(lambda x: x / sum(range(1,6)), range(1,6)))
    filtered_damping = normalized_damping * smoothing_kernel[2]  # unused beyond this
    
    # Critical path: correction factor derived from base constants
    reference_phase = 2 * math.pi
    correction_factor = (reference_phase / 100) * 0.75
    
    # Final computation point
    equilibrium_score = round(frequency_sum * correction_factor)
    
    # Print result as required
    print(f"Result: {equilibrium_score}")
    
    return equilibrium_score

# Input data with meaningful structure
input_signal = [1.2, 3.1, 2.8, 4.5, 6.0, 7.2, 5.8]
analyze_frequency_profile(input_signal)