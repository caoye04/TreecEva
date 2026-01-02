import math

# Simulated sensor data processing with diagnostic analysis
def collect_samples(n):
    raw_data = []
    for i in range(n):
        sample = (i * 2.718) % 50 + (math.sin(i / 3) * 15)
        raw_data.append(round(sample, 2))
    return raw_data

# Irrelevant helper: computes entropy (not used in final result)
def compute_entropy(data):
    freq_map = {}
    for x in data:
        freq_map[x] = freq_map.get(x, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

# Signal normalization using sliding window (used)
def normalize_signal(signal):
    window_size = 3
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window_size + 1)
        end = min(len(signal), i + 1)
        window = signal[start:end]
        avg = sum(window) / len(window)
        smoothed.append(round(avg, 2))
    return smoothed

# Data filtering by threshold (used)
def filter_outliers(data, threshold=35.0):
    return [x for x in data if x <= threshold]  # list comprehension

# Bitmask-based status encoding (distractor)
def encode_status(flags):
    code = 0
    for i, flag in enumerate(flags):
        if flag:
            code |= (1 << i)
    return code  # never actually used

# Core analysis function (used)
def analyze_signal(cleaned):
    # Apply slicing to focus on mid-sequence behavior
    segment = cleaned[len(cleaned)//4 : len(cleaned)//4*3]
    squared_sum = sum([x**2 for x in segment])  # list comprehension
    rms = math.sqrt(squared_sum / len(segment))
    return int(rms)  # deterministic integer output

# Main execution flow
if __name__ == '__main__':
    # Step 1: Collect raw samples
    samples = collect_samples(40)

    # Distractor variables (irrelevant computations)
    sample_entropy = compute_entropy([int(x) for x in samples])  # unused
    device_status = encode_status([True, False, True, False, True])  # unused
    calibration_offset = sum(math.cos(i/5) for i in range(20))  # dead computation

    # Step 2: Normalize signal
    normalized = normalize_signal(samples)

    # Step 3: Filter outliers
    filtered = filter_outliers(normalized, threshold=36.5)

    # Step 4: Process final sample set
    processed_samples = [round(x * 1.08, 2) for x in filtered]  # slight gain adjustment

    # Distractor: sorting unrelated data
    dummy_log = [abs(x - 20) for x in processed_samples]
    dummy_log.sort(reverse=True)  # irrelevant sort operation

    # Key statement
    final_diagnostic = analyze_signal(processed_samples)

    # Output result
    print(f"Result: {final_diagnostic}")