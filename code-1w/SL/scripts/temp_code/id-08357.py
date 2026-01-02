def decode_segment(segment):
    # Irrelevant decoding attempt (distractor)
    decoded = ''.join([chr((ord(c) - 4)) for c in segment])
    return len(decoded) % 7

def validate_checksum(data):
    # Unused validation function (dead code path)
    checksum = 0
    for d in data:
        checksum = (checksum * 3 + d) % 257
    return checksum == 42

def shift_cipher(text, shift):
    # Misleading string transformation (red herring)
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

def analyze_frequency(signal_list):
    # Complex but irrelevant frequency analysis
    freq_map = {}
    for val in signal_list:
        rounded = int(val // 10) * 10
        freq_map[rounded] = freq_map.get(rounded, 0) + 1
    dominant = max(freq_map, key=freq_map.get)
    return dominant if dominant != 0 else 50

def process_transmission(seq, key):
    # Core logic buried among distractions
    temp_buffer = []
    
    # Distractor: unused intermediate calculations
    dummy_sum = 0
    shadow_counter = 0
    for i in range(len(seq)):
        if seq[i] % 3 == 0:
            dummy_sum += seq[i]
        shadow_counter += 1
    
    # Real processing starts here — slicing and logical filtering
    filtered = [x for x in seq if x > 100 and x % 2 == 1]  # Only odd values > 100
    
    # Bit manipulation mixed with arithmetic
    transformed = []
    for val in filtered:
        shifted = (val ^ key) >> 2  # XOR with key then right shift
        transformed.append(shifted)
    
    # String-based control flow (uses slicing and string methods)
    control_flag = 'de-activate boost'
    if control_flag.split()[0] == 'de-activate':  # Slicing logic red herring
        multiplier = 0.75
    else:
        multiplier = 1.25
    
    # Another distractor: unused list transformation
    inverted = [round((255 - v) * 0.5) for v in seq if v < 200]
    
    # Final computation: sum with conditional rounding
    raw_total = sum(transformed)
    if raw_total % 2 == 0:
        final_value = int(raw_total * multiplier)
    else:
        final_value = int(round(raw_total * 1.1))
    
    # Critical assignment
    final_signal = final_value + 50
    return final_signal

# Simulated transmission sequence (real input)
transmission_sequence = [105, 210, 115, 180, 195, 220, 143, 177, 201, 134]
encryption_key = 85

# Unused variables (distractors)
data_payload = [0xAB, 0xCD, 0xEF, 0x12]
encoded_tag = shift_cipher('securelink', 5)
freq_analysis_result = analyze_frequency(transmission_sequence)

# Key execution point
final_signal = process_transmission(transmission_sequence, encryption_key)

# Output
print(f"Result: {final_signal}")