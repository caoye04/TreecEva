from collections import defaultdict

# Simulate a signal processing pipeline with calibration steps
def process_sensor_array(raw_readings):
    temporal_buffer = raw_readings[1:-1]  # Ignore first and last samples
    base_signal = [x * 0.87 for x in raw_readings if x > 0]
    
    # Irrelevant transformation (distractor)
    amplitude_envelope = [abs(x) ** 0.5 for x in raw_readings]
    peak_magnitude = max(amplitude_envelope) if amplitude_envelope else 0

    # Phase analysis with slicing and conditional filtering
    phase_components = []
    for i in range(1, len(base_signal)):
        delta = base_signal[i] - base_signal[i-1]
        if delta != 0:
            phase_components.append(int(delta * 10) % 360)
    
    # Misleading frequency binning (not used in final result)
    freq_distribution = defaultdict(int)
    for p in phase_components:
        freq_distribution[p // 30] += 1

    # Actual phase shift accumulation logic
    cumulative_shifts = []
    for idx, pc in enumerate(phase_components):
        if idx % 2 == 0:
            cumulative_shifts.append(pc)
        else:
            cumulative_shifts.append(-pc)
    
    net_phase_shift = sum(cumulative_shifts[:len(cumulative_shifts)//2])

    # Dead code path - never executed due to fixed condition
    debug_mode = False
    if debug_mode:
        print(f'Debug: {freq_distribution}')

    # Dummy correction function (does not alter net_phase_shift)
    def apply_correction(signal, shift):
        return [val + shift * 0.01 for val in signal]
    
    final_calibration = apply_correction(base_signal, net_phase_shift)
    
    # Output the target variable
    print(f'Result: {net_phase_shift}')

# Input data (seeded from real sensor profile)
raw_input = [0.5, -1.2, 2.3, 4.1, -0.3, 5.5, 3.8, 4.9, -2.1, 0.7]
process_sensor_array(raw_input)