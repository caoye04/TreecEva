import itertools

# Simulated sensor data processing with diagnostic analysis
raw_readings = [0.88, -1.22, 3.14, -2.71, 0.0, 1.41, -1.73, 2.23]

# Irrelevant baseline calibration (distractor)
def calibrate_sensor(x):
    return (x * 1.05) - 0.02

calibrated = [calibrate_sensor(x) for x in raw_readings]

# Noise filter using moving average (partially relevant but not used in final path)
def smooth(signal, window=3):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window + 1)
        smoothed.append(sum(signal[start:i+1]) / (i - start + 1))
    return smoothed

noisy_filtered = smooth(raw_readings, 2)

# Key transformation: apply phase shift and threshold detection
shifted = [(x + 2.0) % 4.0 for x in raw_readings]
thresh_met = [1 if x > 2.5 else 0 for x in shifted]

# Bitmask pattern generation from threshold results (red herring)
binary_pattern = int(''.join(map(str, thresh_met)), 2)
decoymask = binary_pattern ^ 0b11111111  # Unused obfuscation

# Real signal processing begins here — hidden in middle of noise
compressed = list(itertools.accumulate(
    [int(abs(x) * 100) for x in raw_readings],
    func=lambda a, b: (a + b) % 97
))

# Conditional transformation based on parity chain
transformed = []
for val in compressed:
    if val % 3 == 0:
        transformed.append(val * 2)
    elif val % 5 == 0:
        transformed.append(val + 17)
    else:
        transformed.append(val - (val % 4))

# Secondary filtering: extract every third element starting at index 1
every_third = [transformed[i] for i in range(1, len(transformed), 3)]

# Decoy function: looks important but unused
def compute_entropy(data):
    from math import log2
    freqs = {}
    for d in data:
        freqs[d] = freqs.get(d, 0) + 1
    total = len(data)
    return -sum((count/total) * log2(count/total) for count in freqs.values())

# Actual processing pipeline
intermediate_key = sum(every_third) ^ 0xAA  # XOR with hex constant

# Hash-like reduction using lambda and conditional expression
hash_step = lambda x: x * 31 if x < 100 else x // 7
reduced = hash_step(intermediate_key) if intermediate_key % 2 == 0 else hash_step(intermediate_key + 8)

# Final diagnostic logic
status_flags = {
    'normal': 100,
    'warning': 250,
    'critical': 500
}

# Control flow with misleading branches
if reduced > 400:
    level = 'critical'
elif reduced > 200:
    level = 'warning'
else:
    level = 'normal'

# Destructuring assignment (irrelevant to output but adds complexity)
primary, *secondary, tertiary = transformed[:8] if len(transformed) >= 8 else transformed + [0]*8

# Unused recursive function (dead code path)
def recursive_sum(arr, n):
    if n <= 0: return 0
    return arr[n-1] + recursive_sum(arr, n-1)

# Data structure cross-reference distraction
table_map = {i: transformed[i] * primary for i in range(len(transformed))}

processed_data = {
    'values': every_third,
    'checksum': reduced,
    'flag': level
}

# Core analysis function with embedded logic
analyze_signal = lambda data: (
    data['checksum'] + 
    (status_flags[data['flag']] // 10) + 
    (sum(data['values']) % 25)
)

# Critical execution point
final_diagnostic = analyze_signal(processed_data)

print(f"Result: {final_diagnostic}")