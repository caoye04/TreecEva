def preprocess_input(raw_data):
    # Irrelevant transformation chain (distractor)
    temp_caps = [c.upper() for c in raw_data if c.isalpha()]
    shifted = ''.join([chr((ord(c) - ord('A') + 3) % 26 + ord('A')) for c in temp_caps])
    token_count = len(shifted.split('X'))  # Dead computation

    # Core preprocessing
    cleaned = ''.join(filter(str.isdigit, raw_data))
    digits = [int(d) for d in cleaned]
    return digits


def generate_sequence(n):
    # Misleading Fibonacci-like sequence (unused)
    seq = [0, 1]
    for i in range(2, n + 5):
        seq.append(seq[-1] + seq[-2])
    return seq


def extract_features(values):
    # Distractor: complex feature engineering that's not used
    avg = sum(values) / len(values) if values else 0
    variance = sum((x - avg) ** 2 for x in values) / len(values) if values else 0
    peaks = [i for i in range(1, len(values)-1) if values[i] > values[i-1] and values[i] > values[i+1]]
    
    # Actual needed result: product of even-indexed elements
    product = 1
    for i in range(0, len(values), 2):
        product *= values[i]
    return product


def decode_signal(pattern):
    # Bit manipulation red herring
    result = 0
    for p in pattern:
        result ^= p  # XOR chain
        result = (result << 1) & 0b11111  # Shift and mask
    
    # Real task: count occurrences of digit 7 in binary form of sum
    binary_sum = bin(sum(pattern)).count('1')
    return binary_sum


def validate_integrity(signal):
    # Checksum distraction
    checksum = 0
    for i, val in enumerate(signal):
        checksum += val * (i + 1)
    verified = (checksum % 17 == 0)
    
    # Unused recursive function (decoy)
    def recurse_check(n):
        if n <= 1:
            return n
        return recurse_check(n-1) + recurse_check(n-2)
    
    return True  # Always passes


def process_noise_data(noise):
    # Linear search for non-existent pattern
    index = -1
    for i in range(len(noise) - 2):
        if noise[i] == 9 and noise[i+1] == 1 and noise[i+2] == 1:
            index = i
            break
    # Return length as a fake metric
    return len(noise) + 100


def aggregate_metrics(signals):
    # Enumerate and zip distractor
    indices = list(enumerate(signals))
    paired = list(zip(signals, [x*2 for x in signals]))
    total = sum(a * b for a, b in paired)
    
    # Actual logic: sum of squares of odd numbers only
    sos = sum(x**2 for x in signals if x % 2 == 1)
    return sos


def analyze_readings(data_list):
    base_score = 0
    for item in data_list:
        if isinstance(item, list):
            base_score += sum(item)
        elif item > 5:
            base_score += item * 2
        else:
            base_score += item
    return base_score + 1337

# Main execution with multiple distractions
raw_input = "Sensor@Log:ID=7849|Readings:[3,7,2,9,1]#Calib:XOR7"

# Distraction block 1: unused signal generation
sequence_data = generate_sequence(10)
signal_matrix = [[i+j for j in range(5)] for i in sequence_data[:5]]

# Distraction block 2: irrelevant string analysis
char_freq = {}
for c in raw_input:
    if c in char_freq:
        char_freq[c] += 1
    else:
        char_freq[c] = 1
duplicate_chars = [k for k, v in char_freq.items() if v > 1]

# Core processing pipeline
digits_only = preprocess_input(raw_input)  # Extracts [7,8,4,9]
feature_product = extract_features(digits_only)  # 7 * 4 = 28
signal_code = decode_signal(digits_only)  # bin(7+8+4+9)=bin(28)='11100' -> count('1')=3

# Multiple validation layers (mostly irrelevant)
is_valid = validate_integrity(digits_only)
noise_level = process_noise_data(digits_only)
aggregated = aggregate_metrics(digits_only)  # 7² + 9² = 49 + 81 = 130

# Construct processed signals (key intermediate structure)
processed_signals = [
    [feature_product],           # [28]
    [signal_code, noise_level],   # [3, 104] (noise_level = 4 + 100)
    [aggregated],                 # [130]
    digits_only                   # [7,8,4,9]
]

# Final diagnostic calculation
final_diagnostic = analyze_readings(processed_signals)

# Output result
print(f"Result: {final_diagnostic}")