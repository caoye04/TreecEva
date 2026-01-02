import math

# Simulated sensor data and configuration
raw_signals = [3.2, 1.8, 4.5, 0.7, 2.9, 6.1, 2.3, 5.0, 3.7, 4.4]
baseline = 2.5
noise_floor = 0.5
sample_rate = 100

# Irrelevant calibration constants (distractors)
calibration_a = 0.987
offset_x = -0.123
gain_factor = 1.05
smoothing_window = 3
max_amplitude = 10.0

# Signal conditioning parameters (some relevant, some not)
thresh_high = baseline * 1.8
thresh_low = baseline * 0.7
dynamic_range = max_amplitude / gain_factor

# Decoy function – looks important but unused in main logic
def apply_calibration(signal_list, a, offset):
    return [a * x + offset for x in signal_list]

# Another decoy: complex frequency analysis (dead code path)
def analyze_frequency(signal, rate):
    fft_result = []
    for i in range(rate // 10):
        angle = 2 * math.pi * i / (rate // 10)
        re = sum(s * math.cos(angle * j) for j, s in enumerate(signal))
        im = sum(s * math.sin(angle * j) for j, s in enumerate(signal))
        fft_result.append(math.sqrt(re**2 + im**2))
    return fft_result

# Real processing begins here
active_mask = [x > noise_floor for x in raw_signals]
filtered_data = [x for x, active in zip(raw_signals, active_mask) if active]

# Multiple red herrings below
buffer_cache = {}
temp_sum = 0.0
for val in filtered_data:
    temp_sum += val ** 2
    if temp_sum > 10.0:
        buffer_cache[len(buffer_cache)] = temp_sum
        break  # early exit, creates misleading partial result

# Distractor: unused intermediate transformation
decimated_signal = [filtered_data[i] for i in range(0, len(filtered_data), 2)]

# Threshold map with irrelevant entries
threshold_map = {
    'critical': 5.5,
    'warning': 4.0,
    'info': 1.0,  # unused level
    'debug': 0.1,  # decoy level
    'nominal': 2.0  # not used in decision
}

# Conditional expression with side-effect-like structure (no real side effect)
mode_flag = 'aggressive' if len(filtered_data) > 6 else 'conservative'
scaling_factor = 1.2 if mode_flag == 'aggressive' else 0.8

# List comprehension with filtering and scaling (core logic)
scaled_filtered = [
    x * scaling_factor 
    for x in filtered_data 
    if x >= thresh_low
]

# Bit manipulation red herring (irrelevant to final result)
status_word = 0
for x in scaled_filtered:
    if x > 4.0:
        status_word |= 1 << int(x) % 8

# Another decoy dictionary operation
summary_stats = {
    'count': len(scaled_filtered),
    'average': sum(scaled_filtered) / len(scaled_filtered) if scaled_filtered else 0,
    'peak': max(scaled_filtered) if scaled_filtered else 0,
    'flags': bin(status_word)
}

# Core processing function with multiple concepts
def process_signals(data, thresholds):
    high_alerts = [x for x in data if x >= thresholds['critical']]
    mid_alerts = [x for x in data if thresholds['warning'] <= x < thresholds['critical']]
    
    # Complex conditional expression
    penalty = 10 if len(high_alerts) > 1 else (5 if len(high_alerts) == 1 else 0)
    bonus = len(mid_alerts) * 2
    
    # Nested dictionary lookup and arithmetic
    base_score = sum(
        x * math.log(x) if x > 1 else x 
        for x in data
    )
    
    # Irrelevant bit shift distraction inside function
    magic_shift = (len(high_alerts) << 2) ^ (bonus >> 1)
    
    # Final computation — only this matters
    raw_total = base_score + bonus - penalty
    adjusted_total = raw_total * (0.9 + (magic_shift * 0.01))  # dummy use of magic_shift
    
    # This line contains the actual answer derivation
    final_value = int(adjusted_total * 1000) / 1000.0  # round to 3 decimals
    
    return final_value

# Execution point of interest
final_output = process_signals(filtered_data, threshold_map)

# Print required output
print(f"Result: {final_output}")