import math

# Irrelevant helper function (decoy)
def useless_transform(x):
    return (x ** 2 + 3 * x + 1) % 7

def decode_string(s):
    # Distractor: case conversion and string manipulation with no real impact
    inverted = s[::-1].lower()
    shifted = ''.join(chr((ord(c) - 97 + 3) % 26 + 97) if c.isalpha() else c for c in inverted)
    return shifted.title()

# Unused but plausible-looking data structure
temp_buffer = [0] * 15

# Real logic starts here
def analyze_sectors(values):
    sector_sum = 0
    for v in values:
        if v > 0 and v % 2 == 1:
            sector_sum += int(math.sqrt(v)) * 2
    return sector_sum

config = {
    'threshold': 42,
    'mode': 'strict',
    'debug': False,
    'padding': [0, 0, 0]
}

# Misleading precomputation (dead path)
baseline_estimate = sum([i * i for i in range(5)]) * 2.5

# Core data with embedded signal
raw_data = [16, 25, 36, 49, 50, 81]

# Distractor: complex-looking but unused transformation
decoded_key = decode_string('GurJbmP')
shadow_copy = [useless_transform(x) for x in range(len(raw_data))]

# Main processing function
def process_metrics(data, settings):
    temp_result = 0
    
    # Step 1: filter valid entries
    filtered = [d for d in data if d >= settings['threshold']]
    
    # Step 2: apply non-linear transform
    transformed = []
    for item in filtered:
        log_val = math.log(item, 3)
        if log_val.is_integer():
            transformed.append(int(log_val))
    
    # Step 3: accumulate with offset
    accumulation = 0
    for idx, val in enumerate(transformed):
        accumulation += val * (idx + 1)
    
    # Step 4: conditional adjustment
    if settings['mode'] == 'strict':
        accumulation -= 1
    
    # Step 5: cross-check with secondary analysis
    secondary = analyze_sectors(data)
    
    # Step 6: final combination
    result = accumulation * 2 + secondary
    
    # Irrelevant debug print (has no effect)
    if settings['debug']:
        print(f'Debug: {result}')
    
    # Step 7: red herring bitwise operation (unused)
    decoy_mask = (result ^ 255) & 0xFF
    
    # Step 8: actual output
    return result

# Spurious loop with side-effect-free operations
for _ in range(3):
    baseline_estimate = math.floor(baseline_estimate / 2)

# Critical execution point
data = [x + 1 for x in raw_data]  # Shifts data: [17,26,37,50,51,82]
final_score = process_metrics(data, config)

# Output result as required
print(f"Result: {final_score}")