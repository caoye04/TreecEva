def analyze_frequency(data):
    # Irrelevant function: computes frequency but not used in main logic
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    return {k: v for k, v in freq.items() if v > 1}

# Decoy dataset
temp_readings = [23.5, 24.1, 25.0, 23.5, 26.3, 25.0, 27.8, 24.1]
duplicate_temps = analyze_frequency(temp_readings)

# Real processing begins here
segments = ['alpha', 'beta', 'gamma', 'delta']
offsets = [3, 1, 4, 1]
config = {'threshold': 2, 'mode': 'encode'}

# Misleading intermediate calculations
counterfeit_mask = [x ^ 255 for x in range(8)]  # Dead path: never used
dummy_checksum = sum(counterfeit_mask) % 199  # Distractor variable

bit_flags = set()
for i, (seg, offset) in enumerate(zip(segments, offsets)):
    # Meaningful but obfuscated transformation
    hash_val = 0
    for char in seg:
        hash_val += ord(char) * (i + 1)
    
    # Apply offset via modular arithmetic and bit flip
    transformed = (hash_val + offset) % 1000
    if transformed % 2 == 0:
        transformed ^= 0b1101  # Bitwise XOR red herring
    
    # Only certain segments contribute
    if len(seg) > 4 and 'a' in seg:
        bit_flags.add(transformed & 0xFF)  # Store only lower byte

# Another decoy structure
snapshot = {k: v for k, v in enumerate(['init', 'idle', 'run', 'halt']) if v != 'idle'}
status_map = {idx: val.upper() for idx, val in snapshot.items()}  # Unused

# Core logic disguised among noise
def process_segments(segs, cfg):
    base = 0
    for idx, s in enumerate(segs):
        # Conditional expression with string method distraction
        weight = len(s.replace('a', 'aa')) if s.startswith('a') else len(s)
        code_point = 0
        for i, c in enumerate(s):
            # Use of enumerate with complex weighting
            code_point += (ord(c) - 96) * (i + 1) * weight
        
        # Modular arithmetic with conditional twist
        if idx % 2 == 0:
            code_point = code_point % 97
        else:
            code_point = (code_point + 5) // 3
        
        # Only even-indexed segments are aggregated
        if idx % 2 == 0:
            base += code_point
    
    # Final adjustment using bit_flags from earlier
    flag_sum = sum(bit_flags) if bit_flags else 1
    return (base * 3) - (flag_sum % 50)

# Execution point of interest
final_score = process_segments(segments, config)

# Output required format
print(f"Result: {final_score}")