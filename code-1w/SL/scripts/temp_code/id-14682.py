from collections import defaultdict
import math

# Simulate quantum-inspired phase register system with interference patterns
def main():
    # Core state variables
    base_frequencies = [3, 5, 7, 11, 13]
    phase_states = [True, False, True, True, False, True, False]
    activation_threshold = 0.68

    # Irrelevant amplitude tracking (distractor)
    amplitudes = defaultdict(float)
    for i in range(len(base_frequencies)):
        amplitudes[f'freq_{i}'] = round(math.sin(i * 0.7) ** 2, 4)

    # Frequency mapping with harmonic multipliers (partially relevant)
    frequency_map = {}
    for idx, freq in enumerate(base_frequencies):
        harmonic_set = []
        for h in range(1, 5):
            if (freq * h) % 4 == idx % 4:  # red herring condition
                harmonic_set.append(freq * h * 1.5)
        frequency_map[f'band_{idx}'] = sorted(harmonic_set, reverse=True)

    # Decoy function that's never called (dead code path)
    def analyze_coherence(states):
        coherence_score = 0
        for i in range(len(states) - 1):
            if states[i] == states[i + 1]:
                coherence_score += 1
        return coherence_score / len(states)

    # Auxiliary transformation (misleading intermediate result)
    temp_transform = []
    for i, p in enumerate(phase_states):
        if p:
            temp_transform.append((i * 2 + 1) ** 0.5)
        else:
            temp_transform.append(-i / 4.0)

    # Normalization chain (distractor)
    normalized_vals = [abs(x) / sum(abs(v) for v in temp_transform) for x in temp_transform]
    entropy_proxy = -sum(p * math.log(p + 1e-9) for p in normalized_vals)

    # Real computation begins here — actual logic for phase shift
    def calculate_interference(phases, freqs):
        shift_accumulator = 0
        phase_cycle = []

        # Build effective cycle from boolean phases
        for i, active in enumerate(phases):
            if active:
                cycle_value = (i + 1) * 360 // (len(phases) + 1)
                phase_cycle.append(cycle_value)

        # Apply frequency-weighted modulation (only first three bands used)
        modulation_factors = []
        for band_key in [f'band_{j}' for j in range(3)]:
            raw_values = freqs[band_key]
            if raw_values:
                mid_idx = len(raw_values) // 2
                selected = raw_values[mid_idx]
                # Map to angular contribution via integer division and rounding
                angle_contrib = round(selected / 17.0) * 15
                modulation_factors.append(angle_contrib % 360)
            else:
                modulation_factors.append(0)

        # Cross-modulate phase cycle with modulation factors using modular arithmetic
        for step in phase_cycle:
            temp_step = step
            for mf in modulation_factors:
                if mf > 100:  # misleading filter (never true)
                    temp_step = (temp_step + mf) % 360
            # Actual update uses fixed offset based on list comprehension filtering
            valid_mods = [m for m in modulation_factors if m < 100]
            adjustment = sum(valid_mods) // len(valid_mods) if valid_mods else 0
            temp_step = (temp_step + adjustment) % 360
            shift_accumulator += temp_step

        # Final reduction using bitwise blending (relevant)
        final_shift = shift_accumulator
        flag_mask = 0b1101
        if len(modulation_factors) & flag_mask:
            final_shift ^= (len(phase_cycle) << 2)
        final_shift += (final_shift >> 3) & 0b111

        return int(final_shift)

    # Execution point of interest
    net_phase_shift = calculate_interference(phase_states, frequency_map)

    # Post-calculation obfuscation (irrelevant)
    diagnostic_log = []
    for k, v in frequency_map.items():
        nonzero_count = sum(1 for x in v if x > 10)
        diagnostic_log.append(f'{k}: {nonzero_count} high components')

    # Output must be printed exactly like this
    print(f"Result: {net_phase_shift}")

if __name__ == '__main__':
    main()