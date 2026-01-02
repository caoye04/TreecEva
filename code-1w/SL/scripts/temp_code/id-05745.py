def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if abs(x) > 0.1]
    normalized = [round(x / max(filtered), 3) for x in filtered]
    return normalized

# Irrelevant signal processing functions (distractor)
def fft_approx(data):
    result = []
    for i in range(len(data)):
        temp = 0
        for j in range(len(data)):
            temp += data[j] * (1 if (i*j) % 2 == 0 else -1)
        result.append(temp)
    return result

def calculate_entropy(seq):
    from math import log2
    freq = {}
    for item in seq:
        freq[item] = freq.get(item, 0) + 1
    total = len(seq)
    entropy = -sum((count/total) * log2(count/total) for count in freq.values())
    return round(entropy, 3)

# Core logic disguised among distractions
def generate_pattern(n):
    sequence = [1, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])  # Fibonacci-like
    return sequence[:n]

def apply_mask(data, mask_type='xor'):
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    masked = []
    for i, val in enumerate(data):
        if mask_type == 'xor':
            masked.append(val ^ primes[i % len(primes)] if isinstance(val, int) else int(val*10) ^ primes[i % len(primes)])
        else:
            masked.append(val % 5)
    return masked

def validate_integrity(check_data):
    # Complex validation with red herring logic
    if len(check_data) < 10:
        return False
    checksum = sum(1 << (i % 4) for i in check_data if i > 0) % 100
    parity = sum(1 for x in check_data if x % 2 == 0)
    return checksum > 10 and parity > len(check_data) // 3

def transform_metadata(meta_config):
    # Unused but complex function (dead code path)
    keys = list(meta_config.keys())
    values = list(meta_config.values())
    rotated = [v ^ 3 for v in values]
    return dict(zip(keys, rotated))

def analyze_sequence(data):
    # Key analysis with subtle arithmetic
    base_score = sum(data[i] * (i+1) for i in range(len(data)) if i % 2 == 0)
    adjustment = 0
    for i in range(1, len(data), 2):
        if data[i] in {2, 3, 5, 7, 11}:  # Prime check as distraction
            adjustment += 1
        elif data[i] % 2 == 0:
            adjustment -= 2
    # Critical calculation hidden in logic
    trend = sum(1 for i in range(1, len(data)) if data[i] > data[i-1])
    volatility = sum(abs(data[i] - data[i-1]) for i in range(1, len(data)))
    final_score = base_score + adjustment + (trend - volatility//10)
    return final_score

# Simulated sensor input (meaningful initial data)
sensor_readings = [120, 85, 60, 100, 45, 90, 110, 70, 55, 80]

# Irrelevant string processing (distractor using string methods)
diagnostic_log = "ERR_01:CAL_OVR;WARN_05:SEN_RST;INFO_12:FLOW_NORM"
log_entries = diagnostic_log.split(';')
severity_codes = {entry.split(':')[0].split('_')[0] for entry in log_entries}
clearance_flag = ''.join([code[0] for code in sorted(severity_codes)]).lower()

# Data transformation chain
processed = preprocess_signal([s/100.0 for s in sensor_readings])
pattern_hint = generate_pattern(10)
masked_diagnostics = apply_mask(pattern_hint, 'xor')  # Used later

# Set of unique values (set operation used)
unique_masked = set(masked_diagnostics)

# More distractions
config_params = {'mode': 77, 'level': 88, 'status': 99}
transformed_config = transform_metadata(config_params)

# Core assignment - critical execution point
transformed_data = [masked_diagnostics[i] + (i % 4) for i in range(len(masked_diagnostics))]

# Final computation - key statement
final_diagnostic = analyze_sequence(transformed_data)

# Output result
print(f"Result: {final_diagnostic}")