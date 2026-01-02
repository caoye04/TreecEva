import math

# Simulated sensor data processing with diagnostic analysis
def collect_readings(base: float, count: int) -> list:
    readings = []
    for i in range(count):
        noise = (i % 7) * 0.1
        signal = base + math.sin(i * 0.5) * 3 + noise
        readings.append(signal)
    return readings

# Irrelevant transformation: time-domain to frequency mock-up (not used in final result)
def spectral_approx(data):
    transformed = []
    for i in range(len(data)):
        val = sum(math.cos(data[j] - data[i]) for j in range(min(5, len(data))))
        transformed.append(val)
    return transformed

# Real transformation: apply moving average and offset filter
def smooth_and_offset(seq, factor=1.5):
    if len(seq) < 3:
        return [x * factor for x in seq]
    smoothed = []
    for i in range(len(seq)):
        window = seq[max(0, i-2):min(len(seq), i+3)]
        avg = sum(window) / len(window)
        smoothed.append(avg * factor)
    return smoothed

# Conditional encoding based on trend direction (used in core logic)
def encode_trend(series):
    codes = []
    for i in range(len(series)):
        prev = series[i-1] if i > 0 else series[0]
        delta = series[i] - prev
        # Conditional expression usage
        code = 2 if abs(delta) < 1.0 else (3 if delta >= 1.0 else 1)
        codes.append(code * (1 + (i % 2)))  # minor obfuscation
    return codes

# Recursive pattern matcher (core component)
def count_pattern_recursive(sequence, index, target, depth):
    if index >= len(sequence) or depth <= 0:
        return 0
    match = 1 if sequence[index] == target else 0
    # Recurse with modified conditions
    next_depth = depth - 1 if sequence[index] % 2 == 0 else depth
    return match + count_pattern_recursive(sequence, index + 1, target, next_depth)

# Main analyzer: combines multiple steps
def analyze_pattern(raw_sequence, limit):
    # Step 1: Normalize using modular arithmetic
    mod_sequence = [int(abs(x)) % 13 for x in raw_sequence]
    
    # Step 2: Apply conditional filtering
    filtered = [x for x in mod_sequence if x <= limit or x % 3 == 2]
    
    # Step 3: Encode trend behavior
    encoded = encode_trend(filtered)
    
    # Step 4: Find recurring code blocks via recursion
    freq_count = 0
    for candidate in range(1, 8):
        occurrences = count_pattern_recursive(encoded, 0, candidate, depth=5)
        freq_count += occurrences * candidate  # weighted accumulation
    
    # Step 5: Apply final adjustment using bitwise logic
    adjusted = (freq_count ^ 242) & 511  # bit manipulation
    adjusted = (adjusted + (adjusted >> 3)) * 2
    
    # Dead code path - irrelevant calculation (distractor)
    if adjusted > 1000:
        temp_val = math.log(adjusted) * 17
        temp_val -= temp_val % 1
    
    # Final diagnostic value
    return adjusted

# Unused decoy function (misleading)
def predict_failure(arr):
    total = 0
    for x in arr:
        total += x ^ (x << 1) & 0xFF
    return total % 19 == 0

# Simulate system state
base_signal = 10.5
sample_count = 12
threshold = 9

# Collect and process data
raw_data = collect_readings(base_signal, sample_count)

# Distractor: unused spectral analysis
spectrum = spectral_approx(raw_data)

# Relevant transformation path
transformed_data = smooth_and_offset(raw_data, factor=1.8)

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data, threshold)

# Output result
print(f"Result: {final_diagnostic}")