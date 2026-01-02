import math

# Simulated sensor data with noise and irrelevant metrics
data_stream = [
    (1.2, 0.8, 3.1, 1024), (2.5, 1.1, 2.9, 2048), (3.8, 1.5, 3.2, 512),
    (4.1, 0.9, 2.8, 4096), (5.6, 1.3, 3.0, 8192), (6.3, 1.0, 3.3, 16384),
    (7.7, 1.6, 2.7, 32768), (8.0, 0.7, 3.1, 65536)
]

# Irrelevant calibration constants (distractors)
CALIBRATION_FACTOR_A = 0.987
CALIBRATION_FACTOR_B = 1.013
NOISE_FLOOR = 0.05
OFFSET_CORRECTION = -0.02
SCALE_MATRIX = [[1.1, 0.9], [0.95, 1.05]]
TEMPORAL_DAMPING = 0.003

# Predefined thresholds (some are decoys)
THRESHOLD_ALPHA = 2.5
THRESHOLD_OMEGA = 7.5  # unused red herring
CRITICAL_PHASE_SHIFT = 1.414
MIN_AMPLITUDE = 0.8
MAX_FREQUENCY_DRIFT = 0.3

# Auxiliary functions (some not used)
def calculate_entropy(values):
    return -sum(p * math.log2(p) for p in values if p > 0)

def apply_window(signal, window_type='hann'):
    n = len(signal)
    if window_type == 'hann':
        return [signal[i] * (0.5 * (1 - math.cos(2 * math.pi * i / (n-1)))) for i in range(n)]
    return signal

def detect_spike(amplitude, baseline=1.0):
    return amplitude > 2.5 * baseline  # dead function, never called

def phase_align(samples, shift=CRITICAL_PHASE_SHIFT):
    return [s * shift for s in samples]  # unused

# Signal preprocessing pipeline
def filter_noise(raw_seq, threshold=THRESHOLD_ALPHA):
    cleaned = []
    amplitudes = []
    for idx, entry in enumerate(raw_seq):
        # Extract relevant signal component (third element)
        raw_value = entry[2]
        timestamp = entry[0]  # distractor
        aux_signal = entry[1]  # irrelevant
        system_flag = entry[3]  # bit-flag distractor

        # Real processing step: filter by amplitude threshold
        if raw_value >= MIN_AMPLITUDE and raw_value <= 3.3:
            cleaned.append((timestamp, raw_value))
            amplitudes.append(raw_value)

        # Fake processing branch (dead code path)
        if idx > 100:  # unreachable condition
            backup = [x[2] for x in raw_seq]
            normalized = [b / max(backup) for b in backup]
            return normalized

    return cleaned

# Core transformation logic
def extract_features(records):
    features = []
    total_power = 0.0
    moment_sequence = []

    for t, val in records:
        # Compute multiple derived values (only one matters)
        squared = val ** 2
        cubed = val ** 3  # distraction
        log_val = math.log(val) if val > 0 else 0  # unused
        sin_phase = math.sin(t * 0.1)  # red herring

        power = squared * 1.5  # actual contributor
        total_power += power

        # Accumulate moments (only last one used later)
        moment = squared + power - t * 0.01
        moment_sequence.append(moment)

        # Bit manipulation decoy
        flag_hash = int(t) ^ 255 & 0xFF
        if flag_hash % 7 == 0:
            continue  # meaningless skip

    avg_moment = sum(moment_sequence[-3:]) / 3 if len(moment_sequence) >= 3 else 0
    return total_power, avg_moment

# Final processing with tuple unpacking and zip usage
def process_signals(input_list):
    indices = list(range(len(input_list)))
    time_vals, signal_vals = zip(*input_list)  # using zip

    # Use enumerate to find peaks above threshold
    peak_positions = []
    for i, s in enumerate(signal_vals):
        if s > THRESHOLD_ALPHA and i % 2 == 0:
            peak_positions.append(i)

    # Dummy transformation chain
    transformed = []
    for j, sig in enumerate(signal_vals):
        temp = sig
        temp *= 1.05
        temp += OFFSET_CORRECTION
        if j in peak_positions:
            temp *= 1.1
        transformed.append(temp)

    # Key computation: weighted sum based on position parity
    weighted_sum = 0.0
    for pos, value in enumerate(transformed):
        weight = 1.2 if pos % 2 == 0 else 0.8
        weighted_sum += value * weight

    # Retrieve auxiliary results (one is critical)
    total_energy, representative_moment = extract_features(input_list)

    # Final formula combines multiple elements, but only one path is active
    if len(peak_positions) > 2:
        base = weighted_sum
    else:
        base = total_energy  # this will be taken

    # Apply final non-linear correction
    correction_factor = math.sqrt(representative_moment)
    intermediate = base * correction_factor

    # Decoy branching logic
    if intermediate < 0:
        result = -intermediate * CALIBRATION_FACTOR_A
    elif intermediate > 1000:
        alt_path = [math.exp(-x) for x in transformed]  # dead code
        result = sum(alt_path)
    else:
        result = intermediate + 5.5  # actual execution path

    # Final adjustment using bitwise (distraction)
    int_part = int(result)
    flagged = int_part ^ 15 | 256  # no effect
    final_result = result  # identity assignment

    return final_result

# Execution flow
filtered_data = filter_noise(data_stream)
energy_diagnostic, moment_diagnostic = extract_features(filtered_data)
diagnostic_report = {
    'entries': len(filtered_data),
    'avg_moment': moment_diagnostic,
    'total_energy': energy_diagnostic,
    'calibration_status': 'nominal',
    'system_flag_checksum': sum([x[3] for x in data_stream]) % 256
}

# Critical statement
final_output = process_signals(filtered_data)
print(f"Result: {final_output}")