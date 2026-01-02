def preprocess_input(raw):    
    # Irrelevant transformation
    temp_a = ''.join(chr(ord(c) + 1) for c in raw if c.isalpha())
    temp_b = raw[::-1].upper()  # Misleading reverse and uppercase
    stats = {        'vowel_count': sum(1 for c in raw if c.lower() in 'aeiou'),
        'digit_sum': sum(int(c) for c in raw if c.isdigit()),
        'consonant_weight': sum(ord(c) - 96 for c in raw.lower() if c.isalpha() and c not in 'aeiou')
    }
    return stats

# Decoy function that's never called
def legacy_compatibility(payload):
    buffer = []
    for i in range(len(payload)):
        if i % 2 == 0:
            buffer.append(ord(payload[i]) << 2)
    return sum(buffer)

def transform_sequence(seq, key):
    shifted = []
    for i, val in enumerate(seq):
        # Complex but partially irrelevant shifting logic
        shift = (key * i) % 8
        new_val = (val << shift) ^ key
        if new_val > 1000:  # Capping that rarely triggers
            new_val = 999
        shifted.append(new_val)
    return shifted

def evaluate_threshold(values):
    # Red herring: computes a threshold but isn't used in final result
    base = sum(v % 17 for v in values) / len(values)
    penalty = len([v for v in values if v & 1]) * 0.7
    return base - penalty

def analyze_pattern(data_map):
    # Core relevant logic hidden among distractions
    x = data_map['vowel_count']
    y = data_map['digit_sum']
    z = data_map['consonant_weight']
    
    # Real computation path
    intermediate = (x * 13) + (y * 29)
    if z % 2 == 0:
        intermediate -= 15
    else:
        intermediate += 7
    
    # Distractor: unused conditional branch
    if x > 5 and y < 10:
        intermediate = abs(intermediate - 100)
    
    # Another decoy variable
    dummy_result = (z * x) % 97
    
    # Final deterministic calculation
    final_score = (intermediate * 31) % 887
    return final_score

# Main execution flow
raw_input = "quantum2048flux"

# Dead code path - looks important but unused
backup_snapshot = [ord(c) * 3 + 2 for c in raw_input if c in 'aeiou']

# Key preprocessing
preprocessed_stats = preprocess_input(raw_input)

# Create numerical sequence from digit positions
pos_sequence = [i * 2 + 1 for i, c in enumerate(raw_input) if c.isdigit()]

# Apply transformation with fixed key - appears critical but not used later
transformed_seq = transform_sequence(pos_sequence, 7)

# Unused evaluation
threshold_value = evaluate_threshold(transformed_seq)

# Critical statement: this is where the answer is determined
final_diagnostic = analyze_pattern(preprocessed_stats)

print(f"Result: {final_diagnostic}")