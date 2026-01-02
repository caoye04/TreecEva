def preprocess_signal(raw):
    # Irrelevant transformation (distractor)
    return [x * 1.5 + 2 for x in raw if x > 0]

def compute_entropy(seq):
    # Misleading function: looks important but unused in final result
    from math import log
    freq = {}
    for item in seq:
        freq[item] = freq.get(item, 0) + 1
    total = len(seq)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p, 2)
    return round(entropy, 4)

def shift_cipher(text, key):
    # Dead code path — never called
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + key) % 26 + base)
        else:
            result += char
    return result

def generate_primes(n):
    # Distractor: computes primes but not used in main logic
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return [i for i, prime in enumerate(sieve) if prime]

def filter_outliers(data, factor=1.5):
    # Real but indirectly related preprocessing
    sorted_data = sorted(data)
    q1 = sorted_data[len(sorted_data)//4]
    q3 = sorted_data[3*len(sorted_data)//4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    return [x for x in data if lower_bound <= x <= upper_bound]

def transform_sequence(seq):
    # Core relevant function with distractors inside
    temp_result = []
    running_xor = 0
    for i, val in enumerate(seq):
        shifted = val << 1
        flipped = shifted ^ i  # XOR with index
        if flipped & 1:  # Check if odd
            temp_result.append(flipped % 100)
        running_xor ^= flipped  # Accumulate for red herring
    # The actual output uses only a slice
    return temp_result[::2]  # Every other element

def analyze_pattern(arr, limit):
    # Critical function determining final answer
    count = 0
    total = 0
    for x in arr:
        if x < limit:
            count += 1
            total += x * 2
        else:
            total += x // 2
    # Final logic step: combine count and total with bitwise twist
    return (total + count) ^ 1337  # Key deterministic transformation

# --- Main Execution with Heavy Interference ---

# Irrelevant dataset initialization
noise_profile = [0.1, -0.5, 0.3, 0.0, -0.2]
dummy_labels = ['A', 'B', 'C']

# Unused recursive structure (misleads control flow understanding)
def recursive_trace(n):
    if n <= 1:
        return 1
    return n * recursive_trace(n - 2)

# Real input data (obscured among distractors)
sensor_readings = [12, 8, 15, 3, 9, 11, 7, 4]

# Apply irrelevant preprocessing (looks like filtering but unused)
cleaned = preprocess_signal(sensor_readings)

# Real processing begins here — but hard to isolate due to noise
filtered_data = filter_outliers(sensor_readings, factor=2.0)

# Transform using core logic
transformed_data = transform_sequence(filtered_data)

# Decoy operation: appears significant but unused
entropy_value = compute_entropy(filtered_data)

# Another red herring: prime-related logic with no impact
prime_offset = sum(generate_primes(20)[:3])  # 2 + 3 + 5 = 10, unused

# Threshold derived from string operations (real dependency)
diag_key = 'threshold_calib_XYZ'
thresh_str = ''.join([c for c in diag_key if c.isdigit()])
threshold = int(thresh_str) if thresh_str else 10  # No digits → default 10

# Key statement: where the final answer is computed
final_diagnostic = analyze_pattern(transformed_data, threshold)

# Output result as required
print(f"Target result: {final_diagnostic}")