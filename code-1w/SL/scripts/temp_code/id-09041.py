import math

# Simulated sensor array diagnostics with noise filtering and pattern analysis
def collect_signals(base_freq, duration, noise_level=0.7):
    raw_samples = []
    for t in range(1, duration + 1):
        signal = math.sin(base_freq * t) + (noise_level * math.cos(3 * t))
        raw_samples.append(round(signal, 4))
    return raw_samples


def apply_windowing(data, window_type='hann'):
    N = len(data)
    windowed = []
    for i in range(N):
        if window_type == 'hann':
            window = 0.5 * (1 - math.cos(2 * math.pi * i / (N - 1) if N > 1 else 1))
        else:
            window = 1.0
        windowed.append(data[i] * window)
    return windowed


def compute_magnitude_spectrum(windowed_signal):
    # Real FFT simulation for magnitude only
    spectrum = []
    N = len(windowed_signal)
    for k in range(N // 2 + 1):
        re = im = 0
        for n in range(N):
            angle = 2 * math.pi * k * n / N
            re += windowed_signal[n] * math.cos(angle)
            im -= windowed_signal[n] * math.sin(angle)
        magnitude = math.sqrt(re**2 + im**2)
        spectrum.append(round(magnitude, 4))
    return spectrum


def filter_artifacts(spectrum, threshold=0.5):
    cleaned = [val if val > threshold else 0.0 for val in spectrum]
    while 0.0 in cleaned:
        cleaned.remove(0.0)
    return cleaned


def extract_peaks(magnitudes, min_gap=2):
    peaks = []
    L = len(magnitudes)
    for i in range(L):
        if (i == 0 or magnitudes[i] > magnitudes[i-1]) and (i == L-1 or magnitudes[i] >= magnitudes[i+1]):
            peaks.append(i)
    filtered_peaks = []
    for p in peaks:
        if not filtered_peaks or (p - filtered_peaks[-1]) >= min_gap:
            filtered_peaks.append(p)
    return filtered_peaks


def derive_phase_signature(peaks, length):
    signature = 0
    for idx in peaks:
        signature ^= int((idx * 100) % 7919)  # Prime modulus for dispersion
    return signature % 1000


def normalize_readings(data):
    if not data:
        return []
    mean_val = sum(data) / len(data)
    std_val = math.sqrt(sum((x - mean_val)**2 for x in data) / len(data))
    return [(x - mean_val) / (std_val + 1e-8) for x in data]


def aggregate_metrics(peaks, spectrum, phase_key):
    total_energy = sum(s**2 for s in spectrum)
    peak_count_score = len(peaks) * 100
    balance_metric = abs(len(spectrum) - 2 * len(peaks))
    return (total_energy * peak_count_score) / (balance_metric + 1) + phase_key

# Irrelevant helper: computes unused spectral centroid
def compute_centroid(spectrum):
    weighted_sum = sum(i * mag for i, mag in enumerate(spectrum))
    total_mag = sum(spectrum)
    return weighted_sum / total_mag if total_mag else 0

# Another red herring: transforms data in a way that's never used
def encrypt_sequence(seq, key=42):
    encrypted = []
    for val in seq:
        shifted = int((val * 1000) ^ key)
        encrypted.append((shifted * 7 + 3) % 97)
    return encrypted

def simulate_calibration_offsets(shape=(3, 3)):
    offsets = []
    for i in range(shape[0]):
        row = []
        for j in range(shape[1]):
            row.append(round(math.tan(i + j + 0.1), 4))
        offsets.append(row)
    return offsets  # Never used in main logic

# Distractor function: looks important but unused
def validate_coherence(data):
    if len(data) < 2:
        return True
    diffs = [abs(data[i] - data[i-1]) for i in range(1, len(data))]
    return all(d < 1.0 for d in diffs)

# Core transformation pipeline
def preprocess_chain(raw_signal):
    normalized = normalize_readings(raw_signal)
    windowed = apply_windowing(normalized, 'hann')
    spectrum = compute_magnitude_spectrum(windowed)
    cleaned_spectrum = filter_artifacts(spectrum, threshold=0.3)
    return cleaned_spectrum

# Secondary analysis path - partially dead code
unused_intermediate = set()
dummy_tracker = {}
for i in range(5):
    dummy_tracker[f'frame_{i}'] = {"seq": [j**2 + i for j in range(8)], "flag": False}
    unused_intermediate.add(sum(dummy_tracker[f'frame_{i}']["seq"]) % 100)

# Unused list transformation
shadow_buffer = [math.log(2 + x, 2) for x in range(15) if x % 3 != 0]
shadow_buffer = [x for x in shadow_buffer if x > 1.5]
shadow_buffer_sliced = shadow_buffer[::2]  # Distractor slice

# Actual relevant data flow begins here
raw_data = collect_signals(base_freq=0.8, duration=16, noise_level=0.6)
transformed_spectrum = preprocess_chain(raw_data)
peak_positions = extract_peaks(transformed_spectrum, min_gap=1)

# Decoy assignment - looks like calibration
baseline_shift = 0
for i in range(3):
    baseline_shift += math.floor((peak_positions[-1] if peak_positions else 1) / (i + 1))

# Phase signature based on peak indices
phase_code = derive_phase_signature(peak_positions, len(transformed_spectrum))

# Create thresholds set — actual control logic uses subset
all_thresholds = {0.5, 1.0, 1.5, 2.0, 2.5, phase_code / 500.0}
critical_thresholds = {t for t in all_thresholds if t > 0.8}  # Set operation: filtering
backup_caps = set(range(10))
active_caps = backup_caps.difference({0, 2, 4, 6, 8})  # More set distraction

# Main diagnostic logic
composite_score = aggregate_metrics(peak_positions, transformed_spectrum, phase_code)

# This function appears complex but only uses select inputs
def analyze_pattern(pattern_data, threshold_set):
    # Slicing: use only central portion of data
    mid_index = len(pattern_data) // 2
    focus_slice = pattern_data[max(0, mid_index - 3):mid_index + 4]  # Slice of interest
    
    # Irrelevant slicing ahead
    left_wing = pattern_data[:mid_index]
    right_wing = pattern_data[mid_index:]
    if len(left_wing) > len(right_wing):
        left_trimmed = left_wing[1::2]
        right_trimmed = right_wing[::2]
    else:
        left_trimmed = left_wing[::-1]
        right_trimmed = right_wing[:]  # Redundant copy
    
    # Actual computation
    avg_focus = sum(focus_slice) / len(focus_slice) if focus_slice else 0
    spike_count = sum(1 for x in focus_slice if x > avg_focus * 1.3)
    
    # Use phase-derived code from earlier
    global phase_code
    adjustment_factor = (phase_code % 11) / 10.0
    
    # Final diagnostic calculation
    base_diagnostic = (avg_focus * 1000) + (spike_count * 50) + (phase_code * 2)
    refined_diagnostic = base_diagnostic * (1 + adjustment_factor)
    
    # Dead logic branch — never executed due to phase_code constraints
    if phase_code < 0:
        fallback = 0
        for x in left_trimmed:
            fallback ^= int(x * 100)
        return fallback % 10000
    
    # Primary return path
    return int(refined_diagnostic)

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data=transformed_spectrum, thresholds=critical_thresholds)

# Print result as required
print(f"Result: {final_diagnostic}")