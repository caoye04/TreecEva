import math

def process_signal_chain(frequencies, phase_offsets, amplitude_mask):
    # Initialize key parameters
    base_frequency = 50.0
    accumulated_shift = 0.0
    temp_buffer = []
    correction_factor = 1.0
    baseline_error = 0.0314

    # Irrelevant amplitude processing (distractor)
    masked_amplitudes = [amp * 0.9 for amp in amplitude_mask if amp > 0.5]
    avg_amplitude = sum(masked_amplitudes) / len(masked_amplitudes) if masked_amplitudes else 0.0

    # Real computation: process frequency-phase relationship
    for i, (freq, phase) in enumerate(zip(frequencies, phase_offsets)):
        freq_ratio = freq / base_frequency
        normalized_phase = phase % (2 * math.pi)

        # Apply harmonic distortion model
        if freq_ratio > 1:
            harmonic_component = math.sin(normalized_phase * freq_ratio)
            accumulated_shift += harmonic_component * 0.1

        # Track buffer for unused diagnostic (distractor)
        temp_buffer.append({'index': i, 'value': harmonic_component if 'harmonic_component' in locals() else 0})

        # Conditional adjustment based on parity (real logic)
        if i % 2 == 0:
            accumulated_shift += math.cos(normalized_phase) * 0.05
        else:
            accumulated_shift -= math.log(freq_ratio + 1) * 0.02

    # Intermediate red herring variable
    spectral_density = sum([f ** 2 for f in frequencies]) / len(frequencies)

    # Destructuring assignment (tuple unpacking) - python idiom
    config_flags = (True, False, 'calibrated')
    enable_filter, _, status = config_flags

    # Lambda function to compute dynamic offset (required feature)
    dynamic_offset_fn = lambda x: round(x * correction_factor, 4)
    dynamic_offset = dynamic_offset_fn(sum(phase_offsets[:3]))

    # String slicing distraction - parsing dummy ID
    device_id = 'SIG-CHN-7842'
    channel_code = device_id[8:]  # '7842'
    is_valid_channel = channel_code.isdigit()

    # Core calculation with string method distraction
    shift_str = "{:.6f}".format(accumulated_shift)
    decimal_part = shift_str.split('.')[1]  # slicing and split
    precision_digit = int(decimal_part[3]) if len(decimal_part) > 3 else 0

    # Final phase adjustment incorporating string-derived digit (semi-relevant)
    net_phase_shift = accumulated_shift + (precision_digit * 0.001)

    # Key statement: this is where we need the value of net_phase_shift
    final_calibration = apply_correction(net_phase_shift, baseline_error)

    return final_calibration


def apply_correction(value, error):
    return value - error

# Input data setup
freqs = [50, 100, 150, 200]
phases = [0.1, 1.57, 3.14, 4.71]
amplitudes = [0.8, 0.6, 0.9, 0.3]

# Execute
result = process_signal_chain(freqs, phases, amplitudes)

# Extract target variable manually for inspection
base_frequency = 50.0
accumulated_shift = 0.0
for i, (freq, phase) in enumerate(zip(freqs, phases)):
    freq_ratio = freq / base_frequency
    normalized_phase = phase % (2 * math.pi)
    if freq_ratio > 1:
        harmonic_component = math.sin(normalized_phase * freq_ratio)
        accumulated_shift += harmonic_component * 0.1
    if i % 2 == 0:
        accumulated_shift += math.cos(normalized_phase) * 0.05
    else:
        accumulated_shift -= math.log(freq_ratio + 1) * 0.02
shift_str = "{:.6f}".format(accumulated_shift)
decimal_part = shift_str.split('.')[1]
precision_digit = int(decimal_part[3]) if len(decimal_part) > 3 else 0
net_phase_shift = accumulated_shift + (precision_digit * 0.001)

print(f"Result: {net_phase_shift}")