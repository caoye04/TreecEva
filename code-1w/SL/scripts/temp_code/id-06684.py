from collections import defaultdict
import math

def analyze_frequency_response(freq_data):
    magnitude_profile = defaultdict(float)
    phase_contributions = []
    noise_floor = 0.003

    for band, details in freq_data.items():
        raw_magnitude = details['amplitude']
        base_freq = details['frequency']
        
        # Real computation: accumulate magnitude by octave band
        octave_band = int(math.log2(base_freq / 32))
        magnitude_profile[octave_band] += raw_magnitude
        
        # Real phase contribution based on harmonic alignment
        if base_freq % 120 == 0:
            phase_angle = math.sin(math.radians(base_freq))
            phase_contributions.append(phase_angle * raw_magnitude)

        # Irrelevant computations (distractors)
        dummy_correction = raw_magnitude ** 0.1
        spectral_skew = (base_freq * noise_floor) ** 0.5
        if spectral_skew > 1:
            magnitude_profile['skew'] += spectral_skew  # dead code path

    total_power = sum(magnitude_profile[k] for k in magnitude_profile if isinstance(k, int))
    return phase_contributions, total_power


def calculate_interference_phase(shift_registry):
    total_shift = 0.0
    history_log = []  # unused tracking
    compensation_factor = 1.0

    for mode, shifts in shift_registry.items():
        mode_sum = 0
        weight = 1
        
        if mode == 'A':
            weight = 1.5
        elif mode == 'B':
            weight = 0.8
        else:
            weight = 1.1

        for idx, val in enumerate(shifts):
            # Core logic: XOR-based weighting modulation
            modulated = val ^ (idx + 1)
            mode_sum += modulated * weight

            # Distractor: irrelevant transformation chain
            temp_buffer = (val + idx) ** 0.25
            history_log.append(temp_buffer * 0.97)

        # Real impact: accumulate weighted sum
        total_shift += mode_sum

        # Distractor: unused conditional branch
        if mode_sum > 100:
            compensation_factor *= 0.95

    # Final adjustment using bitwise and arithmetic mix
    flag_mask = 0b1101
    adjustment = (flag_mask & int(abs(total_shift)))
    total_shift -= adjustment * 0.5

    return total_shift

# Main execution
freq_data = {
    'band_1': {'frequency': 64, 'amplitude': 12},
    'band_2': {'frequency': 120, 'amplitude': 18},
    'band_3': {'frequency': 240, 'amplitude': 22},
    'band_4': {'frequency': 480, 'amplitude': 30}
}

shift_registry = {
    'A': [5, 12, 9],
    'B': [7, 3],
    'C': [11, 6, 14, 8]
}

# Execute analysis (has side computations but only one return matters)
analyzed_phases, power_metric = analyze_frequency_response(freq_data)

# Critical statement
net_phase_shift = calculate_interference_phase(shift_registry)

# Print result
print(f"Result: {net_phase_shift}")