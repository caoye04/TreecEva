import math

# Irrelevant helper function (dead code path)
def analyze_bandwidth(signal):
    return sum([(x ** 2) % 7 for x in signal if x > 0])

# Decoy transformation with misleading intermediate results
def transform_signal(seq):
    temp_result = [((x << 2) ^ 5) & 15 for x in seq]
    normalized = [val / max(temp_result) * 100 for val in temp_result]
    return [round(n, 3) for n in normalized]

# Unused but plausible-looking processing stage
def calibrate_buffer(buffer):
    adjustment = len(buffer) % 8
    return [b ^ adjustment for b in buffer] + [adjustment]

# Core logic: recursive bit analysis
def count_set_bits(n):
    if n == 0:
        return 0
    return (n & 1) + count_set_bits(n >> 1)

# Conditional expression based filtering
def is_valid_frame(x):
    return True if (x % 4 == 0 and count_set_bits(x) >= 2) else False

# Set-based interference: irrelevant domain data
diagnostic_codes = {f"ERR_{i}" for i in range(10, 90) if i % 7 == 0}
active_diagnostics = {f"ERR_{j}" for j in [14, 21, 49, 56]}
recovered_codes = diagnostic_codes & active_diagnostics

# Data stream simulation with case conversion red herring
def generate_stream(seed=101):
    raw = []
    s = str(seed).upper()
    for i in range(8):
        flipped = s[::-1]
        val = int(flipped) ^ (i * 17)
        raw.append(val % 256)
    return raw

# Primary processing chain
def process_sequence(data):
    # Irrelevant list comprehension distraction
    squared_chain = [d**2 for d in data if d < 100]
    
    # Real work begins: filter valid frames using bit condition
    filtered = [x for x in data if is_valid_frame(x)]
    
    # Dead code block – looks important but unused
    stats = {}
    if len(filtered) > 0:
        stats['peak'] = max(filtered)
        stats['entropy'] = sum([math.log(f+1) for f in filtered])
    
    # Actual transformation affecting final result
    processed = []
    for item in filtered:
        shifted = (item >> 1) ^ 0xA
        processed.append(shifted)
    
    return processed

# Final evaluation function with conditional expression
def evaluate_purity(seq):
    if not seq:
        return -1
    total_weight = 0
    for val in seq:
        # Combination of arithmetic and bit operations
        weight = (val ** 2) - (count_set_bits(val) * 8)
        total_weight += weight
    
    # Final adjustment using set size (irrelevant but connected)
    diagnostic_penalty = len(recovered_codes) * 5
    return total_weight - diagnostic_penalty

# Main execution flow
data_stream = generate_stream(101)

# Misleading prior computation (distraction)
baseline_diagnosis = transform_signal(data_stream)
system_checksum = sum(calibrate_buffer([len(data_stream), 255]))

# Critical statement containing answer
filtration_score = evaluate_purity(process_sequence(data_stream))

print(f"Result: {filtration_score}")