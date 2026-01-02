import itertools

# Simulated sensor data preprocessing with interference
raw_readings = [127, 255, 83, 191, 45, 63, 211, 143]

def apply_mask(x):
    return x & 0x7F

def amplify_signal(x):
    return (x * 3) % 256

def is_stable(x):
    return 50 < x < 200

def compute_checksum(seq):
    # Irrelevant function - not used in main logic
    return sum(seq) % 256

def generate_pairs(data):
    # Dead code path - never called
    return list(itertools.combinations(data, 2))

def filter_outliers(stream):
    # Distractor: complex-looking but unused
    return [x for x in stream if x % 2 == 1 and x > 30]

def shift_window(arr, offset=1):
    # Misleading transformation
    return arr[offset:] + arr[:offset]

def accumulate_with_noise(values):
    # Unused accumulator with red herring logic
    acc = 0
    result = []
    for v in values:
        acc = (acc + v + 7) % 100
        result.append(acc)
    return result

def extract_features(data):
    # Relevant: applies bit mask and amplification
    masked = [apply_mask(x) for x in data]
    amplified = [amplify_signal(x) for x in masked]
    return amplified

def partition_stream(seq):
    # Splits into two streams - only one branch is relevant
    low_band = [x for x in seq if x < 128]
    high_band = [x for x in seq if x >= 128]  # This is ignored
    return low_band

def time_align(sequence):
    # Realignment that affects final input
    reversed_seq = list(reversed(sequence))
    shifted = shift_window(reversed_seq, 2)  # Uses distractor function
    return shifted

def evaluate_peaks(data):
    # Complex peak detection - unused
    peaks = []
    for i in range(1, len(data)-1):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            peaks.append(i)
    return peaks

def normalize_range(x):
    # Used in final processing
    return max(1, min(x, 250)) // 2

def transform_entry(val):
    # Critical transformation step
    if val % 3 == 0:
        return val // 3
    elif val % 3 == 1:
        return (val + 2) // 3
    else:
        return (val + 1) // 3

def process_sequence(seq):
    # Core logic hidden among distractions
    modified = [transform_entry(normalize_range(x)) for x in seq]
    total = sum(modified)
    count = len([x for x in modified if x > 5])  # Conditional count
    return total - count * 2

# Irrelevant global variables
MAX_BUFFER_SIZE = 1024
current_index = 0
temp_cache = set()
log_entries = []
error_flag = False

# Decoy operations
buffer_pool = [0] * MAX_BUFFER_SIZE
for i in range(0, len(buffer_pool), 128):
    buffer_pool[i] = 1

# Main data flow chain
step1 = extract_features(raw_readings)
step2 = partition_stream(step1)
step3 = time_align(step2)

# Transform entry point
transformed_data = []
for item in step3:
    transformed_data.append(item + 5)  # Final adjustment

# Red herring loop
aggregate_score = 0
for reading in raw_readings:
    if reading > 200:
        aggregate_score += 1
    else:
        aggregate_score -= 1

# Unused statistical analysis
mean_val = sum(step3) / len(step3) if step3 else 0
deviations = [abs(x - mean_val) for x in step3]

# Key statement
final_output = process_sequence(transformed_data)

# Output result
print(f"Result: {final_output}")