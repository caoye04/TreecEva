import math

# Simulate sensor data processing with noise filtering and signal transformation
raw_readings = [127, 255, 64, 192, 32, 180]
noise_floor = 30
signal_boost = 1.75
sample_rate = 44100

def apply_window(signal):
    # Hamming window application (relevant)
    windowed = []
    for i in range(len(signal)):
        window_factor = 0.54 - 0.46 * math.cos(2 * math.pi * i / (len(signal) - 1))
        windowed.append(signal[i] * window_factor)
    return windowed

def enhance_contrast(x):
    # Unused function - red herring
    return int((x ** 1.2) / 255 * 100)

def rolling_average(data, window=3):
    # Irrelevant smoothing function - dead code path
    smoothed = []
    for i in range(len(data)):
        start = max(0, i - window // 2)
        end = min(len(data), i + window // 2 + 1)
        avg = sum(data[start:end]) / (end - start)
        smoothed.append(avg)
    return smoothed

def detect_peaks(signal, level=100):
    # Distractor: detects peaks but not used in final logic
    peaks = []
    for i, val in enumerate(signal):
        if val > level:
            peaks.append(i)
    return peaks

# Intermediate transformations with decoy variables
temp_buffer = [x for x in raw_readings if x > noise_floor]
scaled_data = [x * signal_boost for x in temp_buffer]
clipped_data = [min(x, 255) for x in scaled_data]

# Bit manipulation layer - relevant to final result
bitwise_mask = 0b11111111
masked_data = [int(x) & bitwise_mask for x in clipped_data]

# Conditional transformation based on entropy-like measure
entropy_estimate = sum([(x / 255) * math.log(255 / x) if x > 0 else 0 for x in masked_data])
transformation_mode = 'high' if entropy_estimate > 4.0 else 'low'

decoy_matrix = [[i * j for j in range(4)] for i in range(4)]  # Unused 4x4 matrix - distraction

# Signal folding via conditional expression (core concept)
folded_signal = []
for x in masked_data:
    folded = x ^ 0b10101010 if transformation_mode == 'high' else x ^ 0b01010101
    folded_signal.append(folded)

def process_signal(data, limit):
    # Core processing: count how many exceed dynamic threshold
    dynamic_threshold = int(255 * (1 - 1 / (1 + math.exp(-0.05 * limit))))
    count_above = sum(1 for x in data if x > dynamic_threshold)
    total_power = sum(x ** 2 for x in data) / len(data)
    # Final output combines count and normalized power
    return int(count_above * (total_power / 100))

# Transform data through windowing (key step)
transformed_data = apply_window(folded_signal)

# Decoy statistical analysis
mean_val = sum(transformed_data) / len(transformed_data)
variance = sum((x - mean_val) ** 2 for x in transformed_data) / len(transformed_data)

# Threshold derived from modular arithmetic on length
data_length = len(transformed_data)
threshold = (data_length * 73) % 199  # Modular threshold generation

# Critical execution point
final_output = process_signal(transformed_data, threshold)

# Misleading secondary result (decoy output)
secondary_result = sum(transformed_data[i] for i in range(0, len(transformed_data), 2))

# Only print the target result
print(f"Target result: {final_output}")