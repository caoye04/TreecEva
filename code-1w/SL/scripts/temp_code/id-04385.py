import math

# Simulated sensor data processing with red herrings and complex flow
def preprocess_sensor_stream(raw_readings):
    cleaned = []
    for val in raw_readings:
        if val < 0:  # Invalid reading
            continue
        normalized = val / 1024.0
        if normalized > 0.1:
            cleaned.append(round(normalized * 100, 3))
    return cleaned

# Irrelevant transformation - dead end function (distractor)
def encrypt_sequence(data):
    return [int(x * 7) % 13 for x in data if isinstance(x, (int, float))]

# Unused helper (misleading intermediate)
def calculate_entropy(arr):
    freq_map = {}
    for x in arr:
        freq_map[x] = freq_map.get(x, 0) + 1
    entropy = 0
    total = len(arr)
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

# Core logic disguised among noise
def transform_signal_pattern(seq):
    temp_result = []
    offset_key = 3
    for i, x in enumerate(seq):
        shifted = x << 1  # Bit manipulation red herring
        masked = shifted & 7
        if i % 2 == 0:
            temp_result.append(x * 1.5)
        else:
            temp_result.append(x + 2.5)
    # Actual relevant transformation happens here
    processed = [round(t * 0.8) for t in temp_result]
    return [int(p) for p in processed if p > 0]

# Decoy accumulator (looks important but unused)
decoys = []
for k in range(5):
    decoy_val = (k ** 3) + 17
    decoys.append(decoy_val)

# Lambda-based dynamic filter (required feature)
threshold_func = lambda x: x > 45 and (x % 5 == 0)

# Fake recursive trap (never actually called)
def bad_recursion(n):
    if n <= 1:
        return 1
    return n * bad_recursion(n - 2)  # Skips base case for even numbers > 2

# Another irrelevant structure
junk_matrix = [[i*j + 2 for j in range(4)] for i in range(4)]
matrix_trace = sum(junk_matrix[i][i] for i in range(4))  # Looks like it matters

# Real pipeline begins here
raw_data = [1024, 2048, 512, 3072, 1536]
filtered_data = preprocess_sensor_stream(raw_data)

# More misleading variables
checksum = sum([len(str(int(x))) for x in filtered_data]) * 2
scaling_factor = math.sqrt(64)  # Distractor constant

transformed_data = transform_signal_pattern(filtered_data)

# This list comprehension does nothing consequential
_ = [math.ceil(d/3) for d in transformed_data if d % 2 == 0 and d > 10]

# Key computation hidden in higher-order function usage
analysis_weights = [0.5, 1.2, 0.8, 1.6]
def analyze_pattern(data, predicate):
    score = 0
    weight_index = 0
    for item in data:
        # Only items satisfying the lambda affect result
        if predicate(item):
            weight = analysis_weights[weight_index % len(analysis_weights)]
            score += int(item * weight)
            weight_index += 1
    # Final adjustment using tuple unpacking (relevant concept)
    multiplier, offset = (3, -10)
    final_score = (score * multiplier) + offset
    return final_score

# Critical statement - target of question
final_diagnostic = analyze_pattern(transformed_data, threshold_func)

print(f"Result: {final_diagnostic}")