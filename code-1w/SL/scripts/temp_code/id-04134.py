def analyze_component(reading, threshold=75):
    """Irrelevant analysis function (dead code path)."""
    if reading > threshold:
        return reading * 0.9
    else:
        return reading + 10

# Unused data structures (distractors)
diagnostic_logs = [101, 203, 155, 99, 87, 210]
error_flags = {101, 155, 900}
system_state = {'active': True, 'mode': 'debug', 'level': 3}

# Core computation variables
def process_metrics(data_stream):
    filtered = [x for x in data_stream if x % 2 == 1]  # Keep odd values only
    adjusted = [x * 2 if x < 50 else x // 3 for x in filtered]
    return adjusted

base_weights = [3, 1, 4, 1, 5]
bias_correction = sum([w ** 2 for w in base_weights]) // 5

# Bit manipulation decoy
obfuscation_key = 237
scrambled = obfuscation_key ^ 184  # Result: 101, irrelevant
mask = (1 << 5) - 1
masked_value = scrambled & mask  # 5, unused

# Main dataset
raw_input = [12, 63, 44, 81, 27, 96, 39]
temp_buffer = [x for x in raw_input if x > 30]  # Filtering distractor

# Conditional transformation chain
transformed = []
for val in raw_input:
    if val < 40:
        transformed.append(val * 3)
    elif val % 3 == 0:
        transformed.append(val + 17)
    else:
        transformed.append(val)

# Set operations with red herring
unique_transformed = set(transformed)
even_caps = {x for x in unique_transformed if x % 2 == 0}

# Critical data for evaluation
metric_set = [63, 27, 39, 81]
benchmark_data = {
    'baseline': [21, 9, 13, 27],
    'tolerance': 4,
    'scale': 2.5
}

# Decoy function using sets and string operations
def validate_integrity(checksum_str):
    parts = checksum_str.split('-')
    code_set = set(parts[0])
    ref_set = set('abc123')
    return len(code_set & ref_set) >= 3

# Unused recursive distraction
def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

fib_sequence = [fibonacci(i) for i in range(8)]  # [0,1,1,2,3,5,8,13]
fib_sum = sum(fib_sequence)  # 27, misleading intermediate

# Key logic begins here
def evaluate_performance(metrics, config):
    base = process_metrics(metrics)  # [63->21, 27->9, 39->13, 81->27] -> [21,9,13,27]
    target = config['baseline']  # [21,9,13,27]
    
    # Direct comparison
    match_count = 0
    for i in range(len(base)):
        if abs(base[i] - target[i]) <= config['tolerance']:
            match_count += 1
    
    # Scoring mechanism
    raw_score = match_count * 100
    scaled_score = raw_score * config['scale']  # 400 * 2.5 = 1000
    penalty = len(even_caps) * 10  # even_caps has 2 elements? Let's check: transformed=[36,21,?,81+17=98,9,117,39*3=117] → transformed=[36,21,98,98,9,117,117]; evens={36,98} → size=2 → penalty=20
    final = scaled_score - penalty  # 1000 - 20 = 980
    
    # Dead branch (never taken due to logic)
    if system_state['level'] > 5:
        final += 50
        
    return final

# Execution point of interest
final_score = evaluate_performance(metric_set, benchmark_data)
print(f"Target result: {final_score}")