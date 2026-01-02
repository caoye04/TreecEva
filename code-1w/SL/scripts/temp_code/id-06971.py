import math

# Simulated sensor data processing with noise filtering and pattern analysis
def collect_samples(base_signal, noise_level=0.3):
    samples = []
    for i in range(15):
        noise = (i % 3 - 1) * noise_level
        sampled = base_signal[i % len(base_signal)] + noise
        samples.append(round(sampled, 2))
    return samples

# Irrelevant helper: string-based status formatting (distractor)
def format_status(code, detail=""):
    prefix = "ERR" if code > 50 else "OK"
    label = str(code).zfill(3)
    return f"[{prefix}-{label}] {detail}".strip()

# Unused transformation path (dead code path)
def legacy_transform(seq):
    shifted = [x * 1.5 for x in seq if x > 0]
    return [int(math.floor(y)) for y in shifted]

# Signal normalization (used but not directly part of answer)
def normalize(signal):
    mean_val = sum(signal) / len(signal)
    normalized = [round(x - mean_val, 3) for x in signal]
    return normalized

# Frequency domain approximation via simple phase shift (core relevant function)
def apply_frequency_shift(data, shift_factor):
    transformed = []
    for i, val in enumerate(data):
        angle = (i * shift_factor) % (2 * math.pi)
        shifted_val = val * math.cos(angle) + (val * 0.5) * math.sin(angle)
        transformed.append(round(shifted_val, 4))
    return transformed

# Pattern matching using set operations on discretized levels (key logic)
def detect_pattern_levels(signal):
    high_set = {i for i, x in enumerate(signal) if x >= 1.0}
    mid_set = {i for i, x in enumerate(signal) if 0.2 <= x < 1.0}
    low_set = {i for i, x in enumerate(signal) if x < 0.2}
    suppressed = {i for i in high_set if (i+1) % 4 == 0}  # suppression rule
    active_peaks = high_set - suppressed
    return active_peaks, mid_set, low_set

# Main analysis combining multiple concepts (called at end)
def analyze_signal(buffer, shift):
    # Step 1: Apply frequency correction
    corrected = apply_frequency_shift(buffer, shift)
    
    # Step 2: Normalize amplitude
    processed = normalize(corrected)
    
    # Step 3: Discretize into levels and detect patterns
    peaks, mids, lows = detect_pattern_levels(processed)
    
    # Step 4: Compute diagnostic metric
    peak_score = sum(p * 2 for p in peaks)
    mid_score = sum(m for m in mids)
    position_penalty = 0
    sorted_peaks = sorted(peaks)
    for i in range(1, len(sorted_peaks)):
        if sorted_peaks[i] - sorted_peaks[i-1] == 2:
            position_penalty += 3
    
    # Step 5: Apply combinatorial adjustment based on symmetry
    mirrored = {abs(p - 7) for p in peaks if abs(p - 7) != p}
    symmetry_bonus = len(peaks & mirrored) * 5
    
    # Final diagnostic calculation
    final_diagnostic = peak_score - mid_score + symmetry_bonus - position_penalty
    
    # Irrelevant output formatting (distractor)
    status_msg = format_status(23, "Signal lock acquired")
    debug_trace = [format_status(i, str(v)) for i, v in enumerate(processed[:3])]
    
    return int(round(final_diagnostic))

# Initialization data
base_waveform = [1.0, 0.8, 1.2, 0.4, 1.6, 0.7, 0.9, 1.3]
noise_level_config = 0.25
frequency_shift = 0.785  # approx π/4

# Data collection
raw_signal = collect_samples(base_waveform, noise_level_config)

# Normalization stage
normalized_signal = normalize(raw_signal)

# Buffer used in main analysis
pattern_buffer = [round(x * 1.1, 3) for x in normalized_signal]  # minor gain adjustment

# Dead code invocation (unused)
_ = legacy_transform([1, -2, 3, -4])

# String manipulation distractor: log generation
log_prefix = "DIAG"
current_mode = "SCAN"
timestamp_str = f"{log_prefix}_{current_mode.lower()}_t128"
words = timestamp_str.split('_')
sanitized = ''.join(word.capitalize() for word in words)
hash_value = sum(ord(c) for c in sanitized) % 1000

# Set operation red herring
unique_chars = set(sanitized)
control_set = {chr(65 + i) for i in range(10)}
disruptive_interference = unique_chars ^ control_set  # irrelevant XOR

# Critical execution point
final_diagnostic = analyze_signal(pattern_buffer, frequency_shift)

# Output result
print(f"Result: {final_diagnostic}")