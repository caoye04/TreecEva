import math

# Irrelevant helper function (dead code path)
def compute_entropy(values):
    return -sum(p * math.log2(p) for p in values if p > 0)

# Misleading transformation chain
def transform_sequence(seq):
    temp_a = [x ** 2 for x in seq if x % 2 == 0]
    temp_b = [math.sqrt(y) for y in temp_a]
    shifted = [(z + 5) % 10 for z in temp_b]
    return shifted  # Never used in main logic

# Decoy data structure
decoy_map = {
    'offsets': [1, 3, 7, 9],
    'flags': (True, False, True),
    'threshold': 42
}

# Real processing components
def extract_valid_windows(data, size=3):
    windows = []
    for i in range(len(data) - size + 1):
        window = data[i:i+size]
        if sum(window) > 10:
            windows.append(window)
    return windows

def evaluate_peaks(windows):
    peaks = []
    for win in windows:
        mid_val = win[1]
        left_val = win[0]
        right_val = win[2]
        if mid_val > left_val and mid_val > right_val:
            peaks.append(mid_val)
    return peaks

def aggregate_metrics(peaks):
    if not peaks:
        return 0
    avg_peak = sum(peaks) / len(peaks)
    squared_avg = avg_peak ** 2
    adjusted = squared_avg * 1.5
    return int(adjusted)

def build_lookup(keys, base_shift):
    lookup = {}
    for idx, key in enumerate(keys):
        lookup[key] = (idx + base_shift) ** 2
    return lookup  # Used to distract with dictionary operations

# Simulated sensor data (real input)
data_segments = [2, 5, 3, 8, 1, 6, 7, 4, 9]

# Distractor: slicing and reordering that leads nowhere
decoy_slice = data_segments[2:7][::-1]
shadow_copy = decoy_slice[:]
for i in range(len(shadow_copy)):
    shadow_copy[i] += 100  # Dead end modification

# Auxiliary dictionary manipulation (distractor)
key_labels = ['a', 'b', 'c', 'd']
lookup_table = build_lookup(key_labels, 4)
temp_dict = {k: v for k, v in lookup_table.items() if v % 2 == 0}

# Conditional expression red herring
evaluation_mode = 'strict' if len(data_segments) > 5 else 'basic'
mode_factor = 2 if evaluation_mode == 'strict' else 1  # Not actually used later

# Real processing pipeline
windowed_data = extract_valid_windows(data_segments)
peak_values = evaluate_peaks(windowed_data)
interim_result = aggregate_metrics(peak_values)

# Final computation with tuple unpacking distraction
dummy_tuple = (interim_result, len(peak_values), sum(data_segments))
processed_value, _, _ = dummy_tuple

scaling_factor = 3
final_output = processed_value * scaling_factor

# Additional misleading accumulation
running_total = 0
for val in data_segments:
    if val % 2 == 0:
        running_total += val * 2
# This total is never used

print(f"Target result: {final_output}")