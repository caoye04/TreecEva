import itertools

# Simulated sensor data with noise and metadata
raw_sensor_readings = [23.7, 19.1, 25.3, 20.0, 22.5, 18.9, 24.8, 21.2]
metadata_flags = [0b1010, 0b1100, 0b0110, 0b1111, 0b0001, 0b1001, 0b0101, 0b1110]

def apply_noise_filter(data):
    # Irrelevant preprocessing: applies gain but not used later
    amplified = [x * 1.05 for x in data]
    filtered = [x for x in amplified if x > 20.0]  # Discarded path
    return amplified  # Amplified returned but only partially used

def extract_valid_windows(data, window_size=3):
    # Generate sliding windows (used)
    windows = []
    for i in range(len(data) - window_size + 1):
        windows.append(data[i:i + window_size])
    return windows

def calculate_entropy(vector):
    # Unused distractor function
    from math import log2
    total = sum(vector)
    if total == 0:
        return 0
    probs = [v / total for v in vector]
    return -sum(p * log2(p) for p in probs if p > 0)

def transform_signal(signal_batch):
    # Mix of relevant and irrelevant operations
    processed = []
    temp_accuracies = []  # Dead variable collection
    
    for batch in signal_batch:
        shifted = [(int(x) << 1) ^ 0b1101 for x in batch]  # Bit manipulation
        summed = sum(shifted) % 100
        temp_accuracies.append(summed / len(shifted))  # Collected but unused
        processed.append(summed)
    
    # Distractor: complex but unused transformation
    accuracy_score = sum(temp_accuracies) / len(temp_accuracies) if temp_accuracies else 0
    normalized_accuracy = round(accuracy_score * 100, 2)  # Never used
    
    return processed

def merge_with_metadata(checksums, flags):
    # Combines checksums with flag bits via XOR folding
    result = 0
    for cs, fl in zip(checksums, flags):
        result ^= (cs + (fl & 0b0101))  # Only uses subset of flag bits
    return result

def compute_checksum(data_list):
    base = 0
    for val in data_list:
        base = (base * 31 + val) % 999999
    return base if base != 0 else 999999

# Irrelevant auxiliary computation block (dead path)
def analyze_pattern_periodicity(seq):
    periods = []
    for p in range(1, min(5, len(seq))):
        if all(seq[i] == seq[i % p] for i in range(len(seq))):
            periods.append(p)
    return periods  # Not used anywhere

# Real processing pipeline
filtered_readings = apply_noise_filter(raw_sensor_readings)

# Extract 3-element windows from original data (key step)
data_windows = extract_valid_windows(raw_sensor_readings, 3)

# Transform each window through bit operations
transformed_batches = transform_signal(data_windows)

# Merge transformed results with metadata flags
partial_digest = merge_with_metadata(transformed_batches, metadata_flags[:6])  # Truncate to match

# Apply final hash chain
staged_sequence = [partial_digest]
for _ in range(5):
    staged_sequence.append((staged_sequence[-1] * 7 + 3) % 50000)

# Secondary transformation using itertools (required feature)
rolled = list(itertools.accumulate(staged_sequence, lambda a, b: (a + b * 2) % 10000))

# Final checksum computed from rolled sequence
final_checksum = compute_checksum(rolled)

# Red herring: unused statistical analysis
mean_roll = sum(rolled) / len(rolled)
variance_roll = sum((x - mean_roll) ** 2 for x in rolled) / len(rolled)
skew_hint = (sum((x - mean_roll)**3 for x in rolled)/len(rolled)) / (variance_roll + 1e-8)**1.5  # Unused

# Target result output
print(f"Result: {final_checksum}")