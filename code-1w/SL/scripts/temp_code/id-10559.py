def preprocess_signal(data):
    # Irrelevant transformation (dead code path)
    normalized = [x / max(data) for x in data]
    filtered = [x for x in data if x > sum(data) / len(data)]
    return filtered

# Sensor readings from three channels
temp_readings = [23, 18, 31, 44, 27, 19, 36]
humidity_readings = [44, 51, 33, 22, 61, 49, 37]
pressure_readings = [1013, 1008, 1015, 1022, 1010, 1005, 1018]

# Misleading intermediate calculation (not used in final result)
avg_temp = sum(temp_readings) / len(temp_readings)
avg_humidity = sum(humidity_readings) / len(humidity_readings)
deviations = [abs(t - avg_temp) for t in temp_readings]

# Construct composite signal using XOR of indices and values (relevant)
signal_core = []
for i in range(len(temp_readings)):
    val = temp_readings[i] ^ humidity_readings[i]
    val = val ^ (pressure_readings[i] % 29)  # Modulated by prime
    signal_core.append(val)

# Dead-end transformation: statistical analysis (distractor)
mean_signal = sum(signal_core) / len(signal_core)
variance = sum((x - mean_signal) ** 2 for x in signal_core) / len(signal_core)
std_dev = variance ** 0.5

# Key processing: extract pattern signatures via bit counting and set logic
signature_sequence = []
for x in signal_core:
    binary_rep = bin(x)[2:]  # Remove '0b'
    ones_count = binary_rep.count('1')
    zeros_count = binary_rep.count('0')
    parity_flag = ones_count % 2
    # Use set difference to filter noise
    bit_set = set(binary_rep)
    control_set = {'0', '1'}
    if len(bit_set.symmetric_difference(control_set)) == 0:
        signature_sequence.append(ones_count * parity_flag + zeros_count // 2)

# Another red herring: unused recursive function
def calculate_entropy(seq, depth=0):
    if depth >= 3 or len(seq) == 0:
        return 0
    mid = len(seq) // 2
    left = seq[:mid]
    right = seq[mid+1:]
    return seq[mid] / (depth + 1) + calculate_entropy(left, depth+1)

entropy_estimate = calculate_entropy(temp_readings)  # Not used

# Real computation path begins: analyze repeating patterns
observed_counts = {}
for val in signature_sequence:
    observed_counts[val] = observed_counts.get(val, 0) + 1

frequent_values = {k for k, v in observed_counts.items() if v > 1}

# Apply secondary transformation based on combinatorics of frequent elements
combinatoric_weight = 0
for i in frequent_values:
    for j in frequent_values:
        if i < j:
            combinatoric_weight += (i + j) * abs(i - j)

# Decoy list comprehension with string manipulation (irrelevant)
ascii_fragments = [chr(97 + (x % 26)) for x in pressure_readings if x % 3 == 0]
concatenated = ''.join(ascii_fragments)
char_frequency = {c: concatenated.count(c) for c in set(concatenated)}

# Core diagnostic logic
def analyze_pattern(seq):
    if not seq:
        return -1
    base_score = sum(seq) // len(seq)
    unique_elements = set(seq)
    adjustment = len(unique_elements.intersection({x for x in range(1, 10) if x % 3 == 0}))
    # Final adjustment using min/max heuristic
    if len(unique_elements) > 1:
        spread = max(unique_elements) - min(unique_elements)
        adjustment *= (spread % 4)
    return base_score * 10 + adjustment

final_diagnostic = analyze_pattern(signature_sequence)
print(f"Target result: {final_diagnostic}")