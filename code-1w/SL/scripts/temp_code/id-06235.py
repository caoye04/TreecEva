import math

# Simulated sensor data and noise parameters
data_stream = [3, 7, 1, 9, 5, 11, 8, 14, 6, 10, 4, 12]
noise_floor = 4
amplitude_mod = 2
sample_rate = 1000

# Irrelevant signal processing constants (distractors)
carrier_frequency = 440
modulation_index = 0.75
fft_size = 1024
window_overlap = 0.5
scaling_factor = math.pi / 180

# Decoy transformation (dead path)
def apply_fourier_transform(signal):
    return [abs(x) * scaling_factor for x in signal]

# Unused helper function (red herring)
def normalize_signal(data):
    max_val = max(data)
    return [x / max_val for x in data]

# Misleading intermediate calculation with decoy result
temp_correction = sum([amplitude_mod * (i % 3) for i in range(len(data_stream))]) // len(data_stream)
offset_adjustment = int(math.log(carrier_frequency, 2)) - temp_correction

# Real signal filtering logic buried among distractions
raw_threshold = 6
filtered_data = [x for x in data_stream if x > raw_threshold]  # List comprehension used

# Dummy statistical analysis (irrelevant)
mean_value = sum(data_stream) / len(data_stream)
variance = sum((x - mean_value) ** 2 for x in data_stream) / len(data_stream)
std_deviation = math.sqrt(variance)

# Spurious data structure transformations (set operations as distractor)
unique_sorted = set(sorted(data_stream))
duplicate_check = {x for x in data_stream if data_stream.count(x) > 1}
redundant_tuple = (len(unique_sorted), len(duplicate_check), offset_adjustment)

# Conditional expression with misleading branch
processing_mode = 'high_res' if std_deviation > 3 else 'low_res'
mode_factor = 1.5 if processing_mode == 'high_res' else 0.8  # unused

# Core logic hidden in nested conditionals and abstraction
def enhance_value(x, thresh):
    if x > thresh * 2:
        return x * 1.1
    elif x > thresh:
        return x * 1.3  # Critical path: only this applies to some filtered values
    else:
        return x

def process_signals(signal_list, thresh):
    # Nested list comprehension with conditional logic
    enhanced = [int(enhance_value(val, thresh)) for val in signal_list]
    
    # Additional distraction inside function
    squared_errors = [math.pow(e - sum(enhanced)/len(enhanced), 2) for e in enhanced]
    rmse = math.sqrt(sum(squared_errors) / len(squared_errors))
    
    # Final aggregation buried in complex expression
    adjustment = sum([i * 0.1 for i in range(len(enhanced))])  # minor incremental effect
    base_total = sum(enhanced)
    
    # Key computation
    final_score = base_total - int(rmse) + int(adjustment)
    
    # Dead return branch (misdirection)
    return final_score if len(signal_list) % 2 == 1 else final_score + 100  # Always odd length

# Secondary filtering based on irrelevant criterion (distraction)
secondary_mask = [x for x in data_stream if x % 2 == 0]
parity_offset = len(secondary_mask) - len(filtered_data)

# Unused recursive attempt (decoy)
def recursive_sum(arr, idx=0):
    if idx >= len(arr):
        return 0
    return arr[idx] + recursive_sum(arr, idx + 1)

# Actual execution chain
threshold = noise_floor + 2  # evaluates to 6
intermediate_debug = [x - threshold for x in filtered_data]  # red herring list

# Critical statement
final_output = process_signals(filtered_data, threshold)

# Irrelevant post-processing
if final_output > 100:
    final_output = int(final_output * 0.95)
else:
    final_output = int(final_output * 1.05)

# Output result
print(f"Result: {final_output}")