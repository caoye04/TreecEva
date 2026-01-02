import math

# Irrelevant helper function (dead code path)
def unused_checksum(seq):
    return sum(x ^ 2 for x in seq) % 7

# Misleading transformation chain
def corrupt_signal(data):
    shifted = [x << 1 for x in data]
    inverted = [~x & 0xFF for x in shifted]
    return [y + 3 for y in inverted]

# Distractor: complex but unused signal model
class SignalModel:
    def __init__(self):
        self.alpha = 0.7
        self.beta = 1.3
    
    def predict(self, x):
        return self.alpha * x + self.beta

# Real processing begins here
def encode_sequence(seq):
    return [int(math.sqrt(x)) if x > 0 else 0 for x in seq]

def filter_outliers(arr, threshold=50):
    return [x for x in arr if x <= threshold]

# Core logic disguised among red herrings
def transform_frequency_domain(signal):
    temp_result = []
    for i, val in enumerate(signal):
        if i % 2 == 0:
            temp_result.append(val * 2 + 1)
        else:
            temp_result.append(val - (i % 3))
    return temp_result

def accumulate_diagnostics(sig):
    total = 0
    for x in sig:
        if x > 10:
            total += x // 2
        elif x > 5:
            total += x
        else:
            total -= x
    return total

# Unused lambda (distractor)
decoil = lambda z: z ** 2 - z

# Actual main pipeline
raw_data = list(range(1, 21))  # [1, 2, ..., 20]
encoded_data = encode_sequence(raw_data)
filtered_data = filter_outliers(encoded_data)
processed_data = transform_frequency_domain(filtered_data)

# Key distracting computation (misleads about importance of bit operations)
bit_analysis = sum((x & 5) ^ (x >> 1) for x in processed_data) % 100

# Decoy assignment
preliminary_diagnostic = bit_analysis * 2 - 7

# Real diagnostic function using lambda and nested logic
analyze_signal = lambda data: sum(
    math.floor(x * 0.5) if i % 3 == 0 else
    math.ceil(x * 0.3) if i % 3 == 1 else
    x - 2
    for i, x in enumerate(data)
) + len(data)

# Critical execution point
final_diagnostic = analyze_signal(processed_data)

print(f"Result: {final_diagnostic}")