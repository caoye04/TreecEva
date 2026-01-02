from collections import defaultdict, Counter
import math

# Simulated sensor array data processing with interference cancellation
def process_sensor_readings(raw_readings, noise_profile, threshold=0.15):
    filtered_readings = []
    noise_counter = Counter()
    phase_accumulator = defaultdict(float)

    for idx, reading in enumerate(raw_readings):
        if abs(reading - noise_profile.get(idx, 0)) > threshold:
            adjusted = reading * 1.07 - noise_profile.get(idx, 0.05)
            filtered_readings.append(round(adjusted, 6))
            noise_counter['anomalies'] += 1
        else:
            filtered_readings.append(reading)
            noise_counter['clean'] += 1

        # Irrelevant accumulation (distractor)
        phase_accumulator['dummy'] += math.sin(idx) * 0.01

    return filtered_readings, noise_counter


def generate_wave_components(base_freq, harmonics_config, sample_points=100):
    wave_data = []
    harmonic_contributions = []
    temp_buffer = []  # Unused buffer (red herring)

    for i in range(sample_points):
        base = math.sin(2 * math.pi * base_freq * i / sample_points)
        harmonic_sum = 0
        for h_num, strength in harmonics_config.items():
            harmonic_sum += strength * math.sin(2 * math.pi * h_num * base_freq * i / sample_points)
        
        total_wave = base + harmonic_sum
        wave_data.append(round(total_wave, 6))
        harmonic_contributions.append(harmonic_sum)

        # Dead code path - never executed due to logic
        if len(temp_buffer) > 1000:
            temp_buffer.clear()

    # Misleading transformation (not used later)
    normalized_harmonics = [abs(x) / max(map(abs, harmonic_contributions)) for x in harmonic_contributions[:10]]

    return wave_data

# Decoy function - looks important but unused
def compute_spectral_entropy(signal):
    magnitude_spectrum = [abs(math.sin(x)) for x in signal]
    total_power = sum(mag ** 2 for mag in magnitude_spectrum)
    probabilities = [(mag ** 2) / total_power for mag in magnitude_spectrum] if total_power > 0 else [0] * len(magnitude_spectrum)
    entropy = -sum(p * math.log(p, 2) for p in probabilities if p > 0)
    return round(entropy, 6)

# Core interference phase calculator
def calculate_interference_phase(waveform, calibration_multiplier):
    cumulative_shift = 0.0
    peak_count = 0
    zero_crossings = 0
    prev = waveform[0]
    
    # Track phase shifts at zero crossings
    for val in waveform[1:]:
        if prev < 0 <= val:
            zero_crossings += 1
            cumulative_shift += math.atan2(val, prev)
        elif prev > 0 >= val:
            zero_crossings += 1
            cumulative_shift -= math.atan2(val, prev)
        
        if abs(val) > 0.95 and abs(prev) > 0.95:
            peak_count += 1

        prev = val

    # Secondary irrelevant loop (distractor)
    decay_correction = 0.0
    for i in range(1000):
        decay_correction += math.exp(-i * 0.01) * 0.001
        if decay_correction > 0.5:
            break

    # Actual result computation buried in logic
    base_shift = cumulative_shift * calibration_multiplier
    adjustment_factor = (zero_crossings / len(waveform)) * peak_count
    final_shift = base_shift + adjustment_factor * 0.05

    # Red herring: unused conditional branch
    if len(waveform) % 7 == 0:
        dummy_var = math.gamma(final_shift)

    return round(final_shift, 6)

# Irrelevant helper (dead code)
def validate_signal_coherence(signal_vector):
    if not signal_vector:
        return False
    mean_val = sum(signal_vector) / len(signal_vector)
    variance = sum((x - mean_val) ** 2 for x in signal_vector) / len(signal_vector)
    return variance < 0.8

# Main execution flow
if __name__ == "__main__":
    # Simulated raw sensor input
    raw_input_stream = [
        0.02, -0.01, 0.48, -0.52, 0.89, -0.91, 0.33, -0.34, -0.05, 0.04,
        0.51, -0.49, 0.92, -0.88, 0.29, -0.31, 0.03, -0.02, 0.47, -0.53
    ]

    # Noise profile from environment (partially relevant)
    environmental_noise = {i: math.cos(i * 0.3) * 0.08 for i in range(len(raw_input_stream))}

    # Filtering step (relevant preprocessing)
    cleaned_signal, stats = process_sensor_readings(raw_input_stream, environmental_noise)

    # Generate harmonic interference pattern (relevant for final wave)
    harmonics = {2: 0.3, 3: 0.15, 5: 0.08}
    interference_pattern = generate_wave_components(1.0, harmonics, sample_points=len(cleaned_signal))

    # Combine signals (key composition)
    composite_wave = [
        round(cleaned_signal[i] + interference_pattern[i], 6)
        for i in range(len(cleaned_signal))
    ]

    # Calibration constant (looks arbitrary but is used)
    calibration_factor = 1.85

    # Critical statement: what is the value of net_phase_shift here?
    net_phase_shift = calculate_interference_phase(composite_wave, calibration_factor)

    # Print final target result
    print(f"Target result: {net_phase_shift}")