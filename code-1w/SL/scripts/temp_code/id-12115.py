def analyze_pattern(seq):
    if len(seq) < 3:
        return 0
    count = 0
    for i in range(1, len(seq) - 1):
        if seq[i-1] < seq[i] > seq[i+1]:
            count += 1
    return count

# Irrelevant helper function (decoy)
def smooth_data(arr):
    if not arr:
        return []
    smoothed = [arr[0]]
    for i in range(1, len(arr)-1):
        smoothed.append((arr[i-1] + arr[i] + arr[i+1]) / 3)
    smoothed.append(arr[-1])
    return smoothed

# Distractor variables
temp_cache = [i**2 for i in range(10)]
dummy_flag = True
offset_value = 17
useless_threshold = 42.5

# Real data
raw_input = [3, 1, 4, 1, 5, 9, 2, 6, 5]
weights = [0.1, 0.3, 0.2, 0.1, 0.05, 0.05, 0.05, 0.05, 0.1]

# Misleading normalization (not used in final path)
normalized = [x / sum(raw_input) for x in raw_input]

# Another decoy: bit manipulation red herring
bit_encoded = 0
for x in raw_input:
    bit_encoded ^= (x << 2)

# Real signal extraction
filtered_data = [x for x in raw_input if x % 2 == 1]

# Secondary distractor: unused recursion
def recursive_sum(n):
    return n + recursive_sum(n-1) if n > 0 else 0

# Unused lambda (distractor)
transform_fn = lambda x: x * 2 + 1

# Key processing function
def process_results(data, w):
    total = 0.0
    # Emphasize peaks in data using weighted differences
    peaks = analyze_pattern(data)
    
    # Distractor loop with no effect on output
    temp_result = 0
    for j in range(peaks):
        temp_result += offset_value // (j + 1)
    
    # Actual computation starts here
    weighted_sum = sum(d * w[i] for i, d in enumerate(data))
    
    # Simulate confidence adjustment based on pattern complexity
    adjustment_factor = 1.0
    if peaks > 2:
        adjustment_factor = 1.2
    elif peaks == 2:
        adjustment_factor = 1.1
    
    intermediate = weighted_sum * adjustment_factor
    
    # Apply non-linear correction only if certain values exist
    if any(x > 8 for x in data):
        intermediate = intermediate ** 1.1
    
    # Decoy string operation (irrelevant)
    status_msg = ''.join([chr(97 + (i % 26)) for i in range(peaks)])
    
    # Real final transformation
    final_scalar = len(data) / (sum(w) * 10)
    result = intermediate * final_scalar
    
    # Dead code branch (never reached due to logic)
    if dummy_flag and False:
        result -= useless_threshold
    
    return round(result, 6)

# Core execution path
data = [x * 2 for x in raw_input]  # Amplify signal

# Another distraction: zip and enumerate misuse
enumerated_pairs = list(enumerate(zip(raw_input, normalized)))

# Critical statement
final_score = process_results(data, weights)

print(f"Result: {final_score}")