import math

# Simulated sensor data processing with embedded logic chain
data_stream = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
noise_floor = 1.5
amplification_factor = 2.0
sample_rate = 100

def apply_window(signal):
    # Hanning window application (distraction, not used in final)
    N = len(signal)
    return [signal[i] * (0.5 - 0.5 * math.cos(2 * math.pi * i / (N - 1))) for i in range(N)]

def generate_baseline(length):
    # Irrelevant synthetic baseline generation
    return [math.sin(x * 0.1) for x in range(length)]

def shift_phase(data, steps=1):
    # Unused circular shift function (red herring)
    return data[-steps:] + data[:-steps]

def compute_entropy(arr):
    # Distractor: computes entropy but not used in main logic
    from collections import Counter
    counts = Counter(arr)
    total = len(arr)
    return -sum((count / total) * math.log2(count / total) for count in counts.values())

def filter_outliers(seq, limit=3):
    # Dead code path: limit parameter unused in logic
    return [x for x in seq if x <= max(seq) - limit]

# Real transformation begins here
processed = [x * amplification_factor for x in data_stream if x > noise_floor]

# Slice middle segment (actual relevant operation)
trimmed = processed[1:-1]  # Remove first and last elements

# Lambda-based dynamic threshold (key concept)
threshold_func = lambda val: val > (amplification_factor * 3.5)

# Transform via conditional mapping (relevant logic)
transformed_data = []
for item in trimmed:
    if item > 4.0:
        transformed_data.append(int(item) ** 2)
    elif item == 4.0:
        transformed_data.append(17)
    else:
        transformed_data.append(int(item * 2))

# Decoy statistical analysis (distractor block)
mean_val = sum(trimmed) / len(trimmed)
variance = sum((x - mean_val) ** 2 for x in trimmed) / len(trimmed)
std_deviation = math.sqrt(variance)

# Another red herring: tuple unpacking with dummy values
dummy_summary = (len(data_stream), sum(data_stream), noise_floor)
size, total, floor = dummy_summary

# Simulate unused feature extraction
features = []
for i in range(len(transformed_data) - 1):
    features.append(transformed_data[i] ^ transformed_data[i+1])  # XOR pattern (not used)

# Core analysis function with embedded logic
def analyze_pattern(seq, threshold):
    count_above = 0
    running_sum = 0
    history = []
    
    for idx, value in enumerate(seq):
        # Inject position-dependent logic
        adjusted = value + idx
        
        # Conditional mutation
        if adjusted % 2 == 0:
            adjusted = int(adjusted / 2)
        else:
            adjusted = adjusted * 3 + 1  # Collatz-like step
        
        # Accumulate only if passes lambda threshold
        if threshold(value):  # Note: uses original value
            count_above += 1
            
        # Always contribute to sum
        running_sum += adjusted
        history.append(adjusted)
    
    # Final computation based on multiple derived values
    # Mixing count, sum, and history traversal
    result = running_sum
    
    # Additional layer: process history in reverse with slicing
    rev_hist = history[::-1]  # Reverse using slice
    for j, h in enumerate(rev_hist[:len(rev_hist)//2]):  # Half of reversed
        if j % 2 == 1:
            result -= h
    
    # Final interference: irrelevant floating point adjustment
    calibration_offset = math.log(1 + abs(result)) * 0.001
    result = result  # No-op assignment (misleading)
    
    return int(result)

# Execute main analysis
final_diagnostic = analyze_pattern(transformed_data, threshold_func)

# Print result as required
print(f"Target result: {final_diagnostic}")