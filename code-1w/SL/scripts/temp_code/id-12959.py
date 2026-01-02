import math

# Simulate a signal processing pipeline with distractions
def generate_noise(length, seed=42):
    # Irrelevant function: generates unused noise
    result = []
    val = seed
    for i in range(length):
        val = (val * 937) % 101
        result.append(val)
    return result

def deprecated_filter(data):
    # Dead code path - never called
    return [x for x in data if x > 5]

def auxiliary_transform(x):
    # Distractor function: used only on decoy data
    if x % 3 == 0:
        return x ** 2
    else:
        return x + 7

# Real computation begins
raw_measurements = [12, 18, 27, 36, 45, 54, 63, 72]
offset = 3
scaled_data = [x - offset for x in raw_measurements]  # Step 1: adjust baseline

# Bit manipulation red herring
bit_flags = 0b1010
flagged = [(x << 2) ^ bit_flags for x in scaled_data]  # Irrelevant transformation

# Core signal feature extraction
def extract_features(data):
    features = []
    for x in data:
        if x % 9 == 0:  # meaningful filter
            root = math.isqrt(x)
            parity = 1 if (root % 2) == 0 else 0
            features.append(root + parity)
    return features  # returns [4, 6, 6, 8] for scaled_data

features = extract_features(scaled_data)

# Decoy data structure with misleading stats
historical_stats = {
    'avg': 42.5,
    'peak': 987,
    'count': 1200,
    'version': 'legacy_v2'
}

# Unused recursive distraction
def calc_recursive_depth(n):
    if n <= 1:
        return 1
    return calc_recursive_depth(n - 2) + calc_recursive_depth(n - 3)

# Data transformation chain
transformation_key = 'T9X'
key_shift = sum([ord(c) for c in transformation_key]) % 8  # 116 % 8 = 4

transformed_data = [x + key_shift for x in features]  # [8, 10, 10, 12]

# Threshold logic with short-circuit distraction
decoy_condition = (len(historical_stats) > 10 and historical_stats['peak'] < 0) or False
threshold_base = 9
adjustment = -1 if (key_shift & 1) else 1  # key_shift=4 -> even -> adjustment=1
threshold = threshold_base + adjustment  # 10

# Main processing function
def process_signal(signal_list, limit):
    output = 0
    temp_cache = []
    for val in signal_list:
        # Simulate early break condition that doesn't trigger
        if val < 0:
            break
        if val >= limit:  # trigger on 10,10,12
            temp_cache.append(val * 2)
        else:
            temp_cache.append(val // 2)
    # Only this part matters
    for cached in temp_cache:
        if cached % 4 == 0:  # divisible by 4
            output += cached
    return output  # receives [4, 20, 20, 24] -> add 20,20,24 => 64

# Critical execution point
final_output = process_signal(transformed_data, threshold)

# Print required result
print(f"Target result: {final_output}")