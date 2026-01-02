def generate_harmonics(base_freq, count):
    return [base_freq * (i + 1) for i in range(count)]


def filter_resonant(peaks):
    return [p for p in peaks if p % 2 == 1]


def compute_inertia(mode_list):
    moment = 0
    for i, val in enumerate(mode_list):
        moment += (val ** 2) * (i + 1)
    scaling_factor = 0.95
    adjusted_moment = moment * scaling_factor
    return adjusted_moment


def analyze_sequence(modes):
    if len(modes) == 0:
        return 0
    elif len(modes) == 1:
        return modes[0] * 2
    else:
        mid = len(modes) // 2
        left = analyze_sequence(modes[:mid])
        right = analyze_sequence(modes[mid:])
        return left + right * 1.5

# Irrelevant helper (distractor)
def calculate_impedance(frequency, resistance=100):
    reactance = 2 * 3.14159 * frequency * 0.01
    return (resistance**2 + reactance**2) ** 0.5

# Irrelevant data (red herring)
baseline_signals = [12, 45, 67, 89, 23, 56, 78, 91, 14, 37]
signal_power = sum([s**2 for s in baseline_signals]) / len(baseline_signals)

# Main computation chain
fundamental = 13
harmonics_list = generate_harmonics(fundamental, 8)
filtered_peaks = filter_resonant(harmonics_list)
effective_modes = filtered_peaks[::2]  # Take every second resonant harmonic

# Dead code path (misleading)
if len(effective_modes) > 10:
    effective_modes.append(999)
elif len(effective_modes) == 5:
    effective_modes = [x * 1.1 for x in effective_modes]
else:
    pass  # No action (distractor)

# Key assignment with slicing and recursion
thermal_capacity = analyze_sequence(effective_modes[-1::-2])

# Decoy variable with plausible but irrelevant computation
entropy_score = compute_inertia(effective_modes)
impedance_profile = [calculate_impedance(f) for f in harmonics_list[:3]]

# Output the target result
print(f"Result: {thermal_capacity}")