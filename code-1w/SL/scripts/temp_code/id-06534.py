import math

# Irrelevant helper function (decoy)
def normalize_vector(v):
    norm = sum(x ** 2 for x in v) ** 0.5
    return [x / norm for x in v] if norm else v

# Another red herring function
def analyze_distribution(arr):
    mean = sum(arr) / len(arr)
    variance = sum((x - mean) ** 2 for x in arr) / len(arr)
    return {'mean': mean, 'variance': variance}

# Core logic disguised among distractions
def transform_sequence(seq):
    # Distractor: unused intermediate
    temp_buffer = [x * 1.5 for x in seq if x % 2 == 0]
    processed = []
    for i, val in enumerate(seq):
        if val < 0:
            processed.append(abs(val))
        elif val % 3 == 0 and val > 0:
            processed.append(int(math.sqrt(val)))
        else:
            processed.append(val + i)
    return processed

# Misleading aggregation function (never called)
def compute_entropy(data):
    freq_map = {}
    for item in data:
        freq_map[item] = freq_map.get(item, 0) + 1
    probabilities = [f / len(data) for f in freq_map.values()]
    return -sum(p * math.log2(p) for p in probabilities)

# Data obfuscation through string encoding (irrelevant path)
encoded_metadata = "72:101:108:108:111"  # ASCII for "Hello"
decoded_tag = ''.join(chr(int(c)) for c in encoded_metadata.split(':'))

# Simulated sensor readings with noise
raw_readings = [12, -5, 18, 27, 36, 41, 3, 9]

# Apply transformation (relevant)
cleaned_readings = transform_sequence(raw_readings)

# Dead code branch (distractor)
if len(cleaned_readings) > 20:
    cleaned_readings = normalize_vector(cleaned_readings)

# Real processing begins here
shifted_data = [x + 5 for x in cleaned_readings if isinstance(x, int)]

# Filtering with list comprehension and string method decoy
disallowed_chars = "36"
filter_threshold = 10
filtered_data = [x for x in shifted_data if str(x).find(disallowed_chars) == -1 and x > filter_threshold]

# Decoy set operation
unique_backup = set(filtered_data)
unique_backup.add(999)
unique_backup.discard(999)

# Actual accumulation logic
running_total = 0
for index, value in enumerate(filtered_data):
    if index % 2 == 0:
        running_total += value * 2
    else:
        running_total -= value // 2

# Secondary accumulator (distraction)
temp_sum = sum(x for x in filtered_data if x < 50)

# Bit manipulation red herring
bit_fiddled = 0
for x in filtered_data:
    bit_fiddled ^= (x << 1) | 1

# Main scoring function
def calculate_final_score(input_list):
    base = sum(input_list)
    bonus = len([x for x in input_list if x > 20]) * 3
    penalty = len([x for x in input_list if x < 15]) * 2
    return int(base + bonus - penalty)

# Critical assignment
final_score = calculate_final_score(filtered_data)

# Print result as required
print(f"Result: {final_score}")