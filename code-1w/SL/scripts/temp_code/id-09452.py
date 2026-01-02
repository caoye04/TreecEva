import itertools

# Simulated sensor data processing with red herrings and complex logic
raw_signals = [0.78, 0.63, 0.89, 1.02, 0.55, 0.41, 1.15, 0.94]
noise_floor = 0.3
amplification_factor = 2.1
calibration_offset = -0.1

# Irrelevant preprocessing: string-based identifier padding (distractor)
def pad_id(code):
    return code.upper().ljust(8, 'X') + '_V2'

# Decoy function: never called in execution path
def legacy_filter(x):
    return [val for val in x if val > 0.5]

# Unused transformation chain (dead code path)
baseline_shift = list(map(lambda x: x + calibration_offset, raw_signals))
doubled_pairs = list(itertools.combinations_with_replacement(baseline_shift, 2))
summed_combinations = [round(a + b, 3) for a, b in doubled_pairs if a > 0.7 and b < 1.1]

# Real signal enhancement (reused later)
enhanced_signal = [round((x - noise_floor) * amplification_factor, 3) for x in raw_signals]

# Simulated time-series windowing (partially relevant)
window_size = 3
sliding_windows = [enhanced_signal[i:i+window_size] for i in range(0, len(enhanced_signal)-window_size+1)]
window_averages = [sum(win)/len(win) for win in sliding_windows]

# Dummy classification using string methods on numeric strings (distraction)
status_codes = ['OK', 'WARN', 'CRIT']
encoded_flags = [code.center(10) for code in status_codes]
flag_summary = ''.join(encoded_flags).replace(' ', '-').strip('-')

# Actual thresholding logic buried in distractions
def apply_thresholds(seq, limit):
    return [1 if x > limit else 0 for x in seq]

binary_detections = apply_thresholds(enhanced_signal, 1.0)

def aggregate_diagnostics(pattern):
    count_ones = sum(pattern)
    max_run = current = 0
    for bit in pattern:
        if bit == 1:
            current += 1
            max_run = max(max_run, current)
        else:
            current = 0
    return count_ones * max_run

# Another decoy: unused recursive function
def factorial(n):
    return 1 if n <= 1 else n * factorial(n-1)

# Key transformation step (buried)
transformed_data = [round(x ** 1.5, 3) for x in window_averages if x > 0.6]

# Unused bitwise analysis (red herring)
analysis_key = 0b1101
mask = 0b1010
masked_result = analysis_key & mask  # 8 in decimal

# Threshold configuration with misleading defaults
thresholds = {
    'primary': 1.8,
    'secondary': 2.3,
    'dummy': masked_result  # unused field
}

# Core processing function with early returns
def process_metrics(data, config):
    if not data or len(data) < 2:
        return -1
    
    scaled = [x * 0.9 for x in data]
    
    primary_pass = [x for x in scaled if x > config['primary']]
    if len(primary_pass) == 0:
        return sum(scaled) // len(scaled)
    
    secondary_filtered = [x for x in primary_pass if x < config['secondary']]
    if len(secondary_filtered) >= 2:
        product = 1
        for val in secondary_filtered:
            product *= int(val)  # truncates to integer
        return product % 1000
    
    return round(sum(scaled), 2)

# Final computation: target execution point
final_diagnostic = process_metrics(transformed_data, thresholds)

# Output result as required
print(f"Result: {final_diagnostic}")