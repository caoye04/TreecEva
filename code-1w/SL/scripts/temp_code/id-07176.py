def transform_case(char, mode):
    return char.upper() if mode == 'upper' else char.lower()


def count_characters(text, case_sensitive=True):
    freq = {}
    for c in text:
        key = c if case_sensitive else c.lower()
        freq[key] = freq.get(key, 0) + 1
    return freq


def apply_mask(value, mask=0xFF):
    # Irrelevant bit manipulation red herring
    return value ^ mask & 0x0F

# Dead function — never used
def decrypt_cipher(data, key):
    return ''.join(chr(ord(c) ^ key) for c in data)

# Unused utility
def generate_primes(n):
    sieve = [True] * n
    sieve[0:2] = [False, False]
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n, i):
                sieve[j] = False
    return [i for i, prime in enumerate(sieve) if prime]

refinement_steps = [
    lambda x: (x * 3) + 1,
    lambda x: x ^ 0b1010,
    lambda x: (x % 17) * 2
]

threshold_levels = {
    'low': 10,
    'medium': 25,
    'high': 40
}

# Distractor list
sensor_readings = [107, 214, 198, 95, 42, 67, 134, 88, 201]

# Decoy dictionary with misleading values
status_map = {
    'A': 'Active',
    'B': 'Buffering',
    'C': 'Calibrating',
    'D': 'Degraded'
}

# Complex nested structure — partial usage
system_profile = {
    'version': '3.7.1',
    'mode': 'enhanced',
    'filters': [
        {'type': 'alpha', 'level': 3},
        {'type': 'beta', 'level': 5},
        {'type': 'gamma', 'level': 8}
    ],
    'checksum': 0xDEADBEEF
}

# Core logic disguised among distractions
def process_item(item, ops):
    result = item
    for op in ops:
        result = op(result)
    return result


def process_sequence(data_list, operations):
    processed = []
    for val in data_list:
        temp = process_item(val, operations)
        processed.append(temp)
    return processed


def validate_purity(mapped_values, limits):
    base = sum(mapped_values) // len(mapped_values)
    offset = len([v for v in mapped_values if v > limits['medium']])
    penalty = offset * 1.75
    purity_index = base - penalty
    
    # Conditional expression with string method distraction
    label = ('pure' if purity_index > limits['medium'] else 'mixed').title().strip()
    label += '!' if purity_index >= limits['high'] else '?'  # Useless mutation
    
    return int(purity_index)

# Real input data buried in transformations
raw_segment = "tExTfOrAnAlYsIs"
char_count = count_characters(raw_segment, case_sensitive=False)

# Convert character frequencies to numeric seed
seed_value = sum(char_count.values()) * max(char_count.values())  # = 14 * 2 = 28

# Generate initial data from string properties
segment_data = [
    seed_value + 12,           # 40
    seed_value * 2 - 10,         # 46
    seed_value + (seed_value // 2), # 42
    37
]

# Critical execution point
filtration_score = validate_purity(process_sequence(segment_data, refinement_steps), threshold_levels)

# Print final answer as required
print(f"Result: {filtration_score}")