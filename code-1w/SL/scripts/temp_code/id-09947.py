import math

# Simulated sensor data processing with diagnostic analysis
def collect_readings():
    raw = [127, 255, 192, 64, 31, 88, 176]
    return [x ^ 42 for x in raw]  # Bitwise obfuscation (relevant)

def filter_anomalies(data, limit):
    # Irrelevant filtering path (dead code - not used later)
    return [x for x in data if x > limit]

def shift_window(sequence, offset=3):
    # Circular shift - distractor function
    return sequence[offset:] + sequence[:offset]

def compress_signal(signal):
    # Unused compression method (red herring)
    return [s & 127 for s in signal]

def decode_checksum(signal):
    # Decoy calculation: looks important but unused
    chk = 0
    for val in signal:
        chk = (chk + val) % 251
    return chk ^ 17

def generate_reference(size):
    # Generates Fibonacci-like reference sequence (partially relevant)
    ref = [1, 1]
    for i in range(2, size):
        ref.append((ref[-1] + ref[-2]) % 256)
    return ref

def align_sequences(primary, secondary):
    # Misleading alignment that isn't actually used in final computation
    aligned = []
    for a, b in zip(primary, secondary):
        aligned.append((a + b) % 256)
    return aligned

def transform_entry(val, key):
    # Core transformation: XOR with rotating key (relevant)
    return (val ^ key) + 1

def apply_transformation(data, seed):
    result = []
    for i, entry in enumerate(data):
        temp_val = transform_entry(entry, seed)
        if i % 2 == 0:
            temp_val = int(math.sqrt(temp_val * 4))  # Modify even indices
        else:
            temp_val = temp_val // 2  # Halve odd indices
        result.append(temp_val)
    return result

def count_peaks(series):
    # Distractor: counts peaks but not used in final answer
    peaks = 0
    for i in range(1, len(series) - 1):
        if series[i-1] < series[i] > series[i+1]:
            peaks += 1
    return peaks

def calculate_entropy(data):
    # Looks sophisticated but irrelevant to final result
    total = sum(data)
    probs = [d / total for d in data]
    entropy = -sum(p * math.log2(p) for p in probs if p > 0)
    return round(entropy, 3)

def analyze_pattern(dataset, cutoff):
    # Critical logic hidden among distractions
    adjusted = [x - 50 for x in dataset if x >= cutoff]
    base_sum = sum(adjusted)
    modifier = 0
    for idx, val in enumerate(adjusted):
        if val % 2 == 0:
            modifier += idx
        else:
            modifier -= (idx * 2)
    return base_sum + modifier

# Main execution flow
sensor_input = collect_readings()  # Step 1: Get obfuscated data

# Dead branches and decoy variables (distractions)
decoy_threshold = 100
anomalies_filtered = filter_anomalies(sensor_input, 200)  # Unused
reference_seq = generate_reference(len(sensor_input))  # Partially calculated but not used
shifted_data = shift_window(sensor_input, 2)  # Computed but discarded
compressed = compress_signal(shifted_data)  # Another dead end
checksum = decode_checksum(compressed)  # Looks critical, not used

# Real processing begins here
working_data = apply_transformation(sensor_input, seed=13)

# More distractions
peak_count = count_peaks(working_data)
entropy_metric = calculate_entropy(working_data)
fake_aligned = align_sequences(working_data, reference_seq)  # Not used

# Final threshold filter before analysis
effective_threshold = 45 if len(working_data) > 5 else 30

# Key statement
final_diagnostic = analyze_pattern(working_data, effective_threshold)

print(f"Result: {final_diagnostic}")