import math

# Simulated sensor data processing with diagnostic analysis
def collect_samples(duration, rate=100):
    return [int((50 * math.sin(i / 10)) + (30 * math.cos(i / 7)) + 100) for i in range(duration * rate)]

def filter_noise(samples, low_cut=85, high_cut=115):
    # Only values outside the 'noise band' are kept as significant events
    filtered = []
    for s in samples:
        if s <= low_cut or s >= high_cut:
            filtered.append(s)
    return filtered

def compress_sequence(data):
    # Dummy compression: takes every 3rd element
    return data[::3]

def shift_phase(values, offset=2):
    # Circular shift by offset
    return values[-offset:] + values[:-offset]

def generate_baseline(size):
    # Irrelevant function - generates baseline that is never used
    return [90 + abs((i * 7) % 31) for i in range(size)]

def calculate_entropy(data):
    # Distractor: computes entropy but not used in final result
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)

def extract_peaks(signal):
    # Extract peaks (local maxima)
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i-1] < signal[i] > signal[i+1]:
            peaks.append(signal[i])
    return peaks

def smooth_data(data, window=3):
    # Moving average smoothing
    smoothed = []
    for i in range(len(data) - window + 1):
        avg = sum(data[i:i+window]) / window
        smoothed.append(int(avg))
    return smoothed

def classify_regimes(peaks):
    # Classify peak patterns into regimes (distractor logic)
    high_peaks = [p for p in peaks if p > 120]
    mid_peaks = [p for p in peaks if 100 <= p <= 120]
    if len(high_peaks) > len(mid_peaks):
        return 'turbulent'
    elif len(mid_peaks) > 0:
        return 'stable'
    else:
        return 'quiet'

def transform_signal(raw):
    # Key transformation: apply nonlinear enhancement
    transformed = []
    for x in raw:
        if x < 90:
            transformed.append(x * 1.5)
        elif x > 110:
            transformed.append(x * 0.8 + 10)
        else:
            transformed.append(x)
    return [int(val) for val in transformed]

def analyze_pattern(data, limit):
    # Core logic: count how many values exceed dynamic threshold
    base_ref = sum(data[:10]) // 10 if len(data) >= 10 else 100
    dynamic_threshold = base_ref + limit
    count = 0
    for val in data:
        if val > dynamic_threshold:
            count += 1
            if count > 50:  # early break condition
                break
    return count * 2  # final scaling

# --- Main execution with extensive irrelevant operations ---
raw_sensor_data = collect_samples(duration=5, rate=100)  # 500 samples

# Irrelevant preprocessing chain (dead-end paths)
decoy_baseline = generate_baseline(len(raw_sensor_data))
entropy_score = calculate_entropy(raw_sensor_data)  # Computed but unused
smoothed_raw = smooth_data(raw_sensor_data, window=4)

# Real signal path begins
filtered_data = filter_noise(raw_sensor_data, low_cut=88, high_cut=112)
compressed_data = compress_sequence(filtered_data)
shifted_data = shift_phase(compressed_data, offset=3)
refined_signal = extract_peaks(shifted_data)  # Used only to mislead

# Actual transformation branch
transformed_data = transform_signal(shifted_data)  # Critical input

# Decoy classification
regime_type = classify_regimes(refined_signal)  # Unused result

# Final diagnostic depends on transformed_data and threshold
threshold = len(refined_signal) + 15  # derived from peak count

# --- KEY STATEMENT ---
final_diagnostic = analyze_pattern(transformed_data, threshold)

# Additional red herring computations
fake_diagnostic = sum(transformed_data[i] for i in range(0, len(transformed_data), 5)) // 7
shadow_copy = transformed_data.copy()
shadow_copy.reverse()
offset_correction = math.isclose(sum(transformed_data[:5]), 450.0, abs_tol=20)

print(f"Result: {final_diagnostic}")