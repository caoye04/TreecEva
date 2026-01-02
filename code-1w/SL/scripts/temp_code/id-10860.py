import math

# Simulated sensor data with noise and irrelevant transformations
data_stream = [12, 18, 27, 36, 48, 54, 60, 72, 81, 90, 99, 108]
noise_factor = 0.05
amplification_curve = lambda x: x * math.sin(x / 10) if x % 2 == 0 else x * 0.95
calibration_offset = sum([amplification_curve(val) for val in data_stream[:5]]) // len(data_stream[:5])

# Irrelevant preprocessing: frequency analysis (dead end)
frequencies = {}
for val in data_stream:
    bin_key = val // 10
    frequencies[bin_key] = frequencies.get(bin_key, 0) + 1
peak_frequency = max(frequencies.values())
mode_tone = [k*10 for k, v in frequencies.items() if v == peak_frequency][0]

# Distractor: audio mimicry transformation (unused)
audio_envelope = [math.cos(i * 0.5) * 100 for i in range(len(data_stream))]
modulated_output = [data_stream[i] + int(audio_envelope[i] * noise_factor) for i in range(len(data_stream))]

# Relevant path begins: extract every third element and square them
critical_samples = [x**2 for i, x in enumerate(data_stream) if (i + 1) % 3 == 0]

# Apply non-linear transformation with conditional scaling
def transform_value(val):
    if val > 1000:
        return int(val ** 0.5)
    elif val > 500:
        return val // 2
    else:
        return val - (val // 4)

transformed_data = list(map(transform_value, critical_samples))

# Decoy recursive function for entropy calculation (never called)
def compute_entropy(arr, depth=0):
    if depth > 3 or len(arr) == 0:
        return 0.0
    total = sum(arr)
    if total == 0:
        return 0.0
    probs = [x/total for x in arr if x > 0]
    return -sum(p * math.log2(p) for p in probs if p > 0) + compute_entropy(arr[::2], depth+1)

# Another red herring: attempt to fit polynomial (irrelevant)
def polynomial_fit_score(data):
    n = len(data)
    if n < 2:
        return 0
    mean_x = sum(range(n)) / n
    mean_y = sum(data) / n
    cov = sum((i - mean_x) * (data[i] - mean_y) for i in range(n))
    var_x = sum((i - mean_x)**2 for i in range(n))
    slope = cov / var_x if var_x != 0 else 0
    return round(abs(slope), 3)
fit_score = polynomial_fit_score(transformed_data)

# Real computation: count how many transformed values are powers of two
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

power_count = len([x for x in transformed_data if is_power_of_two(x)])

# Linear search for first occurrence above threshold
threshold_trigger = 200
detected_index = -1
for idx, value in enumerate(transformed_data):
    if value > threshold_trigger:
        detected_index = idx
        break

# Mock diagnostic chain using lambda and recursion
recursion_depth_log = []

def analyze_pattern(seq):
    recursion_depth_log.append(1)  # logging fake depth
    if len(seq) == 0:
        return 0
    if len(seq) == 1:
        return seq[0] + power_count
    
    # Recursive reduction with side mutation
    mid = len(seq) // 2
    left_half = seq[:mid]
    right_half = seq[mid:]
    
    # Combine results using arithmetic and bit manipulation
    left_result = analyze_pattern(left_half)
    right_result = analyze_pattern(right_half)
    
    # Core fusion logic: weighted combination
    fusion = ((left_result + right_result) // 2) ^ power_count
    return fusion + (detected_index if detected_index != -1 else 10)

# Key assignment statement
final_diagnostic = analyze_pattern(transformed_data)

# Output result as required
print(f"Result: {final_diagnostic}")