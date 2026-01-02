import itertools
from collections import defaultdict, Counter

# Simulate quantum signal processing with interference patterns
def generate_harmonic_sequence(base_freq, harmonics):
    return [base_freq * (i + 1) for i in range(harmonics)]

def apply_doppler_shift(frequencies, velocity):
    shifted = []
    for f in frequencies:
        shifted.append(f * (1 + velocity / 299792458))  # Simplified relativistic doppler
    return shifted

def compute_interference_pattern(freqs_a, freqs_b):
    pattern = []
    for a, b in itertools.zip_longest(freqs_a, freqs_b, fillvalue=0):
        pattern.append(abs(a - b) ** 2)
    return pattern

def modulate_with_carrier(signal, carrier_freq):
    modulated = []
    for i, s in enumerate(signal):
        modulated.append(s * (1 + (carrier_freq % 10) * 0.1) if i % 2 == 0 else s)
    return modulated

def calculate_entropy(arr):
    # Irrelevant entropy calculation - red herring
    counts = Counter(arr)
    total = len(arr)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Not real entropy, but looks plausible
    return round(entropy, 6)

def phase_lock_loop(signal, reference):
    # Complex but ultimately unused function (dead code path)
    locked = []
    for s, r in zip(signal, reference):
        error = abs((s % 100) - (r % 100))
        correction = 1 - (error / 100)
        locked.append(s * correction)
    return locked

def extract_resonant_peaks(data, threshold_multiplier=1.5):
    avg = sum(data) / len(data)
    peaks = [x for x in data if x > threshold_multiplier * avg]
    return peaks if len(peaks) > 0 else [avg]

def compute_fourier_moment(series, order=2):
    # Another distractor function that isn't used in final computation
    moment = 0
    center = sum(series) / len(series)
    for val in series:
        moment += (val - center) ** order
    return moment ** (1/order) if moment > 0 else 0

def aggregate_phase_shift(waveform, frequency):
    # Core relevant logic
    scaled = [w * frequency * 0.01 for w in waveform]
    filtered = [s for s in scaled if s > 0.5]
    shift_accumulator = 0
    for idx, val in enumerate(filtered):
        if idx % 3 == 0:
            shift_accumulator += val * 0.7
        elif idx % 3 == 1:
            shift_accumulator -= val * 0.3
        else:
            shift_accumulator += val * 0.1
    return int(shift_accumulator)  # Final deterministic answer

# Begin simulation setup
base_frequency = 427
harmonic_count = 7
velocity_factor = 12750

# Generate primary and secondary harmonic sequences
primary_bank = generate_harmonic_sequence(base_frequency, harmonic_count)
secondary_bank = generate_harmonic_sequence(base_frequency + 13, harmonic_count - 1)

# Apply doppler effect to both (only one is actually used later)
doppler_primary = apply_doppler_shift(primary_bank, velocity_factor)
doppler_secondary = apply_doppler_shift(secondary_bank, velocity_factor * -1)

# Compute interference - this result is critical
interference_grid = compute_interference_pattern(doppler_primary, doppler_secondary)

# Modulate with carrier wave - only this matters for final result
modulated_wave = modulate_with_carrier(interference_grid, base_frequency)

# === Distractor Variables and Dead Computations ===

# Unused data structures with complex initialization
diagnostic_log = defaultdict(list)
diagnostic_log['entropy_trace'].append(calculate_entropy(interference_grid))
diagnostic_log['entropy_trace'].append(calculate_entropy(modulated_wave))

data_cube = []
for i in range(3):
    layer = []
    for j in range(3):
        row = [i * j * k for k in range(3)]
        layer.append(row)
    data_cube.append(layer)

# Multiple irrelevant transformations
moment_2 = compute_fourier_moment(modulated_wave, 2)
moment_4 = compute_fourier_moment(modulated_wave, 4)

peak_candidates = extract_resonant_peaks(modulated_wave, 1.8)
adjusted_peaks = [p * 0.92 for p in peak_candidates if p > 100]

# Unused phase lock operation (misleading function call)
if len(adjusted_peaks) > 1:
    locked_phases = phase_lock_loop(adjusted_peaks, primary_bank)
    diagnostic_log['phase_metrics'].extend(locked_phases)

# Nested conditional with decoy logic
status_flags = [True, False, True]
if status_flags[0] and not status_flags[1]:
    temp_buffer = []
    for x in modulated_wave[:10]:
        if x > 50:
            temp_buffer.append(x * 0.1)  # Never used

# Critical execution point
final_flux = aggregate_phase_shift(modulated_wave, base_frequency)

# Print final result as required
print(f"Result: {final_flux}")