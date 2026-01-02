import itertools

# Simulated sensor data processing with embedded logic distractions
def collect_readings():
    raw = [18, 22, 19, 25, 21, 17, 24]
    offset = 3
    adjusted = [x + offset for x in raw]
    return adjusted

# Irrelevant utility - distractor
sanitize_data = lambda data: [x for x in data if x > 0]

# Core transformation function (relevant)
def transform_signal(seq):
    shifted = [(seq[i] + seq[i-1]) % 10 for i in range(len(seq))]
    return [x * 2 for x in shifted]

# Decoy function - never called directly in critical path
def legacy_process(arr):
    total = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            total += arr[i] // 2
    return total

# Unused helper - dead code path
compute_moment = lambda vals, power=2: sum(x ** power for x in vals) / len(vals)

# Complex conditional filter with red herring variables
threshold = 45
buffer_limit = 100
mode_flag = True
data_source = collect_readings()

# Distracting intermediate calculations
avg_source = sum(data_source) / len(data_source)
variance_proxy = sum((x - avg_source) ** 2 for x in data_source)
scaled_var = int(variance_proxy / 10)

# Primary data transformation chain
processed = transform_signal(data_source)
expanded = list(itertools.chain.from_iterable([[x, x+1] for x in processed[:5]]))
filtered = [x for x in expanded if x % 3 == 0]

# Mock diagnostic flags - misleading state tracking
diag_1 = len(processed) > 6
diag_2 = sum(filtered) < 200
status_code = 200 if diag_1 and diag_2 else 500

# Bit manipulation decoy
bit_fiddle = 0
for x in filtered:
    bit_fiddle ^= (x << 1) | 1
bit_fiddle %= 888

# Critical computation buried in noise
rolling_window = [sum(expanded[i:i+3]) for i in range(len(expanded)-2)]
peak_count = sum(1 for x in rolling_window if x > 50)

def analyze_pattern(signal):
    base = sum(signal) // len(signal)
    adjustment = 0
    
    # Nested logic with conditional override red herring
    if peak_count > 3:
        temp_cache = {}
        for i, val in enumerate(signal):
            temp_cache[i] = val * (i+1)
        # This branch is NOT taken
        adjustment = len(temp_cache) if mode_flag else 0
    else:
        # Actual path: uses rolling statistics
        extremes = list(filter(lambda x: x > base * 1.2, signal))
        correction_factor = 1
        if len(extremes) % 2 == 0 and scaled_var > 5:
            correction_factor = 2
        adjustment = len(extremes) * correction_factor
    
    # Final interference: unused branching
    final_shift = 0
    if status_code == 503:
        final_shift = 999
    
    return base + adjustment - (bit_fiddle // 100)

# Key execution point
transformed_data = [x - 5 for x in expanded if x < 60]
final_diagnostic = analyze_pattern(transformed_data)

print(f"Target result: {final_diagnostic}")