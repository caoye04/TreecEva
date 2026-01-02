import itertools

# Simulate agricultural yield prediction with environmental noise filtering

def analyze_microclimates(temps, rainfall):
    # Irrelevant analysis of microclimate zones (dead-end function)
    zones = []
    for t in temps:
        for r in rainfall:
            if t > 25 and r < 100:
                zones.append((t, r, 'Arid'))
            elif t < 15:
                zones.append((t, r, 'Cold'))
    return zones  # Unused return


def filter_noise(data_stream):
    # Apply moving average to remove signal noise (distractor logic)
    smoothed = []
    window = 3
    for i in range(len(data_stream) - window + 1):
        avg = sum(data_stream[i:i+window]) / window
        smoothed.append(round(avg, 2))
    return smoothed  # Result partially used but manipulated further in irrelevant ways


def generate_phase_shift(pattern):
    # Bit manipulation red herring: cyclic phase shifting via XOR rotation
    shifted = []
    for val in pattern:
        rotated = ((val << 1) & 0b11111) | ((val >> 4) & 0b11111)  # 5-bit rotate
        masked = rotated ^ 0b10101
        shifted.append(masked % 10)  # Distortion
    return shifted


def evaluate_stress_factors(ph_levels, conductivity):
    # Environmental stress index - completely unused
    stress_index = 0
    for p, c in zip(ph_levels, conductivity):
        if p < 6.0 or p > 7.5:
            stress_index += 1
        if c > 1.5:
            stress_index += 0.5
    return stress_index


def calculate_harvest(fluctuations, thresholds):
    # Core logic hidden among distractions
    trend_data = fluctuations[::2]  # Slicing: take every second element
    adjusted = [x + 1 for x in trend_data]

    # Real computation begins here
    cumulative = 0
    peak_count = 0
    for i, val in enumerate(adjusted):
        key_threshold = thresholds.get(i % 4, 0)
        
        # Conditional branching with early skip
        if val < key_threshold:
            continue
            
        # Actual contribution to result
        if i % 2 == 0:
            cumulative += val * 2
        else:
            cumulative += val

        # Bitwise interference: toggle on odd indices using XOR
        if i % 3 == 0:
            cumulative = cumulative ^ (i // 3)  # Minor bit flip adjustment

        # Count peaks above dynamic threshold
        if val > 8:
            peak_count += 1

    # Final transformation using itertools.chain to flatten artificial segments
    segments = [range(cumulative, cumulative + peak_count), [peak_count]]
    flat = list(itertools.chain.from_iterable(segments))
    final_score = sum(flat) // (peak_count + 1) if peak_count else 0

    return final_score

# Main execution block
if __name__ == '__main__':
    # Input data
    fluctuations = [3, 9, 5, 12, 7, 4, 11, 6, 8, 10]
    ph_levels = [5.8, 6.3, 7.1, 6.9, 7.6]
    conductivity = [1.2, 1.8, 1.0, 2.1, 1.4]
    temperature_log = [22, 26, 24, 28, 20]
    rainfall_data = [88, 105, 95, 130, 70]

    # Distractor: unused complex structure
    threshold_map = {0: 4, 1: 6, 2: 5, 3: 7, 4: 4}
    del threshold_map[4]  # Mutation with no impact

    # Noise filtering on irrelevant stream
    noisy_signal = [15, 17, 16, 20, 18, 25, 22]
    cleaned = filter_noise(noisy_signal)

    # Phase shift manipulation on decoy pattern
    base_pattern = [1, 0, 1, 1, 0]
    modulated = generate_phase_shift(base_pattern)

    # Microclimate analysis - never used
    microzones = analyze_microclimates(temperature_log, rainfall_data)

    # Real call that produces answer
    final_yield = calculate_harvest(fluctuations, threshold_map)

    # Print result as required
    print(f"Target result: {final_yield}")