from collections import defaultdict, Counter
import math

# Simulated sensor data processing pipeline with red herrings
def fetch_raw_signals():
    return [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8]

def apply_noise_filter(signal):
    # Real operation: smooth out noise using median filter (relevant)
    filtered = []
    for i in range(1, len(signal) - 1):
        window = sorted(signal[i-1:i+2])
        filtered.append(window[1])
    return filtered

def compute_entropy(data):
    # Irrelevant distractor function - never used but looks important
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def validate_checksum(sequence):
    # Distractor: looks critical but unused in main flow
    return sum(sequence) % 7 == 0

def legacy_transform(seq):
    # Dead code path — looks like it might be used
    return [x << 1 for x in seq if x % 2 == 0]

def generate_frequency_map(data):
    # Looks useful, but actually just a red herring
    freq_map = defaultdict(int)
    for item in data:
        freq_map[item] += 1
    return dict(freq_map)

def encrypt_sequence(seq, key=3):
    # Misleading cryptographic distraction
    return [(x + key) * 2 for x in seq]

def decrypt_sequence(seq, key=3):
    # Unused counterpart to encryption — adds confusion
    return [x // 2 - key for x in seq]

def extract_peaks_and_valleys(series):
    # Intermediate transformation that IS used
    extrema = []
    for i in range(1, len(series) - 1):
        if (series[i] > series[i-1] and series[i] > series[i+1]) or \
           (series[i] < series[i-1] and series[i] < series[i+1]):
            extrema.append(series[i])
    return extrema

def rotate_left(arr, n):
    # Bit manipulation distractor
    if not arr:
        return arr
    n = n % len(arr)
    return arr[n:] + arr[:n]

def bit_interleave(a, b):
    # Complex-looking but unused bitwise operation
    result = 0
    for i in range(max(a.bit_length(), b.bit_length())):
        result |= ((a >> i) & 1) << (2 * i)
        result |= ((b >> i) & 1) << (2 * i + 1)
    return result

def aggregate_by_triplets(data):
    # Unused aggregation method — plausible but irrelevant
    groups = [data[i:i+3] for i in range(0, len(data), 3)]
    averages = [sum(g) // len(g) for g in groups if g]
    return averages

def analyze_pattern(data, settings):
    # Core logic buried among distractions
    threshold = settings['threshold']
    mode = settings['mode']
    
    # Step 1: Filter spikes
    cleaned = [x for x in data if x <= threshold]
    
    # Step 2: Detect oscillation frequency
    changes = 0
    for i in range(1, len(cleaned)):
        if (cleaned[i] - cleaned[i-1]) != 0:
            changes += 1
    
    # Step 3: Apply mode-based transformation
    if mode == 'aggressive':
        processed = [x ** 2 for x in cleaned]
    else:
        processed = [x * 2 for x in cleaned]
    
    # Step 4: Count transitions above base
    base = settings.get('base', 5)
    above_base = sum(1 for x in processed if x > base)
    
    # Step 5: Final diagnostic score based on transitions and length
    diagnostic_score = (above_base * len(processed)) - sum(processed) // max(len(processed), 1)
    
    return diagnostic_score

def main():
    # Orchestration with multiple decoys
    raw_stream = fetch_raw_signals()
    
    # Real processing chain
    filtered_data = apply_noise_filter(raw_stream)
    peak_valley_points = extract_peaks_and_valleys(filtered_data)
    transformed_data = rotate_left(peak_valley_points, 2)  # Actual input source
    
    # Irrelevant computations — look active but don't affect result
    _ = generate_frequency_map(raw_stream)
    _ = encrypt_sequence(raw_stream, key=7)
    _ = aggregate_by_triplets(filtered_data)
    _ = bit_interleave(12, 25)
    
    # Configuration with misleading keys
    config = {
        'threshold': 7,
        'mode': 'normal',
        'base': 5,
        'debug_mode': True,
        'buffer_size': 1024,
        'checksum_enabled': False
    }
    
    # Critical execution point
    final_diagnostic = analyze_pattern(transformed_data, config)
    
    # Print required output
    print(f"Target result: {final_diagnostic}")

if __name__ == "__main__":
    main()