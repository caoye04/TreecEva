import math

# Irrelevant helper function (dead code path)
def unused_signal_filter(x):
    return [val for val in x if val % 3 == 0]

# Distractor: complex-looking but unused transformation
class DataObfuscator:
    def __init__(self, key):
        self.key = key

    def scramble(self, data):
        return [d ^ self.key for d in data]

    def unscramble(self, data):
        return [d ^ self.key for d in data]

# Real processing begins here
initial_seed = [2, 3, 5, 7, 11, 13, 17, 19]
decoys = [0] * 5

# Meaningless buffer expansion
temp_buffer = []
for i in range(4):
    temp_buffer.extend([i * 2 + 1])

decoys[2] = sum(temp_buffer)  # distractor assignment

# Actual relevant logic: transform via lambda and string operations
def digit_sum(n):
    return sum(int(d) for d in str(abs(n)))

processed = list(map(lambda x: (x ** 2) + digit_sum(x), initial_seed))

# Another layer of transformation using case conversion on dummy strings
fake_checksum = ''
for num in processed:
    if num % 2 == 0:
        fake_checksum += 'A'
    else:
        fake_checksum += 'b'

# Distractor: character counting with no impact
char_count = {'upper': 0, 'lower': 0}
for ch in fake_checksum:
    if ch.isupper():
        char_count['upper'] += 1
    if ch.islower():
        char_count['lower'] += 1

adjusted_values = [p - digit_sum(p) for p in processed]

# Simulate a recursive filtering process
def recursive_reduce(seq, threshold):
    if len(seq) <= 1 or sum(seq) < threshold:
        return sum(seq)
    return recursive_reduce(seq[:-1], threshold - 5)

# Irrelevant recursive call with decoy result
_ = recursive_reduce(adjusted_values, 40)

# Core transformation that matters
shifted = [int(math.log(val, 2)) if val > 1 else 0 for val in adjusted_values]

def analyze_pattern(arr):
    base = 0
    for idx, v in enumerate(arr):
        if idx % 2 == 0:
            base += v * 2
        else:
            base -= v
    return base * 3

# Secondary transformation before final analysis
device_id_str = "DX-90210"
normalized_id = device_id_str.lower().replace('-', '')

# Distractor: combinatorics on string characters (unused)
perms = 1
for i in range(1, len(normalized_id) + 1):
    perms *= i

# Real transformation chain
transformed_sequence = [s + len(normalized_id) for s in shifted]

# Key statement
final_diagnostic = analyze_pattern(transformed_sequence)

print(f"Result: {final_diagnostic}")