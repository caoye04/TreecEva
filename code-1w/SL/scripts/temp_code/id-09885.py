import itertools

# Simulated sensor data preprocessing with interference
raw_readings = [127, 63, 191, 31, 223, 15, 255, 0]
offset_correction = 1.05
amplification_factor = 2.1
noise_floor = 42

def apply_window(signal, win_type='hann'):
    # Real processing: applies Hann window for spectral analysis
    n = len(signal)
    if win_type == 'hann':
        return [signal[i] * (0.5 * (1 - __import__('math').cos(2 * __import__('math').pi * i / (n - 1)))) for i in range(n)]
    return signal

def extract_peaks(samples):
    # Extracts indices where sample exceeds dynamic threshold
    threshold = sum(samples) / len(samples) + 10
    peak_indices = []
    for i in range(1, len(samples)-1):
        if samples[i] > samples[i-1] and samples[i] > samples[i+1] and samples[i] > threshold:
            peak_indices.append(i)
    return peak_indices

def shift_register(data, shift):
    # Bit manipulation red herring: circular bit shifting
    result = []
    for x in data:
        shifted = ((x << shift) | (x >> (8 - shift))) & 255
        result.append(shifted)
    return result

def frequency_estimator(signal):
    # Misleading frequency estimator (unused path)
    period_guess = 0
    for i in range(1, len(signal)):
        if abs(signal[i] - signal[0]) < 5:
            period_guess = i

    if period_guess > 0:
        return round(1000 / period_guess, 3)
    return 0.0

def envelope_detector(samples):
    # Irrelevant envelope detection
    env = [samples[0]]
    attack = 0.2
    release = 0.1
    for s in samples[1:]:
        if s > env[-1]:
            env.append(env[-1] + attack * (s - env[-1]))
        else:
            env.append(env[-1] - release * (env[-1] - s))
    return env

def signal_processor(clean_signal):
    # Core logic disguised among distractions
    filtered = [x for x in clean_signal if x % 2 == 1]  # Keep only odd values
    paired = list(zip(filtered[:-1], filtered[1:]))
    diffs = [abs(a - b) for a, b in paired]
    total = 0
    for i, val in enumerate(diffs):
        if i % 2 == 0:
            total += val * 3
        else:
            total -= val
    return total

# --- MAIN EXECUTION WITH DISTRACTORS ---

# Distractor 1: Unused noise generation
synthetic_noise = [noise_floor ^ i for i in range(8)]

# Distractor 2: Fake calibration chain
calibration_map = {i: (i * offset_correction) for i in range(256)}
calibrated = [int(calibration_map[x]) for x in raw_readings]

# Distractor 3: Dead function call
_ = frequency_estimator(calibrated)

# Distractor 4: Unused signal transformation
windowed = apply_window(raw_readings)
envelope = envelope_detector(windowed)

# Distractor 5: Bit manipulation decoy
shifted_data = shift_register(raw_readings, 3)
scrambled_pairs = list(itertools.combinations(shifted_data, 2))
hash_candidate = sum(a ^ b for a, b in scrambled_pairs[:5]) % 1000

# Distractor 6: Unused peak detection
peaks = extract_peaks(calibrated)
peak_product = 1
for idx in peaks:
    peak_product *= calibrated[idx]

# REAL SIGNAL PATH (obscured)
base_signal = [x for x in raw_readings if x > 50]  # Filter high-amplitude readings
processed_samples = [x for x in base_signal if x & 1]  # Only odd values

# Key statement
phase_output = signal_processor(processed_samples)

print(f"Result: {phase_output}")