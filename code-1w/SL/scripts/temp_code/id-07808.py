import itertools

# Sensor simulation and diagnostic system with extensive red herrings

def generate_noise(length):
    return [i % 7 for i in range(length)]

def filter_outliers(data, threshold=5):
    return [x for x in data if x <= threshold]

def accumulate(data):
    result = []
    total = 0
    for x in data:
        total += x
        result.append(total)
    return result

def shift_window(data, offset=1):
    return data[offset:] + data[:offset]

def compute_entropy(data):
    from math import log2
    freq = {}
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    entropy = 0
    n = len(data)
    for count in freq.values():
        p = count / n
        entropy -= p * log2(p)
    return round(entropy, 6)

def dummy_analysis_1(logs):
    # Irrelevant function: computes character frequency in string representations
    logs_str = ''.join(map(str, logs))
    char_count = {}
    for c in logs_str:
        char_count[c] = char_count.get(c, 0) + 1
    return sum(char_count.values())

def dummy_analysis_2(logs):
    # Irrelevant function: performs bit manipulation not used in final result
    masked = 0
    for x in logs:
        masked ^= (x << 2) & 0xFF
    return bin(masked)

def extract_peaks(data):
    peaks = []
    for i in range(1, len(data)-1):
        if data[i-1] < data[i] > data[i+1]:
            peaks.append(data[i])
    return peaks or [0]

def smooth_signal(data):
    if len(data) < 3:
        return data
    smoothed = [data[0]]
    for i in range(1, len(data)-1):
        smoothed.append(sum(data[i-1:i+2]) // 3)
    smoothed.append(data[-1])
    return smoothed

def validate_checksum(sequence):
    # Unused validation path
    return sum(sequence) % 11 == 0

def critical_phase_detection(readings):
    # Real logic buried among distractions
    derived = [x * 2 + 1 for x in readings if x % 3 != 0]
    shifted = shift_window(derived, 2)
    accumulated = accumulate(shifted)
    filtered = filter_outliers(accumulated)
    return filtered[-1] if filtered else 0

def analyze_readings(logs):
    # Key processing pipeline
    base_log = [x for x in logs if x > 0]
    
    # Distractor: multiple unused transformations
    noise = generate_noise(len(base_log))
    mixed = [a ^ b for a, b in zip(base_log, itertools.cycle(noise))]
    dummy_1 = dummy_analysis_1(mixed)
    dummy_2 = dummy_analysis_2(mixed)
    
    # More red herrings
    peak_values = extract_peaks(mixed)
    smoothed_data = smooth_signal(mixed)
    entropy_value = compute_entropy(smoothed_data)
    
    # Actual relevant chain starts here
    processed = [x for x in mixed if x % 2 == 1]  # Keep only odd numbers
    processed = [x + 1 for x in processed]         # Increment each
    processed = accumulate(processed)             # Cumulative sum
    
    # Dead branch - looks important but unused
    if len(processed) > 10:
        processed = processed[::2]
    
    # Critical phase detection on original pattern
    phantom_diagnostic = critical_phase_detection(base_log)
    
    # Final computation - depends only on processed[-1] and fixed offset
    final_score = processed[-1] if processed else 0
    calibration = 349
    final_diagnostic = final_score - calibration
    
    # This print is required to expose the variable
    print(f"Target result: {final_diagnostic}")
    
    return final_diagnostic

# Simulated sensor input - deterministic
raw_input = [3, -1, 4, 1, 5, -2, 9, 2, 6, 5, 3, 5, 8, -3, 9, 7, 9, 3, 2, 3]
processed_logs = [x * 2 for x in raw_input if x != -1 and x != -2 and x != -3]
final_diagnostic = analyze_readings(processed_logs)