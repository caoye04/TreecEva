import itertools

def generate_frequency_harmonics(base_freq, harmonics_count):
    """Generate harmonic frequencies (unused distractor function)"""
    return [base_freq * (i + 1) for i in range(harmonics_count)]

def calculate_interference_phase(signal_combinations):
    total_phase = 0
    phase_map = {}
    
    # Real computation: iterate over signal combinations
    for sig_a, sig_b in signal_combinations:
        product = sig_a * sig_b
        if product % 2 == 0:
            shift = len(str(product)) * 1.5
        else:
            shift = -len(str(product)) * 0.75
        
        # Track phase per combination (some used later)
        key = f'{min(sig_a,sig_b)}-{max(sig_a,sig_b)}'
        phase_map[key] = shift
        
        # Accumulate only specific cases
        if sig_a + sig_b > 10:
            total_phase += shift

    # Distractor: unused intermediate calculation
    average_length = sum(len(str(k)) for k in phase_map.keys()) / len(phase_map) if phase_map else 0
    temp_correction = round(average_length * 0.1, 2)
    
    # Another distractor: simulate filter that isn't applied
    filtered_phases = [p for p in phase_map.values() if p > 0]
    dummy_normalization = sum(filtered_phases) / len(filtered_phases) if filtered_phases else 0.0
    
    # Final adjustment based on count of significant shifts
    significant_shifts = sum(1 for p in phase_map.values() if abs(p) >= 1.5)
    total_phase *= (1 + significant_shifts * 0.05)

    return round(total_phase, 4)

# Main execution block
if __name__ == '__main__':
    # Generate base signals (real input)
    primary_signals = [2, 3, 5, 7]
    secondary_signals = [4, 6]

    # Create Cartesian product of signals (key data structure)
    combinations = list(itertools.product(primary_signals, secondary_signals))

    # Unused distractor variables
    noise_floor = 0.023
    calibration_matrix = [[i*j for j in range(3)] for i in range(3)]
    baseline_offset = sum(calibration_matrix[i][i] for i in range(3))

    # Signal power simulation (dead code path - not used)
    def compute_signal_power(sigs):
        return [s**2 * 0.5 for s in sigs]
    
    power_levels = compute_signal_power(primary_signals + secondary_signals)

    # Real critical computation
    net_phase_shift = calculate_interference_phase(combinations)

    # Print final result as required
    print(f'Result: {net_phase_shift}')