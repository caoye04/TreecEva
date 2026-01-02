import math

# Simulated sensor data preprocessing pipeline
raw_readings = [3, 7, 2, 8, 5, 10, 4, 6]
baseline_offset = 1.5
calibration_factor = 0.85

# Irrelevant statistical placeholders (distractors)
mean_placeholder = sum(raw_readings) / len(raw_readings)
std_deviation_fake = math.sqrt(sum([(x - mean_placeholder)**2 for x in raw_readings]) / len(raw_readings))
median_fake = sorted(raw_readings)[len(raw_readings)//2]

# Signal filtering and transformation (relevant path)
def apply_filter(data, factor):
    return [round(x * factor + baseline_offset, 2) for x in data]

filtered_signal = apply_filter(raw_readings, calibration_factor)

# Noise reduction using sliding window (mixed relevance)
def reduce_noise(signal, window_size=2):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window_size)
        segment = signal[start:i+1]
        smoothed.append(sum(segment) / len(segment))
    return [round(x, 2) for x in smoothed]

noisy_correction_flag = True
if noisy_correction_flag:
    filtered_signal = reduce_noise(filtered_signal)

# Data categorization heuristics (distractor-heavy section)
category_map = {}
for val in filtered_signal:
    key = int(val)
    category_map[key] = category_map.get(key, 0) + 1

# Phantom pattern detection (red herring function)
def detect_ghost_peaks(sequence):
    peaks = []
    for i in range(1, len(sequence)-1):
        if sequence[i] > sequence[i-1] and sequence[i] > sequence[i+1]:
            peaks.append(i)
    return [sequence[p] for p in peaks] if peaks else [0]

ghosts = detect_ghost_peaks([int(x) for x in filtered_signal])

# Actual transformation for analysis (critical path)
bitwise_weights = []
for i, val in enumerate(filtered_signal):
    weight = int((val + i) % 8)
    bitwise_weights.append(weight)

transformed_data = list(map(lambda w: (w << 1) ^ 3, bitwise_weights))  # Shift and XOR

# Threshold logic with conditional override (misleading intermediate)
dynamic_threshold = sum(transformed_data) / len(transformed_data)
override_enable = False

if override_enable:
    dynamic_threshold = 10  # Dead code path
else:
    dynamic_threshold += 2.5

# Core diagnostic analyzer (key function)
def analyze_pattern(seq, thresh):
    count_above = len([x for x in seq if x > thresh])
    total_xor = 0
    for x in seq:
        total_xor ^= x  # Bitwise accumulation

    balance_score = abs(count_above - (len(seq) - count_above))
    
    # Secondary decoy computation (irrelevant but plausible)
    entropy_proxy = 0
    for x in seq:
        if x > 0:
            entropy_proxy += x * math.log(x, 2)
    
    # Final decision logic (actual answer path)
    if balance_score <= 2:
        return total_xor + 500
    else:
        return int(entropy_proxy) % 1000

threshold = dynamic_threshold
final_diagnostic = analyze_pattern(transformed_data, threshold)

print(f"Result: {final_diagnostic}")