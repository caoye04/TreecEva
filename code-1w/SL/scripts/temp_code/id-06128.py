def analyze_pattern(sequence):
    count = 0
    for char in sequence:
        if char.isdigit():
            count += int(char) % 3
    return count

raw_data = 'x9k2m4z7p1'

# Irrelevant transformation chain (distractor)
buffer = raw_data.upper().replace('X', 'A').lower()
temp_chars = [c for c in buffer if c in 'kmzp']
shadow_value = sum(ord(c) % 5 for c in temp_chars)

# Semi-relevant preprocessing
numeric_part = ''.join([c for c in raw_data if c.isdigit()])
digit_sum = sum(int(d) for d in numeric_part)
modular_hint = digit_sum % 7

# Threshold calculation with red herring variables
baseline = len(raw_data) * 2
offset = shadow_value // 2  # Not actually used in final logic
thresholds = {
    'low': baseline - 5,
    'high': baseline + 3
}

# Core logic hidden among distractions
def process_results(data, limits):
    raw_length = len(data)
    analyzed = analyze_pattern(data)
    
    # Actual key computation path
    if modular_hint > 4:
        adjustment = 3
    else:
        adjustment = 5  # This will be taken
    
    intermediate = (analyzed * raw_length) + adjustment
    
    # Use string method to extract control flow signal
    flag_char = data[3]  # '2' from 'x9k2...'
    if flag_char in '01234':
        intermediate -= 2
    
    # Simulate stateful decision with dummy recursion
    def recursive_boost(n, depth=0):
        if depth >= 2 or n > 100:
            return n
        return recursive_boost(n + depth * 3, depth + 1)
    
    boosted = recursive_boost(intermediate)
    
    # Final threshold-based adjustment (only one branch matters)
    if boosted < limits['low']:
        result = boosted * 2
    elif boosted > limits['high']:
        result = boosted - 10
    else:
        result = boosted + 1  # This is the actual path
    
    # Dead code (never reached)
    if False:
        result = 999  # unreachable
    
    return result

# Key statement
final_score = process_results(raw_data, thresholds)
print(f"Result: {final_score}")