import math

# Simulated sensor data preprocessing with red herrings
def acquire_signal(raw_stream):
    if not raw_stream:
        return [0]
    processed = []
    for val in raw_stream:
        if val < -50:
            continue  # filter extreme negatives
        processed.append(abs(val) ** 0.5)
    return processed

# Irrelevant transformation: frequency domain mock-up (dead path)
def compute_fourier_magnitude(signal):
    fft_mock = []
    for i in range(len(signal)):
        fft_mock.append(math.sin(i * 0.5) * math.cos(i * 0.3))
    norm = sum(x**2 for x in fft_mock) ** 0.5
    return [x / norm for x in fft_mock] if norm else fft_mock

# Real processing begins here — distractors above
threshold_map = {
    'low': 3.5,
    'medium': 7.2,
    'high': 15.0
}

# Misleading auxiliary function — never called
def calibrate_baseline(data, factor=1.1):
    return [x * factor for x in data if x > 1]

# Core filtering logic with slicing and conditions
def apply_dynamic_filter(signal, config):
    length = len(signal)
    if length < 5:
        signal += [0] * (5 - length)

    # Slice to center window
    mid = length // 2
    window = signal[mid-2:mid+3] if length >= 5 else signal

    # Spurious intermediate calculation (distractor)
    avg_window = sum(window) / len(window) if window else 0
    adjusted = [x for x in window if x > avg_window * 0.7]

    # Actual relevant logic embedded
    result = []
    for x in signal:
        if x > threshold_map['low']:
            result.append(x * 1.2)
        elif x > threshold_map['low'] * 0.5:
            result.append(x * 0.8)
        else:
            result.append(x)
    return result

# Another decoy: entropy estimation (unused)
def estimate_entropy(data):
    from collections import Counter
    counts = Counter([round(x, 1) for x in data])
    total = len(data)
    entropy = -sum((count/total) * math.log2(count/total) for count in counts.values())
    return round(entropy, 3)

# Main processing with nested control flow and slicing
def process_signal(data, thresholds):
    if len(data) == 0:
        return 0

    # Multiple assignment red herring
    temp_a, temp_b, temp_c = 1, 2, 3
    temp_list = [temp_a, temp_b, temp_c]
    temp_sum = sum(temp_list)  # irrelevant

    # Real logic: transform and slice
    scaled = [math.log(x + 1) for x in data if x >= 0]
    if len(scaled) > 6:
        scaled = scaled[:len(scaled)//2]  # slice upper half

    # Boolean logic chain with short-circuiting
    use_enhanced = len(scaled) > 4 and scaled[-1] > thresholds['medium']
    fallback_mode = not use_enhanced and scaled.count(0) == 0

    accumulator = 0.0
    for idx, val in enumerate(scaled):
        if use_enhanced:
            if idx % 2 == 0:
                accumulator += val * 1.5
            else:
                accumulator += val * 0.9
        elif fallback_mode:
            accumulator += val * 1.1
        else:
            accumulator += val

        # Early termination red herring
        if accumulator > 100:
            break  # unreachable in this setup

    # Final adjustment using bitwise (distraction)
    int_accum = int(accumulator)
    masked = int_accum & 0xFFFF  # limit to 16 bits — no real effect
    final_val = masked ^ (masked >> 4)  # more distraction

    return float(final_val)

# Unused global variables (distractors)
baseline_offset = 2.3
calibration_table = {i: i*0.95 for i in range(100)}
system_status = {'active': True, 'mode': 'standby'}

# Signal acquisition
raw_input_stream = [16, -60, 25, 8, 12, 4, 30, 11, 7]
acquired_data = acquire_signal(raw_input_stream)

# Apply main filter
filtered_data = apply_dynamic_filter(acquired_data, {'mode': 'dynamic'})

# Critical statement
final_output = process_signal(filtered_data, threshold_map)

# Print result as required
print(f"Target result: {final_output}")