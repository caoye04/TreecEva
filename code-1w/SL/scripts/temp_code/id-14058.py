import math

# Simulated sensor array data (irrelevant in part)
sensor_grid = [[(i + j) % 7 for j in range(5)] for i in range(6)]
offset_lookup = {i: (i * i) % 13 for i in range(10)}

def decode_sequence(seq):
    # Irrelevant decoding function (dead path)
    return [math.sin(x) for x in seq if x % 2 == 0]

def generate_checksum(data):
    # Unused checksum logic (distractor)
    chk = 0
    for row in data:
        for val in row:
            chk ^= (val * 3) % 9
    return chk

def transform_entry(val, shift):
    # Used only in one branch, mostly irrelevant
    if val < 0:
        return abs(val) ** 0.5
    return ((val + shift) * 2) % 9

def parse_metadata(meta_str):
    # String processing red herring
    parts = meta_str.split('-')
    code = parts[0].upper().strip()
    version = int(parts[1]) if parts[1].isdigit() else 0
    flags = list(code.encode())
    return sum(flags) + version

# Core signal processing chain
raw_readings = [12, 15, 10, 8, 20, 18, 25]
baseline_shift = 7
adjusted = [x - baseline_shift for x in raw_readings]  # Step 1

# Conditional filtering based on dynamic thresholds
thresholds = {'low': 3, 'med': 6, 'high': 10}
dynamic_factor = len(adjusted) // 2
thresholds['adaptive'] = dynamic_factor + 2  # = 5

classified = []
for val in adjusted:  # Step 2
    if val <= thresholds['adaptive']:
        classified.append('L')
    elif val <= thresholds['high']:
        classified.append('M')
    else:
        classified.append('H')  # Step 3

# Bit manipulation layer (partially relevant)
bit_encoded = 0
for i, c in enumerate(classified):
    bit_flag = (ord(c) ^ i) & 7  # XOR and mask
    bit_encoded |= (bit_flag << (i % 8))  # Accumulate in byte pattern

# Decoy transformation tree
shadow_buffer = []
for x in adjusted:  # Dead loop – no usage later
    temp = x * x - 3 * x + 2
    if temp > 10:
        shadow_buffer.append(math.log(temp, 2))

# Actual critical data transformation
processed_data = []
for idx, val in enumerate(adjusted):  # Step 4
    mod_val = val % 4
    shifted = (val + (mod_val ** 2)) / (idx + 1)  # Division by index + 1
    processed_data.append(round(shifted, 3))  # Step 5

# Build threshold map with string-derived keys (uses string method)
keys = ['tune', 'mode-A', 'gain_3', 'calib-X']
normalized_keys = [k.replace('_', '-').upper() for k in keys]  # String manipulation
threshold_map = {}
for i, k in enumerate(normalized_keys):  # Step 6
    factor = 1 + (i % 3)
    threshold_map[k] = round(math.sqrt(factor * 4.5), 2)

# Critical analysis function combining arithmetic and logic
valid_count = 0
def analyze_signal(data, tmap):
    global valid_count
    total = 0.0
    decay = 0.95
    keys_sorted = sorted(tmap.keys(), key=lambda x: len(x))  # Sort by length
    scale = tmap[keys_sorted[0]]  # Use shortest key's value
    
    for i, val in enumerate(data):  # Step 7
        if i % 3 == 0:
            val *= scale  # Amplify every 3rd element
        elif i % 4 == 0:
            val += 1.5
        
        tolerance = threshold_map[normalized_keys[i % len(normalized_keys)]]
        
        # Apply conditional suppression
        if val > tolerance * 2.1:  # Step 8
            val = val * 0.7
        elif val < tolerance * 0.5:
            continue  # Skip small values
            
        total += val * (decay ** i)  # Exponential weighting
        valid_count += 1  # Track contributions
    
    # Final adjustment using bit information (cross-concept)
    entropy_factor = bin(bit_encoded).count('1')  # Population count
    final_score = total * (entropy_factor or 1)  # Avoid zero
    return round(final_score, 5)  # Step 9

# Trigger the key computation
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")