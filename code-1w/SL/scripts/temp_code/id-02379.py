import itertools

# Sensor array simulation for environmental monitoring
def generate_baseline(noise_level=0.05):
    base = [1.0 + i * 0.1 for i in range(10)]
    noise = [(i % 3) * noise_level for i in range(10)]
    return [b + n for b, n in zip(base, noise)]

# Irrelevant auxiliary function - decoy
def calculate_entropy(data):
    total = 0
    for x in data:
        if x > 0:
            total -= x * x
    return total

# Signal processing pipeline
processed_signals = []
def filter_outliers(signal, threshold=1.5):
    mean_val = sum(signal) / len(signal)
    deviances = [(x - mean_val) ** 2 for x in signal]
    std_dev = (sum(deviances) / len(deviances)) ** 0.5
    filtered = [x for x in signal if abs(x - mean_val) <= threshold * std_dev]
    return filtered if len(filtered) > 0 else signal[:len(signal)//2 + 1]

# Unused and misleading preprocessing branch - red herring
def deprecated_normalization(arr):
    max_val = max(arr)
    return [x / max_val * 100 for x in arr]  # Never called

# Core transformation with distractors
raw_data = [
    [12.3, 15.7, 9.1, 14.2, 11.0, 13.8, 10.5, 16.1, 8.9, 12.7],
    [11.9, 14.8, 10.2, 13.6, 12.1, 14.0, 9.8, 15.3, 11.1, 13.4],
    [13.0, 16.2, 8.7, 14.5, 10.9, 13.3, 11.4, 15.8, 9.5, 12.9]
]

aggregated = []
for seq in raw_data:
    smoothed = [round(x * 0.9 + 1.0, 2) for x in seq]  # Distractor transformation
    normalized = [x / max(smoothed) for x in smoothed]  # Intermediate irrelevant scaling
    aggregated.extend(normalized)

# Real processing starts here — slicing and filtering
baseline_shift = generate_baseline()[2:8]  # Slice of real importance
primary_band = aggregated[::3]  # Every third reading — actual signal source

refined_input = filter_outliers(primary_band, threshold=1.2)

# Bit manipulation layer — hidden relevance
def encode_quality_metric(values):
    result = 0
    for v in values:
        shifted = int(v * 100) & 0xFF
        result ^= shifted  # XOR accumulation
    return result >> 4  # Compress to significant nibble

# Data fusion using itertools
paired_deltas = list(itertools.starmap(lambda a, b: abs(a - b), 
                                        zip(refined_input, refined_input[1:])))
signal_entropy = sum(paired_deltas) * 1000

# Dummy control flow with dead path
mode_flag = 'A'
if mode_flag == 'Z':
    signal_entropy *= 2
elif mode_flag == 'X':
    signal_entropy += 100
else:
    pass  # No effect — but looks important

# Main analysis function
quality_code = encode_quality_metric(refined_input)
temp_offset = sum(baseline_shift) * quality_code

interim_score = temp_offset + signal_entropy

# Final diagnostic calculation
checksum = 0
for i, val in enumerate(refined_input):
    checksum += (i + 1) * int(val * 100)

# Critical assignment point
final_diagnostic = int(interim_score) ^ checksum  # Key statement

print(f"Result: {final_diagnostic}")