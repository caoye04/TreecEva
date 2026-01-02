import itertools

def generate_phase_shift(n):
    return [(i ** 2 + 3 * i + 7) % 100 for i in range(n)]

def evaluate_coherence(sequence):
    total = 0
    for i in range(len(sequence)):
        if sequence[i] > 50:
            total += 1
    return total > 3

def filter_resonant_peaks(data):
    peaks = []
    for i in range(1, len(data) - 1):
        if data[i] > data[i - 1] and data[i] > data[i + 1]:
            peaks.append(data[i])
    return [p for p in peaks if p % 2 == 0]

def accumulate_magnetic_moment(values):
    moment = 0
    sign = 1
    for v in values:
        moment += sign * v
        sign *= -1
    return moment

def compute_entropy_signature(arr):
    # Irrelevant entropy-like calculation (dead end)
    from math import log2
    freq = {}
    for a in arr:
        freq[a] = freq.get(a, 0) + 1
    entropy = sum(-f / len(arr) * log2(f / len(arr)) for f in freq.values())
    return round(entropy, 4)

def derive_calibration_offset(seq):
    offset = 0
    for i, s in enumerate(seq):
        if i % 3 == 0:
            offset += s * 2
        elif i % 3 == 1:
            offset -= s // 3
        else:
            offset += s % 7
    return offset

def validate_harmonic_stability(peaks):
    if len(peaks) < 2:
        return False
    diffs = [peaks[i+1] - peaks[i] for i in range(len(peaks)-1)]
    return all(d % 4 == 0 for d in diffs)

def calculate_thermal_integral(sequence):
    integral = 0
    multiplier = 1
    for idx, val in enumerate(sequence):
        if idx % 2 == 0:
            integral += val ** 2
        else:
            integral -= val
        if val > 40:
            multiplier *= 2
    return integral * multiplier

# Main execution with heavy distractions
base_phases = generate_phase_shift(12)
coherence_flag = evaluate_coherence(base_phases)
resonant_peaks = filter_resonant_peaks(base_phases)
stability_test = validate_harmonic_stability(resonant_peaks)

# Decoy computation chain 1: Magnetic analysis
magnetic_data = [x * 3 + 10 for x in base_phases]
magnetic_moment = accumulate_magnetic_moment(magnetic_data)

# Decoy computation chain 2: Entropy analysis
entropy_profile = compute_entropy_signature(base_phases)

calibration_offset = derive_calibration_offset(base_phases)

# Critical data transformation
transformed_signal = [abs(x - 25) for x in base_phases]
smoothed_signal = [sum(transformed_signal[i:i+3]) // 3 for i in range(len(transformed_signal) - 2)]

# Key distraction: unused complex structure
combinations = list(itertools.combinations(smoothed_signal, 3))
triplet_sums = [sum(combo) for combo in combinations if sum(combo) > 50]

# Another red herring: harmonic pairing
paired_harmonics = []
for a, b in itertools.combinations_with_replacement(resonant_peaks, 2):
    if (a + b) % 5 == 0:
        paired_harmonics.append(a * b)

# Real signal processing path
process_sequence = []
for s in smoothed_signal:
    if s % 2 == 0:
        process_sequence.append(s + calibration_offset)
    else:
        process_sequence.append(s - 1)

# Core answer computation — depends on multiple prior steps
thermal_capacity = calculate_thermal_integral(process_sequence)

# Print final result as required
print(f"Result: {thermal_capacity}")