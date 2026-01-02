from itertools import cycle, islice
import math

# Simulate sensor data preprocessing with noise filtering and feature extraction
def generate_sensor_pulse(length, noise_factor=0.1):
    base = [math.sin(i * 0.5) for i in range(length)]
    noise = [noise_factor * (i % 7) for i in range(length)]
    return [b + n for b, n in zip(base, noise)]

# Irrelevant helper: computes statistical dispersion (not used in final result)
def compute_kurtosis(data):
    n = len(data)
    if n == 0:
        return 0.0
    mean_val = sum(data) / n
    variance = sum((x - mean_val) ** 2 for x in data) / n
    if variance == 0:
        return 0.0
    kurtosis = sum((x - mean_val) ** 4 for x in data) / (n * variance ** 2)
    return kurtosis - 3

# Misleading transformation chain: creates decoy features
def apply_envelope(signal):
    envelope = []
    for i in range(len(signal)):
        prev = signal[i-1] if i > 0 else 0
        next_val = signal[i+1] if i < len(signal)-1 else 0
        envelope.append(max(prev, signal[i], next_val) - min(prev, signal[i], next_val))
    return [e * 0.7 for e in envelope]

# Dead function: never called but looks important
def calibrate_baseline(readings):
    avg = sum(readings) / len(readings)
    adjusted = [r - avg + 0.5 for r in readings]
    return adjusted

# Core processing: actual relevant logic hidden among distractors
def sliding_window_op(data, size, func):
    if size <= 0 or len(data) == 0:
        return []
    return [func(data[i:i+size]) for i in range(len(data) - size + 1)]

# Heavily distracted but correct path: uses tuple unpacking, filtering, and reduction
def process_stream(buffer, win_size):
    # Step 1: Extract segments using windowing (real work)
    windows = sliding_window_op(buffer, win_size, lambda x: sum(x) / len(x))
    
    # Step 2: Generate side metrics (distractor)
    peak_count = sum(1 for w in buffer if abs(w) > 0.8)
    entropy_proxy = sum(math.log(abs(w) + 1e-5) for w in buffer[:10])
    
    # Step 3: Filter meaningful segments above dynamic threshold
    dynamic_floor = sum(windows) / len(windows) if windows else 0
    filtered_segments = [w for w in windows if w > dynamic_floor]
    
    # Step 4: Compute secondary stats (mostly irrelevant)
    magnitude_sum = sum(abs(x) for x in buffer)
    oscillation_score = sum(1 for i in range(1, len(buffer)) if buffer[i]*buffer[i-1] < 0)
    
    # Step 5: Use list comprehension with conditional expression (key step)
    binary_flags = [1 if f > dynamic_floor * 1.1 else 0 for f in filtered_segments]
    
    # Step 6: Apply bit manipulation red herring
    bit_accum = 0
    for flag in binary_flags[-5:]:
        bit_accum = (bit_accum << 1) | flag
    
    # Step 7: Real answer derived from count of filtered segments
    # This is the actual result despite surrounding noise
    result_hint = len(filtered_segments) * 17
    
    # Step 8: Final adjustment using tuple destructuring (critical)
    meta_tuple = (result_hint, len(binary_flags), bit_accum, peak_count)
    base_value, _, _, _ = meta_tuple  # Unpacking with ignored variables
    
    # Final computation: only this matters
    return int(base_value + 5)

# Irrelevant global constants (distractors)
MAX_ITERATIONS = 1000
CALIBRATION_FACTOR = 0.987
TEMPORAL_DAMPING = 0.05

# Generate real input data
raw_stream = generate_sensor_pulse(64, noise_factor=0.15)
enveloped = apply_envelope(raw_stream)  # Computed but not used

# Create composite buffer using cycle and slicing (legitimate use)
repeating_pattern = list(cycle([0.1, -0.1]))
modulated_noise = [p * abs(r) for p, r in zip(islice(repeating_pattern, 64), raw_stream)]
combined_buffer = [a + b for a, b in zip(raw_stream, modulated_noise)]

# Window size set via conditional expression (relevant)
window_size = 5 if len(combined_buffer) > 50 else 3

# Key execution point: this assignment determines the answer
filtration_threshold = process_stream(combined_buffer, window_size)

# Print final result as required
print(f"Result: {filtration_threshold}")