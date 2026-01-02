def preprocess_signal(raw):    
    # Irrelevant transformation branch
    if len(raw) < 5:
        return [x * 2 for x in raw]
    
    # Distractor: complex-looking but unused operation
    shifted = [(x + 3) % 256 for x in raw]
    decoy_sum = sum(shifted[::2]) * 0.5

    # Actual relevant path
    filtered = [x for x in raw if x > 0]
    normalized = [round(x / max(filtered), 3) for x in filtered]
    return normalized


def encode_sequence(seq):
    # String-based distractor with case conversion and manipulation
    base_str = ''.join([chr(97 + (x * 7) % 26) for x in seq])
    alternate = base_str.upper()[::-1] + base_str.lower()
    if len(alternate) > 10:
        altered = alternate.replace('A', 'X').replace('Z', 'Y')
    else:
        altered = alternate
    
    # Dead-end computation
    checksum = 0
    for c in altered:
        checksum += ord(c) % 19
    
    # Relevant logic buried here
    length_flag = len(seq) % 4
    return length_flag


def transform_input(data, mode='advanced'):
    # Bitwise operations mixed with red herring
    processed = []
    meta_flags = []
    for item in data:
        # Real transformation
        temp = (item ^ 245) & 127
        processed.append(temp)
        
        # Distractor: tracking parity even though unused later
        parity = bin(temp).count('1') % 2
        meta_flags.append(parity)
    
    # Decoy aggregation
    total_xor = 0
    for m in meta_flags:
        total_xor ^= m
    
    # Only this matters
    if mode == 'advanced':
        return [p * 2 for p in processed]
    return processed


def analyze_pattern(data, settings):
    # Critical logic hidden among multiple conditionals
    threshold = settings.get('threshold', 50)
    activation = settings.get('activation', 'linear')
    
    count_above = 0
    running_product = 1
    for val in data:
        if val > threshold:
            count_above += 1
        if val > 0 and running_product < 1e6:
            running_product *= val
    
    # Red herring: string comparison that looks important
    mode_str = settings.get('mode', 'safe')
    if mode_str.lower() == 'strict'.upper():
        adjustment = -5
    else:
        adjustment = 3
    
    # Another distraction: recursive call that's not really needed
    def helper(n):
        if n <= 1:
            return 1
        return n + helper(n - 2) if n % 3 == 0 else helper(n - 1)
    
    dummy_trace = helper(count_above % 7)
    
    # Real computation path
    raw_score = count_above * running_product
    final_value = raw_score + adjustment
    
    # One more decoy: floating point rounding that doesn't affect outcome
    if final_value > 1000:
        final_value = round(final_value / 100, 4) * 100
    
    return int(final_value)

# Main execution with misleading setup
raw_input = [10, -5, 100, 200, 0, 300]
config = {
    'threshold': 45,
    'activation': 'exponential',
    'mode': 'normal',  # Looks important but only affects adjustment
    'version': '2.1b'
}

# Chain of transformations with distractions
cleaned = preprocess_signal(raw_input)
encoding_flag = encode_sequence(cleaned)
decoy_array = [x | 15 for x in cleaned]  # Unused bitwise OR array
transformed_data = transform_input([int(x * 100) for x in cleaned], mode='advanced')

# Key statement
final_diagnostic = analyze_pattern(transformed_data, config)

# Print result as required
print(f"Target result: {final_diagnostic}")