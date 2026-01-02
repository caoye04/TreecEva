import math

# Simulated sensor array data with noise and calibration offsets
data_stream = [127, 255, 0, 64, 192, 32, 224, 16, 112, 240, 8, 176, 48, 208, 96, 144]
noise_floor = 15
amplification_factor = 1.75
offset_compensation = -3

# Irrelevant calibration constants (distractors)
reference_voltage = 3.3
bit_depth = 8
sample_rate = 44100  # Unused in logic
channel_count = 2     # Dead code path

# Signal processing functions
def apply_noise_filter(values, floor):
    return [x if x > floor else 0 for x in values]

def amplify_signal(signal, factor, offset=0):
    return [(v * factor) + offset for v in signal]

def quantize(values, levels=256):
    scale = levels / 255.0
    return [int(round(v / scale)) for v in values]  # Not actually used later

def extract_peaks(readings, min_threshold=50):
    peaks = []
    for i in range(1, len(readings) - 1):
        if readings[i] > readings[i-1] and readings[i] > readings[i+1] and readings[i] >= min_threshold:
            peaks.append(readings[i])
    return peaks

# Decoy function – looks important but unused
def calculate_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    return -sum((count/total) * math.log2(count/total) for count in counts.values())

def rolling_average(values, window=3):
    smoothed = []
    for i in range(len(values)):
        start = max(0, i - window + 1)
        end = i + 1
        smoothed.append(sum(values[start:end]) / (end - start))
    return smoothed  # Computed but not used

# Core diagnostic logic
raw_filtered = apply_noise_filter(data_stream, noise_floor)
amplified = amplify_signal(raw_filtered, amplification_factor, offset_compensation)

# Apply conditional transformation using lambda and comprehension
transformed = [(lambda x: x ** 0.5 if x < 100 else math.log(x) if x < 200 else x / 10)(val) for val in amplified]

# Extract only high-magnitude events above dynamic threshold
dynamic_baseline = sum(transformed) / len(transformed)
threshold_func = lambda x: x > dynamic_baseline * 1.2

# Filter relevant data segments
filtered_data = [x for x in transformed if threshold_func(x)]

# Secondary filtering based on parity (irrelevant but looks meaningful)
even_dominant = len([x for x in filtered_data if int(x) % 2 == 0]) > len([x for x in filtered_data if int(x) % 2 == 1])

# Fake branching logic with dead end
if even_dominant:
    adjustment = 0.9
else:
    adjustment = 1.1  # Never reached due to data properties

# Critical processing chain
rolling_window = rolling_average([int(x) for x in amplified[:8]])  # Distractor computation

# Real processing function
def process_readings(readings, threshold_pred):
    valid_entries = [r for r in readings if threshold_pred(r)]
    if not valid_entries:
        return -1
    
    # Nested transformations
    processed = [((r * 2) + 5) for r in valid_entries]
    exponent_shift = len(processed) % 3
    
    # Multi-step reduction
    temp_result = 0
    for val in processed:
        temp_result ^= int(val)  # Bitwise accumulation
        temp_result = temp_result % 97  # Modular constraint
    
    # Final nonlinear mapping
    final_score = (temp_result ** (1 + exponent_shift))
    if final_score > 5000:
        final_score /= 2.5
    return round(final_score, 4)

# Execution point of interest
final_diagnostic = process_readings(filtered_data, threshold_func)

# Output result as required
print(f"Result: {final_diagnostic}")